# 子代理会话 sess_subagent_agent_d82c45e2-b6be-4bd7-b6ca-088ec4f3cda7

模型: ?

## 👤 用户（2026-09-13 23:31）

Explore the ComfyUI custom node plugin at `C:\Users\UserX\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\ComfyUI-bsk_UI` (medium-thorough), focusing on the CAMERA CONTROL feature and the BSK parameter panel.

Files of interest: `nodes/camera_control_node.py`, `js/camera_control_node.js`, `nodes/ai_text_node.py`, `nodes/cltagger_node.py`, and any file defining the "BSK 参数集" parameter panel.

Answer these with file:line citations and exact identifier strings:
1. The camera control node — its exact registered node class name(s) and display name(s) (the plugin registers something like `CameraControlNode` / `BSK_相机控制`). What are its FULL input list (names + types + defaults + any dropdown option values) and its output list (names + types)? Read the Python `INPUT_TYPES` / `RETURN_TYPES` / `RETURN_NAMES`.
2. What does the node actually OUTPUT — is it a text/string prompt fragment describing the camera, or numeric parameters, or both? Describe the exact string it builds if it builds one (quote the f-string/template).
3. List the camera dimensions it exposes (the user's notes mention 方位/高度/距离/倾斜/镜头/景深/运镜/构图 = azimuth/elevation/distance/tilt/lens/depth-of-field/camera-move/composition). For each, give the exact input name, type, default, and option list.
4. Is there a companion JS extension (`camera_control_node.js`) that renders a custom widget? What extra UI does it add?
5. The `BSK 参数集` (parameter set) panel shown in the workflow had entries `颜色融合←→文生图` (BOOLEAN) and `CN步数(1-12)` (INT, value 4). Where are these defined and how are additional parameters declared by a workflow author? What is the mechanism (e.g. a JSON/dict registered by the node)?

Report concrete quotable findings (exact names, types, defaults, option lists). Do NOT speculate — if something is not found, state that explicitly.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Let me explore the plugin directory. Let me start by listing files and finding the relevant ones.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" 2>/dev/null; echo \"---NODES---\"; ls -la \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\" 2>/dev/null; echo \"---JS---\"; ls -la \"C:\\Users\\UserX\\AppData\\Local\\ …[截断,原长412]` → `total 1067 drwxr-xr-x 1 user 197121 0 Aug 17 20:06 ./ drwxr-xr-x 1 user 197121 0 Aug 17 19:05 ../ -rw-r--r-- 1 user 197121 8286 Aug 7 21:20 CARD_DEV_GUIDE.md -rw-r--r-- 1 user 197121 35184 Aug 7 21:20 LICENSE drwxr-xr-x 1 user 197121 0 Aug 11 16:07 LICENSES/ -rw-r--r-- 1 user 197121 9705 Aug 11 16:07 README.md -rw-r--r …[截断,原长4017]`

- 🔧 **Bash** `{"command": "find \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" -type f \\( -name \"*.py\" -o -name \"*.js\" -o -name \"*.json\" \\) 2>/dev/null | head -200", "description": "Find all Python, JS, JSON files"}` → `C:\Users\UserX\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\ComfyUI-bsk_UI/bsk_multi_layer_image.py C:\Users\UserX\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\ComfyUI-bsk_UI/bsk_tagger_cli.py C:\Users\UserX\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\C …[截断,原长13237]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:31）

I'll start by exploring the plugin directory structure and locating the files of interest.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Interesting: the nodes directory does NOT contain camera_control_node.py in the list? Wait it does: `nodes/camera_control_node.py` - yes it's there. And `js/camera_control_node.js`. Also param_set_node.py and js/cards/param_set_card.js, and js/cards/camera_control_card.js.

Let me read camera_control_node.py fully first.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\\camera_control_node.py"}` → `1 # SPDX-FileCopyrightText: 2026 灰暗x 2 # SPDX-License-Identifier: AGPL-3.0-or-later 3 """ 4 CameraControlNode - 可视化相机提示词控制节点（重构版）, 参考本节点请注明出处 5 6 设计（见 相机控制节点_方案.md）： 7 1. 方位（Azimuth）由 pos_x 经 az = pos_x * π 分解为 4 个方向分量，按“总和”归一化后瓜分 8 方位预算 = azimuth.weight × 极向门控（门控=1 时方位满权重，仅 |pos_y|→1 即完全指向上/下时 9 门控→0，前后左右不输出；方位权重只与环绕角 …[截断,原长13707]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\\param_set_node.py"}` → `1 # SPDX-FileCopyrightText: 2026 灰暗x 2 # SPDX-License-Identifier: AGPL-3.0-or-later 3 """ 4 BSK 参数集节点 (ParamSet) 5 6 固定 5 组参数，每组 = 标题(titleN) + 值(valueN) + 数据类型(typeN)，输出 outN。 7 - 数据类型 typeN ∈ {BOOLEAN, INT, FLOAT, STRING}，决定后端如何把 valueN 强转。 8 - valueN 声明为 STRING（forceInput=False）：标准 ComfyUI 前端会像 9 bsk_MultiLoraLoader …[截断,原长2469]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:31）

Let me read the camera control node Python source and the parameter set node.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Now I have the camera control node and the param set node. Interesting - the "BSK 参数集" is the ParamSet node. But the user's question 5 says the panel had entries `颜色融合←→文生图` (BOOLEAN) and `CN步数(1-12)` (INT, value 4). These are titles/values set in the workflow node, not hardcoded in param_set_node.py. But there's also js/cards/param_set_card.js which may have a parameter panel. Let me check.

Also need to check __init__.py registrations and the ai_text_node.py and cltagger_node.py. Let me also check the JS camera_control_node.js and param_set_card.js.

Let me read js/camera_control_node.js and js/cards/param_set_card.js, plus search for the strings 颜色融合 and CN步数 across the whole plugin.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\js\\camera_control_node.js"}` → `1 import{app}from"../../scripts/app.js";const NODE_TYPE="CameraControlNode";function cfgFetch(e,t){let n=null;try{"undefined"!=typeof api&&api&&api.fetchApi&&(n=api)}catch(e){}return!n&&window.api&&window.api.fetchApi&&(n=window.api),!n&&app&&app.api&&app.api.fetchApi&&(n=app.api),n?n.fetchApi(e,t):fetch(e,t)}app.regis …[截断,原长30098]`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && grep -rn \"颜色融合\\|CN步数\\|文生图\" --include=*.py --include=*.js --include=*.json . 2>/dev/null | head -50", "description": "Search for panel entry strings across plugin"}` → `(Bash completed with no output)`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:31）

Now let me read the JS extension, param set card, and search for the specific panel entries.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

The grep for 颜色融合/CN步数/文生图 returned nothing. So those specific panel entries are NOT hardcoded in the plugin. They are workflow-authored values stored in the workflow JSON (widgets_values of the BSK_ParamSet node). This confirms Q5: additional parameters are declared by the workflow author by editing titleN/valueN/typeN widgets on the node; the node has 5 fixed slots.

But wait — the user says "BSK 参数集" panel showed those entries with types. There might be a panel UI in panel.js or param_set_card.js that renders them. Let me check param_set_card.js and search for "参数集" and "ParamSet" across js and __init__.py.

Also need to check where param_set_node is registered and check ai_text_node.py and cltagger_node.py. Let me search __init__.py for registration imports of camera/param set, and search for BSK_相机控制.

Note the camera_control_node.js is minified, and it defines NODE_TYPE = "CameraControlNode". There's also js/cards/camera_control_card.js — an alternate card-based UI. Let me read param_set_card.js and search.

Let me run several searches in parallel.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\js\\cards\\param_set_card.js"}` → `1 !function(){"use strict";var e=["BOOLEAN","INT","FLOAT","STRING"],t={BOOLEAN:"false",INT:"0",FLOAT:"0",STRING:""};function n(e,t){var n=document.createElement("div");n.style.cssText="display:inline-flex;align-items:center;flex-shrink:0;";var o=document.createElement("div");o.style.cssText="position:relative;width:34p …[截断,原长5770]`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== NODE_CLASS_MAPPINGS entries camera/param ===\" && grep -n \"CameraControl\\|相机控制\\|BSK_ParamSet\\|参数集\\|param_set\\|camera_control\" __init__.py | head -60", "description": "Search init registrations for camera and param set"}` → `=== NODE_CLASS_MAPPINGS entries camera/param === 3119: # ============ 相机控制节点：配置存取（存于 ComfyUI 用户目录） ============`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== 参数集 / ParamSet refs in js ===\" && grep -rn \"参数集\\|BSK_ParamSet\\|ParamSet\\|param_set\" js/ --include=*.js 2>/dev/null | grep -v \"training_panel\\|workflow_editor\\|panel.js\" | head -40", "description": "Search JS for param set  …[截断,原长392]` → `=== 参数集 / ParamSet refs in js === js/\cards\param_set_card.js:1:!function(){"use strict";var e=["BOOLEAN","INT","FLOAT","STRING"],t={BOOLEAN:"false",INT:"0",FLOAT:"0",STRING:""};function n(e,t){var n=document.createElement("div");n.style.cssText="display:inline-flex;align-items:center;flex-shrink:0;";var o=document.cre …[截断,原长5832]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:31）

