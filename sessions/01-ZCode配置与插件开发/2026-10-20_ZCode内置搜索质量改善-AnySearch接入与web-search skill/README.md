# ZCode内置搜索质量改善-AnySearch接入与web-search skill

- **日期**：2026-10-20 20:32 → 2026-10-21 17:40
- **模型**：DeepSeek V4.1 Flash
- **规模**：376 条消息，5 轮用户输入

## 这个会话做了什么

先实测验证 ZCode 内置搜索质量确实差（bing 关键词匹配差、360/搜狗无高质量结果），再接入 Tavily/Firecrawl/AnySearch 三个搜索 API 做质量对比，最后收敛为 AnySearch+Firecrawl 双后端的 web-search skill，并按用户要求删掉画蛇添足的自建排序。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
