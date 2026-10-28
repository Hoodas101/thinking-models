#!/usr/bin/env python3
"""thinking-models 一致性校验（零依赖）。用法: python3 tools/check.py

校验项:
  1. 版本号与 tools/models.json 一致（SKILL.md / AGENTS.md / .cursorrules）
  2. 所有 #NN 引用：模型编号存在；TM 引用不误指向偏差概念（漏加 BC 前缀）
  3. 所有 BC#NN 引用：偏差编号存在；名称与编号匹配
  4. 数量声明（77 个思维模型 / 39 个偏误）与真源一致（自动跳过「第一层 10 个」「1-3 个」等子集写法）
  5. 文档引用的 .md 文件真实存在（防断链，含 models/ 下 6 个领域文件）
  6. models/*.md 正文的证据标记（证据:<等级名>）与真源 evidence 一致
  7. 真源里每个扩展模型都能在 models/*.md 找到正文（防止只加编号不加内容）
  8. 生成区块（AUTO）与真源一致（调用 tools/gen.py --check）
  9. 分发文件里不含表情符号（emoji 占 token、跨模型渲染不稳定、不携带信息）

退出码 0 = 通过；非零 = 有问题。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = json.loads((ROOT / 'tools' / 'models.json').read_text('utf-8'))
MODELS = {m['id']: m for m in SRC['models']}
BIASES = {b['id']: b for b in SRC['biases']}
N_MODELS = len(MODELS)
N_BIASES = len(BIASES)

DOCS = [
    'SKILL.md', 'AGENTS.md', '.cursorrules', 'REFERENCE.md', 'BIAS-CORRECTION.md',
    'README.md', 'README.en.md', 'CONTRIBUTING.md',
    'models/strategy.md', 'models/decision.md', 'models/systems.md',
    'models/people.md', 'models/growth.md', 'models/advanced.md',
]
EXTERNAL_FILES = {'BIASES.md', 'decision-log.md'}  # 运行时/姊妹 skill 文件，不在本仓库

# 只查 emoji 的额外文件（安装脚本会原样分发给用户，工具脚本自身也要守住同一条规则）
EMOJI_ONLY_FILES = ['install.sh', 'CHANGELOG.md', 'models/SOURCES.md',
                    'tools/gen.py', 'tools/check.py', 'tools/models.json',
                    'tools/regress.py', 'tools/cases.json']

CJK = r'[\u4e00-\u9fff]'
RANGE_RE = re.compile(r'#(\d+)\s*[-–~]\s*(\d+)')
TOKEN_RE = re.compile(r'BC\s?#(\d+)|#(\d+)')
# 子集/区间量词的提示字：命中则说明这个数字不是「库总量」声明，跳过
SUBSET_CUES = set('层选至最仅只如例各每')
# 区间写法（"11-77 个模型"）里的连接符：只有紧跟在另一个数字后才算区间
RANGE_BEFORE_RE = re.compile(r'\d\s*[-–~－]\s*$')

problems = []


def add(msg):
    if msg not in problems:
        problems.append(msg)


def is_name_match(captured, full):
    return captured and (full.startswith(captured) or captured.startswith(full))


def bias_hit(name):
    for b in BIASES.values():
        if is_name_match(name, b['zh']):
            return b
    return None


def scan_refs(fname, text):
    # 先校验并屏蔽区间写法（#11-69）
    def _range(m):
        a, b = int(m.group(1)), int(m.group(2))
        for x in (a, b):
            if x not in MODELS:
                add(f'{fname}: 区间 {m.group(0)} 含不存在的模型编号 #{x}')
        return ' ' * len(m.group(0))

    text = RANGE_RE.sub(_range, text)

    for m in TOKEN_RE.finditer(text):
        line_tail = text[m.end():].split('\n')[0]
        nm = re.match(CJK + r'+', line_tail.lstrip())
        nm = nm.group(0) if nm else ''
        if m.group(1) is not None:  # BC#N
            n = int(m.group(1))
            b = BIASES.get(n)
            if b is None:
                add(f'{fname}: BC#{n} 不存在（偏差编号应为 1-{N_BIASES}）')
            elif nm and not is_name_match(nm, b['zh']):
                tk = MODELS.get(n)
                hint = f'（#{n} 在 model 侧是「{tk["zh"]}」）' if tk else ''
                add(f'{fname}: BC#{n}{nm} 与偏差名称不符，BC#{n} 应为「{b["zh"]}」{hint}')
        else:  # #N（TM）
            n = int(m.group(2))
            mk = MODELS.get(n)
            if mk is None:
                add(f'{fname}: #{n} 不是有效模型编号（应为 1-{N_MODELS}）')
                continue
            if nm and not is_name_match(nm, mk['zh']):
                b = bias_hit(nm)
                if b is not None:
                    add(
                        f'{fname}: #{n}{nm} 疑似偏差编号漏加 BC 前缀，'
                        f'#{n} 现指向「{mk["zh"]}」；偏差「{b["zh"]}」应为 BC#{b["id"]}')
                else:
                    add(f'{fname}: #{n}{nm} 与模型名称不符，#{n} 应为「{mk["zh"]}」')


def _is_subset(text, num_start):
    """数字前 6 字含子集量词，或数字本身处在「11-77」这类区间里时，不是库总量声明。"""
    head = text[max(0, num_start - 8):num_start]
    if RANGE_BEFORE_RE.search(head):
        return True
    return any(ch in SUBSET_CUES for ch in head)


def _check_num(fname, text, num, kind, total):
    if int(num) != total:
        add(f'{fname}: {kind}数量声明 {num} != {total}')


def scan_counts(fname, text):
    # 库总量声明形态：
    #   "N 个思维模型" / "N 个模型…"（排除子集写法）/ "思维模型-N个" / "认知偏误-N个"
    for m in re.finditer(r'(\d+)\s*个\s*(?:思维)?模型', text):
        if not _is_subset(text, m.start(1)):
            _check_num(fname, text, m.group(1), '思维模型', N_MODELS)
    for m in re.finditer(r'(?:思维)?模型\s*[-—－]\s*(\d+)\s*个', text):
        _check_num(fname, text, m.group(1), '思维模型', N_MODELS)
    for m in re.finditer(r'(\d+)\s*个\s*(?:认知偏误|偏误|偏差)', text):
        if not _is_subset(text, m.start(1)):
            _check_num(fname, text, m.group(1), '偏误', N_BIASES)
    for m in re.finditer(r'(?:认知偏误|偏误|偏差)\s*[-—－]\s*(\d+)\s*个', text):
        _check_num(fname, text, m.group(1), '偏误', N_BIASES)


ENTRY_RE = re.compile(r'^\*\*(\d+)\.\s', re.M)
MARKER_RE = re.compile(r'^证据:([^\s(（]+)')
# 证据等级顺序（强→弱）：文档与正文统一用「数字 + 等级名」，不用图标
GRADES = ['学术共识', '实证支持', '经验总结', '隐喻借用', '有争议']
# 表情符号字符类（用转义写，避免本文件自身成为漏网之鱼）：
# U+1F000-1FAFF 象形文字/emoji · U+2600-27BF 杂项符号与装饰符号 · U+2B00-2BFF 杂项箭头与符号 · U+FE0F 变体选择符
# 排版箭头 → ← ↔（U+2190-21FF）不在其中：它们承载逻辑关系，且 token 成本低
EMOJI_RE = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u2122\u2139\u24C2\u20E3\u23E9-\u23FA\u25AA\u25AB\u25B6\u25C0\u25FB-\u25FE]')


def scan_markers(fname, text):
    """models/*.md 正文的证据标记必须与 tools/models.json 的 evidence 一致。"""
    if not fname.startswith('models/'):
        return
    cur = None
    seen = {}
    for line in text.split('\n'):
        m = ENTRY_RE.match(line)
        if m:
            cur = int(m.group(1))
            seen.setdefault(cur, 0)
            continue
        mm = MARKER_RE.match(line)
        if not mm or cur is None or cur not in MODELS:
            continue
        seen[cur] += 1
        label = mm.group(1)
        want = MODELS[cur]['evidence']
        if label != want:
            add(f'{fname}: #{cur} 证据等级标注「{label}」，真源为「{want}」')
        elif line[:len('证据:' + want)] != f'证据:{want}':
            add(f'{fname}: #{cur} 证据标记格式应为 证据:{want}')
    for mid, n in sorted(seen.items()):
        if mid in MODELS and MODELS[mid]['domain'] != '第一层':
            if n == 0:
                add(f'{fname}: #{mid} 缺少证据标记（应为行首顶格 证据:{MODELS[mid]["evidence"]}）')
            elif n > 1:
                add(f'{fname}: #{mid} 证据标记出现 {n} 次（应恰好 1 次）')


def scan_emoji(fname, text):
    """分发文件里不允许出现 emoji：它们占 token、跨模型渲染不稳定，且不携带信息。"""
    hits = sorted({ch for ch in EMOJI_RE.findall(text)})
    if hits:
        add(f'{fname}: 含 {len(hits)} 种 emoji（{"".join(hits)}），请改为纯文字/数字')


def scan_body_coverage(fnames):
    """真源里的每个扩展模型都必须能在 models/*.md 找到正文。"""
    found = set()
    for fname in fnames:
        p = ROOT / fname
        if not (p.exists() and fname.startswith('models/')) or fname == 'models/SOURCES.md':
            continue
        for m in ENTRY_RE.finditer(p.read_text('utf-8')):
            found.add(int(m.group(1)))
    missing = [i for i, m in MODELS.items() if m['domain'] != '第一层' and i not in found]
    if missing:
        add('models/*.md: 缺少正文的模型 ' + ', '.join(f'#{i}' for i in sorted(missing)))


def check_frontmatter(fname='SKILL.md'):
    text = (ROOT / fname).read_text('utf-8')
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        add(f'{fname}: 缺少可解析的 frontmatter（首行应为 ---）')
        return
    fm = m.group(1)
    for key in ('name', 'description', 'version'):
        if not re.search(rf'^{key}[ \t]*:[ \t]*\S', fm, re.M):
            add(f'{fname}: frontmatter 缺少 {key}')
    ver = re.search(r'^version[ \t]*:[ \t]*(\S+)', fm, re.M)
    if ver:
        for m2 in re.finditer(r'\bv(\d+\.\d+(?:\.\d+)?)\b', text[m.end():]):
            if m2.group(1) != ver.group(1):
                add(f'{fname}: 正文版本 v{m2.group(1)} 与 frontmatter {ver.group(1)} 不一致')


CHECK_EXTS = {'.md', '.py', '.sh', '.json'}
SKIP_DIRS = {'.git', '.github', 'docs', '__pycache__'}


def scan_file_coverage():
    """清单与实际文件双向对齐：新增文件忘了登记要报，清单里的文件被删也要报。"""
    listed = set(DOCS) | set(EMOJI_ONLY_FILES)
    for fname in sorted(listed):
        if not (ROOT / fname).exists():
            add(f'{fname}: 检查清单里有此文件，但磁盘上不存在（清单过期）')
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(part in SKIP_DIRS for part in rel.split('/')[:-1]):
            continue
        if p.suffix not in CHECK_EXTS and rel != '.cursorrules':
            continue
        if rel not in listed:
            add(f'{rel}: 未纳入检查清单（tools/check.py 的 DOCS 或 EMOJI_ONLY_FILES）')


def scan_file_refs(fname, text):
    for m in re.finditer(r'([A-Za-z0-9_][A-Za-z0-9_.\-/_]*\.md)', text):
        ref = m.group(1).strip('/')
        base = Path(ref).name
        if base in EXTERNAL_FILES:
            continue
        if (ROOT / ref).exists() or (ROOT / base).exists() or (ROOT / 'models' / base).exists():
            continue
        add(f'{fname}: 引用了不存在的文件 {ref}')


def main():
    ver = SRC['version']
    bad = sorted({m['evidence'] for m in MODELS.values()} - set(GRADES))
    if bad:
        add(f'tools/models.json: 出现未知证据等级 {", ".join(bad)}（应为 {"/".join(GRADES)}）')
    for fname in ['SKILL.md', 'AGENTS.md', '.cursorrules']:
        text = (ROOT / fname).read_text('utf-8')
        if ver not in text:
            add(f'{fname}: 未找到版本号 {ver}（真源 tools/models.json）')

    for fname in DOCS:
        p = ROOT / fname
        if not p.exists():
            continue
        text = p.read_text('utf-8')
        scan_refs(fname, text)
        scan_counts(fname, text)
        scan_markers(fname, text)
        scan_file_refs(fname, text)
        scan_emoji(fname, text)

    for fname in EMOJI_ONLY_FILES:
        p = ROOT / fname
        if p.exists():
            scan_emoji(fname, p.read_text('utf-8'))

    scan_body_coverage(DOCS)
    scan_file_coverage()
    check_frontmatter()

    gen = ROOT / 'tools' / 'gen.py'
    if gen.exists():
        r = subprocess.run([sys.executable, str(gen), '--check'], capture_output=True, text=True)
        if r.returncode != 0:
            tail = (r.stdout + r.stderr).strip().splitlines()
            add('tools/gen.py --check 未通过：' + (tail[-1] if tail else '无输出'))

    if problems:
        print(f'[error] 校验未通过，共 {len(problems)} 项：')
        for x in problems:
            print('   -', x)
        return 1
    print(f'[ok] 校验通过：{N_MODELS} 模型 / {N_BIASES} 偏误 / 版本 {ver}，无 emoji，引用与数量声明一致')
    return 0


if __name__ == '__main__':
    sys.exit(main())