The specific panel strings aren't found in the plugin, so they're likely workflow-authored. Let me verify the param set card, registrations, and the ai/cltagger nodes.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

The __init__.py grep found almost nothing for camera/param. That's odd - the 560KB __init__.py may auto-discover nodes. Let me search how nodes are registered/imported. Search for "nodes" directory auto-load, "NODE_CLASS_MAPPINGS", "camera_control_node", "param_set_node", "importlib", "pkgutil". Also let me look at ai_text_node.py and cltagger_node.py registration.

Let me grep __init__.py for relevant patterns.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\__init__.py", "limit": 120}` → `1 # SPDX-FileCopyrightText: 2026 灰暗x 2 # SPDX-License-Identifier: AGPL-3.0-or-later 3 """ 4 ComfyUI bsk UI 5 # ========================================================== 6 # 警告: 这个插件是我花了大量时间精力做出来的。 7 # 你可以免费使用，你的AI也可以重构它，但请保留原作者的名字和出处。 8 # 我的b站空间: https://space.bilibili.com/26779709 9 # 作者: 灰暗x 10 # =================== …[截断,原长4197]`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== NODE_CLASS_MAPPINGS defs in init ===\" && grep -n \"NODE_CLASS_MAPPINGS\\|NODE_DISPLAY_NAME_MAPPINGS\\|WEB_DIRECTORY\\|importlib\\|pkgutil\\|glob\\|nodes/\" __init__.py | head -80", "description": "Find node auto-registration in ini …[截断,原长383]` → `=== NODE_CLASS_MAPPINGS defs in init === 207:WEB_DIRECTORY = "js" 292: if bg_dir.exists() and list(bg_dir.glob("bsk_bg.*")): 2145:NODE_CLASS_MAPPINGS = { 2167:print(f"[BSK] NODE_CLASS_MAPPINGS contains BSK_TestNode: {'BSK_TestNode' in NODE_CLASS_MAPPINGS}") 2168:print(f"[BSK] NODE_CLASS_MAPPINGS contains BSK_LoadImage: …[截断,原长3290]`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== ai_text_node mappings ===\" && grep -n \"NODE_CLASS_MAPPINGS\\|NODE_DISPLAY_NAME_MAPPINGS\\|INPUT_TYPES\\|RETURN_TYPES\\|RETURN_NAMES\\|class \\|DESCRIPTION\\|CATEGORY\" nodes/ai_text_node.py && echo \"=== cltagger_node mappings === …[截断,原长412]` → `=== ai_text_node mappings === 90:class BSK_AIText: 92: def INPUT_TYPES(cls): 117: RETURN_TYPES = ("STRING",) 118: RETURN_NAMES = ("AI回复",) 120: CATEGORY = "bsk_UI/AI文本" 121: DESCRIPTION = "调用各 AI 提供商的 OpenAI 兼容接口，按规则提示词 + 输入文本生成文本。API 配置存于 ComfyUI 用户目录（不进工作流）。" 242:NODE_CLASS_MAPPINGS = { 246:NODE_DISPLAY_NAME_MAPPINGS …[截断,原长649]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:31）

