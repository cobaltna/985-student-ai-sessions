# 子代理会话 sess_subagent_agent_14f9eb75-06f9-4dcb-ab9f-847cedebc040

模型: GLM-5.3-Flash

## 👤 用户（2026-10-30 01:15）

你是机器人实验课的视频帧分析助手。有一个 51 单片机轮式机器人小车（STC12C5A60S2 主控、TB6612 电机驱动、扩展板、 Yahboom 风格套件）的 6 个实验视频，每个视频已抽取 6 帧（按时间顺序）。请用 Read 工具逐一查看以下全部 36 张图片：

C:\Users\UserX\Downloads\轮式\work\frames\实验1 七彩探照灯实验(1)\frame1.jpg 到 frame6.jpg
C:\Users\UserX\Downloads\轮式\work\frames\实验2 小车前进实验(1)\frame1.jpg 到 frame6.jpg
C:\Users\UserX\Downloads\轮式\work\frames\实验3 小车前后左右综合实验(1)\frame1.jpg 到 frame6.jpg
C:\Users\UserX\Downloads\轮式\work\frames\实验4 舵机旋转控制七彩探照灯(1)\frame1.jpg 到 frame6.jpg
C:\Users\UserX\Downloads\轮式\work\frames\实验5 按键控制小车启动实验(1)\frame1.jpg 到 frame6.jpg
C:\Users\UserX\Downloads\轮式\work\frames\实验6 红外避障实验(1)\frame1.jpg 到 frame6.jpg

对每个实验（视频），输出一份结构化中文报告，包含：
1. **画面场景**：小车外观（颜色、轮数、底盘结构）、所用模块（LED灯/舵机/传感器等位置）、桌面上可见的器材、连接线情况。
2. **电脑软件界面细节**（如帧中出现）：Keil 界面（工程名、代码窗口中可见的代码片段、菜单操作）、烧录软件（软件名称、版本、选择的芯片型号、串口号、按钮文字）、串口调试助手（名称、波特率、收到的数据内容）等。把屏幕上能看清的文字尽量原样抄录。
3. **小车/模块的行为**：按帧序推断行为时序（例如：灯亮什么颜色→什么颜色、小车前进/转弯/停止的先后）。
4. **人手操作动作**：接线、按按键、调节电位器、拿遥控光源等。
5. **对写实验指导书有用的细节**：如接线颜色、杜邦线接法、模块上指示灯状态、可调元件位置等。

要求：只描述你确实在帧中看到的，不确定的注明"无法确认"。最终回复直接给出 6 个实验的完整分析文本（这是返回给主代理的唯一内容，请写全）。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

I need to read all 36 images across 6 experiment folders. Let me start reading them in batches. I can read multiple files in parallel. Let me read the first experiment's frames.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame1.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame2.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame3.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame4.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame5.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame6.jpg"}` → ``

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:15）

我将逐一读取全部36张帧图片进行分析。先读实验1的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

The path doesn't exist as given. Let me list the frames directory to see the actual structure. Note the working directory is C:\Users\UserX\Downloads\轮式\work but the user mentioned C:\Users\UserX\... Maybe the actual user is UserX. Let me check.

</details>

- 🔧 **Bash** `{"command": "ls -R \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\" 2>/dev/null | head -100", "description": "List frames directory structure"}` → `C:\Users\UserX\Downloads\轮式\work\frames: 实验1 七彩探照灯实验(1)/ 实验10 超声波避障实验(1)/ 实验11 带舵机云台的超声波避障实验(1)/ 实验2 小车前进实验(1)/ 实验3 小车前后左右综合实验(1)/ 实验4 舵机旋转控制七彩探照灯(1)/ 实验5 按键控制小车启动实验(1)/ 实验6 红外避障实验(1)/ 实验7 红外跟随实验(1)/ 实验8 寻光行走实验(1)/ 实验9 巡线实验(1)/ C:\Users\UserX\Downloads\轮式\work\frames/实验1 七彩探照灯实验(1): C:\Users\UserX\Downloads\轮式\work\fra …[截断,原长854]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:15）

路径不存在，先查看实际目录结构。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

The directories exist but are empty. The frames haven't been extracted yet, or they're elsewhere. Let me check the work directory for other files.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:\\Users\\UserX\\Downloads\\轮式\\work\" ; find \"C:\\Users\\UserX\\Downloads\\轮式\" -iname \"*.jpg\" -o -iname \"*.png\" -o -iname \"*.jpeg\" 2>/dev/null | head -60", "description": "List work directory and find image files"}` → `total 7388 drwxr-xr-x 1 user 197121 0 Oct 30 01:12 ./ drwxr-xr-x 1 user 197121 0 Oct 30 01:07 ../ -rw-r--r-- 1 user 197121 749 Oct 30 01:12 extract_log.txt drwxr-xr-x 1 user 197121 0 Oct 30 01:12 frames/ -rw-r--r-- 1 user 197121 7092792 Oct 30 01:07 guide.docx drwxr-xr-x 1 user 197121 0 Oct 30 01:07 guide_extract/ drwx …[截断,原长4742]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:16）

目录存在但为空。检查 work 目录下是否有其他位置的图片。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

The frames folders are empty. There's an extract_log.txt which may indicate the frame extraction failed. Let me check the extract_log and look for the source videos. Maybe the videos are elsewhere and frames need to be extracted. Let me read the log.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_log.txt"}` → `1 实验1 七彩探照灯实验(1): 16797 frames, 30.0fps, 559.9s 2 实验10 超声波避障实验(1): 18606 frames, 30.0fps, 620.2s 3 实验11 带舵机云台的超声波避障实验(1): 23187 frames, 30.0fps, 772.9s 4 实验2 小车前进实验(1): 24250 frames, 30.0fps, 808.3s 5 实验3 小车前后左右综合实验(1): 10100 frames, 30.0fps, 336.7s 6 实验4 舵机旋转控制七彩探照灯(1): 20747 frames, 30.0fps, 691.6s 7 实验5 按键控制小车启动实验(1 …[截断,原长551]`

- 🔧 **Bash** `{"command": "find \"C:\\Users\\UserX\\Downloads\\轮式\" -iname \"*.mp4\" -o -iname \"*.avi\" -o -iname \"*.mov\" -o -iname \"*.mkv\" -o -iname \"*.wmv\" -o -iname \"*.flv\" -o -iname \"*.ts\" -o -iname \"*.webm\" 2>/dev/null | head -30", "description": "Find video files under 轮式 directory"}` → `C:\Users\UserX\Downloads\轮式/实验视频mp4/实验1 七彩探照灯实验(1)-soConvert.mp4 C:\Users\UserX\Downloads\轮式/实验视频mp4/实验10 超声波避障实验(1)-soConvert.mp4 C:\Users\UserX\Downloads\轮式/实验视频mp4/实验11 带舵机云台的超声波避障实验(1)-soConvert.mp4 C:\Users\UserX\Downloads\轮式/实验视频mp4/实验2 小车前进实验(1)-soConvert.mp4 C:\Users\UserX\Downloads\轮式/实验视频mp4/实验3 小车前后左右综合实验(1) …[截断,原长725]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:16）

frames 目录为空。查看 extract_log.txt 了解帧抽取情况，并寻找源视频。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

The frames folders are empty but the source videos exist at C:\Users\UserX\Downloads\轮式\实验视频mp4\. The extract_log says frames were counted (probably probed) but the actual frame extraction to JPG didn't complete or wrote elsewhere. The task says "每个视频已抽取 6 帧" — apparently the extraction step failed or was incomplete. I need to extract 6 frames per video myself.

I need ffmpeg. Let me check if ffmpeg is available. Per AGENTS.md, use pwsh for python etc. Let me check ffmpeg availability first.

I'll extract 6 frames evenly spaced per video (e.g., at 10%, 25%, 40%, 55%, 70%, 85% or every 1/7 of duration). A common approach: fps sampling or select at specific timestamps. Let me do: for each video, get duration, then extract frames at t = duration * k/7 for k=1..6.

Let me check ffmpeg availability.

</details>

- 🔧 **Bash** `{"command": "which ffmpeg && ffmpeg -version 2>&1 | head -2", "description": "Check ffmpeg availability"}` → `Exit code 1 which: no ffmpeg in (/c/Users/UserX/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/UserX/bin:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/windows/system32:/c/windows:/c/windows/System32/Wbem:/c/windows/System32/WindowsPowerShell/v1.0:/c/windows/System32/OpenSSH:/c/ …[截断,原长1677]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:16）

源视频在 `实验视频mp4` 目录中，但 frames 目录为空（抽取未完成）。我需要先自行抽帧。检查 ffmpeg 是否可用。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

ffmpeg not in PATH. Check conda env opencv (per memory: docx uses conda `opencv` env). Python with cv2 can extract frames. Let me find conda python path.

</details>

- 🔧 **Bash** `{"command": "ls -d /c/ProgramData/*conda* /c/Users/UserX/*conda* /c/Users/UserX/.conda 2>/dev/null; cat /c/Users/UserX/.zcode/memory/python-envs.md 2>/dev/null | head -50", "description": "Locate conda installation and read python envs memory"}` → `/c/ProgramData/anaconda3/ /c/ProgramData/anacondaDownLoader/ /c/Users/UserX/.conda/ # 本机 Python 环境完整清单（实测 2026-09-12） > 由 `~/.zcode/AGENTS.md` 索引。所有结论均由「直接调用该解释器并 import」实测得出，非推测。 > conda / python **均不在 bash PATH**，必须用全路径调用。 ## 0. 目录真相 `C:\Users\UserX` 是**符号链接** → `C:\Users\UserX`（同一目录）。两种写法等价 （实测 `四.conda\envs\opencv\ …[截断,原长2257]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:16）

ffmpeg 不在 PATH。用 conda opencv 环境的 Python 抽帧。先找 python 路径。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Good. conda opencv env: `C:\Users\UserX\.conda\envs\opencv\python.exe` with cv2. I'll write a Python script to extract 6 frames per video at evenly spaced timestamps (e.g., at fractions 1/7..6/7 of duration, or 0.08, 0.25, 0.42, 0.58, 0.75, 0.92). Let me write the script and run it for the 6 experiments needed (1-6). Actually the task only needs experiments 1-6. But extracting for the requested 6 is enough.

Frame naming: frame1.jpg ... frame6.jpg in the existing directories.

I'll use cv2. Per AGENTS.md: use pwsh for python with Chinese output; write script file with Write tool (Chinese in files should use Read/Write tools). The script itself can avoid printing Chinese. Let me write the script.

</details>

- 🔧 **Write** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames.py", "content": "import cv2, os, sys\n\nbase = r\"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\"\nvid_dir = r\"C:\\Users\\UserX\\Downloads\\轮式\\实验视频mp4\"\n\nexps = [\n \"实验1 七彩探照灯实验(1)\",\n \"实验2 小车前进实验(1)\",\n \"实验3 小车前后左右综合实验(1)\",\n \"实验4 舵机旋转控制七彩探照灯(1)\",\n \"实验5 按键控制小车启动实验(1)\",\n \"实验6 红外避障实验(1)\",\n]\n …[截断,原长401]` → `File created successfully at: C:\Users\UserX\Downloads\轮式\work\extract_frames.py (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:16）

conda opencv 环境可用（含 cv2）。写抽帧脚本，为实验1–6各抽6帧。

- 🔧 **Bash** `{"command": "\"/c/Users/UserX/.conda/envs/opencv/python.exe\" \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames.py\" > \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames_log.txt\" 2>&1; cat \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames_log.txt\"", "description": "Run frame extraction script with conda opencv python", "timeout": 300000}` → `DONE: 实验1 七彩探照灯实验(1) frames: 16797 dur_s: 559.9 DONE: 实验2 小车前进实验(1) frames: 24250 dur_s: 808.3 DONE: 实验3 小车前后左右综合实验(1) frames: 10100 dur_s: 336.7 DONE: 实验4 舵机旋转控制七彩探照灯(1) frames: 20747 dur_s: 691.6 DONE: 实验5 按键控制小车启动实验(1) frames: 10031 dur_s: 334.4 DONE: 实验6 红外避障实验(1) frames: 13851 dur_s: 461.7 ALL DONE`

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Frames extracted. Now read all 36 images. Start with experiment 1 (6 frames).

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame1.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame2.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame3.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame4.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame5.jpg"}` → ``

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame6.jpg"}` → ``

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:17）

抽帧成功。开始逐一查看实验1的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Odd. The script reported success. Maybe the files were written somewhere else due to the path? The script used raw string with UserX. Let me verify with ls.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)/\" 2>&1; echo ---; find \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\" -name \"frame*.jpg\" 2>/dev/null | head -40", "description": "Verify extracted frame files exist"}` → `total 4 drwxr-xr-x 1 user 197121 0 Oct 30 01:12 ./ drwxr-xr-x 1 user 197121 0 Oct 30 01:12 ../ ---`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:17）

脚本报告成功但 Read 找不到文件。用 ls 验证实际文件位置。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

The frames directories are still empty even though cv2.imwrite "succeeded". Something odd — maybe the script wrote to a different location due to path encoding. The Python script was written with UTF-8 encoding but Python on Windows might have interpreted the path differently, or cv2.imwrite failed silently on non-ASCII paths (OpenCV imwrite with non-ASCII paths on Windows often fails silently!). That's a known issue: cv2.imread/imwrite cannot handle non-ASCII paths on Windows.

Solution: use cv2.imencode + open().write, or use numpy fromfile. Let me rewrite: `cv2.imencode('.jpg', frame)[1].tofile(out)` which handles unicode paths.

Also cap.set(POS_MSEC) and read worked since the video path... wait, the video path is also non-ASCII and it opened fine (reported frames count). VideoCapture with unicode path might work in newer OpenCV versions, or it may have silently failed? It reported frames: 16797 which matches the log, so it opened fine. But imwrite failed silently.

Let me use TodoWrite to track progress, then fix the script.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "抽取实验1-6各6帧（修复imwrite非ASCII路径问题）", "priority": "high", "status": "in_progress"}, {"content": "查看实验1帧并分析", "priority": "high", "status": "pending"}, {"content": "查看实验2帧并分析", "priority": "high", "status": "pending"}, {"content": "查看实验3帧并分析", "priority": "high", "status": "pending"}, {"content": "查看实验4帧并分析", "priority": "high", "status": "pending"}, {"conten …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"抽取实验1-6各6帧（修复imwrite非ASCII路径问题）","status":"in_progress","priority":"high"},{"content":"查看实验1帧并分析","status":"pending","priority":"high"},{"content":"查看实验2帧并分析","status":"pending","priority":"high"},{"content":"查看实验3帧并分析","status":"pending","priority":"high"},{"content":"查看实验4帧并分析","st …[截断,原长607]`

