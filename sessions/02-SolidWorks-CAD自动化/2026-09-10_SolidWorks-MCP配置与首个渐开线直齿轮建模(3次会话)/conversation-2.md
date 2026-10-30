## 👤 用户（2026-09-10 23:40）

帮我配置好solidworks的mcp。mcp代码我已经下载了："C:\Users\UserX\Downloads\mcp-server-solidworks-main"

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The user wants me to configure the SolidWorks MCP server. They downloaded the code to "C:\Users\UserX\Downloads\mcp-server-solidworks-main". Let me explore that directory first.

Interestingly, the SolidWorks MCP tools are already available in my tool list (mcp__solidworks__*). But maybe the user wants it configured properly in ZCode. Let me check.

Let me explore the downloaded directory.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\"", "description": "List downloaded MCP server directory"}` → `total 5269 drwxr-xr-x 1 user 197121 0 Sep 10 19:50 . drwxr-xr-x 1 user 197121 0 Sep 10 21:42 .. -rw-r--r-- 1 user 197121 1218 Sep 10 19:44 .gitignore drwxr-xr-x 1 user 197121 0 Sep 10 19:51 .venv -rw-r--r-- 1 user 197121 3059 Sep 10 19:44 CLA.md -rw-r--r-- 1 user 197121 11272 Sep 10 19:44 CONTRIBUTING.md -rw-r--r-- 1 u …[截断,原长793]`

- 🔧 **Bash** `{"command": "cat \"C:/Users/UserX/.zcode/config.json\" 2>/dev/null || ls \"C:/Users/UserX/.zcode/\"", "description": "Check ZCode config"}` → `AGENTS.md cli memory skills v2 workspace`

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

我先看看你下载的 MCP 代码结构。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me look at the structure more. Let me find the config file for MCP. ZCode config might be at ~/.zcode/cli/... Let me check.

Also there's a .venv already, suggesting partial setup. Let me look at the repo structure.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && find . -maxdepth 3 -type f -name \"*.md\" -o -maxdepth 3 -type f -name \"*.json\" -o -maxdepth 3 -type f -name \"*.toml\" -o -maxdepth 3 -type f -name \"*.py\" | grep -v \".venv\" | head -60", "description": "Find config and entry files"}` → `./adapters/claude/adapter_log.py ./adapters/claude/architecture.md ./adapters/claude/config.py ./adapters/claude/execution_client.py ./adapters/claude/ir_execution_port.py ./adapters/claude/response_mapper.py ./adapters/claude/server.py ./cad-planner/architecture.md ./cad-planner/contracts/analysis-artifact.schema.json …[截断,原长1022]`

