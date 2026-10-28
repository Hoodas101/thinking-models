# 贡献指南

欢迎贡献！以下是参与方式：

## 如何贡献

### 新增思维模型
1. 在 `tools/models.json` 的 `models` 数组末尾加一条（`id` / `zh` / `en` / `domain` / `evidence`）
2. 在 `models/<对应领域>.md` 写模型正文：`**编号. 名称** | 信号 | 检查 | 公式 + 证据等级`
3. 运行 `python3 tools/gen.py` 再生成自动块（匹配表 / 场景表 / 交叉引用 / 来源）
4. 运行 `python3 tools/check.py`，退出码必须是 0

> 原则：`tools/models.json` 是唯一真源。匹配表、场景表、交叉引用、来源清单都由 `gen.py` 生成，不要手改 `<!-- AUTO:... -->` 块内部。

### 新增认知偏误
1. 在 `tools/models.json` 的 `biases` 数组末尾加 `{ "id", "zh" }`，编号接着 39 往下排
2. 在 `BIAS-CORRECTION.md` 对应分类末尾写正文：`**编号. 名称** | 表现 | 纠正`
3. 需要出现在交叉引用里时，在 `tools/models.json` 的 `crossref` 加一条（`tm` 可为 null）
4. 运行 `python3 tools/gen.py` + `python3 tools/check.py`

### 改完必须验证
```bash
python3 tools/gen.py --check   # 生成物是否与真源同步
python3 tools/check.py         # 编号 / 断链 / 版本 / 数量声明 / 文件全覆盖
```
两条都退出 0 才算改完。

### 改了 SKILL.md 的判定规则或输出要求
再跑一遍行为回归（需要模型访问，纯文档改动不必跑）：

```bash
python3 tools/regress.py --repeat 3                                    # 本机 ollama
TM_API_KEY=... python3 tools/regress.py --api anthropic --model ...    # 云端
```

看结尾的 `done; failures=N truncated=M`，退出码非 0 就是有门禁没过。文本缓存在 `/tmp/tm_regress.json`：只改门禁逻辑时直接复评旧文本，加 `--refresh` 才重新采样。

### 报告问题
- 模型描述不清晰
- 匹配不准确
- 输出质量问题

请开 issue 描述具体场景和期望改进。

## 风格指南
- 每个模型/偏误控制在 1-2 行
- 信号描述要具体（"什么时候想到用"）
- 检查问题要可操作（"问自己什么"）
- 公式要一句话能说清
