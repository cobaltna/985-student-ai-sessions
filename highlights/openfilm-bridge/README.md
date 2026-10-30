# ZCode × OpenFilm 接入说明

把 ZCode 挂进 OpenFilm 桌面版右侧的对话窗口。OpenFilm 只认 **ACP（Agent Client Protocol）**
智能体，ZCode 没有 ACP 服务端，所以这里用一个桥接进程，把 ACP 翻译成 ZCode 的无头命令行。

```
OpenFilm 聊天窗口 ──ACP/stdio──▶ bridge.mjs ──zcode -p --output-format stream-json──▶ ZCode
                                    │
                                    └─ 会话映射：ACP sessionId ↔ ZCode sess_xxx（--resume 续聊）
```

## 文件

| 路径 | 作用 |
|---|---|
| `C:\Users\UserX\.zcode\openfilm-bridge\bridge.mjs` | ACP 服务端 ↔ ZCode 桥接（无依赖） |
| `C:\Users\UserX\.zcode\openfilm-bridge\bin\openfilm` | 给 ZCode 用的 `openfilm` 命令（POSIX sh） |
| `C:\Users\UserX\.zcode\openfilm-bridge\bin\openfilm.cmd` | 同上，给 cmd.exe 用 |
| `C:\Users\UserX\.zcode\openfilm-bridge\sessions.json` | ACP 会话 → ZCode 会话的映射（30 天自动清理） |
| `C:\Users\UserX\.zcode\openfilm-bridge\install.mjs` | 挂载 / 卸载 / 查看状态 |
| `C:\Users\UserX\.zcode\openfilm-bridge\acp-test.mjs` | 不经过 GUI 的 ACP 冒烟测试 |
| `C:\Users\UserX\AppData\Roaming\OpenFilm\agents.json` | OpenFilm 的智能体选择（`paths.deepseek` 指向桥接） |
| `C:\Users\UserX\.zcode\skills\openfilm\SKILL.md` | 官方 openfilm skill（ZCode 侧） |

## 日常使用

1. 打开 OpenFilm → 右侧聊天窗 → 底部右下角的智能体菜单里选 **ZCode**。
2. 直接说要做什么，例如「把标题改成 X 并延长到 5 秒，改完跑 openfilm look」。
3. 改动实时写进工程目录，Studio 立刻刷新；工具调用以条目形式显示在对话里。

**不需要先跑 `openfilm open`**：OpenFilm 已经把 Studio 开在这个工程上，桥接会把
`openfilm` 命令放进 ZCode 的 PATH。

## 维护命令

```bash
cd /c/Users/UserX/.zcode/openfilm-bridge

node install.mjs --status    # 现在挂在哪个槽位
node install.mjs             # 挂到 deepseek 槽位（默认，本机未装 DeepSeek Harness）
node install.mjs --slot kimi # 换一个槽位（codex/claude/copilot/cursor/opencode/
                             # codebuddy/qwen/kimi/minimax/deepseek）
node install.mjs --remove    # 卸载

node acp-test.mjs --cwd .            # 桥接冒烟测试：新建 / 工具 / 续聊
node acp-test.mjs --cwd . --cancel   # 再加上取消
```

改完 `agents.json` 需要重启 OpenFilm 才生效。

## 为什么不能直接加一个「ZCode」菜单项

OpenFilm 的智能体清单写死在 `resources/app.asar` 里（`agent-definitions.mjs`、
`agents.mjs`、`shell/dist/assets/*.js` 三处都有一份 id 列表），并且 asar 开了
**完整性校验**（`EnableEmbeddedAsarIntegrityValidation`，哈希内嵌在 `OpenFilm.exe`）。
改包会导致应用无法启动。所以只能占用一个已有槽位——本机选了 `deepseek`
（DeepSeek Harness 未安装，是唯一完全空闲的槽位）。

槽位名在「设置 → 智能体」里仍显示为 “DeepSeek Harness”，但聊天窗底部的选择器
显示的是 **ZCode**：桥接在 ACP 里报了一个 `model` 配置项，名字就是 ZCode。

## 桥接做了什么

- **会话**：`session/new` 生成 ACP 会话 id；第一次 `session/prompt` 时把 ZCode 返回的
  `sess_xxx` 记下来，之后每轮加 `--resume sess_xxx`，所以同一对话有上下文。
- **流式**：`model.streaming` 的 `text_delta` → `agent_message_chunk`，
  `reasoning_delta` → `agent_thought_chunk`（ZCode 的推理过程）。
- **工具**：`tool_call` / `tool.updated` 映射成 ACP 的 `tool_call`、`tool_call_update`
  （Read→read、Write/Edit→edit、Grep/Glob→search、Bash→execute、WebFetch→fetch…），
  并提供 `locations`，Studio 里可以点开对应文件。
- **取消**：`session/cancel` 杀掉 ZCode 进程树，回 `stopReason: cancelled`。
- **图片**：ACP 的 image 块落到临时文件，用 `--attach` 交给 ZCode。
- **长消息**：超过 Windows 命令行上限（约 20k 字符）时改成附件投递。
- **模式**：`--mode yolo|build|edit|plan`，默认 `yolo`（`-p` 的默认行为）。

## 两个本机环境坑（已在桥接里绕开）

1. **中文用户名**：真实 profile 是 `C:\Users\UserX`。OpenFilm 自带的
   `%APPDATA%\OpenFilm\bin\openfilm.cmd` 里写死了这个路径，cmd.exe 按 OEM 代码页
   读 `.cmd` 会把它读成乱码（实测 `C:\Users\钂嬫旦瀹嘰...`），命令直接失败。
   桥接改用自己写的 shim（内容全是 ASCII + 环境变量展开），并把它的目录放在
   ZCode 的 PATH 最前面。

2. **ZCode 的环境变量**：`zcode.cjs` 依赖 `ZCODE_BUILTIN_PROVIDER_CONFIG_FILE`
   （不设就报「无法定位 CLI ZCode Built-in Provider Config」），而这个变量只在
   ZCode 自己的进程树里才有。桥接启动 ZCode 时会扫描
   `%USERPROFILE%\.zcode\v2\runtime\provider\<platform>-<arch>\<version>\endpoint-*`
   找到最新的 `zcode-builtin.json` 并注入；同时补上
   `ZCODE_PERSONAL_PROVIDER_CONFIG_FILE`。

## 已知限制

- **审批**：ZCode 以 `-p` 运行时不需要逐条批准，工具全部自动执行（等价 `yolo`）。
  OpenFilm 的「允许/拒绝」按钮不会出现。
- **没有真正的 token 流中断**：每轮是「启动 zcode → 读事件 → 进程退出」，
  所以一轮结束前上下文都留在 ZCode 侧；中途 `Esc` 会杀进程，ZCode 那边保留的部分
  结果不会被 resume 回来（ZCode 只在 turn 结束时落盘）。
- **模型列表**：桥接只报一个 `ZCode` 项（用 ZCode 自己配置的模型）。想换模型请在
  ZCode 里切，或改 `bridge.mjs` 的 `MODEL_OPTION()`。
- **升级 OpenFilm**：`agents.json` 一般会保留；若被重置，重跑 `node install.mjs`。
  升级 ZCode 后桥接通常无需改动（只用 `-p/--json/--output-format/--resume/--attach`）。
- **槽位冲突**：如果你以后真的装了 DeepSeek Harness，它会占用同一个槽位；
  用 `node install.mjs --slot <另一个空槽>` 挪走。