- 🔧 **Bash** `{"command": "ls -la \"C:/Users/UserX/.zcode/cli/\" && find \"C:/Users/UserX/.zcode\" -maxdepth 2 -name \"*.json\" 2>/dev/null", "description": "Look for ZCode config files"}` → `total 25 drwxr-xr-x 1 user 197121 0 Sep 10 19:53 . drwxr-xr-x 1 user 197121 0 Sep 9 23:31 .. drwxr-xr-x 1 user 197121 0 Sep 10 00:59 agents drwxr-xr-x 1 user 197121 0 Sep 10 19:51 artifacts -rw-r--r-- 1 user 197121 550 Sep 10 19:53 config.json drwxr-xr-x 1 user 197121 0 Aug 13 01:01 db drwxr-xr-x 1 user 197121 0 Sep 10 …[截断,原长763]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me look at the README for installation instructions, and check existing config.

</details>

- 🔧 **Bash** `{"command": "cat \"C:/Users/UserX/.zcode/cli/config.json\"; echo \"=== V2 CONFIG ===\"; cat \"C:/Users/UserX/.zcode/v2/config.json\" | head -100", "description": "Read ZCode config files"}` → `{ "mcp": { "servers": { "blockbench": { "type": "http", "url": "http://localhost:3000/bb-mcp" }, "solidworks": { "type": "stdio", "command": "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\.venv\\Scripts\\python.exe", "args": [ "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\adapters\\claude\\server …[截断,原长1976]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && head -150 README.md", "description": "Read README installation section"}` → `# SolidPilot **AI-driven CAD automation for SolidWorks — an MCP (Model Context Protocol) server.** <p align="center"> <img src="sample.gif" alt="SolidPilot Demo"> </p> SolidPilot lets an AI model work with SolidWorks at the **CAD feature level**. The goal is for the model to reason in terms of "which CAD intent am I re …[截断,原长11260]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Interesting — the solidworks MCP is ALREADY configured in `C:/Users/UserX/.zcode/cli/config.json`. And the tools are already available to me (mcp__solidworks__*). So maybe it's already working? Or maybe it was configured but not fully working.

Let me check the README installation instructions to see what's needed: the execution layer is C# .NET Framework 4.8, needs building. And the python venv exists.

Let me read the installation section of README.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && grep -n -i \"install\\|setup\\|prerequisit\\|dotnet\\|msbuild\\|python\\|venv\\|requirement\\|Execution\" README.md | head -80", "description": "Find install/setup sections in README"}` → `11:SolidPilot is **not** a Claude-only plugin; it is **a general bridge between SolidWorks and AI.** Because MCP is an open standard, any MCP-capable AI client can connect — alongside Claude, OpenClaw, OpenAI-based agents, and local LLMs are also targeted. The architecture was designed for this extensibility **from the …[截断,原长5420]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && cat requirements.txt && echo \"=== .venv ===\" && ls .venv/ && ls .venv/Scripts/ 2>/dev/null | head -20", "description": "Check requirements and venv"}` → `mcp>=2.0.0,<3 # official MCP Python SDK v2 (protocol 2026-07-28) httpx>=0.27.0 python-dotenv>=1.0.0 === .venv === CACHEDIR.TAG Lib Scripts pyvenv.cfg share activate activate.bat activate.csh activate.fish activate.nu activate.ps1 activate_this.py cffi-gen-src.exe deactivate.bat dotenv.exe ezdxf.exe f2py.exe fonttools.e …[截断,原长465]`

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

MCP 已经在配置里了。我看看完整安装要求，确认执行层（C# 服务）是否已就绪。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

So the venv exists with dependencies. The config is already registered in ZCode (`C:/Users/UserX/.zcode/cli/config.json`). The MCP tools are already available to me. So the main missing piece is likely:

1. The C# execution layer built (SolidworksExecution.exe) and running on localhost:5000.

Let me check whether the execution layer is built.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && find execution -type f \\( -name \"*.exe\" -o -name \"*.sln\" -o -name \"*.csproj\" \\) 2>/dev/null; echo \"=== bin dirs ===\"; ls -d execution/solidworks/*/bin 2>/dev/null; echo \"=== port 5000 ===\"; netstat -ano | grep \":5000\" | head -5", "description": "Check if execution layer is built or running" …[截断,原长381]` → `execution/solidworks/SolidworksExecution/bin/Debug/SolidworksExecution.exe execution/solidworks/SolidworksExecution/SolidworksExecution.csproj execution/solidworks/SolidworksExecution.sln === bin dirs === execution/solidworks/SolidworksExecution/bin === port 5000 === TCP 0.0.0.0:5000 0.0.0.0:0 LISTENING 4 TCP [::]:5000 …[截断,原长428]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && cat adapters/claude/config.py", "description": "Read adapter config for execution URL"}` → `import os from dotenv import load_dotenv # Load adapters/claude/.env by EXPLICIT path. A bare load_dotenv() searches the current working # directory, but the MCP host launches server.py from an arbitrary cwd, so the adapter's own .env # was silently missed. Anchor it to this file's directory. load_dotenv(os.path.join(o …[截断,原长1624]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Everything looks already set up:
- venv with deps ✓
- C# execution built ✓
- Port 5000 listening ✓ (though PID 4 is the System process... hmm, that's the "System" process which is weird. Actually PID 4 on Windows is the System process — that usually means something like HTTP.sys reserving the port. Actually port 5000 could be reserved by another service. Let me check)

Wait, PID 4 = System. That means port 5000 is held by System/HTTP.sys — which could be the .NET HttpListener running under a service? Actually a .NET HttpListener (HttpListener uses http.sys) run by a user process would show the process PID, not 4. Hmm, actually when HttpListener registers a URL prefix, http.sys holds the port on behalf of the process, and netstat shows PID 4 (System). So it could indeed be our execution server running with HttpListener.

Let me actually test the connection with ensure_ready to see if it's working end-to-end.

Actually, let me first just test the health endpoint.

</details>

- 🔧 **Bash** `{"command": "curl -s -m 10 http://localhost:5000/health; echo \"\"; echo \"--- exit: $? ---\"", "description": "Test execution layer health endpoint"}` → `{"status":"UP","stateVersion":59,"serverTimeUtc":"2026-09-10T15:40:53.3226715Z","comAttached":true,"activeDocument":null,"solidworksProcessCount":1,"solidworksPids":[21248],"solidworksWindowless":0} --- exit: 0 ---`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && ls -la adapters/claude/ && cat adapters/claude/.env 2>/dev/null || echo \"(no .env)\"", "description": "Check adapter dir and .env"}` → `total 222 drwxr-xr-x 1 user 197121 0 Sep 10 20:24 . drwxr-xr-x 1 user 197121 0 Sep 10 19:44 .. -rw-r--r-- 1 user 197121 223 Sep 10 20:24 .env drwxr-xr-x 1 user 197121 0 Sep 10 19:51 __pycache__ -rw-r--r-- 1 user 197121 17013 Sep 10 20:25 adapter.log -rw-r--r-- 1 user 197121 842 Sep 10 19:44 adapter_log.py -rw-r--r-- 1  …[截断,原长1116]`

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

配置和依赖看起来都已就绪。我实际测一下连通性。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Everything is already fully working! The execution layer is UP, COM attached, SolidWorks running (PID 21248, 1 process). 

So the setup is done already. But wait — the user asked me to configure it. Maybe they set it up manually before and want me to verify/complete it? Or maybe they don't know it's already configured.

Let me check the adapter.log to see if the MCP adapter is actually connected and working in ZCode. Also let me test the MCP tools directly via my own tool access.

Actually, the tools ARE in my tool list (mcp__solidworks__*), so the MCP server is loaded. Let me verify by calling ensure_ready or verify_state.

Let me check whether there are gaps:
1. Is `EXECUTION_EXE_PATH` auto-start working? Yes apparently.
2. Is the MCP registered at user scope or workspace scope? It's in `C:/Users/UserX/.zcode/cli/config.json` which is the user-level CLI config.

Hmm, but the user said "帮我配置好 solidworks 的 mcp" — help me configure it. Let me check the state of things and see if the tools actually respond. Let me call verify_state via the MCP tool.

Let me also check the adapter log for errors.

Let me do a real end-to-end test.

</details>

- 🔧 **mcp__solidworks__verify_state** `{}` → `MCP tool returned an error: Error executing tool verify_state Structured content: `

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/mcp-server-solidworks-main\" && tail -30 adapters/claude/adapter.log", "description": "Check adapter log tail"}` → `2026-09-10 20:23:17.322 -> create_sketch op=ebae31c3-46d8-4f7e-b29a-9af944e115b8 sv=55 2026-09-10 20:23:17.644 <- create_sketch COMPLETED sv=56 2026-09-10 20:23:17.646 -> add_sketch_entities op=17027376-53bf-49d1-8720-d56a8e54af76 sv=56 2026-09-10 20:23:18.167 <- add_sketch_entities COMPLETED sv=57 2026-09-10 20:23:18. …[截断,原长2176]`

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

执行层已在运行，COM 已连接。我直接调 MCP 工具做端到端验证。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now I see the real situation:

1. The MCP **is** configured and connected (the adapter log shows successful calls, and my tool call reached the adapter).
2. The `verify_state` error is `NO_ACTIVE_DOCUMENT` — that's because no document is open in SolidWorks. That's expected behavior, not a config failure. But the error surfaced oddly with empty structured content.

Wait, but the error message I got back is "Error executing tool verify_state" with empty structured content. That's the adapter returning an error. Expected since no active document.

So actually the MCP setup seems complete. But let me check the full error - the tool returned an error. Let me try ensure_ready which is the safe idempotent call.

Actually, let me re-read the user request: "帮我配置好solidworks的mcp。mcp代码我已经下载了" — Help me configure the SolidWorks MCP. I already downloaded the code.

Given the config exists already, maybe a previous session (or the user) already did part of it. Let me verify the whole thing works properly. The most likely remaining issue is the error format or something. Let me test ensure_ready.

Also important: the MCP config is in `C:/Users/UserX/.zcode/cli/config.json`. But is that the right place for the current ZCode version? There's also `C:/Users/UserX/.zcode/v2/`. Let me check the zcode-guide skill for where MCP config should live.

Actually the tools ARE available to me, which proves the config is being read and the server is loading. So config location is correct.

Let me test ensure_ready to be thorough.

Hmm, but there's a subtlety: the error return had "Structured content:" empty. Let me check if that's a problem with the adapter's error handling. Let's test with ensure_ready first.

Let me also consider: maybe the user wants it configured so it works reliably. Let me test the full chain.

Let me call ensure_ready.

</details>

- 🔧 **mcp__solidworks__ensure_ready** `{}` → `READY | server=UP | com_attached=True | sw_launched=False | active_document=None | sw_version=34.3.2 | state_version=59 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

MCP 已连上（日志显示调用都成功）。`verify_state` 报的 `NO_ACTIVE_DOCUMENT` 是没开文档，属正常。我跑一次完整链路验证。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The MCP is working. So the setup is essentially complete already. Let me test creating a part to fully verify.

Actually, let me think about what "配置好" means and whether there are gaps:

1. ✅ Code downloaded
2. ✅ Python venv with deps
3. ✅ C# execution layer built
4. ✅ Execution server running (port 5000, auto-start capable)
5. ✅ MCP registered in ZCode config
6. ✅ Tools available and responding

Potential gaps:
- The `open_new_part` etc. — let's test.
- Maybe the user wants the execution server to auto-start on boot? config.py mentions auto-start of the exe by the adapter.

Let me do an end-to-end smoke test: open new part + analyze. That validates the whole chain.

Let me be careful not to disturb the user's open SolidWorks session. There's 1 SolidWorks process running. Opening a new part creates a document. That's a benign operation, but let me ask... actually the user asked me to configure and verify — a smoke test is reasonable and non-destructive (I can close the document after without saving).

Let me do it.

Actually, wait. Let me first check: the user may have previously partially configured. Let me check if there's an issue that the config.json in .zcode/cli is workspace-scoped or user-scoped, and whether MCP is enabled. Since tools work, it's fine.

Let me run a smoke test with open_new_part → analyze_model(geometry) → close without saving.

Actually, since the user has SolidWorks open with possibly unsaved work, opening a new part is safe (SolidWorks supports multiple documents). Let me do it, then close only the new one.

Let me run the test.

</details>

- 🔧 **mcp__solidworks__open_new_part** `{}` → `COMPLETED | state_version=60 | document=零件1 | sketch=None | features=[] Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:40）

MCP 全链路已通（SolidWorks 34.3.2 = 2026）。我做个实际建模冒烟测试，确认工具真能操作 SolidWorks。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

A new part opened. Now let me create a sketch and extrude to fully test. Then clean up by closing without saving.

Let me do a quick build: sketch on Front Plane, rectangle, extrude.

</details>

- 🔧 **mcp__solidworks__create_sketch** `{"plane": "Front Plane"}` → `COMPLETED | state_version=61 | document=零件1 | sketch=草图1 | features=[] | result_geometry={"frame": {"origin": [0.0, 0.0, 0.0], "xdir": [1.0, 0.0, 0.0], "ydir": [0.0, 1.0, 0.0]}, "ref": "Front Plane"} Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me continue the smoke test: add rectangle, extrude, analyze, then close without saving.

Actually, let me finish the test quickly.

</details>

- 🔧 **mcp__solidworks__add_sketch_entity** `{"entity_type": "rectangle", "x1": 0, "y1": 0, "x2": 0.05, "y2": 0.03}` → `COMPLETED | state_version=62 | document=零件1 | sketch=草图1 | features=[] | result_geometry={"kind": "rectangle", "segments": [{"construction": false, "kind": "line", "x1": 0.0, "y1": 0.0, "x2": 0.05, "y2": 0.0}, {"construction": false, "kind": "line", "x1": 0.0, "y1": 0.0, "x2": 0.0, "y2": 0.03}, {"construction": false,  …[截断,原长493]`

- 🔧 **mcp__solidworks__extrude_feature** `{"feature_type": "boss", "depth": 0.02}` → `COMPLETED | state_version=63 | document=零件1 | sketch=None | features=['凸台-拉伸1'] | result_geometry={"volume": 3e-05, "faces": 6, "edges": 12} Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The full chain works: volume = 3e-05 m³ = 30,000 mm³ = 50×30×20 mm. Correct.

Now let me clean up — close the document without saving.

Then report to the user.

Let me also check the drawing/DXF analyze path works offline? Not needed.

Let me close the document without saving.

</details>

- 🔧 **mcp__solidworks__close_document** `{"save": false}` → `COMPLETED | state_version=64 | document=None | sketch=None | features=[] Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:41）

建模链路完全正常（50×30×20mm → 体积 3e-05 m³ 正确）。清理测试文档。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Everything works. Now let me give the user a clear report.

But wait — I should double check whether the user's config is actually complete/ideal. Let me review the whole situation and see if there's anything I should improve:

1. The config in `C:\Users\UserX\.zcode\cli\config.json` — is this user-level or workspace-level? It's under `.zcode/cli/` which looks like user-level CLI config. Good — works everywhere.

2. Auto-start of execution server: config.py auto-spawns the exe. But is that working? Port 5000 is up with COM attached, so yes something is running.

3. Potential issue: the execution server exe is launched manually or auto? Let me check if there's a running SolidworksExecution.exe process.

Actually, one thing worth verifying: does the whole thing survive a restart? The adapter auto-spawns the exe if not running (SERVER_SPAWN_TIMEOUT). That's built in.

Let me check if there's a concern about the `.venv` python path hardcoded — it's fine.

Let me verify the execution process is running as a user process.

Also, I should consider whether the user might want it registered at a different scope or whether there's a ZCode "mcp add" command preferred. Since it works, leave it.

Let me do a final check of running processes and then report.

Actually, let me reconsider — maybe the user's intent is that they downloaded the code fresh and the config I see was set up by me/them earlier in a prior session. The task now is just to confirm it's configured. I've verified it end-to-end.

But let me be thorough about one more thing: is the execution server set to auto-start, or will the user need to launch it manually every reboot? Let me check for a scheduled task / startup entry, and check the process.

Let me check processes.

</details>

- 🔧 **Bash** `{"command": "tasklist 2>/dev/null | grep -i \"solidworks\\|SolidworksExecution\" | head -10; echo \"=== startup entries ===\"; ls \"$APPDATA/Microsoft/Windows/Start Menu/Programs/Startup/\" 2>/dev/null; echo \"(none above = no autostart)\"", "description": "Check running processes and startup entries"}` → `SolidworksExecution.exe 21972 Console 1 51,284 K === startup entries === desktop.ini 发送至 OneNote.lnk (none above = no autostart)`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The execution server is running as PID 21972 (user process). No autostart entry, but the adapter auto-spawns it via `EXECUTION_EXE_PATH` when it's not running. That's the built-in mechanism, so no autostart shortcut is needed.

Everything is configured and verified. Let me report.

Let me summarize what's in place and what I verified. I should be concise but complete.

One more consideration: SolidWorks itself has a process too? The health said solidworksProcessCount: 1, solidworksPids: [21248]. But tasklist didn't show SLDWORKS.exe in grep... because grep -i solidworks should match SLDWORKS.EXE. Hmm, it only showed SolidworksExecution.exe. Maybe SolidWorks was closed since. Let me not worry.

Actually the health check earlier said solidworksProcessCount: 1. And after close_document, SolidWorks may have been shut down if it was windowless/auto. Let me just re-verify health to report accurate state.

Let me do a final health check.

</details>

- 🔧 **Bash** `{"command": "curl -s -m 10 http://localhost:5000/health", "description": "Final health check"}` → `{"status":"UP","stateVersion":64,"serverTimeUtc":"2026-09-10T15:41:24.8633840Z","comAttached":true,"activeDocument":null,"solidworksProcessCount":1,"solidworksPids":[21248],"solidworksWindowless":0}`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Everything is up. SolidWorks is running (PID 21248), COM attached, execution server up, MCP registered and tools responding.

Let me write the final report. Concise, faithful, with the evidence.

Note: I should mention that the config was already in place (probably from a previous session) and I verified it end-to-end rather than claiming I set it up. Be honest.

Actually — hold on. Let me reconsider whether I actually did anything. The user asked me to configure it. It was already configured. I verified it. I should say that plainly: it's already configured and working; here's the evidence; here's what would need to change if something breaks.

Let me also provide the useful facts: config location, each layer, how to restart.

Let me write the report in Chinese since the user writes Chinese.

I should double-check one thing — the MCP config file location. Is `C:\Users\UserX\.zcode\cli\config.json` the user-scope config? Yes it seems so (under the user's home .zcode). Good.

Let me write it up.

</details>

### 🤖 助手（deepseek-v4-flash，2026-09-10 23:41）

SolidWorks MCP 已经**完全配置好并跑通了** —— 实际上配置早已就位（配置文件和依赖都在），我这次做的是端到端验证。下面是实测结果。

## 验证结果（全部实测，非推断）

**MCP 注册** — `C:\Users\UserX\.zcode\cli\config.json`（用户级，对所有工作区生效）：
```json
"solidworks": {
  "type": "stdio",
  "command": "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\.venv\\Scripts\\python.exe",
  "args": ["...\\adapters\\claude\\server.py"],
  "cwd": "...\\adapters\\claude",
  "timeoutMs": 300000
}
```

**四层链路逐层确认：**

| 层 | 状态 | 证据 |
|---|---|---|
| Python 适配器 | ✅ 已安装 | `.venv` 内 mcp / httpx / ezdxf 齐全，且我调用工具成功到达适配器（adapter.log 有记录） |
| C# 执行层 | ✅ 已编译且在跑 | `SolidworksExecution.exe` PID 21972，`/health` 返回 `"status":"UP"` |
| COM 连接 | ✅ 已连接 | `comAttached: true`，SolidWorks 进程 PID 21248 在运行 |
| MCP 工具 | ✅ 可调用 | 见下方冒烟测试 |

**端到端冒烟测试**（真在 SolidWorks 里建了模型再删掉）：
- `open_new_part` → 零件1
- `create_sketch` Front Plane → 草图1
- `add_sketch_entity` 矩形 50×30mm
- `extrude_feature` 拉伸 20mm → 返回 **volume = 3e-05 m³（=30000 mm³，50×30×20 完全正确）**，6 面 12 边
- `close_document` 不保存 → 已清理，没留垃圾文件

## 两个你可能遇到过的"假故障"，都不是配置问题

1. **`verify_state` 报错** —— 返回 `NO_ACTIVE_DOCUMENT`。这是没打开文档时的正常返回，不是配置坏了。
2. **`analyze_model` 超时** —— 你的 `.env` 里已经处理过了：`HTTP_TIMEOUT=180`（默认 30s 对 147 面的复杂零件不够），注释里写得很清楚。这个改法是对的。

## 日常使用要点

- **执行层无需手动启动**：适配器检测不到就会按 `EXECUTION_EXE_PATH` 自动拉起 exe，所以没做开机自启也不影响。重启电脑后第一次调用 MCP 工具会自动把服务带起来。
- **SolidWorks 本身要开着或用 `ensure_ready` 启动** —— 我测过 `ensure_ready` 返回 `sw_version=34.3.2`（SolidWorks 2026），符合项目目标版本。
- **改了 `server.py` 不热重载**：需要断开重连 MCP 才生效，这点 README 里专门提了。
- **首次冷启动慢**：`ensure_ready` 拉起 SolidWorks 可能要几十秒，`.env` 里已给到 180s，正常。

现在可以直接让我建零件、读 DXF/DWG 图纸重建、或做装配体了。有想先试的具体零件吗？
