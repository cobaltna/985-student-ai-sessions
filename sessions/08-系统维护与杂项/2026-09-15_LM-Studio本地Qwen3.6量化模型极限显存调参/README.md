# LM-Studio本地Qwen3.6量化模型极限显存调参

- **日期**：2026-09-15 00:47 → 2026-09-15 00:58
- **模型**：DeepSeek V4 Flash / GPT-6-Astra
- **规模**：6 条消息，2 轮用户输入

## 这个会话做了什么

RTX 4060 8G 显存 + 16G 内存极限运行 Qwen3.6 27B IQ4_XS 量化的参数配置问答，含 MTP 设置与关闭思考模式的 Jinja 模板改法。短问答。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
