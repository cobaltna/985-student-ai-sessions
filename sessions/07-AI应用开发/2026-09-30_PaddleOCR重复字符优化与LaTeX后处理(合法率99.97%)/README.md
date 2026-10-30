# PaddleOCR重复字符优化与LaTeX后处理(合法率99.97%)

- **日期**：2026-09-30 10:23 → 2026-10-04 21:57
- **模型**：DeepSeek V4 Flash / GLM-5.3-Flash
- **规模**：252 条消息，9 轮用户输入

## 这个会话做了什么

排查 PaddleOCR 重复字符/无限重复问题（对照官方环境版本与 issue 区），用官方测试集做大规模验证（57 页全量+3600 个数学片段），写出 LaTeX 后处理器把语法缺陷率从 0.81% 降到 0.03%，并整理出 local-ocr skill。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