Now let me check how nodes are auto-registered and read the ai_text and cltagger node registrations.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Good. Registration auto-discovery at line 11316-11333. Let me read that section to confirm. Also read ai_text_node.py INPUT_TYPES (lines 90-121) and cltagger INPUT_TYPES (around 1032-1064). And check the camera config HTTP endpoints in __init__.py around 3119.

Let me also verify the panel.js references param set / the BSK 参数集 panel. The user mentions "BSK 参数集" panel — likely the card renderer. Let me search panel.js for "参数集" perhaps encoded differently. Actually grep earlier for "参数集" in js found only param_set_card.js. But "BSK 参数集" display name is in Python. Let me also check `js/cards/` registration mechanism — how cards are registered (window.__bskCards.BSK_ParamSet). Let me check __init__.py auto-discovery section and camera config endpoints.

Let me read the relevant sections.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\__init__.py", "offset": 11310, "limit": 30}` → `11310 print("[ComfyUI Panel] Server instance not available, API registration deferred") 11311 11312 except ImportError as e: 11313 print(f"[ComfyUI Panel] Import error: {e}") 11314 print("[ComfyUI Panel] Not running in ComfyUI environment, API registration skipped") 11315 11316 # ========== 自动发现 nodes/ 目录下的节点 ========= …[截断,原长1224]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\__init__.py", "offset": 3110, "limit": 130}` → `3110 "content": content 3111 }) 3112 except Exception as e: 3113 return web.json_response({ 3114 "success": False, 3115 "error": str(e), 3116 "content": "" 3117 }) 3118 3119 # ============ 相机控制节点：配置存取（存于 ComfyUI 用户目录） ============ 3120 CAMERA_CFG_DIR = os.path.join(BSK_USER_DEFAULT_DIR, "camera_configs") 3121 3122 @ser …[截断,原长5439]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\\ai_text_node.py", "offset": 88, "limit": 40}` → `88 89 90 class BSK_AIText: 91 @classmethod 92 def INPUT_TYPES(cls): 93 return { 94 "required": { 95 "rule": ("STRING", { 96 "default": "", 97 "multiline": True, 98 "placeholder": "规则提示词（作为 system 消息）" 99 }), 100 "text": ("STRING", { 101 "default": "", 102 "multiline": True, 103 "placeholder": "输入文本（作为 user 消息，与 rule 合并 …[截断,原长988]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

Let me read the auto-discovery section, camera config endpoints, and the ai_text/cltagger input types.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Now I have most. Let me check the cltagger INPUT_TYPES fully and the mapping names. Also let me look at the camera_control_card.js to answer Q4 about companion JS. The user asks specifically about js/camera_control_node.js which I already read (minified). There's also js/cards/camera_control_card.js. Let me check its registration and whether it's loaded. Also check how cards are loaded (panel.js reference to __bskCards). Let me also confirm cltagger mappings and INPUT_TYPES.

