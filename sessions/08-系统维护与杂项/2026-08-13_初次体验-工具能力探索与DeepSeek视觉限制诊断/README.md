# 初次体验-工具能力探索与DeepSeek视觉限制诊断

- **日期**：2026-08-13 01:02 → 2026-09-30 12:00
- **模型**：DeepSeek V4 Flash / DeepSeek V4 Flash (free) / DeepSeek V4 Pro
- **规模**：16 条消息，7 轮用户输入

## 这个会话做了什么

2026-08-13 的第一次正式会话：问 ZCode 能调用哪些工具、chat/completions 与 responses 接口区别，随后排查上传图片报 400 的原因，结论是 DeepSeek V4 Pro 接口只支持 text 内容块、不支持视觉输入。适合了解一个新手如何摸清 coding agent 的能力边界。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
