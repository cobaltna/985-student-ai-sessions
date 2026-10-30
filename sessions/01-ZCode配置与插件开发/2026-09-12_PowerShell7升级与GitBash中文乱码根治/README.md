# PowerShell7升级与GitBash中文乱码根治

- **日期**：2026-09-12 17:20 → 2026-09-12 17:58
- **模型**：DeepSeek V4 Flash
- **规模**：108 条消息，5 轮用户输入

## 这个会话做了什么

升级 PowerShell 7 并设为默认，随后系统性根治 Git Bash/PowerShell/Python 混用时的中文乱码：逐字节验证各解释器输出编码，给出「日志重定向用 bash、pwsh 输出前设 UTF8」等硬规则，并把结论沉淀进 AGENTS.md 与 python-envs 记忆。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
