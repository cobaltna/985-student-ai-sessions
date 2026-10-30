# 数据格式说明

## conversation.md（人类可读转录）

按消息时间顺序排列，每条消息的渲染规则：

```markdown
## 👤 用户（2026-09-30 14:22）     ← 用户原始输入（含 📎 附件名）

<details><summary>💭 思考链（deepseek-v4.1-flash）</summary>   ← 模型完整思考过程
...
</details>

- 🔧 **Read** `{"file_path": "..."}` → `文件内容前几百字…`      ← 工具调用：名称、输入摘要、结果摘要

### 🤖 助手（deepseek-v4.1-flash，2026-09-30 14:25）           ← 最终回复
...
```

说明：

- 思考链为模型原始 reasoning 文本，未做改写（英文/中文混杂取决于模型）
- 工具调用的输入/结果为**摘要**（防止转录爆炸）；完整内容看 `session.jsonl`
- 会话 ID、绝对路径中的用户名已统一为 `UserX`

## session.jsonl（蒸馏/训练用）

每行一个 JSON：

```json
{
  "role": "user" | "assistant",
  "time": "2026-09-30 14:22",
  "model": "deepseek-v4.1-flash",        // assistant 消息上，来自消息元数据
  "agent": "zcode-documents:visual-judge", // 子代理名，主线程为 null
  "thinking": "完整思考链原文",            // 可能为 null
  "content": "回复正文",
  "tool_calls": [                         // 可能为 null
    {"tool": "Bash", "input": "JSON字符串(截断至6000字符)",
     "output": "结果(截断至4000字符)", "status": "completed"}
  ],
  "attachments": 2                        // 仅 user 消息：附件数
}
```

- `input`/`output` 为脱敏后的字符串（不是结构化 JSON），超长已截断并标注原长
- 一个 assistant 消息可能同时含 thinking、content 与 tool_calls

## meta.json

```json
{
  "session_id": "sess_xxx", "zcode_title": "ZCode 自动起的标题（仅参考）",
  "dominant_model": "...", "models_in_msgs": {"模型ID": 消息数},
  "models_usage": {"模型ID": [输入tokens, 输出tokens]},
  "tools": {"Bash": 85, "Read": 10, "Skill": 1}, "skills": {"skill名": 次数},
  "t_start": "...", "t_end": "...", "msgs": 118, "user_msgs": 2,
  "write_paths": ["该会话写过的文件"], "edit_paths": ["该会话改过的文件"],
  "subagent_sessions": [{"id": "...", "md_kb": 12, "jl_msgs": 34, ...}]
}
```

## 模型 ID 对照

| 转录中的 modelId | 实际模型 |
|---|---|
| deepseek-flash / deepseek-v4-flash | DeepSeek V4 Flash |
| deepseek-v4.1-flash | DeepSeek V4.1 Flash |
| deepseek-v4-pro | DeepSeek V4 Pro |
| GLM-5.3-Flash | 智谱 GLM-5.3-Flash |
| GLM-5.3 | 智谱 GLM-5.3 |
| gpt-6-astra | GPT-6-Astra |
| gpt-5.6-sol / gpt-6.1-sol | GPT-5.6-Sol / GPT-6.1-Sol |
| kimi-k3 | Kimi K3 |
| DeepSeek-V4-Flash[free] | DeepSeek V4 Flash（免费分组） |

## 复现环境备注

原始数据来自 ZCode 本地 SQLite（`~/.zcode/cli/db/db.sqlite` 的 session/message/part 表）与 artifacts 目录，导出脚本未随仓库发布（内含脱敏规则的真实匹配串，发布即泄密）。格式本身足够清晰，可自行写解析器。