- 🔧 **Edit** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames.py", "old_string": " out = os.path.join(outdir, \"frame%d.jpg\" % i)\n cv2.imwrite(out, frame, [cv2.IMWRITE_JPEG_QUALITY, 90])", "new_string": " out = os.path.join(outdir, \"frame%d.jpg\" % i)\n ret2, buf = cv2.imencode(\".jpg\", frame, [cv2.IMWRITE_JPEG_QUALITY, 90])\n if not ret2:\n p …[截断,原长508]` → `The file C:\Users\UserX\Downloads\轮式\work\extract_frames.py has been updated successfully. (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:17）

帧写入失败——这是 OpenCV 在 Windows 上 `imwrite` 不支持非 ASCII 路径的已知问题（读取成功但写出静默失败）。改用 `imencode + tofile` 方式。

- 🔧 **Bash** `{"command": "\"/c/Users/UserX/.conda/envs/opencv/python.exe\" \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames.py\" > \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames_log.txt\" 2>&1; cat \"C:\\Users\\UserX\\Downloads\\轮式\\work\\extract_frames_log.txt\"; echo ---; find \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\" -name \"frame*.jpg\" | wc -l", "description": " …[截断,原长419]` → `DONE: 实验1 七彩探照灯实验(1) frames: 16797 dur_s: 559.9 DONE: 实验2 小车前进实验(1) frames: 24250 dur_s: 808.3 DONE: 实验3 小车前后左右综合实验(1) frames: 10100 dur_s: 336.7 DONE: 实验4 舵机旋转控制七彩探照灯(1) frames: 20747 dur_s: 691.6 DONE: 实验5 按键控制小车启动实验(1) frames: 10031 dur_s: 334.4 DONE: 实验6 红外避障实验(1) frames: 13851 dur_s: 461.7 ALL DONE --- 66`

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Hmm, 66 files — that's 11 experiments × 6 = 66? No wait, I only extracted 6 experiments = 36. 66 = 36 + 30? Maybe old frame extractions from experiment 7-11 exist now? Actually earlier the folders were all empty. 66 files... Let me check. Actually maybe the find counted files in all 11 folders — but we only wrote 6 folders. Let me check per folder. Possibly previous runs created some? Earlier find showed nothing. Strange. Let me list.

</details>

- 🔧 **Bash** `{"command": "for d in \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\"/*/; do echo \"$d: $(ls \"$d\" | wc -l)\"; done", "description": "Count files per frames subfolder"}` → `C:\Users\UserX\Downloads\轮式\work\frames/实验1 七彩探照灯实验(1)/: 6 C:\Users\UserX\Downloads\轮式\work\frames/实验10 超声波避障实验(1)/: 6 C:\Users\UserX\Downloads\轮式\work\frames/实验11 带舵机云台的超声波避障实验(1)/: 6 C:\Users\UserX\Downloads\轮式\work\frames/实验2 小车前进实验(1)/: 6 C:\Users\UserX\Downloads\轮式\work\frames/实验3 小车前后左右综合实验(1)/: 6 C:\Users\UserX\ …[截断,原长659]`

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Interesting — all 11 folders have 6 files now. It seems another agent/process (the coordinator) is also extracting frames in parallel, or the earlier extraction eventually flushed. Either way, my 6 target folders have 6 frames each. 66 = 11×6, so someone extracted all 11 (likely a parallel process also writing). Doesn't matter — the 36 frames I need exist now.

Wait, but did my script's frames actually write? Let me check timestamps to make sure my experiment 1-6 frames are fresh. Actually it doesn't matter much — as long as the files exist and are valid JPEGs. But there's a risk the files are being written concurrently and might be incomplete. Let me quickly verify file sizes.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)/\"", "description": "Check frame file sizes for experiment 1"}` → `total 1280 drwxr-xr-x 1 user 197121 0 Oct 30 01:17 ./ drwxr-xr-x 1 user 197121 0 Oct 30 01:12 ../ -rw-r--r-- 1 user 197121 218253 Oct 30 01:17 frame1.jpg -rw-r--r-- 1 user 197121 237744 Oct 30 01:17 frame2.jpg -rw-r--r-- 1 user 197121 167769 Oct 30 01:17 frame3.jpg -rw-r--r-- 1 user 197121 175602 Oct 30 01:17 frame4.jp …[截断,原长433]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:18）

所有目标帧已就位。验证文件大小正常后开始查看实验1的帧。

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验1 七彩探照灯实验(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 1 frames analyzed:

Frame 1 (~45s): WPS 文字 opening "1.七彩探照灯实验.docx". Visible text: "2、实验目的：单片机上电之后，实验效果为七彩灯轮询，主要是学习51单片机的引脚端口控制和LED的使用。" "3、实验原理：所谓的RGB三色灯和普通的LED灯其实没有什么不同，只是在封装上，RGB灯内封装了三个LED（红，绿，蓝），通过控制三种LED亮度（256种亮度级别可选），可以混合出不同的颜色（256*256*256）。由电路原理图可知，本实验中采用的RGB LED灯是共阴LED，一个引脚接地，其余的三个RGB引脚分别接在51单片机最小系统板上的P4.6, P4.5,P4.4 引脚上，同时每个LED灯需要串联一个220欧的电阻作为限流电阻，我们只需在51单片机主控板上控制相应的引脚为高电平，即可点亮相应的LED。" 还有 "这里需要说明一下，我们在讲解本次实验之前会首先对重要寄存器进行一个讲解，" Status bar: 页面1/5, 120% zoom.

Frame 2 (~140s): WPS 文字 same doc, page 2/5. Text about STC12C5A60S2 IO modes: "STC12C5A60S2 系列单片机所有 IO 口（相对于以前的 STC89C52 来说新增了P4口和P5口）可由软件配置成如下4种工作类型：1、准双向口/弱上拉（标准8051输出模式）2、强推挽输出/强上拉 3、仅为输入（高阻）4、开漏输出。STC12C5A60S2系列单片机上电复位后为准双向口/弱上拉模式。2V以上时为高电平，0.8V以下时为低电平。每个IO口驱动能力均可达20mA，但整个芯片最大不得超过120mA。大家如果想了解每个寄存器的详细使用方法，可以参考《STC12C5A60S2单片机中文参考手册》。下面我们就本次实验所用到的P4口的寄存器做一个简单的介绍：P4口的地址是C0H." Plus table 3-1: P4端口地址在C0h，P4口中的每一位均可位寻址，位地址如下: 位 P4.7~P4.0, 位地址 C7h C6h C5h C4h C3h C2h C1h C0h. 表3-1 P4口的各个位地址表.

Frame 3 (~232s): WPS doc page 3/5: "4、实验步骤 4-1. 看懂原理图" with schematic image "STC最小系统接口" U3 STC, showing pins P1.0-P1.7, IN1-IN8 (1-8), RST/RXD/TXD/INT0/INT1/T0/T1/WR/RD (9-17), XTAL2/XTAL1/GND (18-20), VCC/P0.0-P0.7 (40-32), EA/ALE/PSEN (31/30/29), LED_G(31) LED_R(30) LED_B(29) highlighted with red boxes, 28 K2 FM, 27 P6WMB(?), 26 PWM8?, 25 BIN2, 24 BIN1, 23 AIN2, 22 AIN1, 21 PWMA. 图4-1 单片机主控板电路图. Note red boxes around LED_R (pin30), LED_G (pin31), LED_B (pin29).

Frame 4 (~325s): Keil μVision4, project "ColorLED", file tabs main.c and STC12C5A60S2.H. Code visible:
```
/**
 * @par Copyright (C): 2010-2019, Shenzhen Yahboom Tech
 * @file         ColorLED.c
 * @author       Danny
 * @version      V1.0
 * @date         2017.08.16
 * @brief        七彩探照灯实验
 * @details
 * @par History  见如下说明
 */
#include "STC12C5A60S2.H"

#define ON 1    //使能LED
#define OFF 0   //禁止LED

//定义RGB七彩灯引脚
sbit LED_R = P4^6;  //LED_R接在STC12C5A60S2的EA (P4^6) 管脚
sbit LED_G = P4^5;  //LED_G接在STC12C5A60S2的ALE (P4^5) 管脚
sbit LED_B = P4^4;  //LED_B接在STC12C5A60S2的PSEN (P4^4) 管脚

/**
 * Function    delay
 * @author     Danny
 * @date       2017.08.16
 * @brief      延时函数
 * @param      xms: 延时时间（ms）
 * @retval     void
 * @par History 无
 */
void delay(unsigned int xms)
```
Project tree: 目标1 → 源代码组1 → main.c, stc12c5a60s2.h.

Frame 5 (~410s): WPS doc page 5/5, code in doc:
```
int main()
{
    //设置P4口作为普通的IO口使用
    P4SW |= (1<<4);
    P4SW |= (1<<5);
    P4SW |= (1<<6);

    while (1)
    {                    //   LED_R  LED_G  LED_B
        color_led(ON, OFF, OFF); //  1      0     0
        delay(1000);
        color_led(OFF, ON, OFF); //  0      1     0
        delay(1000);
        color_led(OFF, OFF, ON); //  0      0     1
        delay(1000);
        color_led(ON, ON, OFF);  //  1      1     0
        delay(1000);
        color_led(ON, OFF, ON);  //  1      0     1
        delay(1000);
        color_led(OFF, ON, ON);  //  0      1     1
        delay(1000);
        color_led(ON, ON, ON);   //  1      1     1   (highlighted/selected line)
    }
    return 0;
}
通过输入参数开关来控制哪个颜色灯亮灭，从而组合不同颜色。
```

Frame 6 (~515s): STC-ISP V6.85 software. Title: "STC-ISP (V6.85) (售电电话:0513-55012928) 官网:www.STCMCU.com (技术支持QQ:800003751) --- STC: 全球最大的805..." Tabs: 单片机型号: STC12C5A60S2; 引脚刷新 Auto; 串口号 USB-SERIAL CH340 (COM3); 扫描; 最低波特率 2400; 最高波特率 115200; 程序文件是EEPROM文件 checkbox; 打开程序文件 / 打开EEPROM文件 buttons; 起始地址 0x0000; 硬件选项: 随机数据/0/UV/1、程序加密后传输 Id=4; checkboxes: 选择使用内部IRC时钟（不选外部时钟）; 振荡器放大器增益(12M以上建议选择); 复位脚用作I/O口; RESET脚刷低电平高于1.33V时芯片复位; 上电复位使用较长延时; 上电复位可由硬件启动看门狗; 暂门狗定时器分频系数 256; 空闲时浏览器停止看门狗计数; 下次下载时P1.0/P1.1为0/0才可下载程序; 下次下载用户程序时删除用户EEPROM区; 在代码区的最后添加ID号; 选择Flash空白区域的填充值 FF. Buttons: 下载/编程, 停止, 重复编程; 检测MCU选项, 注意/帮助, 重复延时 3秒; 每次下载前重新装载目标文件 (checked), 当目标文件变化时自动装载并发送下载命令 (checked); 发布项目程序, 发布项目帮助, 读取本机磁盘号, 提示音.

Hex window shows program file content 00000h: 02 00 32 43 5B 10 43 BB 20 43 BB 40 E4 FB FA 12 ... 代码长度 009BH, 校验和 437DH, 区域填充, 清空区...
Text below: P1.0和P1.1与下次下载无关; 下次下载用户程序时, 不删除用户EEPROM区; 芯片出口系列号: D170B1E2AF246F; 单片机型号: STC12C5A60S2; 固件版本号: 7.1.41(?); 操作成功！; file path: E:\VC51\四驱车C51平台开发手册\ST_4WD_C51\5.?\..\ColorLED.H(?)

Build output (Keil behind): "compiling main.c... linking... Program Size: data=9.0 xdata=0 code=158 creating hex file from "ColorLED"... "ColorLED" - 0 Error(s), 0 Warning(s)."

Right-bottom PiP: hands connecting white USB cable to robot; robot has blue LED lights glowing (two 7-color LED modules lit blue) on the top plate, black wheels visible, dark chassis. Actually robot view: top-down-ish view showing blue LEDs on module, hands holding white cable.

Now experiment 2.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验2 小车前进实验(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:18）

实验1帧已查看完毕。继续查看实验2的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 2 frames:

Frame 1 (~65s): WPS 文字 "2.小车前进实验.docx" (both "1.七彩探照灯实验.docx" and "2.小车前进实验.docx" tabs open). Text: "...机。通过控制驱动芯片的AIN1, AIN2, BIN1, BIN2, PWMA, PWMB 的电平高低来控制电..." then "机的正转，反转，停止。本次实验主要是控制 AIN1 为高电平，AIN2 为低电平，BIN1 为高电平，BIN2为低电平，进而通过控制 PWMA, PWMB 在 0–255 之间控制小车的速度。一路 PWM 控制小车一侧电机的速度。" "脉冲宽度调制（PWM），是英文"Pulse Width Modulation"的缩写，简称脉宽调制，是利用微处理器的数字输出来对模拟电路进行控制的一种非常有效的技术。简单一点，就是对脉冲宽度的控制." "STC12C5A60S2 系列单片机的 PCA 模块可以通过程序设定，使其工作于8位PWM模式。本次实验我们是用定时器0产生PWM控制电机，从而进一步控制小车的的运动。" Table: 符号/描述/地址/位地址及其符号/复位值: CCON PCA Control Register D8H CF CR - - - - CCF1 CCF0 00xxx,000; CMOD PCA Mode Register D9H CIDL - - - - CPS2 CPS1 CPS0 0xxx,0000. Page 2/28, zoom 110%.

Frame 2 (~202s): WPS doc page 2(?). Table 4-1 STC12C5A60S2 系列单片机特殊功能寄存器表 (AUXR1 Auxiliary Register 1 A2H - PCA_P4 SPI_P4 S2_P4 GF2 ADRJ - DPS x000,00x0). "下面我们就本次实验所用到的定时器0 做一个简单的介绍：工作方式寄存器 TMOD (89H)" TMOD table D7..D0: GATE C/T M1 M0 GATE C/T M1 M0 (定时器1 / 定时器0). "GATE（TOMD.3）：GATE=1 时表示必须是 INT0 脚为高以及 TR0 控制位置1 时才可以打开定时器0/计数器0。" "C/T（TOMD.2）：C/T=1 时用作定计数器，C/T=0 由 TH 和 TL 用作定时器。" "M1,M0（TOMD.1,TOMD.0）：用来选择定时器0/计数器0的工作模式。如下四种" (工作方式... below cut off). Page 2/28? shows 页码2. Zoom 110%.

Frame 3 (~339s): WPS doc page 3/28: "根据我们上面的介绍，本次实验中我们设定定时器0为工作方式1 TMOD=0X01;（2）设置定时/计数器初值，直接将初值写入寄存器 TH0, TL0。计算初值的方法如下：设计数器的最大值为M，则置入的初值X为 计数公式 X=M-计数值 定时方式由 (M-X) T=定时值，得 X=M-定时值/T T为计数周期，是单片机的机器周期。方式0时，M=2^13=8192. 方式1时，M=2^16=65536. 方式2和3时，M=2^8=256。根据我们上面的介绍，本次实验中我们所用的晶振是11.0592Mhz, 设置定时器0为1ms定时。计算过程如下：设机器周期为Tcy, 定时器产生一次中断的时间为t，那么需要计数的个数N=t/Tcy. 可以得出：Tcy=12(1/11.0592Mhz) N=1ms/12(1/11.0592Mhz)=921.6(922) TH0=(65536-922)/32, TL0=(65536-922)%32. 因此：TH0=0XFC; TL0=0X66;" (TH0=0XFC, TL0=0X66 in red).

Frame 4 (~473s): WPS doc page 5/28: schematic fragment "电机驱动芯片" with pins PGND2, PWMB, BO1(?), VM3, BO1, VM2, BO1, PGND, R24 0R, ground. 图4-2 电机驱动芯片 TB6612FNG. "4-2. 理解原理图 由图4-1和4-2 由电路原理图可知 AIN1, AIN2, PWMA, BIN1, BIN2, PWMB 分别接在单片机主控板上的 P2.2, P2.1, P2.0，P2.3, P2.4, P2.5。" Table 图4-3 引脚控制逻辑表: AIN1 AIN2 BIN1 BIN2 PWMA PWMB A01/A02: 1 0 1 0 1 1 正转; 0 1 0 1 1 1 反转; 1 1 1 1 1 1 刹车; 0 0 0 0 0(?) 1 自由停车; X X X X 0 0 刹车. "X:任意电平 VM:CGND:电机/input，VM接 GND接员(?) VOC:CGND:提供/input，VCC接从外部输入进来的5VF, GND接员(?) PWMA/PWMB:可以直接接VCC，然后通过AIN1/AIN2 BIN1/BIN2来控制2个电机". "4-3. 程序核心代码如下：" "1. 基本状态以及汇总…引脚的口…" (cut). Page 5/28.

Frame 5 (~606s): Keil μVision4 project "advance", main.c lines 105-135:
```
108 /**
109 * Function      run
110 * @author       Danny
111 * @date         2017.08.16
112 * @brief        小车前进
113 * @param[in]    void
114 * @param[out]   void
115 * @retval       void
116 * @par History  无
117 */
118 void run(void)
119 {
120     //左电机前进
121     Left_motor_go = 1;    //左电机前进使能
122     Left_motor_back = 0;  //左电机后退禁止
123     //更新指定管脚的PWM值，更改可实现控速（0-20）
124     push_val_left=10;
125
126     //右电机前进
127     Right_motor_go=1;    //右电机前进使能
128     Right_motor_back=0;  //右电机后退禁止
129     //更新指定管脚的PWM值，更改可实现控速（0-20）
130     push_val_right=10;
131     return;
132 }
134 /**
135 * Function      timer0
```
Project tree: 目标1 → 源代码组1 → main.c, stc12c5a60s2.h.

Frame 6 (~744s): Keil main.c lines 153-182:
```
154 /**
155 * Function      main
156 * @author       Danny
157 * @date         2017.08.16
158 * @brief        先延时2s，接着前进
159 * @param[in]    void
160 * @retval       void
161 * @par History  无
162 */
163 void main()
164 {
165     P2=0XC0;    //关电机
166     TMOD=0X01;  //定时器工作方式1
167     TH0=0XFC;   //1ms定时，装入初值
168     TL0=0X66;
169     TR0=1;      //启动Tt0工作 (启动t0工作)
170     ET0=1;      //允许Tt0中断 (允许t0中断)
171     EA =1;      //开总中断   (highlighted)
172
173     delay(2000);//延时2s
174
175     while(1)
176     {
177         run();   //前进
178     }
179     return;
180 }
```

No robot visible in these frames — all screen capture. Video is 808s; frames at 65/202/339/473/606/744s. Robot behavior can't be inferred from frames — no robot shots. I should note that.

Now experiment 3.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验3 小车前后左右综合实验(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:19）

实验2完成。继续查看实验3的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 3 frames:

Frame 1 (~28s): WPS "3.小车前后左右综合实验.docx" (3 tabs: 1.七彩探照灯实验, 2.小车前进实验, 3.小车前后左右综合实验). Shows 图1-1 51单片机主控板 caption, 图1-2 4个直流减速电机 (yellow TT gear motors photo). "2.实验目的：单片机上电后，小车先延时2s，再前进1s，后退1s,左转2s,右转2s,原地左转3s,原地右转3s,停止0.5s。处于这样的循环状态。" "3.实验原理：对于4路直流减速电机的控制我们采用的是TB6612FNG驱动芯片来驱动电机。" Page 1/15, 100%.

Frame 2 (~56s): page 5/15: 图4-3 引脚控制逻辑表 (same logic table as exp2): AIN1 AIN2 BIN1 BIN2 PWMA PWMB A01/A02: 1 0 1 0 1 1 正转; 0 1 0 1 1 1 反转; 1 1 1 1 1 1 刹车; 0 0 0 0 1 1 自由停车; X X X X 0 0 刹车. Notes: X:任意电平; VM/GND:电机电源输入，VM接正 GND接负; VCC/GND:逻辑电平输入，VCC接从外部输入进来的5VF(5V), GND接负; PWMA/PWMB:可以直接接VCC，然后通过AIN1/AIN2 BIN1/BIN2来控制2个电机. "4-3. 程序核心代码如下：1.基本变量以及引脚的定义: //定义电机引脚 sbit Left_motor_go=P2^1; //左电机前进AIN2 sbit Left_motor_back=P2^2(?)" (cut).

Frame 3 (~84s): Keil μVision4 project "CarRun", main.c lines 109-135:
```
/**
 * Function      run
 * @author       Danny
 * @date         2017.08.16
 * @brief        小车前进
 * @param[in]    time: 延时时间
 * @param[out]   void
 * @retval       void
 * @par History  无
 */
void run(unsigned int time)
{
    //左电机前进
    Left_motor_go = 1;    //左电机前进使能
    Left_motor_back = 0;  //左电机后退禁止
    //更新指定管脚的PWM值，更改可实现控速（0-20）
    push_val_left=10;

    //右电机前进
    Right_motor_go=1;    //右电机前进使能
    Right_motor_back=0;  //右电机后退禁止
    //更新指定管脚的PWM值，更改可实现控速（0-20）
    push_val_right=10;

    //延时
    delay(time * 100);
    return;
```
Build Output: Build target '目标 1', compiling main.c..., linking..., Program Size: data=13.2 xdata=0 code=485, creating hex file from "CarRun"..., "CarRun" - 0 Error(s), 0 Warning(s).
Project tree: 目标1 → 源代码组1 → main.c, stc1...

Frame 4 (~112s): Keil main.c lines 214-240:
```
214     push_val_right=0;
215
216     //延时
217     delay(time * 100);
218     return;
219 }
221 /**
222 * Function      spin_left
223 * @author       Danny
224 * @date         2017.08.16
225 * @brief        小车原地左转  原地左转(左轮后退，右轮前进)
226 * @param[in]    time
227 * @param[out]   void
228 * @retval       void
229 * @par History  无
230 */
231 void spin_left(unsigned int time)
232 {
233     //左电机后退
234     Left_motor_go = 0;    //左电机前进禁止
235     Left_motor_back = 1;  //左电机后退使能
236     //更新指定管脚的PWM值，更改可实现控速（0-20）
237     push_val_left=10;
238
239     //右电机前进
240     Right_motor_go=1;    //右电机前进使能
```
There's a red circle highlight annotation around "左轮后退" in the @brief line (a hand-drawn marker/cursor effect from the video). Build output same: CarRun 0 errors 0 warnings.

Frame 5 (~140s): Keil main.c lines 335-360 (main function):
```
335 * @retval       void
336 * @par History  无
337 */
338 void main()
339 {
340     P2=0XC0;    //关电机
341     TMOD=0X01;  //定时器工作方式1
342     TH0=0XFC;   //1ms定时，装入初值
343     TL0=0X66;
344     TR0=1;      //启动Tt0工作 (启动t0工作)
345     ET0=1;      //允许Tt0中断
346     EA =1;      //开总中断  (highlighted)
347
348     while(1)
349     {
350         delay(2000);    //延时2s
351         run(10);        //前进1s（10 * 100ms）
352         back(10);       //后退1s
353         left(20);       //左转2s
354         right(20);      //右转2s
355         spin_left(30);  //原地左转3s
356         spin_right(30); //原地右转3s
357         brak*(5);       //停止0.5s   (likely brake(5))
358     }
359     return;
360 }
```
Build output same.

Frame 6 (~168s): STC-ISP V6.85 (same as before, 单片机型号 STC12C5A60S2, 串口号 USB-SERIAL CH340 (COM3), 最低2400, 最高115200), hex content 代码长度 01E5H, 校验和 DD3CH; text: "正在检测目标手...成功 [D:562*]" "当前波特率: 115200" "正在擦除目标区域..." "下次下载用户程序时, 不删除用户EEPROM区; 单片机型号: STC12C5A60S2; 固件版本号: 7.1.41". Buttons 下载/编程, 停止(highlighted), 重复编程; 检测MCU选项, 注意/帮助, 重复延时3秒. Keil build output at bottom: linking..., Program Size: data=13.2 xdata=0 code=485, creating hex file from "CarRun"... "CarRun" - 0 Error(s), 0 Warning(s).
PiP bottom-right: robot top view: blue LED modules glowing on top plate, black wheels, hands plugging a white USB cable into the main board; robot chassis dark gray with expansion plate; red wires visible.

Now experiment 4.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验4 舵机旋转控制七彩探照灯(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:20）

实验3完成。继续查看实验4的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 4 frames:

Frame 1 (~55s): WPS "4.舵机旋转控制七彩探照灯.docx" (4 tabs open). Page 2/9: "2、实验目的：先延时0.5s，接着舵机开始旋转不同的角度控制七彩灯。" "3、实验原理：舵机工作原理：控制信号由接收机的通道进入信号调制芯片，获得直流的偏置电压。它内部有一个基准电路，产生周期为20ms，宽度为1.5ms的基准信号，将获得的直流偏置电压与电位器的电压比较，获得电压差输出。最后电压差的正负输出到电机驱动芯片决定电机的正反转。当电机转速一定时，通过级联减速此轮带动电位器旋转，使得电压差为0，电机停止转动。舵机的控制：一般需要一个20ms左右的时基脉冲，该脉冲的高电平部分一般为0.5ms-2.5ms范围内的角度控制脉冲部分。本次实验的采用的舵机是180度间服（伺服），控制关系如下：0.5ms---0度; 1.0ms---45度; 1.5ms---90度; 2.0ms---135度; 2.5ms---180度." Zoom 120%.

Frame 2 (~111s): page 3/9: schematics: 图4-2 RGB三色灯 (P4 connector: LED_B2, LED_G3, LED_R4, XH2.54-4P), 图4-3 舵机 (J1: 1 IO, 2 VCC, 3 GND, D1 DUO(?) diode symbol). "注：舵机 SG90 需连接到舵机接口 J1 上方可进行实验。" (red text). "4-1. 看懂原理图 由 4-1, 4-2, 4-3 电路原理图可以知道相应的连接电路，LED_R 连接到主控板上的数字 EA 口，LED_G 和 LED_B 分别接在主控板上的 ALE 和 PSEN，J1 连接到主..." (cut). Page 3/9, zoom 120%.

Frame 3 (~166s): Keil μVision4 project "ServoControlCorlor" (sic), main.c lines 58-84:
```
58 * @retval        void
59 * @par History   无
60 */
61 void servo_control_color()
62 {
63     //定义舵机转动位置
64     int pos = 0;
65     int i = 0;
66     for (pos = 1; pos < 180;  pos=pos+5)
67     {
68         //舵机0度转到180,每次延时5ms
69         for(i=0;i<15;i++)
70         {
71             myangle=pos;
72             delay(5);
73         }
74         //旋转到相应的角度,判断调用相关函数
75         color_light(pos);
76     }
77     for (pos = 180; pos > 0;  pos=pos-5)
78     {
79         //舵机180旋转到0,每次延时5ms
80         for(i=0;i<15;i++)
81         {
82             myangle=pos;
83             delay(5);
84         }
```
Build Output: Build target '目标 1', compiling main.c..., linking..., Program Size: data=9.0 xdata=9 code=803, creating hex file from "ServoControlCorlor"..., "ServoControlCorlor" - 0 Error(s), 0 Warning(s).

Frame 4 (~222s): main.c lines 198-225:
```
198 * @author      Danny
199 * @date        2017.08.16
200 * @brief       先延时0.5. 接着调用舵机控制七彩灯程序
201 * @param[in]   void
202 * @retval      void
203 * @par History 无
204 */
206 void main()
207 {
208     unsigned char i =0;
209     TMOD=0X10;  //定时器工作方式1
210     TH1=0XFF;   //100us定时，装入初值
211     TL1=0XA4;
212     TR1=1;      //启动Tt1工作 (启动t1工作)
213     ET1=1;      //允许Tt1中断 (允许t1中断)
214     EA =1;      //开总中断
215
216     //设置P4口作为普通的IO口使用
217     P4SW |= (1<<4);
218     P4SW |= (1<<5);
219     P4SW |= (1<<6);
220
221     //舵机引脚初始为高电平
222     ServoPin=1;
223
224     //初始化舵机位置向前
225     for(i = 0; i<15;i++)
```
Build output same.

Frame 5 (~277s): main.c lines 172-198:
```
172 * @brief       TIMER1中断服务子函数产生PWM信号，控制舵机
173 * @param[in]   void
174 * @param[out]  void
175 * @retval      void
176 * @par History 无
177 */
178 void timer1() interrupt 3
179 {
180     int PulseWidth;
181     TH1=0XFF;          //100us定时，装入初值
182     TL1=0XA4;
183     count++;
184                //定义脉宽变量
185     PulseWidth = ((myangle*11)+500)/100; //为了将0-180度转换为相应的脉宽值  (highlighted)
186     if(count == PulseWidth)
187     {
188         ServoPin=0;    //将舵机接口电平置低
189     }
190     if(count == 190)   //190为最终调试获得的一个最佳值
191     {
192         count = 0;
193         ServoPin=1;    //将舵机接口电平置高
194     }
195 }
197 /**
198 * Function     main
```
Build output same.

Frame 6 (~332s): same as frame 5 but highlight on line 193 ServoPin=1; //将舵机接口电平置高. Build output same. So frames 5 and 6 nearly identical (both showing timer1 ISR). Note: no robot PiP visible in exp4 frames; all Keil/WPS screens.

Now experiment 5.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验5 按键控制小车启动实验(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:20）

实验4完成。继续查看实验5的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 5 frames:

Frame 1 (~27s): WPS "5.按键控制小车的启动.docx" (5 tabs). Page 1/13: "2.实验目的：单片机上电后，按下启动键，小车先延时2s，再前进1s，后退1s,左转2s,右转2s,原地左转3s,原地右转3s,停止0.5s。" "3.实验原理：通常我们的按键开关一般都是机械弹性开关，当机械触点断开、闭合时，由于机械触点的弹性作用，一个按键开关在闭合时不会马上就能稳定的接通，在断开时也不会一下子彻底断开，而是在闭合和断开时会伴随着一连串的抖动。" Below: 按键抖动波形图 (键按下). 100%.

Frame 2 (~54s): page 2/13: 图3-1 按键抖动状态图 with waveforms labeled 键按下, 前沿抖动, 键稳定, 后沿抖动. "抖动时间一般都是由按键的机械特性决定的，一般都会在10ms 以内，为了确保程序对按键的一次闭合只响应一次，必须进行按键的消抖处理，有硬件消抖和软件消抖。其中，软件消抖指的是检测出键闭合后执行一个延时程序，产生5ms～10ms的延时，让前沿抖动消失后再一次检测键的状态，如果仍保持闭合状态电平，则确认为真正有键按下。当检测到按键被释放后，也要给5ms～10ms 的延时，待后沿抖动消失后才能转入该键的处理程序。硬件消抖是在开关两段接一个0.1uf 的电容。本次实验我们采取的是软件延时去抖。另外关于PWM 的原理以及定时器的理论知识请见实验二以及实验三。"

Frame 3 (~81s): page 2/13 scrolled: same 图3-1 caption, "下面我们来讲解按键控制小车启动实验的硬件和软件设计。4、实验步骤 4-1. 看懂原理图".

Frame 4 (~108s): Keil μVision4 project "KeyScanStart", main.c lines 46-72:
```
46 }
48 /**
49 * Function      key_scan
50 * @author       Danny
51 * @date         2017.08.16
52 * @brief        按键检测（包含软件按键去抖）
53 * @param[in]    void
54 * @param[out]   void
55 * @retval       void
56 * @par History  无
57 */
58 void key_scan(void)
59 {
60   while (key!=0);       //当按键没有被按下一直循环
61   while (scan(void))    -- actually "while (scan(void))" seems wrong; likely "while(!scan)"? Reading: line61 "while (scan(void))" hmm. Probably it's "while (!scan());"? The screenshot shows "while (scan(void))". Hard to be sure; I'll transcribe as seen: "while (scan(void))" — but that's likely "while (scan())" cut off. I'll note as seen.
62 {
63   while (key!=0);   //当按键没有被按下一直循环
64   while (key==0)    //当按键被按下时
65   {
66     delay(10);      //延时10ms
67     if (key==0)     //第二次判断按键是否被按下
68     {
69       delay(100);
70       while (key==0);  //判断按键是否被松开
71     }
72   }
```
Actually reading more carefully: line 61 "while (scan(void))" doesn't make sense; it might be "while (!key_scan())". Let me transcribe conservatively: line 60: `while (key!=0);   //当按键没有被按下一直循环`; line 61: `while (scan(void))` — hmm could be `while (!scan())`. The visible text is "while (scan(void))". I'll transcribe with caution noting possible misreading.

Project tree: 目标1 → 源代码组1 → main.c, stc12c5a60...

Frame 5 (~134s): main.c lines 358-385:
```
358 *                   原地左转3s,原地右转3s,停止0.5s
359 * @param[in]   void
360 * @retval      void
361 * @par History 无
362 */
364 void main()
365 {
366     P2=0XC0;   //关电机
367     TMOD=0X01; //定时器工作方式1
368     TH0=0XFC;  //1ms定时，装入初值
369     TL0=0X66;
370     TR0=1;     //启动Tt0工作 (启动t0工作)
371     ET0=1;     //允许Tt0中断
372     EA =1;     //开总中断
373
374     key_scan();     //调用按键扫描函数
375     while(1)
376     {
377         delay(2000);    //延时2s
378         run(10);        //前进1s（10 * 100ms）
379         back(10);       //后退1s
380         left(20);       //左转2s
381         right(20);      //右转2s
382         spin_left(30);  //原地左转3s
383         spin_right(30); //原地右转3s
384         brake(5);       //停止0.5s
385     }
```

Frame 6 (~161s): STC-ISP V6.85 downloading KeyScanStart hex (代码长度 01F2H, 校验和 D8F9H). Tooltip visible: "下次是否需要P1.0和P1.1同时为低电平时才可下载程序; 连接: P1.0和P1.1同时为低电平时才可下载; 不接: 下载时不会割P1.0和P1.1的电平" (approximately - tooltip about P1.0/P1.1). 操作成功！ 固件版本号: 7.1.41. 单片机型号: STC12C5A60S2. File path: E:\VC51\四驱车C51平台开发手册\ST_4WD_C51\5...\KeyScanStart.h(ex). Keil build output: Program Size: data=13.2 xdata=0 code=490, creating hex file from "KeyScanStart"... "KeyScanStart" - 0 Error(s), 0 Warning(s). Buttons 下载/编程 highlighted (blue), 停止, 重复编程.
PiP: robot top view with blue LED modules lit, main board with STC chip visible, hand plugging white USB cable, then hand near board. Robot: dark chassis, two blue LED modules at front, black wheels.

Now experiment 6.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame1.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame2.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame3.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame4.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame5.jpg"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\轮式\\work\\frames\\实验6 红外避障实验(1)\\frame6.jpg"}` → `[Attached image/jpeg: Read image]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:21）

实验5完成。继续查看实验6的6帧。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Experiment 6 frames:

Frame 1 (~37s): WPS "6.红外避障实验.docx" (6 tabs: 2.小...进实验, 3.小车...综合实验, 4.舵...探照灯, 5.按...的启动, 6.红...避障实验). Page 1/11: 图1-2 2路红外避障模块 (photo of robot with blue push button module highlighted red box, servo; caption annotation). "2、实验目的：单片机上电之后，启动红外避障功能，当左边传感器检测到障碍物时小车向右转，当右边传感器检测到时小车向左转。" "3、实验原理：红外传感器具有一对红外发射与接收管，发射管发射出一定频率的红外线，" Zoom 120%.

Frame 2 (~74s): page 1/11 continued: "当检测方向遇到障碍物时，红外线红外线反射回来被接收管接收。它常用于安装在小车上，判断前方是否有障碍物。可通过电位器设置阈值。正前方有障碍时绿灯亮起，OUT引脚为低电平，反之为高电平。红外传感器避障的基本原理是利用物体的反射性质，在一定范围内，如果没有障碍物，发射出去的红外线，因为传播的距离越来越远而逐渐减弱，最后消失。如果有障碍物红外线遇到障碍物，被反射到达传感器接收头。我们本次实验采用的是两路红外传感器分别连接在51单片机主控板上的P1.6, P1.4引脚上。我们通过检测两端口的电平来判断障碍物的情况，并做出相应的避障动作。另外关于PWM的原理以及定时器的理论知识请见实验二以及实验三。" Below "4、实验步骤" (cut).

Frame 3 (~111s): page 3/11: "4-2 理解原理图 由电路原理图可知左边的红外传感器接在主控板上的P1.6（IN7）口上，右边的则接在P1.4(IN5)口上。模块状态指示灯示意图:" Labeled photo of IR module: S2: 可测光源AD值 (potentiometer), L1: 避障灯, GND 地, LT 寻光输出, HW 避障输出, VCC 电源 (4-pin connector), L3: 电源灯, L2: 寻光灯. "注：1. 进行实验时，Arduino 功能跳线不需要插跳线帽，这是 51 单片机上面。(yellow highlighted 不需要) 2. 本次实验中我们可以调整红外避障模块上的电位器来设置红外避障的距离，以达到比较好的实验效果。调节方法：调节该模块上的电位器【SW1】，使得红外发射管【LEAS1】红外接收管【RC1】距离障碍物小于10cm时，LED灯【L1】亮起；否则，LED..." (cut).

Frame 4 (~148s): Keil μVision4 project "infrared_avoid", main.c lines 258-287:
```
259     TMOD=0X01;  //定时器工作方式1
260     TH0=0XFC;   //1ms定时，装入初值
261     TL0=0X66;
262     TR0=1;      //启动Tt0工作 (启动t0工作)
263     ET0=1;      //允许Tt0中断
264     EA =1;      //开总中断
266     //调用按键扫描函数
267     key_scan();
269     while(1)
270     {
271         //遇到障碍物,红外避障模块的指示灯亮,端口电平为0
272         //未遇到障碍物,红外避障模块的指示灯灭,端口电平为1
273         LeftSensorValue  = AvoidSensorLeft;
274         RightSensorValue = AvoidSensorRight;
276         if (LeftSensorValue == 1 && RightSensorValue == 1)
277         {
278             run();        //当两侧均未检测到障碍物时调用前进函数
279         }
280         else if (LeftSensorValue == 1 && RightSensorValue == 0)
281         {
282             spin_left(2); //右边探测到有障碍物，有信号返回，原地向左转
283         }
284         else if (RightSensorValue == 1 && LeftSensorValue == 0)
285         {
286             spin_right(2);//左边探测到有障碍物，有信号返回，原地向右转
287         }
```
Build Output: Program Size: data=15.2 xdata=0 code=468; creating hex file from "infrared_avoid"...; "infrared_avoid" - 0 Error(s), 0 Warning(s).

Frame 5 (~186s): main.c lines 265-293 plus Build Output "Build target '目标 1' compiling main.c... linking..." and status bar "Rebuild all target files" — the mouse is clicking the Rebuild button (red circle annotation on toolbar). Code continues:
```
288         else
289         {
290             spin_right(2);//当两侧均检测到障碍物时调用固定方向的避障(原地右转)
291         }
292     }
293     return;
```
So the behavior: both clear → run; right sensor detects (RightSensorValue==0) → spin_left(2); left detects → spin_right(2); both detect → spin_right(2).

Frame 6 (~223s): same Keil code; PiP video bottom-right: robot on wooden floor, blue LED modules lit, red LED on main board lit, hand (finger) touching/pushing robot front; white USB cable plugged into board; black wheels; front IR sensors visible. The person's hand is near the front of the robot (probably placing obstacle or holding robot). Robot appears tilted showing bottom/front. Actually image shows top view of robot with hand at bottom edge.

Now I have all 36 frames reviewed. Let me also mark todos and compose the final comprehensive Chinese report.

Let me double check some details for accuracy:

Exp1 frame6: STC-ISP V6.85; the title bar "STC-ISP (V6.85) (售电电话:0513-55012928)" — likely "售前电话" but rendered small; I'll transcribe as seen with caution. Also "暂门狗定时器分频系数" is likely "看门狗定时器分频系数". I'll note uncertain characters. 代码长度 009BH, 校验和 437DH. Chip: STC12C5A60S2, 固件版本号 7.1.41(?), 芯片出口系列号(?): D170B1E2AF246F — likely "芯片出厂序列号". I'll transcribe approximately and note.

Exp1 frame4 Keil project name: "ColorLED" (title "ColorLED - µVision4"). Code as transcribed. Frame6 build output: compiling main.c... linking... Program Size: data=9.0 xdata=0 code=158. creating hex file from "ColorLED"... "ColorLED" - 0 Error(s), 0 Warning(s).

PiP exp1 frame6: hands plugging white USB cable into robot; robot top plate with two LED modules glowing blue; dark chassis; two wheels visible (mid/rear). The LEDs are on small PCB modules at front corners. Also on the robot there's the main board.

Exp2: no robot PiP visible in any frame (all screen). Durations: 808s total; frames at 8% (65s), 25% (202s), 41.5% (335s), 58.5% (473s), 75% (606s), 92% (744s). All WPS/Keil. Note robot behavior not visible from frames; cannot confirm.

Exp2 frame1 top text partially visible: "...机。通过控制驱动芯片的AIN1, AIN2, BIN1, BIN2, PWMA, PWMB 的电平高低来控制电..." 

Exp2 frame4: schematic shows "电机驱动芯片" with PGND2, PWMB(14?), VM3(13?), BO1, VM2... transcribed: pins labeled PWMB(15?), VM3(14?), BO1, VM2(13?), BO1... and R24 0R. 图4-2 电机驱动芯片 TB6612FNG. Text: "由图4-1和4-2 由电路原理图可知 AIN1, AIN2, PWMA, BIN1, BIN2, PWMB 分别接在单片机主控板上的 P2.2, P2.1, P2.0，P2.3, P2.4, P2.5。" Logic table 图4-3.

Exp2 frame5/6: Keil project "advance". run() function with Left_motor_go, push_val_left=10 etc. main() with P2=0XC0; TMOD=0X01; TH0=0XFC; TL0=0X66; TR0=1; ET0=1; EA=1; delay(2000); while(1){run();}.

Exp3: project CarRun; main with the full sequence; frame6 STC-ISP downloading, 正在擦除目标区域..., 当前波特率: 115200. PiP: robot with blue LEDs, hands plugging USB cable.

Exp4: project "ServoControlCorlor" (typo in original). servo_control_color(), timer1() interrupt 3, main() with TMOD=0X10, TH1=0XFF, TL1=0XA4, TR1=1, ET1=1, EA=1, P4SW |= (1<<4/5/6), ServoPin=1. Doc: SG90 servo connect to J1. 0.5ms→0°, 1.0ms→45°, 1.5ms→90°, 2.0ms→135°, 2.5ms→180°. No robot PiP in the 6 frames.

Exp5: project "KeyScanStart". key_scan with debounce; main with key_scan() then while(1) sequence. STC-ISP with tooltip about P1.0/P1.1. PiP robot with blue LEDs, red LED on board.

Exp6: project "infrared_avoid". Sensors on P1.6 (IN7) left, P1.4 (IN5) right. Module labeled S2 pot (可测光源AD值), L1 避障灯, L2 寻光灯, L3 电源灯, pins GND/LT/HW/VCC. Adjust SW1 so L1 lights when obstacle <10cm. Code logic as transcribed. PiP in frame6.

Now compose the final report in Chinese, structured per experiment with the 5 required sections. Only describe what's actually seen; mark uncertainties. Also mention that exp1/3/5/6 include STC-ISP screens; exp2/4 don't show robot PiP except noted.

Frame timestamps: I can give approximate video-time positions (8%, 25%... of total duration). I'll note approximate time offsets: for each experiment list frame times: e.g. Exp1 (559.9s): f1≈45s, f2≈140s, f3≈232s, f4≈325s, f5≈410s, f6≈515s. Exp2 (808.3s): 65, 202, 335, 473, 606, 744. Exp3 (336.7s): 27, 84, 140, 197, 253, 310. Wait — compute: 0.08*336.7=26.9; 0.25=84.2; 0.415=139.7; 0.585=197.0; 0.75=252.5; 0.92=309.8. Good.

Exp4 (691.6s): 55.3, 172.9, 287.0, 404.6, 518.7, 636.3. Hmm 0.415*691.6=287.0; 0.585=404.6; 0.75=518.7; 0.92=636.3.

Exp5 (334.4s): 26.8, 83.6, 138.8, 195.6, 250.8, 307.6.

Exp6 (461.7s): 36.9, 115.4, 191.6, 270.1, 346.3, 424.8.

Wait — earlier I described frame times differently (I guessed ~28s for exp3 f1 etc.). The extraction used fracs 0.08, 0.25, 0.415, 0.585, 0.75, 0.92. So for exp3: 26.9, 84.2, 139.7, 197.0, 252.5, 309.8. My earlier narrative guesses are irrelevant; I'll use computed times.

Note the caveat: since the frames folders were empty initially, I extracted them myself; mention this briefly in the report header? The instruction says final reply should be the 6-experiment analysis. I should briefly note the extraction step at the top (one line) since the main agent should know frames were regenerated. Keep it short.

Also cleanup: I created extract_frames.py and log. That's fine to leave; it's a working artifact. Maybe delete? The task didn't ask; leave it, mention briefly.

Let me write the final comprehensive Chinese report now. It must be complete since it's the only content returned.

Structure per experiment:
1. 画面场景
2. 电脑软件界面细节
3. 小车/模块的行为
4. 人手操作动作
5. 对写实验指导书有用的细节

Be careful to only state what's seen. For experiments where no robot PiP appears (exp2 frames, exp4 frames, exp5 mostly screen), state that.

One correction: Exp5 frame6 tooltip text — the tooltip near "下次冷启动时P1.0/P1.1为0/0才可下载程序" checkbox reads something like "连接:P1.0和P1.1同时为低电平时才可下载" / "不接:下载时不会检测P1.0和P1.1的电平". I'll transcribe with "约/无法完全确认" caveat.

Exp1 frame6 title: "STC-ISP (V6.85) (售电电话:0513-55012928) 官网:www.STCMCU.com (技术支持QQ:800003751) --- STC: 全球最大的805..." — likely "售前电话". I'll note approximate.

Also in exp1 f6 hex area first line: "00000h: 02 00 32 43 5B 10 43 BB 20 43 BB 40 E4 FB FA 12" — I transcribed partially; fine to quote first bytes as seen but risk of misreading; I'll include a short excerpt with caution. Actually for the guide, the important bits: 代码长度 009BH、校验和 437DH.

For exp3 f6: 代码长度 01E5H, 校验和 DD3CH; text "正在检测目标手...成功 [D:562*]" — probably "正在检测目标手机...成功 [D:562*]"? Hmm. STC-ISP messages are like "正在检测目标单片机 ... 单片机型号STC12..." Actually the text at that moment: "正在检测目标手... 成功 [D:562*]" unclear; the left shows "正在擦除目标区域...". I'll quote with caution: "正在检测目标…成功" "当前波特率: 115200" "正在擦除目标区域...".

Exp3 f6 STC-ISP hardware options checkboxes visible same as exp1. PiP: hand plugging white USB cable into robot; robot's two blue LED modules lit; black wheels; red/black wires.

For exp5 f6: hex 代码长度 01F2H, 校验和 D8F9H; 操作成功！; Keil build output code=490 for KeyScanStart.

Also exp5 f6 PiP shows a red LED lit on the mainboard (likely power LED), blue 7-color LED modules lit blue.

Exp6 build: Program Size: data=15.2 xdata=0 code=468.

Keil menu bars: File Edit View Project Flash Debug Peripherals Tools SVCS Window Help — same across.

WPS tabs accumulate: exp3 shows 3 tabs; exp4 shows 4 tabs; exp5 shows 5 tabs; exp6 shows 6 tabs (2,3,4,5,6 visible + 1 maybe scrolled out; in exp6 f1 tabs visible: 2.小...进实验, 3.小车...综合实验, 4.舵...探照灯, 5.按...的启动, 6.红...避障实验). In exp1 only 1 tab ("我的WPS" + 1.七彩探照灯实验.docx). Exp2: 2 tabs (1.七彩探照灯实验.docx, 2.小车前进实验.docx). Good detail.

Desktop wallpaper differs per video (beach cliff for exp1, waterfall/green for exp2-3? Actually exp2 wallpaper: waterfall/flowers right side; exp3: orange canyon + lavender field; exp4: lavender field; exp5: canyon; exp6: waterfall green). Not important but can mention briefly.

Robot description (from PiP shots in exp1 f6, exp3 f6, exp5 f6, exp6 f6): dark gray/black acrylic chassis, 4 wheels (two visible per view; exp6 f6 shows 4 black wheels), two LED modules on front corners glowing blue, main control board (dark PCB) mounted mid with white USB cable, expansion plate. In exp6 f6: robot has front IR sensor modules? Actually the two blue modules on the front are the 7-color LED modules... wait, in exp6 (红外避障) the front modules glowing blue would be the IR avoid modules? The IR module in doc f3 has L1 避障灯 etc. The PiP shows two small PCBs at front glowing blue — those are likely the IR避障 modules with their LEDs, or the RGB LED modules. In exp1 (LED experiment) the same blue glow — so blue-glowing modules = RGB LED modules (7-color showing blue). In exp5/6 PiPs the same two blue modules appear. So the robot carries the RGB modules at front; the IR sensors may be mounted lower at front edge — in exp6 f6, at the front lower edge there appear small boards. Can't confirm precisely; note as such.

Yellow TT gear motors shown in exp3 doc figure 图1-2.

Now, write the final answer. It will be long; that's expected ("请写全"). Use clear markdown headers per experiment.

Also add a short preamble noting frames were extracted at 8%/25%/41.5%/58.5%/75%/92% of each video's duration (since original frames folder was empty), plus durations. This is honest about method and useful for the main agent.

Write it now.

</details>

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-30 01:21）

全部36帧已查看完毕。以下为6个实验的完整分析报告。

---

**说明**：`work\frames` 下原有目录为空，我已用 conda opencv 环境从 `实验视频mp4` 目录的源视频重新抽帧（每个视频取 8%、25%、41.5%、58.5%、75%、92% 处共 6 帧，按时间顺序即 frame1→frame6）。各视频时长：实验1≈560s、实验2≈808s、实验3≈337s、实验4≈692s、实验5≈334s、实验6≈462s。以下分析基于这36帧（抽帧脚本留存于 `C:\Users\UserX\Downloads\轮式\work\extract_frames.py`）。

这些视频是“屏幕录制 + 右下角实物小窗（PiP）”形式的教程录像，主体内容是 WPS 文字打开的实验指导书 docx、Keil µVision4 代码界面、STC-ISP 烧录软件界面。

---

## 实验1 七彩探照灯实验

**1. 画面场景**
- 6 帧均为电脑屏幕截图，无独立实拍场景帧；仅 frame6 右下角小窗可见小车：深灰色多层亚克力底盘、黑色橡胶轮（画面中可见2轮以上）、车体前部两侧各有一块小型 LED 模块，正发出蓝光，主控板在车体中部，一根白色 USB 线连向板子。桌面上可见的器材无法确认（无整屏实拍）。

**2. 电脑软件界面细节**
- frame1–3、frame5：WPS 文字，文档名"1.七彩探照灯实验.docx"（标签栏还有“我的WPS”），缩放 120%，共5页。可抄录的文字：
  - “2、实验目的：单片机上电之后，实验效果为七彩灯轮询，主要是学习51单片机的引脚端口控制和LED的使用。”
  - “3、实验原理：所谓的RGB三色灯和普通的LED灯其实没有什么不同，只是在封装上，RGB灯内封装了三个LED（红，绿，蓝），通过控制三种LED亮度（256种亮度级别可选），可以混合出不同的颜色（256*256*256）。由电路原理图可知，本实验中采用的RGB LED灯是共阴LED，一个引脚接地，其余的三个RGB引脚分别接在51单片机最小系统板上的P4.6, P4.5, P4.4引脚上，同时每个LED灯需要串联一个220欧的电阻作为限流电阻……控制相应的引脚为高电平，即可点亮相应的LED。”
  - frame2（第2页）：STC12C5A60S2 的 IO 口4种工作类型（准双向口/弱上拉、强推挽输出/强上拉、仅为输入（高阻）、开漏输出）；上电复位后为准双向口/弱上拉，2V以上为高电平、0.8V以下为低电平，每个IO口驱动能力20mA、整个芯片最大不超过120mA；“P4口的地址是C0H”；表3-1“P4口的各个位地址表”：位 P4.7~P4.0 对应位地址 C7h、C6h、C5h、C4h、C3h、C2h、C1h、C0h。
  - frame3（第3页）：“4、实验步骤 4-1.看懂原理图”，插入“图4-1 单片机主控板电路图”，为“STC最小系统接口（U3 STC）”引脚图，其中 31（EA）、30（ALE）、29（PSEN）三个引脚旁分别标注 LED_G、LED_R、LED_B 并用红框圈出；其余引脚含 IN1~IN8(P1.0~P1.7)、RST/RXD/TXD/INT0/INT1/T0/T1/WR/RD、XTAL1/XTAL2、P0.0~P0.7、K2 FM、PWMA/B、AIN1/AIN2、BIN1/BIN2 等。
  - frame4：Keil µVision4，标题栏"ColorLED - µVision4"，菜单 File/Edit/View/Project/Flash/Debug/Peripherals/Tools/SVCS/Window/Help，工程树“目标1→源代码组1→main.c、stc12c5a60s2.h”。代码窗口（main.c）可抄录：
    ```c
    /**
     * @par Copyright (C): 2010-2019, Shenzhen Yahboom Tech
     * @file      ColorLED.c
     * @author    Danny
     * @version   V1.0
     * @date      2017.08.16
     * @brief     七彩探照灯实验
     */
    #include "STC12C5A60S2.H"
    #define ON 1    //使能LED
    #define OFF 0   //禁止LED
    //定义RGB七彩灯引脚
    sbit LED_R = P4^6;  //LED_R接在STC12C5A60S2的EA (P4^6) 管脚
    sbit LED_G = P4^5;  //LED_G接在STC12C5A60S2的ALE (P4^5) 管脚
    sbit LED_B = P4^4;  //LED_B接在STC12C5A60S2的PSEN (P4^4) 管脚
    ```
    以及 delay 函数注释头（@param xms: 延时时间（ms））。
  - frame5（docx第5页）主函数代码：
    ```c
    int main()
    {
        //设置P4口作为普通的IO口使用
        P4SW |= (1<<4);
        P4SW |= (1<<5);
        P4SW |= (1<<6);
        while (1)
        {                        //  LED_R LED_G LED_B
            color_led(ON, OFF, OFF);  // 1 0 0
            delay(1000);
            color_led(OFF, ON, OFF);  // 0 1 0
            delay(1000);
            color_led(OFF, OFF, ON);  // 0 0 1
            delay(1000);
            color_led(ON, ON, OFF);   // 1 1 0
            delay(1000);
            color_led(ON, OFF, ON);   // 1 0 1
            delay(1000);
            color_led(OFF, ON, ON);   // 0 1 1
            delay(1000);
            color_led(ON, ON, ON);    // 1 1 1   （此行被鼠标选中高亮）
        }
        return 0;
    }
    ```
    下方文字：“通过输入参数开关来控制哪个颜色灯亮灭，从而组合不同颜色。”
- frame6：STC-ISP V6.85 烧录软件。标题栏含“STC-ISP (V6.85) (售电电话:0513-55012928) 官网:www.STCMCU.com (技术支持QQ:800003751)”（“售电电话”疑为“售前电话”，小字无法完全确认）。界面抄录：单片机型号 STC12C5A60S2；串口号 USB-SERIAL CH340 (COM3)；最低波特率 2400、最高波特率 115200；硬件选项含“选择使用内部IRC时钟（不选外部时钟）”“振荡器放大器增益(12M以上建议选择)”“复位脚用作I/O口”“上电复位使用较长延时”“看门狗定时器分频系数 256”（截图小字似为“暂门狗”，实应为看门狗）“下次下载时P1.0/P1.1为0/0才可下载程序”等；按钮：下载/编程、停止、重复编程、检测MCU选项、注意/帮助、重复延时3秒、“每次下载前重新装载目标文件”（勾选）、“当目标文件变化时自动装载并发送下载命令”（勾选）。hex 窗口显示代码长度 009BH、校验和 437DH。信息区：“芯片出口系列号： D170B1E2AF246F（疑为“出厂序列号”）、单片机型号： STC12C5A60S2、固件版本号： 7.1.41、操作成功！”，文件路径"E:\VC51\四驱车C51平台开发手册\ST_4WD_C51\5…\ColorLED…"。同帧背后 Keil 的 Build Output："compiling main.c... linking... Program Size: data=9.0 xdata=0 code=158 creating hex file from "ColorLED"... "ColorLED" - 0 Error(s), 0 Warning(s)."

**3. 小车/模块的行为**
- 仅 frame6 小窗可见：两个七彩灯模块持续发蓝光（对应程序轮询中的一种颜色状态）。其余帧为屏幕画面，无法从帧序确认灯色变化的完整时序；依代码可知设计行为为红→绿→蓝→黄(红+绿)→品红(红+蓝)→青(绿+蓝)→白(红+绿+蓝)各1秒循环。

**4. 人手操作动作**
- frame6 小窗：双手正在把白色 USB 线（一端似连 USB 转串口/供电）插到小车主控板上；其余帧无手部动作（纯屏幕操作，鼠标在 docx/Keil 中滚动、选中代码行）。

**5. 对写实验指导书有用的细节**
- RGB 灯为共阴接法，引脚经 220Ω 限流电阻接 P4.6/P4.5/P4.4（即复用 EA/ALE/PSEN 脚），需用 P4SW 寄存器把 P4.4~P4.6 设为普通 IO。
- 主控板原理图中 LED_R/LED_G/LED_B 集中在 29/30/31 脚（PSEN/ALE/EA）。
- 烧录环境：STC-ISP V6.85 + CH340 串口（COM3）+ 115200 波特率，固件版本 7.1.41。
- 实物车前部两块 RGB 灯板、白色 USB 下载线。

---

## 实验2 小车前进实验

**1. 画面场景**
- 6 帧全部为屏幕画面（WPS docx 与 Keil），右下角无实物小窗，小车外观、桌面器材在本视频抽帧中不可见（无法确认）。

**2. 电脑软件界面细节**
- frame1：WPS 文字"2.小车前进实验.docx"（同时开着"1.七彩探照灯实验.docx"两个标签），110%缩放，页2/28。可抄录：“……机。通过控制驱动芯片的AIN1, AIN2, BIN1, BIN2, PWMA, PWMB 的电平高低来控制电……”“机的正转，反转，停止。本次实验主要是控制AIN1为高电平，AIN2为低电平，BIN1为高电平，BIN2为低电平，进而通过控制PWMA, PWMB 在0–255之间控制小车的速度。一路PWM控制小车一侧电机的速度。”“脉冲宽度调制（PWM），是英文”Pulse Width Modulation“的缩写……就是对脉冲宽度的控制。”“STC12C5A60S2系列单片机的PCA模块可以通过程序设定，使其工作于8位PWM模式。本次实验我们是用定时器0产生PWM控制电机，从而进一步控制小车的的运动。”下方寄存器表：CCON（PCA Control Register, D8H, CF CR … CCF1 CCF0, 复位值00xxx,000）、CMOD（PCA Mode Register, D9H, CIDL … CPS2 CPS1 CPS0）。
- frame2：表4-1“STC12C5A60S2系列单片机特殊功能寄存器表”（可见 AUXR1, A2H, …PCA_P4 SPI_P4 S2_P4 GF2 ADRJ … DPS）。文字：“下面我们就本次实验所用到的定时器0做一个简单的介绍：工作方式寄存器 TMOD（89H）”，TMOD 位表 D7~D0：GATE C/T M1 M0（定时器1）| GATE C/T M1 M0（定时器0）；“GATE（TOMD.3）：GATE=1时表示必须是INT0脚为高以及TR0控制位置1时才可以打开定时器0/计数器0。”“C/T（TOMD.2）：C/T=1时用作定计数器，C/T=0由TH和TL用作定时器。”“M1,M0（TOMD.1,TOMD.0）：用来选择定时器0/计数器0的工作模式。如下四种（工作方式…）”。（注：原文把"TMOD"误写作"TOMD"，按截图抄录。）
- frame3（页3/28）：初值计算全文：“本次实验中我们设定定时器0为工作方式1 TMOD=0X01；（2）设置定时/计数器初值，直接将初值写入寄存器TH0, TL0。计算初值的方法如下：设计数器的最大值为M，则置入的初值X为 计数公式X=M-计数值 定时方式由(M-X)T=定时值，得X=M-定时值/T T为计数周期，是单片机的机器周期。方式0时，M=2¹³=8192. 方式1时，M=2¹⁶=65536. 方式2和3时，M=2⁸=256。根据我们上面的介绍，本次实验中我们所用的晶振是11.0592Mhz，设置定时器0为1ms定时。……N=1ms/12(1/11.0592Mhz)=921.6(922) TH0=(65536-922)/32, TL0=(65536-922)%32. 因此：TH0=0XFC; TL0=0X66;”（TH0=0XFC、TL0=0X66 为红色强调）。
- frame4（页5/28）：插入“图4-2 电机驱动芯片 TB6612FNG”原理图（可见 PGND2、PWMB、VM3、BO1/BO2、VM2、PGND、R24 0R 等网络标号）与“图4-3 引脚控制逻辑表”。文字：“4-2.理解原理图 由图4-1和4-2由电路原理图可知AIN1, AIN2, PWMA, BIN1, BIN2, PWMB分别接在单片机主控板上的P2.2, P2.1, P2.0，P2.3, P2.4, P2.5。”逻辑表内容：AIN1/AIN2/BIN1/BIN2/PWMA/PWMB→AO1/AO2：1 0 1 0 1 1=正转；0 1 0 1 1 1=反转；1 1 1 1 1 1=刹车；0 0 0 0 1 1=自由停车；X X X X 0 0=刹车；注释“X:任意电平；VM/GND:电机电源输入，VM接正GND接负；VCC/GND:逻辑电平输入，VCC接从外部输入进来的5V，GND接负；PWMA/PWMB:可以直接接VCC，然后通过AIN1/AIN2 BIN1/BIN2来控制2个电机”。“4-3.程序核心代码如下：”。
- frame5、frame6：Keil µVision4，标题栏"advance - µVision4"，工程树“目标1→源代码组1→main.c、stc12c5a60s2.h”。代码：
  - frame5（run 函数，行105–135）：
    ```c
    void run(void)
    {
        //左电机前进
        Left_motor_go = 1;    //左电机前进使能
        Left_motor_back = 0;  //左电机后退禁止
        //更新指定管脚的PWM值，更改可实现控速（0-20）
        push_val_left=10;
        //右电机前进
        Right_motor_go=1;     //右电机前进使能
        Right_motor_back=0;   //右电机后退禁止
        //更新指定管脚的PWM值，更改可实现控速（0-20）
        push_val_right=10;
        return;
    }
    ```
    （下接 timer0 函数注释头）
  - frame6（main 函数，行153–182）：
    ```c
    void main()
    {
        P2=0XC0;    //关电机
        TMOD=0X01;  //定时器工作方式1
        TH0=0XFC;   //1ms定时，装入初值
        TL0=0X66;
        TR0=1;      //启动t0工作
        ET0=1;      //允许t0中断
        EA =1;      //开总中断   （此行高亮）
        delay(2000);//延时2s
        while(1)
        {
            run();   //前进
        }
        return;
    }
    ```
- 本视频帧中未出现 STC-ISP 烧录界面与串口助手（无法确认其烧录过程）。

**3. 小车/模块的行为**
- 全部帧为代码/文档画面，无法从帧序观察小车运动。依代码与文档，设计行为为：上电先关电机（P2=0xC0），延时2秒后双电机以 PWM 占空比 10/20 前进，循环不止。

**4. 人手操作动作**
- 无实拍手部画面；可见的只有鼠标滚动文档、代码窗口滚动。

**5. 对写实验指导书有用的细节**
- TB6612FNG 控制引脚与单片机的对应：AIN1=P2.2、AIN2=P2.1、PWMA=P2.0、BIN1=P2.3、BIN2=P2.4、PWMB=P2.5。
- 晶振 11.0592MHz，1ms 定时初值 TH0=0xFC、TL0=0x66；软件 PWM 档位注释为 0–20 级，示例值 10。
- 逻辑表（正转/反转/刹车/自由停车）完整可抄（见上）。

---

## 实验3 小车前后左右综合实验

**1. 画面场景**
- frame1–5 为屏幕画面；frame6 右下角小窗可见小车：深灰色底盘、黑色大轮（画面可见2轮）、车前部两块 LED 模块亮蓝光，中部主控板（深色PCB）上有红色指示灯，红/黑电源线、白色 USB 线插在板上，一只手正在把白色 USB 线插头按进板子。桌面上其他器材无法确认。

**2. 电脑软件界面细节**
- frame1：WPS"3.小车前后左右综合实验.docx"（标签栏有“1.七彩探照灯实验”“2.小车前进实验”“3.小车前后左右综合实验”三个文档标签），100%，页1/15。可见“图1-1 51单片机主控板”图注、黄色 TT 直流减速电机照片及“图1-2 4个直流减速电机”图注。文字：“2.实验目的：单片机上电后，小车先延时2s，再前进1s，后退1s，左转2s，右转2s，原地左转3s，原地右转3s，停止0.5s。处于这样的循环状态。”“3.实验原理：对于4路直流减速电机的控制我们采用的是TB6612FNG驱动芯片来驱动电机。”
- frame2（页5/15）：再次出现“图4-3 引脚控制逻辑表”（内容同实验2：1 0 1 0 1 1 正转 / 0 1 0 1 1 1 反转 / 1 1 1 1 1 1 刹车 / 0 0 0 0 1 1 自由停车 / X X X X 0 0 刹车，及 VM、VCC 注释）。“4-3.程序核心代码如下：1.基本变量以及引脚的定义：//定义电机引脚 sbit Left_motor_go=P2^1; //左电机前进AIN2 sbit Left_motor_back=P2^2…（截断）”
- frame3：Keil µVision4，标题栏"CarRun - µVision4"，工程树“目标1→源代码组1→main.c、stc1…”。代码（行109–135）：
  ```c
  /**
   * Function   run
   * @author    Danny
   * @date      2017.08.16
   * @brief     小车前进
   * @param[in] time: 延时时间
   */
  void run(unsigned int time)
  {
      //左电机前进
      Left_motor_go = 1;    //左电机前进使能
      Left_motor_back = 0;  //左电机后退禁止
      //更新指定管脚的PWM值，更改可实现控速（0-20）
      push_val_left=10;
      //右电机前进
      Right_motor_go=1;    //右电机前进使能
      Right_motor_back=0;  //右电机后退禁止
      //更新指定管脚的PWM值，更改可实现控速（0-20）
      push_val_right=10;
      //延时
      delay(time * 100);
      return;
  ```
  Build Output：“Build target '目标 1' compiling main.c... linking... Program Size: data=13.2 xdata=0 code=485 creating hex file from "CarRun"... "CarRun" - 0 Error(s), 0 Warning(s).”
- frame4（行214–240）：
  ```c
  214  push_val_right=0;
  216  //延时
  217  delay(time * 100);
  218  return;
  221  /**
  222  * Function   spin_left
  225  * @brief     小车原地左转  原地左转(左轮后退，右轮前进)  ←"左轮后退"处有红圈标注（视频讲解痕迹）
  231  void spin_left(unsigned int time)
  233      //左电机后退
  234      Left_motor_go = 0;    //左电机前进禁止
  235      Left_motor_back = 1;  //左电机后退使能
  237      push_val_left=10;
  239      //右电机前进
  240      Right_motor_go=1;    //右电机前进使能
  ```
- frame5（main 函数，行338–360）：
  ```c
  void main()
  {
      P2=0XC0;    //关电机
      TMOD=0X01;  //定时器工作方式1
      TH0=0XFC;   //1ms定时，装入初值
      TL0=0X66;
      TR0=1;      //启动t0工作
      ET0=1;      //允许t0中断
      EA =1;      //开总中断   （高亮）
      while(1)
      {
          delay(2000);    //延时2s
          run(10);        //前进1s（10 * 100ms）
          back(10);       //后退1s
          left(20);       //左转2s
          right(20);      //右转2s
          spin_left(30);  //原地左转3s
          spin_right(30); //原地右转3s
          brake(5);       //停止0.5s   （截图字形似"brak*"/"brake"，按上下文应为brake）
      }
      return;
  }
  ```
- frame6：STC-ISP V6.85（同样配置：STC12C5A60S2、USB-SERIAL CH340 (COM3)、2400~115200），hex 区“代码长度 01E5H 校验和 DD3CH”，信息区“正在检测目标…成功 [D:562*]（小字无法完全确认）”“当前波特率： 115200”“正在擦除目标区域...”“单片机型号： STC12C5A60S2 固件版本号： 7.1.41”；“停止”按钮处于按下高亮状态。底部 Keil Build Output 同上（code=485, "CarRun" 0 Error(s), 0 Warning(s)）。

**3. 小车/模块的行为**
- frame6 小窗：车上两块 RGB 模块亮蓝光、板上红色指示灯亮，小车处于静态（正在接线/刚烧录阶段）。运动时序无法从抽帧直接观察；设计行为依代码为：上电→延时2s→前进1s→后退1s→左转2s→右转2s→原地左转3s→原地右转3s→停止0.5s，循环。

**4. 人手操作动作**
- frame6：一只手正将白色 USB 线插入主控板（烧录接线动作）。其余帧无手部动作。

**5. 对写实验指导书有用的细节**
- 电机为黄色 TT 直流减速电机（图1-2），4路由 TB6612FNG 驱动。
- 每个动作函数带 time 参数，内部 delay(time*100)，即单位约 100ms；前进/后退 PWM 值 10（0–20 可调）。
- 原地左转=左轮后退+右轮前进（代码注释明确，视频还用红圈强调）。
- 编译结果 data=13.2, code=485，可作为工程正确性参照。

---

## 实验4 舵机旋转控制七彩探照灯

**1. 画面场景**
- 6 帧均为屏幕画面（WPS docx + Keil），右下角无实物小窗，小车外观与桌面器材在本视频抽帧中不可见（无法确认）。

**2. 电脑软件界面细节**
- frame1：WPS"4.舵机旋转控制七彩探照灯.docx"（4个文档标签），120%，页2/9。文字：“2、实验目的：先延时0.5s，接着舵机开始旋转不同的角度控制七彩灯。”“3、实验原理：舵机工作原理：控制信号由接收机的通道进入信号调制芯片，获得直流的偏置电压。它内部有一个基准电路，产生周期为20ms，宽度为1.5ms的基准信号……当电机转速一定时，通过级联减速此轮带动电位器旋转，使得电压差为0，电机停止转动。”“舵机的控制：一般需要一个20ms左右的时基脉冲，该脉冲的高电平部分一般为0.5ms-2.5ms范围内的角度控制脉冲部分。本次实验的采用的舵机是180度间服（按截图字形，应为“伺服”），控制关系如下：0.5ms——0度 / 1.0ms——45度 / 1.5ms——90度 / 2.0ms——135度 / 2.5ms——180度”。
- frame2（页3/9）：两张原理图——“图4-2 RGB三色灯”（P4 端子：LED_B2、LED_G3、LED_R4，XH2.54-4P）和“图4-3 舵机”（J1 端子：1=IO、2=VCC、3=GND，D1 二极管）。红色文字：“注：舵机SG90需连接到舵机接口J1上方可进行实验。”“4-1.看懂原理图 由4-1, 4-2, 4-3电路原理图可以知道相应的连接电路，LED_R连接到主控板上的数字EA口，LED_G和LED_B分别接在主控板上的ALE和PSEN，J1连接到主…”（截断）。
- frame3–6：Keil µVision4，标题栏"ServoControlCorlor - µVision4"（原工程名拼写即如此，含拼写错误 Corlor），工程树“目标1→源代码组1→main.c、stc12c5a6…”。Build Output："Build target '目标 1' compiling main.c... linking... Program Size: data=9.0 xdata=9 code=803 creating hex file from "ServoControlCorlor"... "ServoControlCorlor" - 0 Error(s), 0 Warning(s)."
  - frame3（行58–84，servo_control_color 函数）：
    ```c
    void servo_control_color()
    {
        //定义舵机转动位置
        int pos = 0;
        int i = 0;
        for (pos = 1; pos < 180;  pos=pos+5)
        {
            //舵机0度转到180,每次延时5ms
            for(i=0;i<15;i++)
            {
                myangle=pos;
                delay(5);        （此行高亮）
            }
            //旋转到相应的角度,判断调用相关函数
            color_light(pos);
        }
        for (pos = 180; pos > 0;  pos=pos-5)
        {
            //舵机180旋转到0,每次延时5ms
            for(i=0;i<15;i++)
            {
                myangle=pos;
                delay(5);
            }
    ```
  - frame4（main 前半，行198–225）：
    ```c
    /**
    * @brief   先延时0.5. 接着调用舵机控制七彩灯程序
    */
    void main()
    {
        unsigned char i =0;
        TMOD=0X10;  //定时器工作方式1  （此行高亮）
        TH1=0XFF;   //100us定时，装入初值
        TL1=0XA4;
        TR1=1;      //启动t1工作
        ET1=1;      //允许t1中断
        EA =1;      //开总中断
        //设置P4口作为普通的IO口使用
        P4SW |= (1<<4);
        P4SW |= (1<<5);
        P4SW |= (1<<6);
        //舵机引脚初始为高电平
        ServoPin=1;
        //初始化舵机位置向前
        for(i = 0; i<15;i++)
    ```
  - frame5、frame6（timer1 中断，行172–198，两帧仅高亮行不同）：
    ```c
    /**
    * @brief  TIMER1中断服务子函数产生PWM信号，控制舵机
    */
    void timer1() interrupt 3
    {
        int PulseWidth;
        TH1=0XFF;        //100us定时，装入初值
        TL1=0XA4;
        count++;
                 //定义脉宽变量
        PulseWidth = ((myangle*11)+500)/100; //为了将0-180度转换为相应的脉宽值 （frame5高亮此行）
        if(count == PulseWidth)
        {
            ServoPin=0;    //将舵机接口电平置低
        }
        if(count == 190)   //190为最终调试获得的一个最佳值
        {
            count = 0;
            ServoPin=1;    //将舵机接口电平置高 （frame6高亮此行）
        }
    }
    ```
- 本视频帧中未出现 STC-ISP 界面（无法确认烧录画面）。

**3. 小车/模块的行为**
- 抽帧中无实物画面，行为无法直接观察。依代码设计：上电延时0.5s后，舵机角度从0°→180°步进5°再180°→0°往返扫描，每个角度调用 color_light(pos) 使七彩灯随角度变色。

**4. 人手操作动作**
- 无手部画面；仅鼠标滚动/选中代码行。

**5. 对写实验指导书有用的细节**
- 舵机型号 SG90（180°），必须接主控板舵机接口 J1（1=IO信号、2=VCC、3=GND，板上带 D1 二极管）。
- PWM 用定时器1方式1产生，100us 中断节拍，初值 TH1=0xFF、TL1=0xA4；脉宽=(角度×11+500)/100，周期计数 190（约19ms），均写入注释，可直接引用。
- RGB 灯接线与实验1相同（EA/ALE/PSEN 即 P4.6/P4.5/P4.4，XH2.54-4P 端子"P4"）。
- 编译结果 data=9.0, xdata=9, code=803。

---

## 实验5 按键控制小车启动实验

**1. 画面场景**
- frame1–5 为屏幕画面；frame6 右下角小窗可见小车俯视：深灰色底盘、黑色轮、车体前部两块模块亮蓝光，中部深色主控板上有一颗红色 LED 点亮，一只手在板边按压白色 USB 插头进行接线。桌面其他器材无法确认。

**2. 电脑软件界面细节**
- frame1：WPS"5.按键控制小车的启动.docx"（5个文档标签），100%，页1/13。文字：“2.实验目的：单片机上电后，按下启动键，小车先延时2s，再前进1s，后退1s，左转2s，右转2s，原地左转3s，原地右转3s，停止0.5s。”“3.实验原理：通常我们的按键开关一般都是机械弹性开关，当机械触点断开、闭合时，由于机械触点的弹性作用，一个按键开关在闭合时不会马上就能稳定的接通，在断开时也不会一下子彻底断开，而是在闭合和断开时会伴随着一连串的抖动。”下方为按键抖动波形示意图（标注“键按下”）。
- frame2（页2/13）：完整的“图3-1 按键抖动状态图”（波形标注：前沿抖动、键稳定、后沿抖动）。文字：“抖动时间一般都是由按键的机械特性决定的，一般都会在10ms以内，为了确保程序对按键的一次闭合只响应一次，必须进行按键的消抖处理，有硬件消抖和软件消抖。其中，软件消抖指的是检测出键闭合后执行一个延时程序，产生5ms～10ms的延时，让前沿抖动消失后再一次检测键的状态，如果仍保持闭合状态电平，则确认为真正有键按下。当检测到按键被释放后，也要给5ms～10ms的延时，待后沿抖动消失后才能转入该键的处理程序。硬件消抖是在开关两段（应为“两端”）接一个0.1uf的电容。本次实验我们采取的是软件延时去抖。”“另外关于PWM的原理以及定时器的理论知识请见实验二以及实验三。”
- frame3（页2/13 下部）：“下面我们来讲解按键控制小车启动实验的硬件和软件设计。”“4、实验步骤 4-1.看懂原理图”。
- frame4：Keil µVision4，标题栏"KeyScanStart - µVision4"，工程树“目标1→源代码组1→main.c、stc12c5a60…”。代码（行46–72，key_scan 函数）：
  ```c
  /**
  * Function   key_scan
  * @brief     按键检测（包含软件按键去抖）
  */
  void key_scan(void)
  {
    while (key!=0);      //当按键没有被按下一直循环
    while (scan(void))   （第61行，按截图抄录；疑似为 scan() 相关判定，小字无法完全确认）
    {
      while (key!=0);    //当按键没有被按下一直循环
      while (key==0)     //当按键被按下时
      {
        delay(10);       //延时10ms
        if (key==0)      //第二次判断按键是否被按下
        {
          delay(100);
          while (key==0); //判断按键是否被松开
        }
      }
  ```
- frame5（main 函数，行358–385）：
  ```c
  void main()
  {
      P2=0XC0;   //关电机
      TMOD=0X01; //定时器工作方式1
      TH0=0XFC;  //1ms定时，装入初值
      TL0=0X66;
      TR0=1;     //启动t0工作
      ET0=1;     //允许t0中断
      EA =1;     //开总中断
      key_scan();     //调用按键扫描函数
      while(1)
      {
          delay(2000);    //延时2s
          run(10);        //前进1s（10 * 100ms）
          back(10);       //后退1s
          left(20);       //左转2s
          right(20);      //右转2s
          spin_left(30);  //原地左转3s
          spin_right(30); //原地右转3s
          brake(5);       //停止0.5s
      }
  ```
- frame6：STC-ISP V6.85（同前配置：STC12C5A60S2、USB-SERIAL CH340 (COM3)、2400/115200），hex 区“代码长度 01F2H 校验和 D8F9H”；“下载/编程”按钮为蓝色按下状态；界面弹出提示框（悬停于“下次冷启动时P1.0/P1.1为0/0才可下载程序”复选框），文字约为：“下次是否需要P1.0和P1.1同时为低电平时才可下载程序 / 连接：P1.0和P1.1同时为低电平时才可下载 / 不接：下载时不会检测P1.0和P1.1的电平”（小字，个别字无法完全确认）；信息区“操作成功！”“单片机型号： STC12C5A60S2”“固件版本号： 7.1.41”，文件路径"E:\VC51\四驱车C51平台开发手册\ST_4WD_C51\5…\KeyScanStart.h…"。Keil Build Output：“linking... Program Size: data=13.2 xdata=0 code=490 creating hex file from "KeyScanStart"... "KeyScanStart" - 0 Error(s), 0 Warning(s).”

**3. 小车/模块的行为**
- frame6 小窗：RGB 模块亮蓝光、主控板红色 LED 亮，小车静止（接线/烧录阶段）。按键触发后的运动时序无法从抽帧观察；设计行为依代码：等待 key_scan() 检测到启动键按下后，进入循环执行 延时2s→前进1s→后退1s→左转2s→右转2s→原地左转3s→原地右转3s→停止0.5s。

**4. 人手操作动作**
- frame6：一只手把白色 USB 插头接到主控板并按压确认。软件侧为鼠标点击“下载/编程”。启动按键本身被按下的画面未出现在抽帧中（无法确认）。

**5. 对写实验指导书有用的细节**
- 软件消抖流程可直接引用：检测 key==0 → delay(10) 二次确认 → delay(100) → 等待松开 while(key==0)。
- main 中在 while(1) 动作循环之前调用 key_scan()，实现“按键启动”。
- STC-ISP 中与 P1.0/P1.1 下载条件相关的复选框与悬停说明可作为烧录注意事项写入。
- 编译结果 data=13.2, code=490（与实验3的485相差为按键扫描代码）。
- 车上可见红色电源指示灯、蓝色 RGB 模块，可作为接线正确时的外观判据。

---

## 实验6 红外避障实验

**1. 画面场景**
- frame1–5 为屏幕画面；frame6 右下角小窗可见小车俯视：深灰/黑色底盘、4个黑色橡胶轮，车前部两块模块亮蓝光，中部主控板上红色 LED 点亮，白色 USB 线插在板侧，一根手指在车尾/车侧扶住小车（似在固定或演示）。所用的两路红外避障模块在图中位于车前部（具体安装位置细节小窗分辨率下无法完全确认）。

**2. 电脑软件界面细节**
- frame1：WPS"6.红外避障实验.docx"（标签栏可见“2.小…进实验”“3.小车…综合实验”“4.舵…探照灯”“5.按…的启动”“6.红…避障实验”共5+个文档标签），120%，页1/11。插图“图1-2 2路红外避障模块”：照片中红色框圈出车上的按键模块（蓝色按钮的小板）与一个舵机，并有黄色标注条（小字无法辨认）。文字：“2、实验目的：单片机上电之后，启动红外避障功能，当左边传感器检测到障碍物时小车向右转，当右边传感器检测到时小车向左转。”“3、实验原理：红外传感器具有一对红外发射与接收管，发射管发射出一定频率的红外线，”
- frame2（页1/11 下部）：“当检测方向遇到障碍物时，红外线红外线反射回来被接收管接收。它常用于安装在小车上，判断前方是否有障碍物。可通过电位器设置阈值。正前方有障碍时绿灯亮起，OUT引脚为低电平，反之为高电平。”“红外传感器避障的基本原理是利用物体的反射性质，在一定范围内，如果没有障碍物，发射出去的红外线，因为传播的距离越来越远而逐渐减弱，最后消失。如果有障碍物红外线遇到障碍物，被反射到达传感器接收头。我们本次实验采用的是两路红外传感器分别连接在51单片机主控板上的P1.6, P1.4引脚上。我们通过检测两端口的电平来判断障碍物的情况，并做出相应的避障动作。”“另外关于PWM的原理以及定时器的理论知识请见实验二以及实验三。”
- frame3（页3/11）：“4-2 理解原理图 由电路原理图可知左边的红外传感器接在主控板上的P1.6（IN7）口上，右边的则接在P1.4(IN5)口上。模块状态指示灯示意图：”配有红外模块实物标注图：S2=可测光源AD值（电位器）、L1=避障灯、L2=寻光灯、L3=电源灯、接线端子4根=GND地/LT寻光输出/HW避障输出/VCC电源。“注：1. 进行实验时，Arduino功能跳线不需要插跳线帽，这是51单片机上面。（”不需要“为黄色高亮） 2. 本次实验中我们可以调整红外避障模块上的电位器来设置红外避障的距离，以达到比较好的实验效果。调节方法：调节该模块上的电位器【SW1】，使得红外发射管【LEAS1】红外接收管【RC1】距离障碍物小于10cm时，LED灯【L1】亮起；否则，LED…”（截断；LEAS1/RC1 按截图抄录，可能是 LEDS1/RC1，无法完全确认）。
- frame4–6：Keil µVision4，标题栏"infrared_avoid - µVision4"，工程树“目标1→源代码组1→main.c、stc…”。Build Output："Program Size: data=15.2 xdata=0 code=468 creating hex file from "infrared_avoid"... "infrared_avoid" - 0 Error(s), 0 Warning(s)."（frame5 中还出现“Build target '目标 1' compiling main.c... linking...”，底部状态栏显示“Rebuild all target files”，鼠标正点击 Rebuild 图标并带红圈讲解标注。）
  - 代码（行258–293，main 内避障逻辑）：
    ```c
    TMOD=0X01;  //定时器工作方式1
    TH0=0XFC;   //1ms定时，装入初值
    TL0=0X66;
    TR0=1;      //启动t0工作
    ET0=1;      //允许t0中断
    EA =1;      //开总中断
    //调用按键扫描函数
    key_scan();
    while(1)
    {
        //遇到障碍物,红外避障模块的指示灯亮,端口电平为0
        //未遇到障碍物,红外避障模块的指示灯灭,端口电平为1
        LeftSensorValue  = AvoidSensorLeft;
        RightSensorValue = AvoidSensorRight;
        if (LeftSensorValue == 1 && RightSensorValue == 1)
        {
            run();         //当两侧均未检测到障碍物时调用前进函数
        }
        else if (LeftSensorValue == 1 && RightSensorValue == 0)
        {
            spin_left(2);  //右边探测到有障碍物，有信号返回，原地向左转 （frame5此行高亮）
        }
        else if (RightSensorValue == 1 && LeftSensorValue == 0)
        {
            spin_right(2); //左边探测到有障碍物，有信号返回，原地向右转
        }
        else
        {
            spin_right(2); //当两侧均检测到障碍物时调用固定方向的避障（原地右转）
        }
    }
    return;
    ```

**3. 小车/模块的行为**
- frame6 小窗：小车 RGB 模块亮蓝光、主控板红色 LED 亮，小车由手扶住，未观察到明显运动。避障动作时序无法从抽帧直接观察；设计行为依代码：两侧无障碍→前进；右传感器检测到障碍→原地左转；左传感器检测到障碍→原地右转；两侧均检测到→原地右转（固定方向）。注意代码注释中端口电平为0代表“遇障碍（指示灯亮）”，为1代表“未遇到”。

**4. 人手操作动作**
- frame6：手指扶车/拨动小车（演示或固定）。frame5 可见鼠标点击 Keil 的 Rebuild all target files 按钮。调节电位器 SW1 的实拍动作未出现在抽帧中（文档中仅有文字说明，无法确认）。

**5. 对写实验指导书有用的细节**
- 左红外传感器接 P1.6（对应主控板 IN7 口），右红外传感器接 P1.4（对应 IN5 口）。
- 模块板载元件标注：电位器 S2（可测光源AD值）、避障灯 L1、寻光灯 L2、电源灯 L3；4线排针 GND/LT(寻光输出)/HW(避障输出)/VCC；该模块为“避障+寻光”复用设计。
- 距离整定方法：调电位器 SW1，使障碍物距离小于 10cm 时 L1 亮起。
- 注意事项：51 平台下“Arduino 功能跳线”不需要插跳线帽。
- 上电流程仍含 key_scan() 按键启动；编译结果 data=15.2, code=468。

---

**跨实验共性信息（对写指导书有用）**
- 软件链固定为：WPS 文字看 docx 指导书 → Keil µVision4 编译（工程名依次为 ColorLED / advance / CarRun / ServoControlCorlor / KeyScanStart / infrared_avoid，目标名“目标 1”，源文件 main.c + stc12c5a60s2.h）→ STC-ISP V6.85 烧录（芯片 STC12C5A60S2、CH340 串口 COM3、波特率 2400–115200、固件 7.1.41）。
- 各工程编译均 0 Error / 0 Warning，Program Size 分别为 code=158 / 485（advance 未捕获）/ 485 / 803 / 490 / 468，可作对照。
- 小车为 Yahboom 风格 51 四驱车：深灰多层底盘、4 个 TT 减速电机+黑色车轮、TB6612FNG 驱动、前部两块 RGB 七彩灯模块、STC12C5A60S2 主控板，烧录用白色 USB 线。
- 所有实验代码注释均为中文，作者 Danny，日期 2017.08.16，版权行"2010-2019, Shenzhen Yahboom Tech"。
- 未能覆盖的部分：实验2、实验4 的抽帧中无实物小窗；各实验的小车实际运动/灯光变化时序大多未出现在抽帧时刻——如需行为时序截图，建议在上述时间点附近补帧（尤其实验1 的 515s 前后、实验5 的 307s 之后、实验6 的 424s 之后）。
