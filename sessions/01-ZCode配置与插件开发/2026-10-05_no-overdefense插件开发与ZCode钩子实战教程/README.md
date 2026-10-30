# no-overdefense插件开发与ZCode钩子实战教程

- **日期**：2026-10-05 01:03 → 2026-10-27 23:19
- **模型**：GLM-5.3 / GLM-5.3-Flash
- **规模**：140 条消息，9 轮用户输入

## 这个会话做了什么

从「AI 过度防御性编程」的痛点出发：检查已有 skill 的过度约束 → 精简为 1000 字 skill + 1 个钩子 → 因 ZCode 钩子触发 bug 改走插件通道 → 模拟真实项目测试副作用 → ZCode 更新后验证补丁仍在。完整的「痛点→skill→hook→插件」开发闭环，插件源码在 highlights/ 里有收录。

## 文件

- `conversation.md` — 人类可读转录：用户输入 / 思考链（折叠块）/ 工具调用及结果摘要 / 助手回复
- `session.jsonl` — 机器可读版（蒸馏用）：每行一条消息，含 thinking / content / tool_calls
- `meta.json` — 模型用量、工具统计、产物路径等元数据
