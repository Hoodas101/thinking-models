#!/usr/bin/env python3
"""从 tools/models.json 生成文档中「单一真源」的区块，消除 SKILL/AGENTS/REFERENCE 之间手工同步的漂移。

用法:
    python3 tools/gen.py           # 就地写入
    python3 tools/gen.py --check   # 只检查是否与真源一致，不一致则非零退出（供 CI / 提交前用）

真源: tools/models.json。文档里以 <!-- AUTO:name --> ... <!-- /AUTO:name --> 圈定生成区。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = json.loads((ROOT / 'tools' / 'models.json').read_text('utf-8'))
MODELS = {m['id']: m for m in SRC['models']}


def name(zh_id_or_name):
    return MODELS[zh_id_or_name]['zh']


def en_of(mid):
    return MODELS[mid]['en']


def block_scenarios():
    lines = ['| 场景 | 第一优先 | 第二优先 |', '|---|---|---|']
    for s in SRC['scenarios']:
        lines.append(f"| {s['when_zh']} | #{s['primary']} {name(s['primary'])} | #{s['secondary']} {name(s['secondary'])} |")
    return '\n'.join(lines)


def block_top10():
    lines = []
    for m in SRC['models']:
        if m['domain'] == '第一层':
            lines.append(f"{m['id']}. {m['top_zh']}")
    return '\n'.join(lines)


def block_scenarios_en():
    lines = ['| Scenario | Primary | Secondary |', '|---|---|---|']
    for s in SRC['scenarios']:
        lines.append(f"| {s['when_en']} | {en_of(s['primary'])} | {en_of(s['secondary'])} |")
    return '\n'.join(lines)


def block_top10_en():
    lines = []
    for m in SRC['models']:
        if m['domain'] == '第一层':
            lines.append(f"{m['id']}. {m['top_en']}")
    return '\n'.join(lines)


def block_crossref():
    lines = ['| 概念 | TM编号 | BC编号 | 说明 |', '|---|---|---|---|']
    for c in SRC['crossref']:
        tm = f"#{c['tm']}" if c['tm'] else '—'
        bc = f"BC#{c['bc']}" if c['bc'] else '—'
        note = c['note'] or '—'
        lines.append(f"| {c['concept']} | {tm} | {bc} | {note} |")
    return '\n'.join(lines)


def block_entries():
    blocks = []
    for g in SRC['entries']:
        lines = [f"### {g['group']}", f"| 用户说 | 级别 | {g['header']} |", '|---|---|---|']
        for r in g['rows']:
            lines.append(f"| {r['when']} | {r['level']} | {r['models']} |")
        blocks.append('\n'.join(lines))
    return '\n\n'.join(blocks)


def block_links():
    lines = ['| 用完这个 | 接着看 | 为什么 |', '|---|---|---|']
    for l in SRC['links']:
        lines.append(f"| #{l['from']} {name(l['from'])} | #{l['to']} {name(l['to'])} | {l['note']} |")
    return '\n'.join(lines)


# 证据等级（强→弱，1-5）→ (中文说明, 中文用法, 英文标签, 英文说明, 英文用法)
# 只用数字和文字：图标占 token、跨模型渲染不稳定，且旧版同一个图标被两个不同等级共用，信息有歧义。
EVIDENCE = [
    (1, '学术共识', '认知科学/行为经济学教科书级结论', '可以放心作为纠正依据',
     'Academic consensus', 'Textbook-level findings in cognitive science / behavioral economics', 'Safe as grounds for a correction'),
    (2, '实证支持', '有具体研究支持（如飞轮效应源于 Collins 实证对照研究）', '作为主要参考，注意研究场景与你的场景差异',
     'Empirically supported', "Backed by specific studies (e.g. Flywheel traces to Collins' comparative research)", "Primary reference; check that the study's context matches yours"),
    (3, '经验总结', '来自 practitioner（芒格、Taleb 等）的启发式，无系统实验', '当作提问的镜子，不是答案的权威',
     'Practitioner heuristic', 'From Munger / Taleb-style experience, no systematic experiments', 'Use as a mirror for questions, not an authority for answers'),
    (4, '隐喻借用', '从物理/化学/生物借来的概念（黑天鹅、耗散结构、勒沙特列）', '**警惕**：隐喻是类比不是证明，跨域迁移时最易出错',
     'Borrowed metaphor', 'Concepts imported from physics/chemistry/biology (Black Swan, dissipative structures, Le Chatelier)', '**Caution**: a metaphor is an analogy, not a proof; cross-domain transfer is where errors concentrate'),
    (5, '有争议', '学术界存在实质分歧（彼得原理、破窗效应）', '仅作思考入口，不作为决策依据',
     'Controversial', 'Real academic disagreement (Peter Principle, Broken Windows)', 'Entry point for thinking only, never the basis of a decision'),
]


def _evidence_counts():
    ext = [m for m in SRC['models'] if m['domain'] != '第一层']
    return ext, {lvl: sum(1 for m in ext if m['evidence'] == lvl) for _, lvl, *_ in EVIDENCE}


def block_evidence_zh():
    ext, cnt = _evidence_counts()
    lines = ['| 等级 | 数量 | 含义 | 怎么用 |', '|---|---|---|---|']
    for n, lvl, meaning, how, *_ in EVIDENCE:
        lines.append(f"| {n} {lvl} | {cnt[lvl]} | {meaning} | {how} |")
    return '\n'.join(lines)


def block_evidence_en():
    ext, cnt = _evidence_counts()
    lines = ['| Grade | Count | Meaning | How to use it |', '|---|---|---|---|']
    for n, lvl, _m, _h, en, en_meaning, en_how in EVIDENCE:
        lines.append(f"| {n} {en} | {cnt[lvl]} | {en_meaning} | {en_how} |")
    return '\n'.join(lines)


def sources_md():
    lines = [
        '# 模型出处（可核实来源）',
        '',
        '> 由 `tools/gen.py` 从 `tools/models.json` 生成，勿手改。仅收录高频模型；未收录模型的证据等级见各领域文件（`models/*.md`）。',
        '> 级别：verified=一手论文/原始研究 · secondary=可靠二手或概念性著作 · draft=示意。',
        '',
        '| # | 模型 | 出处 | 级别 |',
        '|---|---|---|---|',
    ]
    for s in SRC['sources']:
        m = MODELS[s['id']]
        titles = '<br>'.join(r['title'] for r in s['refs'])
        levels = '<br>'.join(r['level'] for r in s['refs'])
        lines.append(f"| {m['id']} | {m['zh']} | {titles} | {levels} |")
    return '\n'.join(lines) + '\n'


# 文档 → 生成区块映射
TARGETS = {
    'SKILL.md': {'scenarios': block_scenarios, 'top10': block_top10},
    'AGENTS.md': {'scenarios_en': block_scenarios_en, 'top10_en': block_top10_en},
    'REFERENCE.md': {'crossref': block_crossref, 'links': block_links, 'entries': block_entries},
    'README.md': {'evidence_zh': block_evidence_zh},
    'README.en.md': {'evidence_en': block_evidence_en},
}

# 整文件生成
FULL_FILES = {
    'models/SOURCES.md': sources_md,
}


def apply_block(text, name_, body, path, problems):
    pat = re.compile(r'(<!-- AUTO:%s -->\n)(.*?)(\n<!-- /AUTO:%s -->)' % (re.escape(name_), re.escape(name_)), re.S)
    if not pat.search(text):
        problems.append(f'{path}: 缺少标记 <!-- AUTO:{name_} --> ... <!-- /AUTO:{name_} -->')
        return text
    return pat.sub(lambda m: m.group(1) + body + m.group(3), text)


def main():
    check = '--check' in sys.argv
    problems = []
    changed = []

    for fname, blocks in TARGETS.items():
        p = ROOT / fname
        text = p.read_text('utf-8')
        for bname, fn in blocks.items():
            text = apply_block(text, bname, fn(), fname, problems)
        if problems:
            continue
        recomputed = text
        if recomputed != p.read_text('utf-8'):
            changed.append(fname)
            if not check:
                p.write_text(recomputed, encoding='utf-8')

    for fname, fn in FULL_FILES.items():
        p = ROOT / fname
        body = fn()
        old = p.read_text('utf-8') if p.exists() else None
        if old != body:
            changed.append(fname)
            if not check:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(body, encoding='utf-8')

    if problems:
        print('[error] 生成失败：')
        for x in problems:
            print('   -', x)
        return 1
    if check:
        if changed:
            print('[error] 以下文件与 tools/models.json 不一致，请运行 python3 tools/gen.py：')
            for x in changed:
                print('   -', x)
            return 1
        print('[ok] 生成区与 tools/models.json 一致')
        return 0
    if changed:
        print('[ok] 已更新：' + ', '.join(changed))
    else:
        print('[ok] 无需变更')
    return 0


if __name__ == '__main__':
    sys.exit(main())