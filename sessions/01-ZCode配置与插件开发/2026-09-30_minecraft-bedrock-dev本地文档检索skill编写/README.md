# minecraft-bedrock-dev本地文档检索skill编写

- **日期**：2026-09-30 11:55 → 2026-09-30 11:57
- **模型**：GLM-5.3-Flash
- **规模**：9 条消息，1 轮用户输入

## 这个会话做了什么

用 skill-creator 写了一个不到 50 行的 skill：查基岩版 API/JSON 字段时先搜本地 900 个爬取文档，搜不到才上网且只认官方源。小 skill 的设计取舍示范。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