Let me read cltagger INPUT_TYPES and mappings, and camera_control_card.js.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\\cltagger_node.py", "limit": 85, "offset": 1032}` → `1032 class BSK_Tagger: 1033 """本地 ONNX 图像打标节点，支持 CLTagger 与 WD14 两种打标器。""" 1034 1035 @classmethod 1036 def INPUT_TYPES(cls): 1037 return { 1038 "required": { 1039 "image": ("IMAGE",), 1040 "tagger_type": (["cltagger", "wd14"], {"default": "cltagger"}), 1041 "wd14_model": (list(WD14_MODELS.keys()), {"default": "wd-vit-t …[截断,原长3350]`

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== camera_control_card.js (readable head) ===\" && head -c 3000 js/cards/camera_control_card.js; echo; echo \"=== __bskCards registration keys ===\" && grep -oh \"__bskCards\\.[A-Za-z_]*\" js/cards/*.js | sort -u", "description": "Read …[截断,原长412]` → `=== camera_control_card.js (readable head) === !function(){"use strict";var e={weight_min:.1,weight_max:10,no_weight:!1,no_weight_threshold:.5,azimuth:{enabled:!0,weight:10,deadzone_ratio:.2,directions:{front:{tag:"from front",enabled:!0},back:{tag:"from behind",enabled:!0},left:{tag:"from right",enabled:!0},right:{tag …[截断,原长3399]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

Let me read the cltagger input types/mappings and the camera control card.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I have enough for Q1-Q4. For Q5, the specific entries aren't hardcoded; they're workflow-authored values in the ParamSet node's widgets. Let me verify the mechanism: title/value/type widgets, 5 fixed slots. The workflow JSON stores widgets_values. Let me check if any workflow JSON in panel/ contains "CN步数" or "颜色融合" — grep across whole plugin including json found nothing earlier (grep included json). So they are in the user's workflow file, not the plugin.

But maybe the panel.js has a "BSK 参数集" panel that displays these. The earlier grep for 参数集 in js only found param_set_card.js. Let me double check panel.js for "ParamSet" (case) — earlier grep excluded panel.js. Let me grep panel.js explicitly for ParamSet / BSK_ParamSet.

Also the user says "The `BSK 参数集` (parameter set) panel shown in the workflow had entries". This is likely the card render for the node in their workflow. The additional parameters are declared by editing the title/value/type slots (max 5). There's no dynamic arbitrary params — MAX=5 fixed.

Let me confirm panel.js references and check the camera_control_card.js registration to describe its UI (Q4 mentions camera_control_node.js; but there are two JS files). Let me get the registration name at end of camera_control_card.js and its key UI.

Let me also confirm no other "BSK 参数集" panel implementation in panel.js.

</details>

- 🔧 **Bash** `{"command": "cd \"C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\" && echo \"=== panel.js ParamSet/camera refs ===\" && grep -o \"__bskCards\\.[A-Za-z_]*\\|BSK_ParamSet\\|CameraControlNode\\|BSK 参数集\" js/panel.js | sort | uniq -c | head -40; echo \"=== camera_control_card registration tail ===\" && tail -c 1200  …[截断,原长412]` → `<persisted-output> Output too large (1.2MB). Full output saved to: C:\Users\UserX\.zcode\cli\exec\sess_subagent_agent_d82c45e2-b6be-4bd7-b6ca-088ec4f3cda7\call_00_aIUdxrPfapuRvWhuwtvn9622-stdout.log Preview (first 2KB): === panel.js ParamSet/camera refs === 1 BSK_ParamSet 1 CameraControlNode === camera_control_card reg …[截断,原长1574]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

Let me verify panel.js integration and the card registration details.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

The panel.js refs to BSK_ParamSet and CameraControlNode appear once each. Let me grep more precisely (small output). Actually the output was huge because of the "card loading mechanism" grep matching long minified lines. Let me do targeted small greps.

But I think I have enough. Let me quickly verify the panel.js context around BSK_ParamSet to confirm it's just a generic map lookup. Use grep -o with context is hard in minified. Let me just search for the string presence; it's likely registry mapping `__bskCards[classType]`.

Actually the key question 5 mechanism is answered: the card renderer reads titleN/valueN/typeN. Additional params declared by workflow author by setting widget values. Let me confirm there isn't a JSON schema mechanism elsewhere e.g. prompt_format_node. But question specifically about BSK 参数集 panel. I'm confident.

Let me do a quick final targeted check to see if "BSK 参数集" appears anywhere and if the two named entries exist in any workflow JSON. Already grep'd all py/js/json for 颜色融合/CN步数/文生图 → nothing. Good.

Let me also check the param_set_card registration and how types captured: e=["BOOLEAN","INT","FLOAT","STRING"], defaults t={BOOLEAN:"false",INT:"0",FLOAT:"0",STRING:""}. Confirmed.

One more: Q1 asks exact registered node class name(s) and display name(s). CameraControlNode -> "BSK_相机控制". Also note JS card registers under window.__bskCards.CameraControlNode. And the JS extension name "BSK.CameraControl".

Q3: camera dimensions exposed as node inputs are only pos_x, pos_y, pos_z, roll + config STRING. The specific camera dimensions (azimuth/elevation/distance/tilt/lens/dof/movement/composition/style) are NOT individual inputs — they live inside the `config` JSON string (DEFAULT_CONFIG) and are edited via the custom JS widget / card. This is an important finding: the user's notes list 方位/高度/距离/倾斜/镜头/景深/运镜/构图, but these aren't dropdown inputs; they're config fields. I should state that explicitly with the exact default config values and option lists (directions/categories).

Let me make sure about the exact option lists:
- azimuth.directions: front/back/left/right with tags and enabled
- elevation.categories: bird/high/eye/low/worm
- distance.categories: ecu/cu/medium/full/wide
- tilt.dutch_tag
- extras: lens/dof/movement/composition/style with enabled/value/weight

Q2: output is a STRING prompt fragment. It builds weighted tags `(tag:weight)` joined by ", " and appends trailing ",". Quote f-strings:
- `_emit_weighted`: f"({t}:{cls._fmt_weight(w)})"
- `_fmt_weight`: f"{round(float(w), 2):.2f}"
- dof: f"({val}:{self._fmt_weight(w)})"
- final: `result = ", ".join(parts); if result: result += ","`
- no-weight: joined by ", " then + ",".

Q4: js/camera_control_node.js is minified, registers extension name "BSK.CameraControl" via app.registerExtension, hooks node type CameraControlNode / display name BSK_相机控制, hides native widgets pos_x/pos_y/pos_z/roll/config, adds a DOM widget "camera_ui" with: 3D orbit canvas (drag to rotate, wheel = distance/Z, shift+wheel = roll, arrow keys, [ ] , .), sliders for X/Y/Z/roll, buttons 相对拖拽/归位, save/copy/paste/load config via /comfyui_panel/camera_configs endpoints, collapsible sections 权重设置/自定义提示词/相机控制, live prompt preview textarea labeled "正向输出（接 CLIP Text Encode / PromptFormatNode）", no-weight toggle.

There is also js/cards/camera_control_card.js registering window.__bskCards.CameraControlNode — a card renderer for the panel UI. And camera_core.js window.BskCameraCore with loadConfig/clamp/AXIS_LABELS/EXTRA_LABELS/LENS_OPTIONS/computePrompt. Let me quickly read camera_core.js to cite exact identifiers (AXIS_LABELS, EXTRA_LABELS, LENS_OPTIONS).

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\js\\camera_core.js"}` → `1 !function(){"use strict";var e={weight_min:.1,weight_max:10,no_weight:!1,no_weight_threshold:.5,azimuth:{enabled:!0,weight:10,deadzone_ratio:.2,directions:{front:{tag:"from front",enabled:!0},back:{tag:"from behind",enabled:!0},left:{tag:"from right",enabled:!0},right:{tag:"from left",enabled:!0}}},elevation:{enabled …[截断,原长6391]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

Let me read camera_core.js for exact shared identifiers.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I now have all the information. Let me compose the final report with file:line citations.

Let me double-check Q1: Is there only CameraControlNode? Yes, nodes/camera_control_node.py lines 423-428. Registered via auto-discovery in __init__.py:11316-11331.

Note: There's also `__init__.py` NODE_CLASS_MAPPINGS at 2145 but camera/param set are auto-discovered from nodes/.

Q5: the mechanism. BSK_ParamSet at nodes/param_set_node.py:18-82. MAX=5, TYPES=("BOOLEAN","INT","FLOAT","STRING"). INPUT_TYPES optional title{i}/value{i}/type{i}, value declared STRING so it renders as a text field and exports with workflow. RETURN_TYPES ("*",)*5, RETURN_NAMES out1..out5. Mechanism: workflow author sets the node's widget values (title1..title5, value1..value5, type1..type5); ComfyUI serializes widgets_values into the workflow JSON. The card renderer js/cards/param_set_card.js (window.__bskCards.BSK_ParamSet) renders title text input, type dropdown, and type-dependent value editor (BOOLEAN switch, INT/FLOAT number, STRING text), and reads upstream links. So entries `颜色融合←→文生图` and `CN步数(1-12)` are literal title widget values authored in the workflow, not declared in plugin code — grep found no occurrence. Types BOOLEAN/INT and value 4 likewise come from typeN/valueN widget values in the workflow JSON. There is no JSON/dict schema registration; it's fixed 5 slots.

Let me also mention the panel.js/panel integration for cards: cards are loaded and looked up by class type. I only confirmed one occurrence each in panel.js. Good enough; I can state cards are registered on window.__bskCards and panel.js references them (I saw 1 match each for BSK_ParamSet and CameraControlNode). I shouldn't overstate. Let me just say the card renderer is keyed by node class type on window.__bskCards.

Actually let me verify how panel.js maps card renderers, to be precise. The grep output was too large because of minified lines. Let me do a small targeted extraction using grep -o with a pattern around __bskCards in panel.js. But it might be huge. Let me try a bounded pattern.

Actually, I can state confidently enough: param_set_card.js (line 1) registers window.__bskCards.BSK_ParamSet. panel.js references "BSK_ParamSet" once. That's enough to say the panel looks up the card renderer by class type. I don't need more.

Now Q3 asks "List the camera dimensions it exposes ... For each, give the exact input name, type, default, and option list." Critical nuance: the node has NO discrete inputs for these; they are fields of the config JSON. The only node inputs are pos_x/pos_y/pos_z/roll/config. So I must state that explicitly and then give the config fields.

Dimensions:
- 方位 azimuth: config["azimuth"] = {enabled: True, weight: 10.0, deadzone_ratio: 0.2, directions: front/back/left/right}
  - directions options (each {tag, enabled}): front "from front", back "from behind", left "from right", right "from left" — note swapped semantic tags (left direction tag = "from right").
- 高度 elevation: {enabled True, extra 10.0, categories bird/high/eye/low/worm with tags}
- 距离 distance: {enabled True, extra 0.0, categories ecu/cu/medium/full/wide with tags}
- 倾斜 tilt: {enabled True, deadzone 0.15, extra 0.0, dutch_tag "dutch angle"}
- 镜头 lens: extras.lens {enabled False, value "85mm lens"} (no weight)
- 景深 dof: extras.dof {enabled False, value "shallow depth of field", weight 1.3}
- 运镜 movement: {enabled False, value "handheld camera"}
- 构图 composition: {enabled False, value "rule of thirds"}
- 风格 style: {enabled False, value "cinematic"}

Also top-level config fields: weight_min 0.1, weight_max 10.0, no_weight False, no_weight_threshold 0.5, extra_master 1.0, wheel_step 0.0003.

Q2: output details. RETURN_TYPES=("STRING",), RETURN_NAMES=("相机提示词",). Weighted mode builds `(tag:weight)` with 2-decimal weight. Plain mode no weight. Ends with trailing comma.

Let me also give the exact output format example is not needed, but quote f-strings.

Q4: js/camera_control_node.js adds DOM widget named "camera_ui". Extension name "BSK.CameraControl". Hides native widgets. Wait — actually the camera_control_node.js is the plain canvas extension. The camera_control_card.js is the card. Both exist. The user asked "Is there a companion JS extension (camera_control_node.js) that renders a custom widget? What extra UI does it add?" Yes.

Let me write the report now. Cite exact lines.

Important line numbers:
- camera_control_node.py:
  - class CameraControlNode: 102
  - INPUT_TYPES: 105-130
  - pos_x 109-112, pos_y 113-116, pos_z 117-120, roll 121-124, config 125-128
  - RETURN_TYPES 132, RETURN_NAMES 133, FUNCTION 134, CATEGORY 135, DESCRIPTION 136
  - NODE_CLASS_MAPPINGS 423-425, display 426-428
  - DEFAULT_CONFIG 27-80
  - _fmt_weight 139-142 (f"{round(float(w), 2):.2f}")
  - _emit_weighted 149-152 (f"({t}:{cls._fmt_weight(w)})")
  - execute 266-348, final join 345-348
  - dof 339-341
  - _compute_prompt_no_weight 350-420, final 419-420
- param_set_node.py: class 18, MAX 19, TYPES 20, INPUT_TYPES 22-29, RETURN_TYPES 31, RETURN_NAMES 32, FUNCTION 33, CATEGORY 34, DESCRIPTION 35, _coerce 37-65, pass_through 67-73, mappings 76-82.
- param_set_card.js line 1: types array e, defaults t, window.__bskCards.BSK_ParamSet, loop d<=5.
- camera_control_node.js line 1: registerExtension name "BSK.CameraControl", NODE_TYPE="CameraControlNode", addDOMWidget("camera_ui"...).
- camera_core.js line 1: window.BskCameraCore with EXTRA_LABELS, AXIS_LABELS, LENS_OPTIONS.
- ai_text_node.py: class 90, INPUT_TYPES 92-115, mappings 242-248 (need display name). Let me check lines 242-248.
- cltagger_node.py: class 1032, INPUT_TYPES 1036-1056, RETURN 1058-1060, mappings 1107-1113.

I didn't read ai_text_node mappings display name. Let me quickly read lines 240-250. Also the grep showed class at 90. Let me fetch.

Actually the user asked "Files of interest include ai_text_node.py, cltagger_node.py" but questions focus on camera and param set. I'll include a brief registration summary for those two since asked in files of interest. Let me get ai_text display name.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Comfy-Desktop\\ComfyUI-Installs\\ComfyUI\\ComfyUI\\custom_nodes\\ComfyUI-bsk_UI\\nodes\\ai_text_node.py", "limit": 12, "offset": 241}` → `241 242 NODE_CLASS_MAPPINGS = { 243 "BSK_AIText": BSK_AIText, 244 } 245 246 NODE_DISPLAY_NAME_MAPPINGS = { 247 "BSK_AIText": "BSK AI文本生成", 248 } 249 `

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

Let me grab the ai_text node mappings for completeness.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I have all findings. Let me write the final report. No need for TodoWrite — this is a research task, near complete. Compose final answer with file:line citations.

</details>

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-13 23:32）

# Findings: ComfyUI-bsk_UI camera control + BSK 参数集

Root: `C:\Users\UserX\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\ComfyUI-bsk_UI`

Registration mechanism: `__init__.py:11316-11331` auto-discovers every `nodes/*.py`, importing `NODE_CLASS_MAPPINGS` / `NODE_DISPLAY_NAME_MAPPINGS`. `WEB_DIRECTORY = "js"` at `__init__.py:207`. So the node is registered through that loop, not a manual entry in `__init__.py`.

---

## 1. Camera control node registration, inputs, outputs

File: `nodes\camera_control_node.py`

- Class: `CameraControlNode` (`camera_control_node.py:102`)
- `NODE_CLASS_MAPPINGS` = `{"CameraControlNode": CameraControlNode}` (`:423-425`)
- `NODE_DISPLAY_NAME_MAPPINGS` = `{"CameraControlNode": "BSK_相机控制"}` (`:426-428`)
- `RETURN_TYPES = ("STRING",)` (`:132`), `RETURN_NAMES = ("相机提示词",)` (`:133`)
- `FUNCTION = "execute"` (`:134`), `CATEGORY = "bsk_UI/相机"` (`:135`)
- `DESCRIPTION` at `:136`

`INPUT_TYPES` (`:105-130`) — exactly 5 required inputs, all scalar/serialized; there are no image/latent inputs:

| name | type | default | min | max | step | extra |
|---|---|---|---|---|---|---|
| `pos_x` | FLOAT | 0.0 | -1.0 | 1.0 | 0.01 | `label`: 左右 (X) |
| `pos_y` | FLOAT | 0.0 | -1.0 | 1.0 | 0.01 | `label`: 上下 (Y) |
| `pos_z` | FLOAT | 0.0 | -1.0 | 1.0 | 0.01 | `label`: 前后 (Z) |
| `roll` | FLOAT | 0.0 | -1.0 | 1.0 | 0.01 | `label`: 翻滚 (Roll) |
| `config` | STRING | `DEFAULT_CONFIG_JSON` | — | — | — | `multiline: True` |

Note: `roll` is documented (`:19`) as being written by the canvas frontend via Shift+wheel / `,` `.` keys.

Output list: a single `STRING` named `相机提示词`.

---

## 2. What the node actually outputs

It outputs a **text prompt fragment**, not numeric parameters. Weighted mode emits `(tag:weight)` segments joined with `", "`, then appends a trailing comma. Exact builders:

- `_fmt_weight` (`:139-142`): `f"{round(float(w), 2):.2f}"` (always 2 decimals)
- `_emit_weighted` (`:149-152`): `f"({t}:{cls._fmt_weight(w)})"` — splits comma-containing tags into separate weighted fragments
- `_emit_plain` (`:154-157`): unweighted mode, comma-split tags
- DOF special case (`:339-341`): `f"({val}:{self._fmt_weight(w)})"`
- Final assembly (`:345-348`):
  ```
  result = ", ".join(parts)
  if result:
      result += ","
  return (result,)
  ```
- No-weight mode final (`:419-420`): `", ".join(parts)` then `result + ","`.

There is no numeric output and no negative-prompt output (comment at `:16` and `:5-17` explicitly says negative output was removed).

---

## 3. Camera dimensions — where they actually live

Important: the dimensions 方位/高度/距离/倾斜/镜头/景深/运镜/构图 are **not** individual node inputs and there are **no dropdown (`[...]`) input types**. They are fields of the `config` JSON string, with `DEFAULT_CONFIG` at `camera_control_node.py:27-80` (mirrored in `js/camera_core.js:1` as `BskCameraCore.DEFAULT_CONFIG`). The only discrete UI options are the tag categories inside that config, edited via the custom JS widget/card.

Top-level config defaults (`:27-80`): `weight_min` 0.1, `weight_max` 10.0, `no_weight` False, `no_weight_threshold` 0.5, `extra_master` 1.0, `wheel_step` 0.0003.

Per-dimension, exact config keys, defaults, and option lists:

- **方位 azimuth** — `config.azimuth` (`:32-42`): `enabled` True, `weight` 10.0, `deadzone_ratio` 0.2.
  Options `directions` (each `{tag, enabled}`), values:
  - `front` → tag `"from front"`, enabled True
  - `back` → tag `"from behind"`, enabled True
  - `left` → tag `"from right"`, enabled True (note reversed wording)
  - `right` → tag `"from left"`, enabled True
  - Computation (`:276-305`): `az = pos_x * pi`, split into cos/sin components, normalized; azimuth budget = `azimuth.weight * az_gate` where `az_gate = clamp((1-|pos_y|)/(1-0.9),0,1)`; skip if ratio ≤ 0 or weight < deadzone_ratio.

- **高度 elevation** — `config.elevation` (`:43-53`): `enabled` True, `extra` 10.0.
  Options `categories` (each `{tag, enabled}`): `bird` → `"directly above, from above, aerial view,"`; `high` → `"high angle, from above"`; `eye` → `"eye-level"`; `low` → `"low angle, from below,"`; `worm` → `"directly below"`.
  Bins by `pos_y` (`_elevation_key`, `:210-220`): >0.7 bird, >0.2 high, ≥-0.2 eye, ≥-0.7 low, else worm. Weight = `|pos_y| * (1 + extra_master*elevation.extra)`.

- **距离 distance** — `config.distance` (`:54-64`): `enabled` True, `extra` 0.0.
  Options `categories`: `ecu` → `"extreme close-up"`; `cu` → `"close-up"`; `medium` → `"medium shot"`; `full` → `"full body"`; `wide` → `"wide shot"`.
  Bins by `pos_z` (`_distance_key`, `:222-232`) with ranges `DIST_RANGES` (`:89-95`): ecu (0.7,1.0), cu (0.2,0.7), medium (-0.2,0.2), full (-0.7,-0.2), wide (-1.0,-0.7); `DIST_FAR_STRONGER = {"medium","full","wide"}` (`:99`).

- **倾斜 tilt** — `config.tilt` (`:65-70`): `enabled` True, `deadzone` 0.15, `extra` 0.0, `dutch_tag` `"dutch angle"`. Emitted when `|roll| >= deadzone` (`:326-328`, `_weighted_tilt` `:254-264`).

- **镜头 lens** — `config.extras.lens` (`:74`): `enabled` False, `value` `"85mm lens"`.
- **景深 dof** — `config.extras.dof` (`:75`): `enabled` False, `value` `"shallow depth of field"`, `weight` 1.3.
- **运镜 movement** — `config.extras.movement` (`:76`): `enabled` False, `value` `"handheld camera"`.
- **构图 composition** — `config.extras.composition` (`:77`): `enabled` False, `value` `"rule of thirds"`.
- **风格 style** — `config.extras.style` (`:78`): `enabled` False, `value` `"cinematic"`.

`extras` loop order is fixed `("lens","dof","movement","composition","style")` (`:332-343`). No-weight mode variants at `:350-420`; no-weight defaults: eye/medium do not emit, secondary azimuth directions emit only if ratio ≥ `no_weight_threshold` (default 0.5).

---

## 4. Companion JS extension

File: `js\camera_control_node.js` (single minified line 1). Yes — it renders a custom DOM widget.

- Registers `app.registerExtension({name:"BSK.CameraControl", ...})` with `const NODE_TYPE="CameraControlNode"`; matches `comfyClass === "CameraControlNode"` or display name `"BSK_相机控制"`.
- Hides the native widgets `pos_x`, `pos_y`, `pos_z`, `roll`, `config` (sets `hidden` and `computeSize()=>[0,-4]`).
- Adds a DOM widget via `this.addDOMWidget("camera_ui","camera_ui",h,{serialize:!1,hideOnZoom:!1})`.
- Extra UI added:
  - Toolbar with buttons 保存 / 复制 / 粘贴 / 设置 and a config-load `<select>` hitting HTTP endpoints `/comfyui_panel/camera_configs` (GET), `/camera_configs/save`, `/camera_configs/load` (endpoints defined at `__init__.py:3119-3176`; storage dir `user/default/camera_configs`).
  - 3D orbit/globe canvas: drag to rotate (relative or absolute mode), wheel = distance (`pos_z`, step `config.wheel_step`), Shift+wheel = roll, arrow keys move X/Y, `[` `]` = Z, `,` `.` = roll; buttons `相对拖拽` (toggle to `绝对拖拽`) and `归位 (X/Y/Z/R=0)`.
  - Sliders + numeric inputs for X/Y/Z/Roll labeled from `BskCameraCore.AXIS_LABELS` (`js\camera_core.js:1`: x=左右 (X), y=上下 (Y), z=远近 (Z), roll=翻滚 (R)).
  - Collapsible `<details>` sections: 权重设置, 自定义提示词, 相机控制.
  - Weight settings: 无权重模式 toggle, 无权重·次要方向阈值, 方位权重（整体）, 权重最大值(钳制上限), 额外权重总控, 高度额外权重, 距离额外权重, 滚轮步进(距离), 倾斜额外权重, 方位死区比例, 倾斜死区.
  - Custom-prompt fieldsets 方位/高度/距离/倾斜 with per-tag enable toggles + tag text inputs; 额外相机提示词 with `lens/dof/movement/composition/style` labels from `BskCameraCore.EXTRA_LABELS`, lens datalist `BskCameraCore.LENS_OPTIONS`.
  - Read-only live preview textarea labeled `正向输出（接 CLIP Text Encode / PromptFormatNode）`, driven by `BskCameraCore.computePrompt(...)`.
- Shared algorithm core: `js\camera_core.js` exposes `window.BskCameraCore` with `DEFAULT_CONFIG`, `EXTRA_LABELS`, `AXIS_LABELS`, `LENS_OPTIONS` (= `["85mm lens","50mm lens","35mm lens","24mm lens","wide angle lens","fisheye lens","telephoto lens","macro lens"]`), `loadConfig`, `computePrompt`, `computePromptNoWeight`, `fmtWeight`, `clamp`, `emitWeighted`, etc. The canonical algorithm is the Python node (`camera_control_node.py:17`: frontend `computePrompt` is preview only and must match the Python file).
- Separate panel card renderer: `js\cards\camera_control_card.js` registers `window.__bskCards.CameraControlNode` (same config/UI, for the bsk panel). Both files present.

---

## 5. `BSK 参数集` panel — where those entries come from

File: `nodes\param_set_node.py`

- Class `BSK_ParamSet` (`:18`); `NODE_CLASS_MAPPINGS = {"BSK_ParamSet": BSK_ParamSet}` (`:76-78`); display name `"BSK 参数集"` (`:80-82`); `CATEGORY = "bsk/utilities"` (`:34`).
- Fixed 5 slots: `MAX = 5` (`:19`); `TYPES = ("BOOLEAN", "INT", "FLOAT", "STRING")` (`:20`).
- `INPUT_TYPES` (`:22-29`) returns `{"required": {}, "optional": {...}}` with, for i in 1..5:
  - `title{i}`: `("STRING", {"default":"", "forceInput":False, "multiline":False})`
  - `value{i}`: `("STRING", {"default":"", "forceInput":False, "tooltip":...})`
  - `type{i}`: `(TYPES, {"default":"INT"})`
- `RETURN_TYPES = ("*",)*5`, `RETURN_NAMES = ("out1",...,"out5")` (`:31-32`); `FUNCTION = "pass_through"` (`:33`).
- Coercion: `_coerce` (`:37-65`) — empty INT→0, FLOAT→0.0, BOOLEAN→False, STRING→`""`; `"1"/"true"/"yes"/"y"/"t"`→True; non-string upstream objects pass through unchanged.

Mechanism for declaring parameters: there is **no JSON/dict schema registration and no dynamic list**. The workflow author declares each parameter by setting the node's `titleN` / `valueN` / `typeN` **widget values** directly on the node. The node always exposes exactly 5 fixed slots. `valueN` is typed `STRING` specifically so standard ComfyUI renders an editable text field and serializes it into `widgets_values` in the workflow (docstring `param_set_node.py:3-16`), and the backend coerces per `typeN`.

The two concrete entries you saw (`颜色融合←→文生图` BOOLEAN, `CN步数(1-12)` INT value 4) are **literal title/value widget data authored inside that workflow** — not declared anywhere in the plugin. This is confirmed: a recursive grep for `颜色融合`, `CN步数`, and `文生图` across all `.py`, `.js`, and `.json` files in the plugin returned **no matches**. So their types/values come from the node's `typeN`/`valueN` widget values stored in the workflow JSON.

Panel card renderer: `js\cards\param_set_card.js` (single minified line 1) registers `window.__bskCards.BSK_ParamSet`. It:
- Iterates `d <= 5` (slots 1..5), rendering a title text input (`titleN`), a type dropdown from `["BOOLEAN","INT","FLOAT","STRING"]`, and a type-dependent value editor — BOOLEAN switch, INT/FLOAT number input, STRING text input — writing into `valueN`.
- Uses per-type defaults `{BOOLEAN:"false", INT:"0", FLOAT:"0", STRING:""}`.
- Detects upstream connections to `valueN` (disables title/type/value when connected) and shows the downstream target of `out{i}` via a `?` tooltip.
- `panel.js` references `BSK_ParamSet` and `CameraControlNode` (one occurrence each) as the card registry keys.

---

## Bonus registrations (files of interest)

- `nodes\ai_text_node.py`: class `BSK_AIText` (`:90`); `NODE_CLASS_MAPPINGS = {"BSK_AIText": BSK_AIText}` (`:242-244`); display `"BSK AI文本生成"` (`:246-248`); `RETURN_TYPES = ("STRING",)` / `RETURN_NAMES = ("AI回复",)` (`:117-118`); `CATEGORY = "bsk_UI/AI文本"` (`:120`). Inputs (`:92-115`): required `rule` STRING multiline, `text` STRING multiline, `enabled` BOOLEAN default True (labels 启用/禁用); optional `image` IMAGE, `send_image` BOOLEAN default False (labels 识图/纯文本). Card `js\cards\ai_text_card.js` registers `__bskCards.BSK_AIText`.
- `nodes\cltagger_node.py`: class `BSK_Tagger` (`:1032`); `NODE_CLASS_MAPPINGS = {"BSK_Tagger": BSK_Tagger}` (`:1107-1109`); display `"BSK 图像打标器"` (`:1111-1113`); `RETURN_TYPES = ("STRING",)`, `RETURN_NAMES = ("tags",)`, `OUTPUT_IS_LIST = (True,)` (`:1058-1060`); `CATEGORY = "bsk_UI/打标"` (`:1063`). Inputs (`:1036-1056`): `image` IMAGE; `tagger_type` combo `["cltagger","wd14"]` default `"cltagger"`; `wd14_model` list from `WD14_MODELS.keys()` default `"wd-vit-tagger-v3"`; `general_threshold` FLOAT 0.35 (0-1 step .05); `character_threshold` FLOAT 0.60; `sort_mode` combo `["default","novelai"]`; BOOLEANs `exclude_meta`/`exclude_rating`/`exclude_quality` (True), `replace_underscore`/`trailing_comma` (False), `enabled` (True); `exclude_tags` STRING; `max_resolution` INT 1280 (64-4096 step 64); `trigger_word` STRING; `batch_dir` STRING. Card `js\cards\cltagger_card.js` registers `__bskCards.BSK_Tagger`.

Nothing was found that was not reported; specifically, no dropdown option lists exist on `CameraControlNode` inputs, and the two named `BSK 参数集` entries are workflow data rather than plugin-declared parameters.
