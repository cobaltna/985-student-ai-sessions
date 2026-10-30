## 👤 用户（2026-09-15 13:18）

我要做实验2，3，4.请把我当作什么都不知道的小白，极其详细且具体的无遗漏的介绍实验全流程和原理解析以及实验结果

> 📎 附件: 虚拟仪器设计实验指导书.pdf

<details><summary>💭 思考链（deepseek-flash）</summary>

The user wants me to explain experiments 2, 3, 4 from a PDF lab manual, treating them as a complete beginner. I need to read the PDF first.

Let me read the PDF file.

The file is at C:\Users\UserX\Downloads\虚拟仪器设计实验指导书.pdf

Let me use the Read tool - it may not handle PDF. Let me try. Actually the pdf skill exists. Let me first try reading.

Let me check what tools work. Read tool supports images, not PDFs likely. Let me try Bash with python to extract text.

Actually, per the memory, there's python via conda. Let me check.

Let me start by trying to read the PDF.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\虚拟仪器设计实验指导书.pdf"}` → ``

### 🤖 助手（deepseek-flash，2026-09-15 13:18）

我先读取这份实验指导书，看看实验 2、3、4 的具体内容。

<details><summary>💭 思考链（deepseek-flash）</summary>

The Read tool can't handle PDF well. Let me use python to extract text.

Let me find python. Per memory, conda python at some path. Let me check.

</details>

- 🔧 **Bash** `{"command": "ls C:/Users/UserX/.zcode/memory/ 2>/dev/null; echo \"---\"; where python 2>/dev/null; echo \"---\"; ls \"C:/Users/UserX/miniconda3/python.exe\" \"C:/Users/UserX/anaconda3/python.exe\" 2>/dev/null", "description": "Locate python interpreter and memory files"}` → `Exit code 2 README.md output-preferences.md ppt-master-project.md python-envs.md teaching-workspace.md verification-notes.md --- ---`

### 🤖 助手（deepseek-flash，2026-09-15 13:18）

PDF 较大，我用 Python 提取文本。

<details><summary>💭 思考链（deepseek-flash）</summary>

Let me read the python-envs.md to find the python path.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\memory\\python-envs.md"}` → `1 # 本机 Python 环境完整清单（实测 2026-09-12） 2 3 > 由 `~/.zcode/AGENTS.md` 索引。所有结论均由「直接调用该解释器并 import」实测得出，非推测。 4 > conda / python **均不在 bash PATH**，必须用全路径调用。 5 6 ## 0. 目录真相 7 8 `C:\Users\UserX` 是**符号链接** → `C:\Users\UserX`（同一目录）。两种写法等价 9 （实测 `四.conda\envs\opencv\python.exe` 两侧同为 104264 字节 / Oct 22 2025）。 10 11 ## 1. docx / Offi …[截断,原长3283]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Let me use the conda opencv python to extract PDF text with fitz (pymupdf).

</details>

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/.zcode/workspace/default && \"/c/Users/UserX/.conda/envs/opencv/python.exe\" -c \"\nimport fitz, json\nd = fitz.open(r'C:\\Users\\UserX\\Downloads\\虚拟仪器设计实验指导书.pdf')\nprint('pages:', d.page_count)\ntoc = d.get_toc()\nprint('toc:', json.dumps(toc, ensure_ascii=False))\n\" 2>&1 | head -60", "description": "Inspect PDF page count and table of content …[截断,原长383]` → `warning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead. pages: 22 toc: [[1, "fengmian", 1], [1, "虚拟仪器设计实验指导书", 2], [2, "1.虚拟仪器实验 初识myDAQ", 2], [2, "2.虚拟仪器实验 音频均衡器设计", 9], [2, "3.虚拟仪器实验 myQUAKE", 13], [2, "4.虚拟仪器实验 myVTOL", 17], [2, "5.虚拟仪器实验 myTEMP", 21]]`

<details><summary>💭 思考链（deepseek-flash）</summary>

22 pages. Experiment 2 starts at page 9, experiment 3 at page 13, experiment 4 at page 17, experiment 5 at page 21.

Let me extract full text of pages 9-21 (0-indexed 8-20).

Let me dump the whole text to a file to read.

</details>

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/.zcode/workspace/default && \"/c/Users/UserX/.conda/envs/opencv/python.exe\" -c \"\nimport pymupdf, io, sys\nd = pymupdf.open(r'C:\\Users\\UserX\\Downloads\\虚拟仪器设计实验指导书.pdf')\nout=[]\nfor i in range(0, d.page_count):\n p=d[i]\n out.append('===== PAGE %d ====='%(i+1))\n out.append(p.get_text())\n out.append('----- images on page: %d -----'%len(p.ge …[截断,原长400]` → `ok`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\lab_text.txt"}` → `1 ===== PAGE 1 ===== 2 3 4 5 虚拟仪器设计 6 7 实验指导书 8 9 10 11 12 某985高校工学院 13 2018 年5 月 14 15 ----- images on page: 0 ----- 16 ===== PAGE 2 ===== 17 虚拟仪器设计 试验一 18 初识myDAQ：基本操作与信号采集分析 19 一、 实验目的 20 在实验过程中，学生将会学习到关于数据采集与信号处理的知识。实验中将 21 运用来自NI 公司的仪器myDAQ，学生可以通过myDAQ 进行多种方式的数据收 22 集、测量、信号分析、控制和电路分析等。该实验被分为5 个部分： 23 ① 利用myDAQ 作为数 …[截断,原长13686]`

<details><summary>💭 思考链（deepseek-flash）</summary>

I now have the full text. Let me also look at the images in the PDF that are relevant to experiments 2, 3, 4 — the figures (前面板/程序框图 screenshots). The user wants "极其详细且具体的无遗漏的介绍实验全流程和原理解析以及实验结果".

The figures are screenshots of front panels and block diagrams. It would help to extract images from pages 9-20 and view them, so I can describe the front panel and block diagram in detail.

Let me extract images from pages 9-21.

Actually, let me render the relevant pages as images and view them, which might be better - it gives the full page layout including figures.

Let me render pages 9-20 at reasonable resolution and read them.

Page 9-12 (exp 2), 13-16 (exp 3), 17-20 (exp 4).

Let me render them. But rendering 12 pages as images consumes a lot of context. Let me be selective: render the pages with figures — the ones with images: page 9(1), 10(4), 11(2), 12(0 total 0?), let me check.

From the extraction:
- PAGE 9: images 1
- PAGE 10: images 4
- PAGE 11: images 2
- PAGE 12: images 0
- PAGE 13: 0
- PAGE 14: 1
- PAGE 15: 2
- PAGE 16: 2
- PAGE 17: 0
- PAGE 18: 1
- PAGE 19: 2
- PAGE 20: 1

So figures are on pages 10, 11 (exp2), 14, 15, 16 (exp3), 18, 19, 20 (exp4).

Let me render these pages to PNG and view them. That's 8 pages. That's a lot of images but valuable for detail. Let me do it in batches.

Actually, let me render at moderate zoom to keep size manageable.

Let me do it.

</details>

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/.zcode/workspace/default && \"/c/Users/UserX/.conda/envs/opencv/python.exe\" -c \"\nimport pymupdf\nd = pymupdf.open(r'C:\\Users\\UserX\\Downloads\\虚拟仪器设计实验指导书.pdf')\nfor pno in [10,11,14,15,16,18,19,20]:\n p = d[pno-1]\n pix = p.get_pixmap(matrix=pymupdf.Matrix(2.0,2.0))\n pix.save(r'C:\\Users\\UserX\\.zcode\\workspace\\default\\p%02d.png'%pno)\n …[截断,原长400]` → `10 1191 1684 11 1191 1684 14 1191 1684 15 1191 1684 16 1191 1684 18 1191 1684 19 1191 1684 20 1191 1684`

### 🤖 助手（deepseek-flash，2026-09-15 13:18）

我已提取全文。现在把实验 2/3/4 中的插图（前面板、程序框图截图）渲染出来看，确保讲解与实际截图一致。

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p10.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

That page has no block diagram figures of substance — just icon images. Let me check p11 which has the 前面板 图1 and 程序框图 图2.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p11.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Excellent. Now I have the block diagram for Experiment 2. Very useful.

Now let's look at pages 14, 15, 16 for Experiment 3, and 18, 19, 20 for Experiment 4.

Let me read p14 and p15.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p14.png"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p15.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Now p16 → 电机控制程序框图 (function generator).

Let me read p16, p18, p19, p20.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p16.png"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p18.png"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p19.png"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\p20.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

I now have everything I need. I have read the full text of experiments 2, 3, 4 and their figures.

Now the user wants: "我要做实验2，3，4.请把我当作什么都不知道的小白，极其详细且具体的无遗漏的介绍实验全流程和原理解析以及实验结果"

So they want a very detailed, beginner-friendly, complete walkthrough of experiments 2, 3, 4 — full procedure, principle analysis, and expected results.

This is a writing/explanation task. Should I use EnterPlanMode? No — it's not a coding task, it's an explanation task. The plan mode tool says it's for implementation tasks requiring code. This is pure explanation/research output. So I should just write it.

The output should be in Chinese (the user writes in Chinese). It should be extremely detailed and beginner-oriented.

Let me think about what to cover for each experiment:

**实验二：音频均衡器 (Audio Equalizer)**
- 实验目的
- 实验材料
- 原理：音频频谱、人耳听觉范围 20Hz-20kHz、低音/中音/高音划分、带通滤波器原理、加权求和、音量控制、功率谱密度
- 全流程：硬件连接（AUDIO IN 接手机/播放器，AUDIO OUT 接耳机/音箱，USB 接电脑）、软件配置（DAQ 助手设置）、编写程序 10 步
- 程序框图数据流解析
- 实验结果：拉杆改变音效；波形图显示功率谱
- 注意事项、常见问题

**实验三：myQuake 加速度计**
- 实验目的
- 材料：myDAQ、myQuake miniSystem、加速度传感器
- 信号连接表：电机→AO0，Accel A→AI0，Accel B→AI1
- 平台搭建 6 步
- 原理：偏心电机产生振动、加速度传感器 MEMS 原理、8位设置字（P0-P7）控制轴选和量程、数字输出 port0、低通滤波 10Hz、峰值检测
- 程序：两个循环（采集循环 + 电机控制循环）
- 结果：16-18% 时电机产生 P 波，结构开始摇晃；Y轴单位问题（g 或 m/s²）
- 注意：其实myDAQ的AI采集的是电压，波形图Y轴显示的是 V (加速度计输出电压)；题目问"Y轴显示的值单位应该是什么"

Let me think about this: the front panel chart is labeled "Accelerometer Response" with range -0.25 to 0.25. That looks like volts? Actually myDAQ AI range ±2V... -0.25 to 0.25 seems like g units maybe. Hmm.

Actually the question in the manual "思考在Y轴显示的值单位应该是什么？" — the answer: the accelerometer outputs a voltage proportional to acceleration; the front panel shows voltage (V) unless converted. The chart auto-scales. The true unit should be g (重力加速度) or m/s², but the raw display is V. So the answer is: 显示的是电压值(V)，需要通过灵敏度换算成 g 或 m/s²。

Let me be careful and give both: the displayed value is in volts (raw sensor output), but physically it represents acceleration; unit should be g or m/s² after conversion via sensitivity (e.g., 300mV/g).

Actually looking at the front panel: chart range -0.25 to 0.25, "Accelerometer Response". And "Peak Reading A (V)" — explicitly labeled (V)! So yes, the reading is in volts. Good — that's strong evidence.

So answer: Y轴当前显示的是电压 V，物理意义是加速度，正确单位应为 g（或 m/s²）。

The DAQ assistant AI range: myDAQ AI0/AI1 default ±10V or ±2V? In experiment 2 they set ±2. For exp 3, the note doesn't say range. The chart auto-scales.

**实验四：myVTOL 垂直起降控制**
- 目的：位置监测、PID控制风扇转速改变升力、平衡
- 材料
- 信号连接：霍尔传感器→AI0，可变直流风扇→AO0
- 平台搭建 5 步
- 原理：霍尔效应传感器测角度（非接触式角位置传感）、风扇推力、力矩平衡、PID 控制原理（P/I/D 各自作用）、开环 vs 闭环、条件结构切换模式
- 程序：前面板（Control Mode, Sensor Reading, Fan Control Output 表盘, PID Set Point(Target Sensor Reading), PID Gain Settings(P/I/D), Manual Fan Power Control, Stop, waveform chart with Actual Reading & Set Point, AutoScale）
- 程序框图：DAQmx 创建虚拟通道、myDAQ 写入、DAQmx 读取、DAQmx 清除任务、条件结构
- 步骤 4-8：运行、校准（手动预置臂水平，记录读数 ~2.04V 或 2.1V）、设目标、手动模式测试、PID 模式整定
- 结果：两条曲线重合 = 水平；PID 参数整定效果
- PID 整定方法：先 P，再加 I，最后 D

Note the front panel shows Sensor Reading 2.04 V, Target Sensor Reading 2.1 V, P=1.000, I=0.03, D=0.050, Fan Control Output gauge 0-10, Manual Fan Power Control 0-10.

Let me also cover LabVIEW basics for a complete beginner: 前面板 vs 程序框图, 控件 vs 显示控件, while 循环, Express VI, DAQ 助手.

Given "极其详细且具体的无遗漏", I should write a long, structured document. Should I write it to a file too? The user says "介绍" — they want me to explain. Probably output in chat is fine, but it's going to be very long. Given it's a terminal rendering markdown, a long answer is acceptable.

Hmm, but this is really long content. Maybe I should write it to a markdown file AND give a summary in chat? The user asked to "极其详细且具体的无遗漏的介绍" — they want the content. I think producing it directly in chat is the most direct satisfaction. But such a long doc might be better as a file they can keep.

Let me consider: they're doing a lab and need to write a lab report. A markdown file in the workspace would be handy. But they may just want to read it.

I'll output the full thing in chat (that's what "介绍" means), and it's the most useful. Given the length, I'll be thorough but organized.

Actually, let me reconsider — the answer will be extremely long. I think that's what's asked. Let me write it well.

Let me also double check some technical details:

实验二 filter settings:
- Bass: 带通, 低截止 20Hz, 高截止 140Hz
- Midtone: 带通, 低截止 400Hz, 高截止 2600Hz
- Treble: 带通, 低截止 5200Hz, 高截止 10000Hz

Step6: 三个积相加，和再乘 Volume
Step8: 频谱测量接"之前的积" — which 积? Probably the final output (after volume). The manual says "将"频谱测量"的"信号"与之前的积连上". Ambiguous. In the block diagram, Spectral Measurements "Signals" connects from... looking at the diagram, the Spectral Measurements is fed from the DAQ Assistant2's data path? Actually looking at the image, the "Spectral Measurements" box has "Signals" input connected via a green wire that goes... The green line comes from the far right of the summation chain. Actually in the image, the green line at the far right connects to Spectral Measurements. Signals → Power Spectrum → Waveform Graph.

Hmm, looking more carefully: there's a green wire that runs from the left (DAQ assistant1 data) across the top and down to the right side. The multipliers are orange. Green = dynamic data type. The Spectral Measurements signal input seems to receive the summed/weighted signal (the final output), which then also goes to DAQ Assistant2 data.

I'll describe it as: 频谱测量的信号输入接在最终加权后的输出信号上（与送给 DAQ 助手2 的是同一路信号），所以波形图显示的是实际输出音频的功率谱。

Also note: Step5 says 3 vertical progress bars connect to the products — display the weighted component magnitudes.

Step4: Volume, Bass, Midtone, Treble — 垂直指针滑动杆 (vertical pointer slide), default range 0-1 (from screenshot the scale is 0 to 1).

That's important: 滑动杆范围是 0~1（图中刻度 0, 0.2, 0.4, 0.6, 0.8, 1）。

DAQ助手1 (采集): 模拟输入→电压, 通道 audioInputLeft + audioInputRight, 范围 -2~2V, 连续采样, 待读取采样 320
DAQ助手2 (输出): 生成信号→模拟输出→电压, 通道 audioOutputLeft + audioOutputRight, 范围 -2~2V, 连续采样, 待写入采样 320

320 samples at default 44100? Actually the myDAQ audio input sample rate default is 44100 Hz... Hmm, myDAQ audio channels sample rate is fixed at 44100 Hz (the audio codec). Actually myDAQ audio input supports 8k-96k? The DAQ Assistant default for audio is 44100 Hz. So 320 samples ≈ 7.26 ms buffer. That's a reasonable low-latency buffer.

Note the manual doesn't specify sample rate for exp 2. I'll mention it defaults to 44100 Hz and 320 samples ≈ 7ms.

Let me be careful not to overstate. I'll say: 采样率在 DAQ 助手中采用默认值（myDAQ 音频通道通常为 44100 Hz）；320 点对应约 7.3 ms 的数据块.

Also Nyquist: 44100 Hz → 可分析到 22050 Hz，覆盖人耳 20kHz 上限，所以高音滤波器 5200-10000Hz 完全在范围内。The waveform graph X axis goes 0-5000 in the screenshot. Hmm, that's just the visible range.

Actually the screenshot shows Frequency (Hz) 0 to 5000.

Now 实验三 details:

设置字表:
Accel_A: P0-P7
- X轴: 1 0 G / / / / 1
- Y轴: 0 1 G / / / / 1
- Z轴: 1 1 G / / / / 1

Accel_B:
- X轴: / / / / 1 0 G 1
- Y轴: / / / / 0 1 G 1
- Z轴: / / / / 1 1 G 1

G=0 → ±1.5g; G=1 → ±6g

/ 表示无关位 (don't care)

P7 = 1 是使能位

So 8 bits: [P0..P7], 从布尔数组转成数字，通过 DAQ 助手（数字输出 port0）写入硬件。

Note: The block diagram shows two "Axis" enum controls → each goes into a 2-bit selection (via a case/array?), combined with G into an appended array (8 elements), then 布尔数组转数字 (Boolean Array to Number), then into DAQ Assistant (数字输出, port0, 数据).

Actually looking at the block diagram image: Axis (enum) → two "index array"? It looks like there's a "Boolean To (0,1)" etc. There are small yellow boxes. Then "appended array" → 8-element array → "Boolean Array To Number" → DAQ Assistant data.

Hmm, P7 = 1 is the last element, the enable.

Also: The DAQ Assistant for digital output — "停止(T)" terminal.

信号采集部分: DAQ Assistant2 采集 ai0 与 ai1 (模拟输入) → Filter (低通 10Hz) → 拆分信号 (Split Signals?) → 峰值检测 (Peak Reading A(V), Peak Reading B(V)) + Waveform Chart.

Actually in the diagram: DAQ Assistant2 data → (green) → index array / split → Filter on one branch → then 3 "Waveform Chart"? Let me look again.

From p16 image: DAQ Assistant2 数据 → blue wire → a "索引数组" (index array) box → then splits into red dots → three branches: one to a filter box? Actually there's "Filter 信号 滤波后的信号" — with only "信号" input shown and green output.

Hmm the diagram at p16 top: DAQ Assistant2 → 数据 → [index array icon] → red branch → to a box with "信号" ... Actually there appear to be three boxes at right: two with sine-wave icons (Abs/Amplitude?) and one "Waveform Chart".

Let me re-render that region at higher zoom to read it properly. Actually, it's a minor detail. Let me zoom into p16 top figure to describe accurately.

Actually — being "无遗漏" matters. Let me zoom in on the block diagrams to describe them accurately. Let me render crops at high zoom.

Let me crop p15 and p16 block diagram regions.

Actually, let me do this: render p15 top figure (图2) and p16 top figure (图4) and the 图3 电机控制 at 4x, cropping.

Let me compute crop boxes. Page is 1191x1684 at 2x. 图2 on p15 occupies roughly y from ~170 to ~560 (in the 2x image). Let me crop x 200-1100, y 150-580.

Hmm, I'd rather just re-render at higher zoom and read. Let me try cropping with pymupdf clip in PDF coordinates.

Page 15 (index 14): size? Let me just use pixmap clip in pixel space via PIL, simpler with the already-rendered PNGs.

Let me use PIL to crop and upscale.

Actually p15's 图2 is at roughly y=170..560, x=240..1070 in the 1191-wide image. Let me crop and save.

Let me do it for:
- p15 top region (图2 数据连续采样循环)
- p16 top region (图4 加速度信号连续采样)
- p16 bottom region (电机控制程序框图) — this one I already read well.

And p11 block diagram (图2) — I read it well enough.

Let me crop p15 and p16 tops.

</details>

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/.zcode/workspace/default && \"/c/Users/UserX/.conda/envs/opencv/python.exe\" -c \"\nfrom PIL import Image\nim = Image.open('p15.png')\nprint(im.size)\nim.crop((240,150,1080,600)).resize((1680,900), Image.LANCZOS).save('crop_p15_fig2.png')\nim2 = Image.open('p16.png')\nim2.crop((240,140,1080,560)).resize((1680,840), Image.LANCZOS).save('crop_p16_fi …[截断,原长412]` → `(1191, 1684) ok`

### 🤖 助手（deepseek-flash，2026-09-15 13:19）

我已经拿到全部文字和大部分插图。再放大看一下实验三的两张框图细节。

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\crop_p15_fig2.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Now I can see 图2 clearly:
- Axis (U16 enum) x2 → each goes to a "Boolean To (0,1)"? No — each Axis enum goes through: a blue "U16" → then a small box "数组"? Actually it's [index array] then [Boolean To (0,1)]? The yellow boxes with "真/假" are "Boolean To (0,1)" or "选择" (Select) functions. The blue "2" constant is likely "数组大小/替换数组元素" or the "build array" size.

Let me interpret: Axis enum (U16) → 索引数组(index array) → 选择(Select)? Actually the pattern "enum → 数组常量(2元素) → 索引数组" ...

Hmm. The typical pattern: Axis enum value 0/1/2 → index into a 2-element boolean array [[T,F],[F,T],[T,T]] representing the 2-bit code. Then "Boolean Array To Number"? 

Looking at the layout: Axis(U16) → [索引数组 icon] → yellow box (真/假 select) with blue "2" constant below. Then output goes into two "数组" (array) constant boxes shown as "F"/"T" ("F" and "T" green constants visible). Then into an "数组" building block (the tall box with 8 elements = "Build Array"), labeled "appended array", then → "布尔数组转数字" (the small box with dotted icon) → → DAQ Assistant data.

Actually more precisely per the text: "该部分程序最终将设定的8位设置字放入数组中，再将其从布尔型转换成数据型式传入myDAQ助手中"

So: 两个 Axis 枚举 → 各生成一组布尔位 → 合并成一个 8 元素布尔数组 (Build Array, 名为 "appended array") → 布尔数组转数字 (Boolean Array To Number) → DAQ Assistant (数字输出 port0) 的 "数据" 输入。

And there's a "F" green constant and a "T" green constant feeding the array (probably P2=G 和 P7=1 常量).

Then DAQ Assistant stop terminal, and stop button shared with the while loop.

Below: DAQ Assistant2 (模拟输入 ai0/ai1) → 数据 → Filter (信号→滤波后的信号) → [索引数组? no] → then split: a "index array / 拆分信号" icon (the box with grid) → then three branches:
- → 绝对值(Abs)? the "Y" box is "数组最大值与最小值" or "Amplitude and Level Measurements"? Actually the "Y" icon in a box = "复数至极坐标"? No.
  
Hmm the small box with "Y" shape = "Absolute Value"? Actually the icon showing a curve with an axis is "Amplitude and Level Measurements" Express VI? Or it's "按名称解除捆绑"?

Actually the "Y" looking icon that appears twice (for A and B) — this is likely "索引数组" or "拆分信号" then "Amplitude and Level"? The output goes to a box then to "Peak Reading A (V)" numeric indicator.

The classic pattern: filter output → 拆分信号 (Split Signals) → ch A, ch B → each goes through "绝对值和电平测量/Amplitude and Level Measurements" or "数组最大值" → Peak Reading.

Hmm. Actually the icon "⌐Y⌐" — that's the "Amplitude and Level Measurements" no... Let me think: In LabVIEW, the "Y" logo appears in... Hmm.

Actually I recall the icon that looks like a small box with a sine wave and "Y" is "Amplitude and Level Measurements" Express VI. But those are typically bigger.

Alternatively "缩放与映射"? 

Hmm, honestly, the exact identity of that small icon is uncertain. It could be "数组最大值与最小值" (Array Max & Min) which returns max and min, with the min discarded. The icon for Array Max & Min is a box with "max" and "min". 

Given the "Peak Reading" name, it's most likely 数组最大值 (Array Max & Min) taking the max, i.e., 峰值检测. That matches "Peak Reading".

I'll describe it functionally: 把滤波后的两路信号分开，各自取峰值（数组最大值/峰值检测），显示为 Peak Reading A (V) / Peak Reading B (V)，同时把两路波形送 Waveform Chart 显示。

I should be honest about the uncertainty of the exact icon. Actually, I shouldn't over-hedge. I'll describe the function: 拆分 + 取峰值. And note the reading unit is V.

Hmm, but "无遗漏" — accuracy matters more than pretending. I'll present it as "拆分成 A/B 两路 → 各自求峰值 → Peak Reading A(V)/Peak Reading B(V) 数值显示；两路波形同时送 Waveform Chart".

Also note: there's an "索引数组" (Index Array) before the split, and the DAQ assistant2 has "stop (F) 2" terminal and a red dot (error).

Also bottom-left: a small box "1" with an icon (提取单频信息?) - that's probably the "While 循环" iteration terminal or a "Amplitude and Level". Ignore.

Now let me look at p16 crop for 图4.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\crop_p16_fig4.png"}` → `[Attached image/jpeg: Read image]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Now I can see 图4 clearly: DAQ Assistant2 (数据) → blue wire → 索引数组/拆分信号 → Filter (信号 → 滤波后的信号) → then 拆分信号(Split Signals, icon with dotted pattern) → 3 branches:
- top → [小盒子 with "Y"] → [索引数组 icon] → Peak Reading A (V)  (DBL)
- middle → [拆分信号 icon] → Waveform Chart
- bottom → [小盒子 with "Y"] → [索引数组 icon] → Peak Reading B (V)

The "Y" box: looks like a box with a sine-curve and "Y" — this is "Amplitude and Level Measurements"? Or actually it might be "Absolute Value"? Hmm, the icon with a horizontal line and "Y" ... 

In LabVIEW, the "Y" symbol appears in the "Amplitude and Level Measurements" no. Let's think: the icon is a rectangle with a diagonal line rising and the letter "Y" to the right — that's the icon for **"Y" = 数组子集? No.

Actually! The icon with a curve going up and "Y" is the LabVIEW icon for "Amplitude and Level Measurements. Hmm.

Wait — I think it's actually the icon for **"Peak Detector"? No.

Let me reconsider. A rectangle containing a rising diagonal line plus "Y" — that's the LabVIEW **"Index Array"**? No, Index Array is a box with an arrow.

Hmm, the icon "⌐/Y" — the rising line and Y. In LabVIEW function palette, "Y" appears in the Waveform Conditioning? 

Actually I strongly suspect this is the **"Amplitude and Level Measurements"** no...

Alternatively it's **"信号拆分 → 提取 Y"**? Hmm.

Actually, in LabVIEW the icon that shows a curve with an axis and a "Y" label is **"Amplitude and Level Measurement"**? 

Hmm, let me think about "Scaling and Mapping"?

OK here's another thought: the box shows a rising edge and "Y" = it's a **"Get Waveform Components"** (获取波形分量) — which extracts Y (the amplitude array), t0, dt, or attributes from a waveform! YES! The "Get Waveform Components" icon in LabVIEW is a small box with a waveform and you select the component — it commonly displays "Y" when set to extract the Y array. That fits perfectly: 从波形中提取 Y（幅值数组）。

And then → [索引数组 icon] → Peak Reading (DBL). Hmm, Index Array on Y array would give a single sample, not a peak. 

Actually the second icon after "Y" looks like a 2x2 grid box = "数组最大值与最小值" (Array Max & Min)! The Array Max & Min icon is indeed a box with a small grid/max-min layout. Yes! Array Max & Min in LabVIEW looks like a rectangle with a small "max/min" indicator.

So: 波形 → 获取波形分量(Y) → 数组最大值与最小值 → 取 max → Peak Reading A (V).

That makes total sense: Peak Reading = 该次采样的峰值电压。

And the middle branch: 波形 → [拆分信号/索引] → Waveform Chart.

Good, I'm now fairly confident. But I should present this at the functional level with a light hedge on exact icon names, since I'm inferring. Actually, I'll describe it as: 用"获取波形分量"取出 Y（幅值数组），再用"数组最大值与最小值"取峰值，得到 Peak Reading A/B (V)。

Hmm, but I should be careful. Let me just describe functionally and note "（图中小图标即取波形 Y 分量 + 取数组最大值，即峰值）". That's honest and useful.

Actually, let me reconsider the first icon again — the blue-outlined box with an X-cross pattern at the far left after DAQ Assistant2. That's "索引数组" (Index Array) or "拆分信号". Hmm, blue outline = Express VI? The blue box with X pattern = "从动态数据转换" or "拆分信号" Express VI. 

Given the manual's own text and that this is a teaching doc, I'll describe at the level: DAQ 助手2 采集 → 拆分出两路波形 → 滤波 → 再拆分 → 峰值 + 波形图表.

OK. Now I have enough. Also note 图4 lacks the "stop(F) 2" ... no it has it.

One more: the "1" box with icon at bottom left = 波形图表 or "From DDT"? It's the same in both figures. Probably the "索引数组" constant 1. Not important.

Now let me also verify experiment 4's front panel details, which I read: 
- Chart y-axis "Sensor Input" 2.0 to 2.5, x-axis Time 0-329
- Legend: Actual Reading (blue), Set Point (yellow)
- AutoScale checkbox
- Control Mode button: "Manual"
- Sensor Reading: 2.04 V indicator
- Fan Control Output [V]: gauge 0-10
- PID Set Point: Target Sensor Reading = 2.1 (numeric)
- PID Gain Settings: Proportional 1.000, Integral 0.03, Derivative 0.050
- Manual Fan Power Control: vertical slider 0-10
- Stop button

Program diagram (图2): 
- myDAQ1/ai0 with "AI电压" property node → DAQmx 创建虚拟通道 → 读取 → 
- Condition structure (条件结构) with Control Mode selector (TF)
- Inside false(假) case: Target Sensor Reading, Fan Power Control → to PID? Actually 图3 手动控制 = 假 case (false): shows Fan Power Control input going out, and 0 constant on the derivative/integral side. So 假 = Manual.
  Wait 图3 shows 假 case with "Fan Power Control" going out to the right, and a "0" blue constant. So Manual → directly outputs fan power.
- 图4 shows 真 case (true): Derivative, Integral, Proportional inputs → PID VI (图标带 PID) → 输出
  Plus the setpoint comes from Target Sensor Reading and process variable from Sensor Reading (the line crossing).
- Then output → 索引/数值 → Fan Control Output [V] indicator and → DAQmx 写入 (myDAQ1/ao0, AO电压).
- Also DAQmx 清除任务 ×2 at the end.
- stop button → while loop.

Great.

Now — deliverables. The user wants a very detailed beginner-level walkthrough. I'll write it in Chinese, well structured.

Given the extreme length, I wonder if I should also save to a file. I'll produce it in chat as the primary deliverable. Actually, considering the user will likely use it for their lab report, saving a .md file in the workspace would be a nice touch. But the instruction says don't do extra unrequested work... Actually a companion file is genuinely useful here and low cost. Hmm — but they asked to "介绍", reading in chat is fine. I'll provide it in chat and offer to save as a file.

Actually, let me save it as a file too since it's long and they'll want to keep it. I'll do both: write the file and present the content. Hmm, presenting fully in chat + writing file = duplication of a lot of tokens. 

I think the best UX: write the full document into a markdown file AND present the full content in chat? That doubles output. Better: present in chat (that's what was asked). Then mention I can export to Word/Markdown if needed.

Hmm, but a 15k-word answer in a terminal is painful to read and they can't easily keep it. Let me ask? No — don't ask, just decide. 

The user said "请把我当作什么都不知道的小白，极其详细且具体的无遗漏的介绍实验全流程和原理解析以及实验结果". They want an explanation. I'll give the explanation in chat. That's the direct answer.

I'll write it thoroughly. Let me structure:

0. 通用基础：LabVIEW + myDAQ 是什么，怎么读框图（给小白打底）
1. 实验二
   - 一句话目标
   - 你需要准备/接线
   - 原理（音频、频段划分、带通滤波、加权求和、功率谱）
   - 逐步操作（10 步展开成小白版）
   - 框图数据流复盘
   - 实验结果：你应该看到什么
   - 常见问题/坑
2. 实验三
   - 目标、材料
   - 接线表
   - 平台搭建
   - 原理：偏心电机、压电/MEMS加速度计、8位设置字、量程g、低通10Hz抗混叠、峰值
   - 程序两部分
   - 操作步骤
   - 实验结果：16-18%起振，P波，Y轴单位问题
   - 坑
3. 实验四
   - 目标、材料、接线
   - 原理：霍尔传感器测角、风扇升力、力矩平衡、开环/闭环、PID三项各自作用、整定
   - 前面板各控件说明
   - 框图说明（DAQmx 函数 + 条件结构）
   - 操作步骤 4-8
   - 实验结果
   - PID 整定实操建议
4. 三个实验的对比总结 + 实验报告怎么写（对应指导书要求的报告要素）

Let me also add a "实验报告模板/要点" since the manual mentions 实验报告要求 for exp 1 and general habits.

Let me be careful about facts:
- myDAQ 规格: 2 路模拟输入 (AI0, AI1, ±10V, 16位, 200kS/s 复用), 2 路模拟输出 (AO0, AO1, ±10V, 16位, 200kS/s), 8 路 DIO, 音频输入/输出 (3.5mm, 立体声, 左/右声道), +5V/-15V/+15V 电源输出, 数字万用表 (DMM)。这是标准 myDAQ 规格。AI 范围可设为 ±10V/±2V/±1V 等（myDAQ 支持 ±10V, ±2V, ±1V, ±0.5V? 实际支持 ±10V 和 ±2V 等）。Let me state ±10V/±2V 常用。

Actually myDAQ AI ranges: ±10 V, ±2 V. Yes I believe myDAQ supports ±10V and ±2V. Good.

- AO ranges: ±10V, ±2V.
- 音频通道: line-level, ±2V range, 采样率 44.1kHz? Actually the myDAQ audio in/out are fixed at 44.1 kHz or 48 kHz. The DAQ Assistant for audio channels uses... I recall myDAQ audio sample rate is fixed at 44.1 kHz for input and 48 kHz? Hmm. Let me not over-specify. I'll say "音频通道采样率通常为 44.1 kHz（DAQ 助手中为默认值）" and hedge with "以 DAQ 助手默认显示为准". Actually safer: "采样率保持 DAQ 助手的默认值（myDAQ 音频通道约 44.1 kHz）". I'll mark it lightly.

Hmm — actually I should be careful. Let me soften: "音频通道的采样率由硬件固定（约 44.1 kHz 量级），指导书没有让你改，保持默认即可。" That's safe.

- myDAQ DIO: 8 lines port0, 3.3V logic (5V tolerant? myDAQ DIO is 3.3V LVTTL). Actually myDAQ DIO is 3.3 V. But the manual says LED with 220Ω and 5V. In exp1 they use the side "5V" port. For exp3, the digital output port0 sets the accelerometer board's config. Fine.

- 偏心电机: eccentric motor (unbalanced mass) — 占空比控制转速. The 函数发生器 (NI ELVISmx Function Generator) generates a square/pulse on AO0 → drives the motor. Actually the Function Generator Express VI outputs a waveform, and %Full Scale is the amplitude (duty cycle). Hmm, the manual says "产生脉冲并通过改变其占空比来调节电机的转速". Actually %Full Scale controls amplitude 0-100%, which changes motor speed. I'll explain: 通过改变输出脉冲的幅值/占空比来改变电机的平均驱动电压，从而改变转速.

Hmm, the "%Full Scale" terminal on the NI ELVISmx Function Generator controls the amplitude as a percentage of full scale. So changing it changes the peak-to-peak. For a motor driven by a square wave into a driver, higher amplitude = higher average voltage = faster. I'll explain it as: %Full Scale 相当于调制驱动电机的脉冲幅度（等效改变了电机的平均驱动电压/功率），所以值越大电机转得越快。The manual says duty cycle; I'll mention both and align with the manual's wording (占空比/幅值), noting the manual's description.

Actually to be faithful: the manual says "利用'函数发生器'vi 产生脉冲并通过改变其占空比来调节电机的转速". I'll present it as the manual does but note the actual control is the %Full Scale (幅值) 输入. Hmm — this could confuse. Let me phrase: 函数发生器产生脉冲信号送到 AO0；前面板上的 %Full Scale（0~100%）接到函数发生器的幅值输入，改变它等价于改变驱动电机的脉冲幅度/占空比，从而调节平均驱动电压与转速。

That's accurate and reconciles both.

- 加速度传感器: myQuake 用的是 MEMS 加速度计（类似 ADXL 系列，3轴，模拟输出，带自检和量程选择引脚）。灵敏度典型 ~300 mV/g。The 8-bit 设置字 controls: P0/P1 (A: axis select), P2 (range G), P7 (enable, =1); P4/P5 (B axis), P6 (B range), P7 enable.

Let me build the truth table clearly:
Accel A:
- X: P0=1, P1=0, P2=G, P3=/, P4=/, P5=/, P6=/, P7=1
- Y: P0=0, P1=1, ...
- Z: P0=1, P1=1, ...
Accel B:
- X: P4=1, P5=0, P6=G, P7=1, P0-P3=/
- Y: P4=0, P5=1, ...
- Z: P4=1, P5=1, ...

G: 0 → ±1.5g, 1 → ±6g

Note: this is the ADXL321-like? Actually ±1.5g/±6g is the ADXL... hmm, ADXL193 is ±120g. ±1.5g/±6g — that's the ADXL311? Actually the "KX" series. Whatever. Not needed.

Hmm, but the manual's table only shows G as a column with "/" for others. So P3 for A is don't care, P0-P3 for B are don't care.

Now P7=1 for both A and B (enable for both chips? or P7 = 总使能). Since both tables show P7=1, P7 is a common enable.

OK.

Now the "8位设置字放入数组→布尔转数字→DAQ助手" flow. In the diagram: two Axis enums each produce 2 bits; a "F"/"T" constant array provides P2(G)? and P7(1). Then Build Array (8 elements) → Boolean Array To Number → DAQ Assistant 数据.

Hmm, actually G seems to be fixed to F (0) → ±1.5g, since the front panel has no G control. The front panel only has Axis dropdowns for A and B, and Peak Reading. So G is hard-coded. In the diagram there's a green "F" and "F"/"T" boxes. Likely G=0 (F=false → ±1.5g) hard-coded, and P7=1 (T) hard-coded.

So the front panel Axis selection is the only user control for the accelerometers; G is fixed. I'll note: 前面板没有量程选择，程序里把 G 位固定为 0（±1.5g），P7 使能位固定为 1；如果你想改量程到 ±6g，需要把 G 位改成 1 再重新运行。

That's a good "why" for the 小白.

- 结果: 电机 16~18% 开始起振，结构摇晃，P波（初级/主波）。The manual mentions "电机可以开始产生P波并且建筑结构也相应地开始摇晃". "P波" here is the resonant/sinusoidal waveform — likely "P波" refers to the sinusoidal wave (可能是"正弦波"的误写 or "primary wave"). I'll describe: 波形图上出现明显的周期性振荡（指导书称"P波"，即结构受迫振动的主振动波形）。

Hmm, actually "P wave" in seismology = primary wave, compressional. In the myQuake context (Quake = earthquake), the eccentric motor simulates an earthquake, so "P波" = 地震纵波. Makes sense: myQuake simulates earthquakes; P wave is the first-arriving compressional wave. So 起振后结构开始摇晃，产生类似地震 P 波的振动信号。

Good, I'll explain that context.

- Y轴单位: 前面板图例 Peak Reading A (V) 明确标注 (V)，所以显示的是电压。物理量是加速度；正确单位应为 g（或 m/s²），需要用传感器灵敏度（mV/g）换算。The chart axis "-0.25~0.25" with AutoScale is 电压 V. So answer: 电压 V；若换算成加速度则应为 g 或 m/s²。

That's a solid, evidence-based answer.

Now for 实验二 results:
- 前面板：4 个滑动杆（Volume/Bass/Midtone/Treble，0~1），波形图显示 Voltage_0/Voltage_1 两路功率谱，X 轴 Frequency 0~5000 Hz（可自动缩放），Y 轴 Amplitude。
- 现象：拉 Bass 杆 → 低频段（20~140Hz）功率抬升，听感低音变强；拉 Treble → 高频段（5.2k~10kHz）抬升，听感变"亮"/"尖"；Midtone 抬中频，人声突出；Volume 整体增益。
- 归零某一路 → 该频段被完全去掉（如 Bass=0 → 只留中高频）。
- 三个都归零 → 输出近似静音。

Good.

Common pitfalls for exp2:
- 先开 LabVIEW 程序再点音源播放 → 顺序问题（指导书：先点播放再点运行，或者反过来都行，但要注意先运行 VI 再播放可避免缓冲区问题）。Manual says: 点击音频源上的播放按钮。点击 LabVIEW 环境中的运行按钮。
- 音响啸叫：麦克风/耳机串音 → 用耳机而不是音箱+麦克风。Actually with speaker output + phone input it's fine.
- 音量过大导致削波（输出超 ±2V 范围）→ 削波失真。建议 Volume 不要长时间拉满。
- 反馈啸叫：如果同时用 myDAQ 音频输入接麦克风、输出接音箱，会形成正反馈啸叫 → 本实验输入是播放器，不是麦克风，但如果你误用麦克风就会啸叫。
- 采样/缓冲不匹配：两个 DAQ 助手的"待读取/待写入采样"都是 320，若不一致会导致欠载/过载杂音。
- 通道选错 (audioInputLeft/Right 选成 ai0/ai1) → 采不到声音。

For exp3 pitfalls:
- 加速度传感器 X/Y/Z 轴方向要一致（两个传感器安装方向一致，才能做相关分析）。
- Accel A 装低位、Accel B 装高位。
- 灰接头接蓝接头。
- 12V 电源。
- 数字输出 port0 一定要配置成输出，否则设置字不生效 → 传感器可能输出无效。
- 低通 10Hz：因为结构振动频率只有几 Hz，10Hz 低通滤掉高频噪声与 50Hz 工频干扰。
- 起振前先把转速设 0。
- 结构要固定好（用燕尾夹夹住底座），否则只是整体滑动而不是振动。
- 波形图 Y 轴量程要合适。

For exp4 pitfalls:
- 平台必须水平放置。
- 9V 电源、极性。
- 先手动校准水平位置并记录传感器读数，再把它填进 Target Sensor Reading。
- 手动模式调 Fan Power 让两条曲线重合。
- PID 整定：P 太大振荡，I 消除静差但太大会积分饱和/超调，D 抑制超调但对噪声敏感。
- 建议整定顺序：先 P（I=D=0）加到临界振荡再回退一半；再缓慢加 I 消除静差；最后加一点 D 抑制超调。
- 注意占空比/风扇死区：低于某个电压风扇不转。
- 注意安全：风扇转速高时设备臂会摆动，注意不要让导线缠绕。

PID 原理讲解（小白版）：
- 误差 e = SP - PV
- 输出 = Kp*e + Ki*∫e dt + Kd*de/dt
- P：与误差成正比，误差越大修正越强；只有 P 会有稳态误差。
- I：对误差积分，消除稳态误差；太大会超调、振荡。
- D：对误差变化率响应，提前"刹车"，抑制超调；对噪声敏感。
- 在 myVTOL 里：SP = Target Sensor Reading（水平位置对应的传感器电压），PV = Sensor Reading（实际电压），输出 = Fan Control Output [V]（0~10V），驱动风扇产生升力 → 改变臂的倾角 → 改变霍尔传感器读数 → 闭环。

Also 从图4 PID case 看：PID VI 输入有 setpoint (Target Sensor Reading 通过蓝色线) 和 process variable (Sensor Reading 通过橙色线)，输出 → 索引 → Fan Control Output。还有 output range 10/0 常数给了 PID 的输出限幅（0~10V）。图4 右上和右下有 "10" 和 "0" 的橙色常数 → 上下限。

That matches: PID output range [0, 10].

Good — I can mention: 图中 PID VI 上方有输出上下限（10 和 0），把输出限制在 0~10V，保护风扇。

Wait, in 图4 the "10" appears twice? There's a "10" orange constant near Derivative/Integral/Proportional cluster and the PID icon, and a "10"/"0" at bottom right going to the right edge. Hmm. In 图3 (manual case) there's "10" and "0" at bottom right too. Probably the output range 0-10 cluster. I'll mention it lightly as "输出限幅 0~10".

Actually in the main 图2, near the PID VI (右上) there's "10" then the PID icon with inputs 1,3 and the boxes. The "10" might be a numeric constant for the output high limit. And at bottom right "10"/"0" cluster = DAQ 写入的通道?

I'll keep it general: PID VI 设置了输出上下限（0~10 V）。

Hmm, in 图2 there's "10" and near it a box, plus "3" — these could be the PID VI's "output range" high limit 10 and low limit 0? And "3" might be something else. I'll not over-specify.

OK. Also mention: DAQmx 函数（创建虚拟通道 myDAQ1/ai0 "AI电压"、myDAQ1/ao0 "AO电压"、读取、写入、清除任务）—— 相比 DAQ 助手更底层，需要手动指定采样数/速率。

Now, LabVIEW 基础（小白必备）:
- 前面板 (Front Panel) = 用户界面，放控件 (Control, 输入) 和显示控件 (Indicator, 输出)
- 程序框图 (Block Diagram) = 代码，Ctrl+E 切换
- 数据流：节点所有输入就绪才执行
- While 循环 + 停止按钮
- Express VI（DAQ 助手、滤波器、频谱测量、仿真信号、单频测量、函数发生器）—— 蓝色边框，双击配置
- 动态数据类型（深蓝粗线）—— Express VI 之间传的是"动态数据"
- 数值/布尔/数组/波形 各自的线型颜色

Let me write: 
- 橙色细线 = 数值
- 绿色细线 = 布尔
- 深蓝色粗线 = 动态数据
- 棕色粗线 = 波形
- 蓝色细线 = 整型

From the diagrams: 数值是橙色/黄色, 布尔是绿色, 动态数据是深蓝, 波形是棕色(在exp3里滤波后信号是棕色? 实际"滤波后的信号"输出是深蓝动态数据). In p11 exp2 diagram the audio path is blue (动态数据) and the multipliers show orange 数值 DB等. Hmm, the multiplier boxes have "DBL" labels = 双精度数值. Yes, because 滤波器 Express VI 输出动态数据，转成数值后相乘。

Actually in the exp2 block diagram, the wires between filters and multipliers appear blue-ish/dark. The multipliers have "DBL" tags meaning the output is DBL. Hmm, multiplication of dynamic data? Express VI "滤波器" outputs dynamic data; you can multiply dynamic data by a numeric scalar (LabVIEW auto-converts). The "DBL" labels are on the slide controls.

Fine — I'll describe at a functional level and mention line colors generally.

Alright. Also mention 软件环境: LabVIEW + NI-DAQmx 驱动 + NI ELVISmx 驱动（实验三用到 NI ELVISmx Function Generator）+ NI MAX。

Let me now write the answer. It's going to be long. I'll use clear headings, tables, and numbered steps.

One consideration: should I write this to a file as well? I'll produce the chat answer, and at the end offer to export. Actually — given the length and that they'll need it for a report, let me just also save it as a Markdown file. Hmm, that requires me to output the content twice (once in Write, once in chat). That's expensive.

Decision: output in chat only, then offer to save as .md/.docx. That respects "简单任务直接做" and avoids duplication.

Hmm, but actually, thinking about user benefit: a very long chat message in a terminal is hard to use. But the user explicitly asked to "介绍". I'll go with chat.

Let me clean up the temp files at the end? I created lab_text.txt, p*.png, crop*.png in the workspace. I should probably clean them up or leave them. They might be useful. I'll leave them but mention. Actually, cleanliness — let me remove the PNGs but keep lab_text.txt? Hmm, the user might want the images. Let me just leave them and mention where they are. Actually no, clutter. I'll clean up the pngs and keep the extracted text, mentioning it.

Hmm, actually the crop images might be useful for the report (实验报告要放前面板与程序框图截图). But those are from the manual, not their own. They need their OWN screenshots.

Let me keep the extracted text file and delete the PNGs. Actually, let me keep them — they're just 8 files and could be handy. No — I'll clean the crops at least.

Simplest: leave everything, mention the text file path. Minor. Actually let me clean up to be tidy: delete crops and page PNGs.

Eh. Let me just leave them; deleting adds a risky step. I'll mention.

Hmm, I'd rather be tidy. Let me delete the pngs (I generated them, safe to delete).

OK now let me write the final answer.

Let me make sure I structure it for a complete beginner:

---

# 总览 / 先决条件

## 0.1 这套实验到底是什么
虚拟仪器 = 用电脑软件代替传统仪器的面板和功能 + 一块数据采集卡做 I/O。myDAQ 就是那块卡，LabVIEW 就是那个软件。

## 0.2 myDAQ 接口速查
| 接口 | 说明 | 本课用到 |
- AI0/AI1: 模拟输入, ±10V/±2V, 16位
- AO0/AO1: 模拟输出, ±10V/±2V
- DIO 0-7 (port0): 数字 I/O, 3.3V
- AUDIO IN/OUT: 3.5mm 立体声, line level
- +5V / ±15V: 电源输出
- DMM: 万用表

## 0.3 LabVIEW 5 分钟速成
前面板/程序框图/数据流/While循环/Express VI/线型颜色/DAQ助手怎么配

## 0.4 三个实验的定位

---

# 实验二 音频均衡器

## 2.1 一句话
## 2.2 试验台与接线（看图+文字）
## 2.3 原理（3层：音频频谱→滤波分频→加权混合；功率谱）
## 2.4 程序搭建 10 步（小白版，每步说清"在哪、点什么、为什么"）
## 2.5 程序框图数据流复盘
## 2.6 运行与实验结果（你该看到什么）
## 2.7 坑与排错

---

# 实验三 myQuake

## 3.1 一句话
## 3.2 材料与信号连接表
## 3.3 平台搭建 6 步
## 3.4 原理（偏心电机/加速度计/设置字/低通/峰值）
## 3.5 程序结构（2个循环）
## 3.6 操作步骤
## 3.7 实验结果（起振16-18%，P波，Y轴单位）
## 3.8 坑与排错

---

# 实验四 myVTOL

## 4.1 一句话
## 4.2 材料与信号连接
## 4.3 平台搭建
## 4.4 原理（霍尔测角/风扇升力/开环闭环/PID三兄弟）
## 4.5 前面板每个控件是什么
## 4.6 程序框图
## 4.7 操作步骤 4-8
## 4.8 PID 整定实操手册（小白版）
## 4.9 实验结果
## 4.10 坑与排错

---

# 三实验横向对比表

# 实验报告怎么写

Let me write it out now. I'll keep tables where helpful.

Let me be careful with the number of tokens — this will be maybe 6000-9000 words in Chinese. That's fine.

Let me write.

One more check: 实验二 Step2 says "待读取采样"设置为320. And Step7 待写入采样 320. Yes.

And "音频转接线" needed: 3.5mm to 3.5mm or dual RCA→3.5mm.

myDAQ AUDIO IN is a 3.5mm stereo jack; AUDIO OUT is a 3.5mm stereo jack. So you connect 手机 → 3.5mm 公对公线 → myDAQ AUDIO IN；myDAQ AUDIO OUT → 耳机/有源音箱。

Note: myDAQ audio out is line-level, so passive speakers won't work — need powered speakers or headphones. Good tip.

Also: if the phone has no 3.5mm jack, need a USB-C/Lightning → 3.5mm adapter.

Let me write the answer now.

Also for exp 2: the sample rate. DAQ Assistant for audio channels: myDAQ audio in/out sample rate is set in DAQ Assistant; default 44100 Hz. I'll mention as "默认（myDAQ 音频通道通常是 44100 Hz）", hedged.

Actually hold on — the manual says "待读取采样 320" but doesn't say rate. If the rate is 44100, 320 samples = 7.26 ms. Latency ~7ms, good for real-time audio. If rate were 10000, 320 = 32ms (audible latency). I'll present: 保持默认采样率（myDAQ 音频通道约 44.1 kHz），320 点 ≈ 7 ms 一块，延迟小，适合实时监听。

Hmm, I want to avoid asserting a wrong number. Let me phrase: "采样率保持 DAQ 助手的默认值（myDAQ 音频通道的默认采样率约 44.1 kHz 量级；以你屏幕上显示为准）。320 点一块 → 约几毫秒，人耳听不出延迟。"

OK good.

Also mention: 两个 DAQ 助手的采样数必须一致（都是 320），否则会周期性出现"咔哒"声（缓冲区欠载/溢出）。

Let me write.

For the report requirements, the manual's exp1 lists report contents: 概要/实验过程简短描述/实验感想/理解/截图。I'll adapt for 2,3,4.

Alright, writing now. I'll also clean up PNGs first.

Actually let me not spend a tool call on cleanup — I'll do it in one bash call along with nothing else. It's cheap. Let me do it at the end... no, I can't call tools after the final answer. Let me do the cleanup before writing the answer.

Eh, it's fine — I'll leave the files and mention them. Actually a tidy workspace is better. One quick call.

Let me just do it.

</details>

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/.zcode/workspace/default && rm -f p10.png p11.png p14.png p15.png p16.png p18.png p19.png p20.png crop_p15_fig2.png crop_p16_fig4.png && ls", "description": "Clean up temporary rendered images"}` → `985经管类预推免清单-20260914.md _ocr.ps1 _pdf_extract.mjs _pdf_render.mjs bigfiles.csv build_plan_docx.py cleanup_log.txt cleanup_tier1.ps1 cleanup_tier2.ps1 duplicates.csv extract_pdf.py lab_text.txt pdf_text/ scan_bigfiles.ps1 scan_dups.ps1 scan_size.ps1 solidworks-gear/ sw-schema.mjs top_level.txt xjtu/ xjtutjms_2027.pdf xj …[截断,原长410]`

<details><summary>💭 思考链（deepseek-flash）</summary>

Cleanup done. I also notice there's 某985高校实习计划安排.docx — the user is from 某985高校, matching the lab manual (某985高校工学院). 

Now let me write the comprehensive answer.

Let me write it all out.

</details>

### 🤖 助手（deepseek-flash，2026-09-15 13:20）

已读完指导书全文（22 页）并把实验二/三/四的插图都看清了。下面按「**先补基础 → 再逐个实验 → 最后横向总结**」的方式写，假设你完全没碰过 LabVIEW 和 myDAQ。

---

# 第 0 章　先补 10 分钟基础（不看这章后面会卡）

## 0.1 什么叫"虚拟仪器"

传统仪器 = 一块铁盒子，面板上的旋钮、屏幕都焊死在硬件里。
虚拟仪器 = **一块通用的数据采集卡（本课是 NI myDAQ）+ 一台电脑上的软件（LabVIEW）**。

- 采集卡只负责"把模拟电压变成数字、把数字变成模拟电压"（叫 I/O）；
- 滤波、频谱分析、PID 运算、显示——全部在电脑里用软件做。

所以你会发现：实验二、三、四用的**是同一个人硬件 myDAQ**，只是插了不同的"外围小板子"（myQuake / myVTOL 电路板），装的是不同的 LabVIEW 程序。这就是"虚拟"的含义——**功能由软件决定**。

## 0.2 myDAQ 接口速查表

| 接口 | 类型 | 说明 | 本课哪里用到 |
|---|---|---|---|
| **AI0 / AI1** | 模拟输入 | 测电压，16 位，量程可选 ±10 V 或 ±2 V | 实验三（接两个加速度计）、实验四（接霍尔传感器） |
| **AO0 / AO1** | 模拟输出 | 输出指定电压，量程 ±10 V 或 ±2 V | 实验三（驱动偏心电机）、实验四（驱动风扇） |
| **DIO0~DIO7（port0）** | 数字 I/O | 8 根线，3.3 V 逻辑，可整口一起写 | 实验三（给加速度计写 8 位"设置字"） |
| **AUDIO IN** | 3.5 mm 立体声输入 | 线路电平（不能接麦克风大信号） | 实验二（接手机/播放器） |
| **AUDIO OUT** | 3.5 mm 立体声输出 | 线路电平，**推不动无源音箱** | 实验二（接耳机或有源音箱） |
| **+5V / ±15V** | 电源输出 | 给外部小板子供电 | 实验一、三、四 |
| **DMM** | 数字万用表 | 测电阻/电压/二极管 | 实验一 |

> ⚠️ 关键概念：**AI/AO 是"电压"通道，AUDIO IN/OUT 是"音频"通道**。它们在 DAQ 助手里是**两套完全不同的通道名**（`ai0` vs `audioInputLeft`），选错就一点信号都没有。

## 0.3 LabVIEW 五分钟速成

### 两个界面，Ctrl+E 来回切
| | 前面板 Front Panel | 程序框图 Block Diagram |
|---|---|---|
| 是什么 | **用户界面**（旋钮、指示灯、图表） | **源代码**（连线、运算、循环） |
| 放什么 | 控件（输入，如旋钮）/ 显示控件（输出，如波形图） | 函数、Express VI、结构 |
| 谁给谁 | 你在前面板操作 → 数据流进框图 | 框图算完 → 结果回到前面板显示 |

**一条铁律**：图上的所有东西都是**同一份数据的两种视图**。你在前面板加一个旋钮，框图里就自动多出一个旋钮图标，它们永远是同一个东西。

### 数据流（LabVIEW 的执行规则）
一个节点（方块）**只有它所有输入端口都有数据了，才会执行**。跟 C 语言"从上往下逐行执行"完全不同，是"数据到了就跑"。所以**连线就是程序逻辑**，线断了程序就不跑（LabVIEW 会把运行箭头变成断裂箭头 ▶️ 断裂）。

### While 循环
一个框框，右下角有"条件接线端"：
- 接 **停止按钮**（Stop）：点一下 → 循环结束；
- 本课所有程序都是"**采集/控制持续进行，直到你按 Stop**"——这就是 While 循环。

左下角 `i` 是循环计数（第几次循环）。

### Express VI —— 小白最重要的概念
你会在函数选板看到一批**蓝色边框、图标很大**的方块，叫 **Express VI**。它们的特点是：
- **双击会弹出配置对话框**，勾勾选选就行，不用写代码；
- 输出/输入是**"动态数据"（深蓝色粗线）**，能自动携带采样率、时间信息；
- 本课用到的 Express VI：**DAQ 助手、滤波器、频谱测量、仿真信号、单频测量、函数发生器、获取波形分量、数组最大值与最小值**。

### 线型/颜色速记
| 颜色 | 含义 |
|---|---|
| **深蓝粗线** | 动态数据（Express VI 之间） |
| **橙色细线** | 数值（DBL 双精度） |
| **绿色细线** | 布尔（真/假） |
| **蓝色细线** | 整型 |
| **棕色** | 波形 |
| **虚线/断裂** | 类型不匹配 → 程序跑不起来 |

### DAQ 助手（DAQ Assistant）——三课的核心武器
它是"**配置采集卡**"的图形化向导。双击后走三步：
1. **选择任务类型**：`采集信号(输入)` 或 `生成信号(输出)`；
2. **选择通道**：模拟输入→电压→勾 `ai0`；或音频→`audioInputLeft/Right`；或数字输出→port0；
3. **设置参数**：量程（±2 V / ±10 V）、采集模式（连续采样）、采样率、待读取/待写入采样数。

配置完点确定，它会**自动生成一个 While 循环**，把 VI 放进去。以后想改参数，双击那个方块就能重新打开向导。

---

# 第 1 章　实验二：基于 myDAQ 的音频均衡器

## 1.1 一句话目标

> **把手机/播放器放的音乐，从 myDAQ 的 AUDIO IN 收进来 → 用软件切成"低音 / 中音 / 高音"三段 → 每段用一个滑块单独调音量 → 三段重新合起来、再整体调一次总音量 → 从 AUDIO OUT 送到耳机。同时用波形图看输出的功率谱。**

这就是一个**三路带通 + 加权求和**的数字音频均衡器（和你在音乐 App 里看到的 EQ 是同一原理）。

## 1.2 试验台搭建（动手第一步）

**材料清单**
1. myDAQ 及 USB 线
2. 音频转接线（3.5 mm 公对公线；手机若无耳机孔需 USB-C/lightning 转 3.5 mm 转接头）
3. 扬声器或耳机（**必须是有源音箱**，myDAQ 音频输出是线路电平，推不动无源喇叭）
4. 电脑 + LabVIEW + NI-DAQmx 驱动

**接线（照着插，别插错）**

```
手机/播放器 ──3.5mm音频线──► myDAQ 的 AUDIO IN
myDAQ 的 AUDIO OUT ──► 耳机 或 有源音箱
myDAQ ──USB线──► 电脑
```

**软件前置检查**：打开 NI MAX → 「设备和接口」里应能看到 **Dev1/Dev2（myDAQ）** → 右键「自检」通过。如果这里就不通过，后面全白搭。

## 1.3 原理：这个东西到底在算什么

### (1) 先把"声音"看成一条频谱

人耳能听 20 Hz ~ 20 kHz。任何音乐都可以被分解成"某个频率上有多大能量"。工程上习惯粗分三段：

| 频段 | 频率范围 | 听感 | 典型乐器/成分 |
|---|---|---|---|
| **Bass 低音** | 20 – 140 Hz | 轰、有力度、胸口震动 | 贝斯、大鼓 |
| **Midtone 中音** | 400 – 2600 Hz | 人声、主要旋律 | 人声、吉他中频 |
| **Treble 高音** | 5200 – 10000 Hz | 亮、清脆、有"空气感" | 镲片、齿音 |

> 注意三个频段**不是无缝拼接**的：140–400 Hz 和 2600–5200 Hz 是"缝隙"，被三个滤波器一起衰减掉了。这是指导书原文的设定，**只要照做就行**。副作用是声音会略"瘦"一点，这是正常现象，不是 bug。

### (2) 怎么"切"出某一段？——带通滤波器

- **带通滤波器 (Bandpass)**：只让"低截止频率 ~ 高截止频率"之间的频率通过，低于和高于的都被大幅衰减。
- 例：设为「低截止 20 Hz，高截止 140 Hz」→ 输出就只剩低音。

指导书要配 3 个带通：

| 对应滑块 | 滤波器类型 | 低截止 | 高截止 |
|---|---|---|---|
| Bass | 带通 | **20 Hz** | **140 Hz** |
| Midtone | 带通 | **400 Hz** | **2600 Hz** |
| Treble | 带通 | **5200 Hz** | **10000 Hz** |

> 顺带解释"为什么是 5200–10000 而不是到 20000"：myDAQ 音频通道采样率约 44.1 kHz，按奈奎斯特定理，**能正确表示的最高频率约 22 kHz**，所以 10 kHz 完全在安全范围内。

### (3) 加权 + 求和 = 均衡

设三段滤波后的信号为 `B(t)`, `M(t)`, `T(t)`，三个滑块值为 `b, m, t`（范围 0~1），总音量滑块为 `V`（0~1），则：

$$y(t) = V \cdot \big[\, b\cdot B(t) + m\cdot M(t) + t\cdot T(t) \,\big]$$

- **滑块 = 权重（增益）**。拉到 1 → 该段原样通过；拉到 0.5 → 该段音量减半；拉到 0 → 该段**彻底消失**。
- 三段求和后的信号，再用 `V` 统一缩放 → **总音量与音色分调**，互不干扰。
- 这就是"**均衡**"的本质：**不改音高、不改节奏，只改各频段的能量配比**。

### (4) 波形图上看什么？——功率谱密度

程序最后接了一个「**频谱测量**」，配置为「**功率谱密度 / 线性**」。

- **频谱** 回答的问题是："这段信号里，各个频率各有多少能量？"
- 横轴 = 频率 (Hz)，纵轴 = 幅值（功率）。
- 你拉 Bass 滑块，就会看到 **0~140 Hz 那一段曲线整体抬高**；拉 Treble，**5 kHz 以上抬高**。
- 这是**最直观的验收方式**：耳朵听 + 眼睛看谱，双重证明程序做对了。

> 补充：指导书截图里图例是 `Voltage_0 (Power Spectrum)` 和 `Voltage_1 (Power Spectrum)`——因为采的是**立体声左右两路**，所以谱有两条曲线。

## 1.4 程序搭建：10 个 Step 的小白版

### Step 1　打开 LabVIEW
运行 LabVIEW → 「文件」→「新建 VI」。你会得到**一个空白前面板 + 一个空白程序框图**，按 **Ctrl+E** 在两者间切换。

### Step 2　建"音频采集"（DAQ 助手 1）

在**程序框图**里右键 → 函数选板 → 「**测量 I/O**」→「**DAQ 助手**」，放到框图空白处 → **双击它**：

1. 选择「**采集信号**」→「**模拟输入**」→「**电压**」→ 下一步
2. **物理通道界面：同时勾选 `audioInputLeft` 和 `audioInputRight`**（按住 Ctrl 多选，两个都要！）→ 完成
3. 设置窗口：
   - 输入范围：**-2 到 2**（伏）
   - 「定时设置」→ 采集模式：**连续采样**
   - **待读取采样：320**
4. 点确定

**发生了什么**：LabVIEW 自动生成了一个 While 循环，DAQ 助手在里面。以后所有 VI 都放在这个循环里。

> **为什么范围是 ±2 V？** myDAQ 音频通道是线路电平（约 1 V 峰峰值级别），±2 V 足够覆盖又不会削波。范围选太大（±10 V）会让 16 位 ADC 的分辨率白白浪费 5 倍。

> **为什么"待读取采样"是 320？** 这是**每次循环从卡里读多少个点**。采样率约 44.1 kHz 时，320 点≈**7 毫秒**一块。块太小 → CPU 忙不过来会"咔哒"；块太大 → 延迟明显。320 是个平衡点。
> **记住 320 这个数**——后面 DAQ 助手 2 的"待写入采样"**必须也是 320**，两边对不上会周期性出现爆音。

### Step 3　加 3 个滤波器

函数选板 →「**Express**」→「**信号分析**」→「**滤波器**」，放**三个**在 While 循环里。每个**双击**配置：

| 第几个 | 类型 | 低截止频率 | 高截止频率 |
|---|---|---|---|
| 滤波器 1（给 Bass 用） | **带通** | 20 | 140 |
| 滤波器 2（给 Midtone 用） | **带通** | 400 | 2600 |
| 滤波器 3（给 Treble 用） | **带通** | 5200 | 10000 |

点确定。

> 滤波器是**串联还是并联**？这里是**并联**——三个滤波器**都接同一路原始信号**（DAQ 助手的 data 输出），各自输出一段。千万别串起来接。

### Step 4　放 4 个滑块，做 3 次乘法

1. **前面板** → 控件选板 →「**数值**」→ **垂直指针滑动杆**，放 4 个。
   分别右键→属性/或直接双击标签，改名为：
   **`Volume`、`Bass`、`Midtone`、`Treble`**
   （默认量程 **0 ~ 1**，截图里刻度就是 0, 0.2, 0.4, 0.6, 0.8, 1）

2. **回到程序框图**（Ctrl+E）。此时框图上已经自动出现了这 4 个滑块图标。
   加 3 个「**乘法**」节点（函数选板 →「编程」→「数值」→「乘」）。
   连线：

```
滤波器1(滤波后的信号) × Bass滑块      → 积B
滤波器2(滤波后的信号) × Midtone滑块   → 积M
滤波器3(滤波后的信号) × Treble滑块    → 积T
```

> 注意：**`Volume` 滑块这一步不参与乘法**，它是留到最后统一乘的。

### Step 5　放 3 个进度条，看每段有多强

前面板 → 控件选板 →「数值」→ **垂直进度条**，放 3 个，分别命名为 **Bass、Midtone、Treble**。
把上面三个"积"分别连到这 3 个进度条上。

**作用**：这是**可视化的音量指示**——你拉滑块时，能看到每段的电平实时变化。这也是后面实验报告截图里很好看的素材。

### Step 6　三段求和，再乘总音量

程序框图：
```
积B ─┐
积M ─┼─► [加] ─► [加] ─► [乘] ◄── Volume滑块
积T ─┘                     │
                    最终输出信号 y(t)
```
1. 用「加」节点把 积B + 积M → 和1
2. 和1 + 积T → 和2
3. 和2 × Volume 滑块 → **这就是最终要播出去的信号**

### Step 7　建"音频输出"（DAQ 助手 2）

再放一个 DAQ 助手（**同一个 While 循环里**），双击：

1. 选择「**生成信号**」→「**模拟输出**」→「**电压**」→ 下一步
2. 物理通道：**同时勾选 `audioOutputLeft` 和 `audioOutputRight`** → 完成
3. 设置：
   - 信号输出范围：**-2 到 2**
   - 定时设置：**连续采样**
   - **待写入采样：320**（必须和 DAQ 助手 1 一致！）
4. 确定

然后把上一步的**"最终输出信号 y(t)"连到 DAQ 助手 2 的「数据」输入端口**。

> ⚠️ 千万别把 DAQ 助手 1 的输出直接连到 DAQ 助手 2 上——那样就是把输入原样输出，成了"直通线"，滑块全失效。

### Step 8　加频谱测量

函数选板 →「**Express**」→「**信号分析**」→「**频谱测量**」，双击配置：
- 选择 **功率谱密度**
- 选择 **线性**
- 点确定

把它的「**信号**」输入接到**最终输出信号 y(t)**（也就是和送给 DAQ 助手 2 的是同一路信号）。

> **为什么接最终输出、而不是接原始输入？**
> 因为你要看的是"**经过均衡处理之后**，实际播出的是什么频谱"。接原始信号就只能看到播放器原曲，滑块怎么拉曲线都不动，实验就白做了。

### Step 9　加波形图

前面板 → 控件选板 →「**图形**」→ **波形图（Waveform Graph）**。
程序框图里，把「频谱测量」的「**功率谱**」输出连到波形图。

### Step 10　运行

点工具栏的**运行箭头** ▶（或 Ctrl+R）。前面板的 STOP 按钮能停止。

**最终的完整数据流（对照指导书的程序框图）**

```
                       ┌─► Filter1(Bass 20-140)  ─► ×Bass ────┐
DAQ助手1 ──data──┬─────┼─► Filter2(Mid 400-2600) ─► ×Midtone ─┼─► Σ ─► ×Volume ─┬─► DAQ助手2 ─► AUDIO OUT
audioIn L/R      │     └─► Filter3(Treble 5.2k-10k)─►×Treble ──┘                   │
                 │                                                                    └─► 频谱测量 ─► 波形图
              (还在While循环里，Stop按钮控制退出)
```

## 1.5 运行步骤与**实验结果**

**操作顺序（指导书原文）**：
1. 点击音频源（手机）上的**播放**按钮；
2. 点击 LabVIEW 的**运行**按钮；
3. 用鼠标拖动前面板的**音量、BASS、MIDTONE、TREBLE 拉杆**，边拉边听耳机。

### ✅ 你应该观察到的结果

| 你的操作 | 听到的 | 波形图（功率谱）上看到的 |
|---|---|---|
| 四个滑块都在 0.5 | 正常音乐 | 频谱呈较平缓的分布 |
| **把 Bass 拉到 1** | 低音明显变强、变"轰" | **0–140 Hz 区域曲线整体抬高**，Bass 进度条变长 |
| **把 Bass 拉到 0** | 低音消失，声音变"薄" | 0–140 Hz 几乎压到接近 0 |
| **把 Treble 拉到 1** | 声音变"亮"、"脆"，镲片突出 | **5.2k–10k Hz 区域抬高**，Treble 进度条变长 |
| **把 Treble 拉到 0** | 声音发闷，像蒙了层布 | 高频区域被压平 |
| **把 Midtone 拉到 1** | 人声、主旋律突出 | 400–2600 Hz 抬高 |
| **只留 Volume，其余三个全 0** | 近乎静音（只剩频段缝隙的极少残留） | 频谱被压到很低 |
| **Volume 从 0 拉到 1** | 整体音量线性增大 | 全频段等比抬高（形状不变） |

**报告里放这些截图**：① 前面板全貌（4 个滑块 + 3 个进度条 + 频谱图 + STOP）；② 程序框图全貌；③ 至少一张"Bass 拉满前 vs 拉满后"的频谱对比图。

## 1.6 坑与排错（实验二）

| 现象 | 原因 | 解决 |
|---|---|---|
| 完全没声音 | 通道选成了 `ai0/ai1` 而不是 `audioInputLeft/Right` | 双击 DAQ 助手重选 |
| 完全没声音 | 手机没播放 / 音量 0 / 音频线插在了耳机孔 | 检查音源和线 |
| 周期性"咔哒/爆音" | 两个 DAQ 助手的 320 对不上，缓冲区欠载/溢出 | 两边都设 320 |
| 声音严重失真/破音 | Volume 长期拉满导致输出超过 ±2 V 削波 | 降低 Volume |
| 声音很怪、像"电话音" | 这是**正常的**——三段滤波器之间有空隙，部分频段被砍掉了 | 不是 bug |
| 运行箭头是**断裂的** | 有线没连 / 类型不匹配（如把动态数据接到了布尔） | 看断裂箭头指向哪，逐条检查连线 |
| 耳机里有尖锐啸叫 | 你把 AUDIO IN 接成了麦克风，输出又接到音箱 | 本实验输入应是**播放器**，不是麦克风 |

---

# 第 2 章　实验三：myQuake 加速度计信号采集

## 2.1 一句话目标

> **用偏心电机"摇"一个建筑模型（模拟地震），用两个加速度传感器测结构上下两个点的振动，在 LabVIEW 里实时显示波形和峰值。同时学会用 8 位"设置字"通过数字口去配置传感器。**

## 2.2 材料与信号连接

**材料**
1. myDAQ 及 USB 线
2. **myQuake NI miniSystem**（含偏心电机、测量电路板）+ 2 个加速度传感器
3. LabVIEW + **NI ELVISmx 驱动**（因为要用"函数发生器"Express VI）

**信号连接表（背下来）**

| myQuake 部件 | 接到 myDAQ |
|---|---|
| **电机** | 模拟输出 **AO 0** |
| **Accel A**（加速度传感器 A） | 模拟输入 **AI 0** |
| **Accel B**（加速度传感器 B） | 模拟输入 **AI 1** |

## 2.3 实验平台搭建（6 步）

1. **把待测结构放到平台上**：为了保证能在更宽振幅范围内测量，可以用办公室**公文夹**之类的小物件把结构**底座与平台固定住**。
   > 🔑 这一步很关键：如果结构只是"放"在平台上，「振动」就变成了整体"滑动"，测到的是噪声。
2. **把 myQuake 测量电路板与 myDAQ 连接**，注意插紧。
3. **安装两个加速度传感器**：用**燕尾夹**把它们固定在结构上要测的两个点上。
   - 一个**靠近底座**，一个**靠近顶部**——这样才能测出偏心电机对上下两点造成的**不同**影响（这正是"结构动力学"的核心：越高处振幅越大）。
4. **连接传感器线**：加速度计的**灰色接头**插到 myQuake 电路板对应的**蓝色接头**。
   - **Accel A → 位置较低的那个传感器**
   - **Accel B → 位于顶端的那个传感器**
   > ⚠️ **注意事项（指导书原文强调）**：两个加速度传感器的连接方式（**X、Y、Z 轴方向**）必须**保持一致**！否则你测到的两个信号方向不同，做相关性分析就完全错了。
5. **确认 myDAQ 已连电脑且可用**（用实验一里的 NI MAX「自检」）。
6. **连接 12 V 直流电源**（给偏心电机供电）。

## 2.4 原理：这一章在讲什么

### (1) 偏心电机 = "人造地震"

普通电机旋转是平衡的。**偏心电机**在转轴上挂了一块**不平衡的质量块**，转起来就产生周期性离心力 → 传递到平台上 → 平台振动 → 结构摇晃。

- **转速**决定激励频率：转得越快，摇晃频率越高；
- 当激励频率接近结构的**固有频率**时，会发生**共振**，振幅急剧放大——这就是指导书里说的"**建筑结构开始摇晃**"。
- 名字 `myQuake`（quake = 地震）就是这个意思：**用偏心电机模拟地震波**。指导书说的"产生 **P 波**"，就是地震学里的**纵波（Primary wave）**，即最先到达的压缩波。这里指结构受迫振动的主振动波形。

### (2) 加速度传感器怎么工作

加速度计内部是一块 Micro-Electro-Mechanical 的**微加工质量-弹簧结构**（MEMS），加速度让它产生位移，通过电容/压阻变化转成**电压输出**：

$$\text{输出电压} \propto \text{加速度}$$

所以传感器输出的是**电压（V）**，而它**代表的物理量是加速度**。两者之间的换算系数叫**灵敏度**（单位 mV/g）。

结构不振动时，加速度计受重力作用，**静态输出是一个非零的直流电压**（对应 1 g），这是正常的。

### (3) ★重点★ 8 位"设置字"——用数字口配置传感器

myQuake 板上的加速度计芯片可以通过**引脚组合**来选择：**测哪个轴（X/Y/Z）** 和 **用多大**量程**。程序要做的就是把 8 个引脚的状态（0/1）打包成一个字节，通过 **myDAQ 的 DIO port0** 一次性写出去。

**Accel A（传感器 A）设置字：**

| | P0 | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|---|---|---|---|---|---|---|---|---|
| **X 轴** | **1** | **0** | G | / | / | / | / | **1** |
| **Y 轴** | **0** | **1** | G | / | / | / | / | **1** |
| **Z 轴** | **1** | **1** | G | / | / | / | / | **1** |

**Accel B（传感器 B）设置字：**

| | P0 | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|---|---|---|---|---|---|---|---|---|
| **X 轴** | / | / | / | / | **1** | **0** | G | **1** |
| **Y 轴** | / | / | / | / | **0** | **1** | G | **1** |
| **Z 轴** | / | / | / | / | **1** | **1** | G | **1** |

**注**：
- `X = 0 或 1`；`/` = 无关位（don't care，随便填）；
- **G 代表量程**：`G = 0` → 量程 **±1.5 g**；`G = 1` → 量程 **±6 g**；
- **P7 = 1** 是**使能位**（两个传感器都要置 1）。

**怎么读这张表**（举例）：
- 要让 **Accel A 测 Z 轴**：P0=1, P1=1, P7=1 → 二进制位 `11xxxxx1`
- 要让 **Accel B 测 X 轴**：P4=1, P5=0, P7=1

**程序实现**（对应指导书"图 3 量程及通道选择程序实现"）：
```
前面板的两个 "Axis" 下拉枚举（Accel A 的轴、Accel B 的轴）
        │
        ├─► 各自查表，产生 2 位布尔值
        │
        └─► 加上常量："G 位" 和 "使能位 P7 = 1"
                        │
                        ▼
              [Build Array 组成 8 元素布尔数组]  ← 名为 "appended array"
                        │
                        ▼
              [布尔数组转数字 Boolean Array To Number]  →  得到 0~255 的整数
                        │
                        ▼
              DAQ Assistant（数字输出 → port0 → 数据）
```
> 指导书原话："该部分程序最终将设定的 **8 位设置字放入数组**中，再将其**从布尔型转换成数字型式**传入 myDAQ 助手中，通过硬件设定所选的传感器轴向及其量程。"

> 💡 **小白提示**：前面板上**没有量程选择控件**——程序里把 **G 位固定成了 0（即 ±1.5 g）**，P7 固定为 1。这是合理的：结构振动是小振幅，±1.5 g 量程分辨率更高。
> 如果你想把量程改成 ±6 g（测更剧烈的振动），需要**回到程序框图把 G 那一位改成 1**，然后重新运行。

### (4) 为什么要加 10 Hz 低通滤波器

**低通滤波器** = 只让低于截止频率的信号通过，高于的衰减掉。
截止频率设为 **10 Hz**，意思是：**只保留 10 Hz 以下的振动，把更高频的东西全部滤掉**。

滤掉的是什么？
- **50 Hz 工频干扰**（实验室里最讨厌的东西）；
- 电机的电磁噪声、开关噪声；
- 传感器的高频本底噪声。

留下来的就是**结构真实的基础振动**（几 Hz 级别的晃动）。所以波形会干净很多——这正是"虚拟仪器"的价值：**硬件只管采，软件负责净化**。

### (5) 峰值读数 (Peak Reading) 是怎么来的

程序从滤波后的信号里**取出 Y 分量（幅值数组）**，再**取数组最大值**，得到这一次采样的**峰值电压**，显示成 `Peak Reading A (V)` / `Peak Reading B (V)`。

> 这个 `(V)` 标注非常关键——见下面 2.7 的"Y 轴单位"。

## 2.5 程序结构：两个循环

指导书的程序框图分**两个并列的 While 循环**：

**循环 ①「数据连续采样循环」**（图 2 / 图 4）——两部分组成：

```
【2.1 加速度传感器的选择与量程设置部分】
   Axis(枚举) ──► 查表 ──► 位 ──┐
   Axis(枚举) ──► 查表 ──► 位 ──┼─► Build Array(8元素) ──► 布尔数组转数字 ──► DAQ Assistant(data)
                               │                                              （数字输出 port0）
                     常量: G=0, P7=1 ──┘

【2.2 信号采集部分】
   DAQ Assistant2 ──data──► [Filter 低通 10Hz] ──► 拆分 A/B ──┬─► 取波形Y分量 ─► 数组最大值 ─► Peak Reading A (V)
   （模拟输入 ai0 & ai1）                 信号→滤波后的信号    │
                                                             ├─► Waveform Chart（两路波形显示）
                                                             └─► 取波形Y分量 ─► 数组最大值 ─► Peak Reading B (V)
```

**循环 ②「电机转速控制循环」**（指导书"图 3 电机控制程序框图"）：
```
   前面板 "%Full Scale" 滑块 ──► NI ELVISmx Function Generator ──► 输出到 myDAQ AO0 ──► 偏心电机
   （Stop 按钮控制这个 While 循环）
```
> 注意：**"函数发生器" Express VI 在函数选板的「测量 I/O」→「NI ELVISmx」里**，添加后在设置窗口中把 **Device 改成你当前连接的 myDAQ 设备名**（比如 Dev1）。

**关于"转速"的控制原理**：函数发生器产生脉冲信号送到 AO0；`%Full Scale`（0~100%）接到函数发生器的幅值输入，改变它等价于改变驱动电机的**脉冲幅度（等效占空比/平均驱动电压）**，从而改变电机的平均功率和转速。**值越大，电机转得越快。**

## 2.6 前面板（图 1）控件说明

| 控件 | 类型 | 含义 |
|---|---|---|
| **Accelerometer A → Axis** | 下拉枚举 | 选择 A 传感器测哪个轴（X/Y/Z） |
| **Accelerometer B → Axis** | 下拉枚举 | 选择 B 传感器测哪个轴 |
| **Peak Reading A / B** | 数值显示 | A/B 两路信号的**峰值电压 (V)** |
| **Motor Control %Full Scale** | 水平滑块 0~100 | 偏心电机转速（截图中显示 18.954） |
| **大波形图 "Accelerometer Response"** | 波形图 | Y 轴 -0.25~0.25，实时显示 A（蓝）/ B（黄）两路波形 |
| **Stop** | 按钮 | 停止 |

## 2.7 运行步骤与**实验结果**

**操作步骤（指导书 4~6 步）**

1. **根据固定的加速度传感器的偏向**，在前面板中选择 Accel A 与 Accel B 的轴向（哪个轴朝振动方向，就选哪个轴）。
2. 将**电机转速控件设为 0%**，点工具栏**运行箭头**运行 VI。
3. **缓慢增加偏心电机控件的值**，大约在 **16% ~ 18%** 左右，电机开始产生 **P 波**，建筑结构开始摇晃。
4. 观察现象，思考：**Y 轴显示的值单位应该是什么？**

### ✅ 你应该观察到的结果

| 阶段 | 现象 |
|---|---|
| 转速 = 0% | 波形图上是**几乎平直的一条线**（叠加少量噪声），Peak Reading 是个很小的恒定值（**这不代表加速度为 0**，而是加速度计静止时受重力的静态输出 + 噪声） |
| 转速 0% → 16% | 电机声音逐渐变大，但**结构还没动**——波形仍接近平直。这个区间叫"**死区**" |
| **转速 ≈ 16% ~ 18%** | ★**临界点**★：电机输出力矩终于克服结构静摩擦/惯量，**结构开始摇晃**，波形图上出现**明显的周期性振荡**（指导书称"**P 波**"），Peak Reading 数值突然跳大 |
| 转速继续增大 | **振幅明显增大**，波形呈规则的正弦状，且**Accel B（顶部）的振幅大于 Accel A（底部）** |
| 转速接近某个值 | 若激励频率接近结构固有频率 → **共振**，振幅急剧飙升（这就是地震中高楼倒塌的原因） |

**关于"Y 轴显示的值单位应该是什么？"——这是指导书留给你的思考题，答案如下：**

> 波形图纵轴的标签是 **"Accelerometer Response"**，而同一张前面板上峰值读数明确标着 **`Peak Reading A (V)` / `Peak Reading B (V)`**。所以：
> **目前纵轴显示的其实是"电压"，单位是 V（伏特）。**
>
> 但它**物理上代表的是加速度**。加速度传感器的输出是"电压 ∝ 加速度"，两者相差一个**灵敏度系数**（典型值约 **300 mV/g**）。因此：
> - **严格意义上正确的单位应该是 `g`（重力加速度，1 g ≈ 9.8 m/s²）或 `m/s²`**；
> - 程序里**没做单位换算**，直接把传感器输出的电压画出来了，所以现在轴上是 V。
> - 若要换算：$$\text{加速度} = \frac{V_{\text{读数}}}{300\ \text{mV/g}}\ \ [\text{g}]$$
>
> 这个思考题的用意就是让你意识到：**虚拟仪器里，物理量→电压→数字量之间的"标定/换算"是必须自己做的一步，软件不会自动帮你完成。**

**报告里放这些截图**：① 前面板（含波形图上有明显振动波形）；② 两个循环的程序框图；③ 峰值读数截图；④ 可选：不同转速下的波形对比。

## 2.8 坑与排错（实验三）

| 现象 | 原因 | 解决 |
|---|---|---|
| 波形全是噪声、没有规律振动 | 结构没固定好，只是整体在滑 | 用燕尾夹/公文夹把底座夹紧 |
| 波形一直平直，加大转速也没用 | ① 电机电源（12 V）没接；② 数字输出 port0 没配置成**输出**；③ DAQ 助手设备名没改成实际 myDAQ | 逐项检查 |
| 两路信号几乎一样 | 两个传感器装得太近（都靠底座或都靠顶部） | 按要求一低一高 |
| A/B 两路相关性很差 | 两个加速度计的 **X/Y/Z 方向没对齐** | 重新安装，保证朝向一致 |
| 波形毛刺很多 | 没加低通滤波器，或截止频率设错 | 加"低通 10 Hz" |
| 电机不转 | `%Full Scale` 是 0；或函数发生器 Device 选错 | 加大 %Full Scale；改 Device |
| 转速加到 16% 还不振 | 平台不水平 / 结构太重 / 12 V 电源电压不足 | 检查电源和固定 |

---

# 第 3 章　实验四：myVTOL 垂直起降控制系统（PID）

## 3.1 一句话目标

> **用一个"会转的风扇"把一根横臂吹起来，用霍尔传感器测臂的角度，让电脑自动调整风扇转速，把臂稳定保持在水平位置上。**

要完成三件事：
1. **起升装置位置监测**（霍尔传感器读数）
2. **通过 PID 控制器调整风扇转速，改变起升力**
3. **使用可调风扇维持设备平衡**

## 3.2 材料与信号连接

**材料**
1. myDAQ 及 USB 线
2. **myVTOL NI miniSystem**（VTOL = Vertical Take-Off and Landing，垂直起降）
3. LabVIEW

**信号连接表（背下来）**

| myVTOL 部件 | 接到 myDAQ |
|---|---|
| **霍尔效应传感器** | 模拟输入 **AI 0** |
| **可变直流风扇** | 模拟输出 **AO 0** |

## 3.3 实验平台搭建（5 步）

1. **把 myVTOL 平台放在一个水平的台面上**（平台不水平，后面的"目标工作点"就全是错的）。
2. 把 myVTOL 的**测量电路板与 myDAQ 连接**，注意连接性。
3. 连接 **9 V 直流电源**或装 **9 V 电池**。
   > ⚠️ 用电池时**确认极性**与电池盒中的极性指示吻合！接反可能烧板子。
4. **打开 myVTOL 电路板的电源开关**。
5. 确保 myDAQ 已连接电脑并可正常使用。

## 3.4 原理：PID 到底在干什么

### (1) 霍尔效应传感器怎么测位置

**霍尔效应**：电流通过一块半导体薄片时，若旁边有磁场，载流子会被洛伦兹力推偏，在薄片两侧产生一个**与磁场强度成正比的电压**——这就是霍尔电压。

在 myVTOL 里：
- 风扇臂的转轴处装有一块**小磁铁**，旁边固定一个**霍尔传感器**；
- 臂**转动角度不同** → 磁铁相对传感器的位置/角度不同 → 传感器感受到的磁场不同；
- → 输出一个**随角度变化的电压**。

所以：**传感器电压 ≙ 臂的角度 ≙ 风扇的升力 ≙ 风扇功率**。这一串"≙"就是整个控制回路的基础。

> 从前面板截图看，传感器读数在 **2.00 ~ 2.50 V** 之间（纵轴刻度），当前读数 **2.04 V**，默认目标 **2.1 V**。水平位置的读数通常在**中间某个值附近**（要靠第 5 步自己校准）。

### (2) 风扇怎么把臂"吹起来"

风扇螺旋桨转动 → 向下推动空气 → 空气给风扇一个**向上的反作用力**（升力）。
- 升力 ∝ 转速²（近似） ∝ 输入电压；
- 所以**控制风扇的驱动电压 AO0，就等于控制升力**，也就等于控制臂的**抬起角度**。

这是一个**力矩平衡**问题：
- 风扇升力产生的**抬头力矩** ↔ 臂自身重力的**低头力矩**；
- 两者平衡 → 臂停在某个角度。

### (3) 开环 vs 闭环（这是本实验的灵魂）

| | 手动控制（开环） | PID 控制（闭环） |
|---|---|---|
| 你怎么做 | 你手动拉滑块给风扇电压 | 你只告诉程序"我要 2.1 V"，程序自己算 |
| 能不能稳住 | **很难**。气流扰动、电压漂移、电机发热，臂会自己飘走 | 能。偏差一出现就自动修正 |
| 像什么 | 用手一直扶着 | 空调恒温 |

**闭环控制回路**：
```
   目标值 SP ──► 误差 e = SP − PV ──► [PID 运算] ──► 风扇电压 AO0 ──► 风扇转速/升力
   (2.1 V)              ▲                                                  │
                        │                                                   ▼
      实际值 PV ◄────── 霍尔传感器 AI0 ◄─────────────────────────────── 臂的角度
```

### (4) ★PID 三个环节各自的作用★（小白必读）

PID 的输出公式：

$$u(t) = \underbrace{K_p \cdot e(t)}_{P} \;+\; \underbrace{K_i \int_0^t e(\tau)\,d\tau}_{I} \;+\; \underbrace{K_d \cdot \frac{de(t)}{dt}}_{D}$$

其中 **误差 `e = 目标值 − 实际值`**。

| 环节 | 数学含义 | 通俗解释 | 调的太大 | 调的太小 |
|---|---|---|---|---|
| **P 比例** | 正比于当前误差 | "差得多就使劲推"。误差 0.1 V → 输出 1 V | **来回振荡**，像新手开车方向盘打过度 | 反应迟钝，到不了目标（有**静差**） |
| **I 积分** | 正比于误差的历史累积 | "差得久就再加把劲"。哪怕误差只剩一点点，只要**存在**就一直累加 | **超调大、积分饱和**，来回慢慢晃 | **消不掉静差**，永远差一点点到不了目标 |
| **D 微分** | 正比于误差的变化率 | "眼看要冲过头了，提前刹车" | **对噪声极敏感**，电机尖叫抖动 | 冲过头、超调大 |

**一句话记忆**：
- **P 决定"反应快不快"**
- **I 决定"最终准不准"**（消除稳态误差）
- **D 决定"刹不刹得住"**（抑制超调）

**推荐整定顺序（一定要按这个顺序，别三个一起乱拧）**：
1. **先把 I 和 D 设为 0**（截图默认 I=0.03, D=0.050，整定时可先改成 0）；
2. **只调 P**：从小往大加 → 直到臂开始**等幅振荡** → 然后把 P **减小到振荡值的一半**；
3. **再加 I**：从很小的值开始（如 0.001）缓慢增加 → 直到**静差消失**为止，**别再加了**；
4. **最后加一点 D**：从 0 缓慢增加到**超调被明显压下去**为止。

指导书前面板的默认值是：**P = 1.000，I = 0.03，D = 0.050**——这是一个已经调好的可用起点，你可以先照这个跑，再故意改坏看看会发生什么（这正是实验报告最好的素材）。

## 3.5 前面板（图 1）每个控件是什么

| 控件 | 默认值 | 作用 |
|---|---|---|
| **波形图 Sensor Input** | 纵轴 2.0~2.5，横轴 Time 0~329 | 实时显示两条曲线：**Actual Reading（蓝，实际读数）** 和 **Set Point（黄，目标值）** |
| **AutoScale** | 勾选框 | 让纵轴自动缩放 |
| **Control Mode** | `Manual` 按钮 | **手动/PID 模式切换**（点击切换） |
| **Sensor Reading** | 2.04 V | 霍尔传感器**当前实际读数** |
| **Fan Control Output [V]** | 表盘 0~10 | **实际送到风扇的电压**（手动或 PID 算出来的） |
| **PID Set Point → Target Sensor Reading** | 2.1 | **目标工作点**（第 6 步要输入你自己测的水平位置读数） |
| **PID Gain Settings → Proportional** | 1.000 | Kp |
| **PID Gain Settings → Integral** | 0.03 | Ki |
| **PID Gain Settings → Derivative** | 0.050 | Kd |
| **Manual Fan Power Control** | 垂直滑块 0~10 | 手动模式下直接给风扇的电压 |
| **Stop** | 按钮 | 停止 |

> **模式互锁**（指导书特别强调）：控制模式选"手动"时，**PID 不起作用**；选"PID"时，**手动滑块不起作用**。程序里用一个**条件结构（Case Structure）**实现这个切换。

## 3.6 程序框图（图 2/3/4）

**图 2「位置监测及风机控制部分」的主干**：

```
myDAQ1/ai0 (AI电压) ──► DAQmx 创建虚拟通道 ──► DAQmx 读取 ──► Sensor Reading（数值显示）
                                    │                              │
                                    │                              ▼
                                    │                    ┌─── 条件结构（Control Mode 选择）───┐
                                    │                    │                                    │
                                    │              【假 = 手动模式】              【真 = PID 模式】
                                    │              Manual Fan Power Control ──►   Target Sensor Reading（SP）
                                    │                 直接输出到风扇              Sensor Reading（PV）
                                    │                                            PID VIs ──► 限幅 0~10 V
                                    │                    └────────────┬───────────────┘
                                    ▼                                 ▼
                              （输出值） ──────────────► Fan Control Output [V]（表盘）+ Waveform Chart
                                                          │
myDAQ1/ao0 (AO电压) ◄── DAQmx 创建虚拟通道 ◄── DAQmx 写入 ◄─┘
                                                          │
                        Stop 按钮 ──► While 循环条件       DAQmx 清除任务（×2，退出时释放资源）
```

**手动部分（图 3，"假"分支）**：滑块 `Fan Power Control` 的值直接输出 → 送给风扇；同时给 PID 路径一个 0。

**PID 部分（图 4，"真"分支）**：
- `PID Set Point → Target Sensor Reading` 作为 **SP（目标值）**；
- `Sensor Reading` 作为 **PV（过程变量/实际值）**；
- `Proportional / Integral / Derivative` 三个数值框作为 **Kp / Ki / Kd**；
- 送进 PID VI 运算 → **输出限幅在 0~10 V**（图中"10"和"0"常量就是上下限，**防止输出超范围烧风扇**）→ 送给 `Fan Control Output`。

**用到的 DAQmx 函数**（指导书提示在「测量 I/O」→「DAQmx – 数据采集」里）：
| 函数 | 作用 |
|---|---|
| **DAQmx 创建虚拟通道** | 声明"我要用 myDAQ 的 ai0（AI电压）/ ao0（AO电压）" |
| **DAQmx 读取** | 从 AI 通道读一个采样值 |
| **DAQmx 写入** | 往 AO 通道写一个电压值 |
| **DAQmx 清除任务** | 程序结束时**释放硬件资源**（不做这一步，下次运行可能报"设备被占用"） |

> **和 DAQ 助手的区别**：DAQ 助手是"配置向导"，简单但不灵活；DAQmx 是"底层 API"，需要自己指定通道名、采样数、速率，但**可以在循环里随时读写单个点**——这正是实时闭环控制需要的。

## 3.7 运行步骤与**实验结果**

**指导书第 4~8 步：**

**第 4 步　运行**：点工具栏的**运行箭头** ▶ 运行 VI。

**第 5 步　校准 VTOL 的位置（关键！）**
- 在**手动模式**下（或断电状态下）**用手/手动预置调整 VTOL 设备臂**，直到**风扇位于水平位置**；
- **记录此时传感器读数**（看 `Sensor Reading` 数值框，比如是 **2.04 V**）。
> 这个读数的含义：**"水平"这个物理状态对应的传感器电压**。它是整套控制的"零点"。

**第 6 步　建立目标稳定工作点**
- 在 **`Target Sensor Reading`** 里输入刚才记录的读数（如 2.04 或截图里的 2.1）。
- 这就在系统里建立了**目标稳定工作点**。

**第 7 步　手动模式演示**
- 把 **Control Mode 设为 "Manual"**；
- **调整 `Manual Fan Power Control`** 让设备臂升降；
- **观察前面板波形图**：当 `Actual Reading`（实际读数）曲线与 `Set Point`（目标）曲线**重合**时，说明设备臂处于**水平位置**。
> 这里你会亲身体会到**开环控制的痛苦**：调到重合了，手一松（或气流一变），曲线又飘走了。

**第 8 步　PID 模式**
- 把 **Control Mode 切到 "PID"**（此时手动滑块失效）；
- **调整比例、积分、微分三个环节**，使电机稳定在目标稳定工作点。

### ✅ 你应该观察到的结果

| 阶段 | 波形图现象 | 表盘 |
|---|---|---|
| 程序刚运行，风扇未转 | `Actual Reading` 是某个静止值；`Set Point` 是你设的目标值，**两条线是分开的两条水平线** | Fan Control Output = 0 |
| 手动模式，慢慢加大功率 | 实际读数曲线**开始向目标曲线移动** | 表盘指针上升 |
| 手动模式，调到刚好重合 | 两条线**贴合**，臂水平 | 表盘停在某个值（约 3~5 V） |
| 手动模式，故意再加大一点 | 实际读数**越过**目标线（超调），臂抬过头 | 表盘继续升高 |
| 切到 PID 模式（参数合适） | 实际读数**快速上升、略微超调后回落，最终与目标线完全重合并稳定** ——★这是本实验最漂亮的结果★ | 表盘在某个值附近**微调抖动**，说明控制器在工作 |
| PID 参数 **P 太大** | 实际读数曲线**上下等幅振荡**（自激振荡） | 表盘指针剧烈来回摆 |
| PID 参数 **P 太小** | 实际读数**慢慢爬升但永远差一截**到不了目标（静差） | 表盘停在偏低的位置 |
| **只有 P 没有 I** | **稳态误差**：曲线稳定在目标下方一点，一直差那么一点 | — |
| 加上合适的 **I** | 静差被消除，曲线最终**精确贴合**目标 | — |
| **D 太大** | 曲线出现**高频抖动/毛刺**（D 放大了传感器噪声） | 表盘高频抖动 |

**验收标准（实验四做成功的标志）**：
1. PID 模式下，`Actual Reading` 与 `Set Point` 两条曲线**长时间重合**且**不振荡**；
2. 用手**轻轻拨一下设备臂**（加一个扰动），曲线偏离后能**自动回到**目标值——这叫**抗扰动能力**，是闭环控制的核心价值。

**报告里放这些截图**：① 前面板（标注各控件含义）；② 主程序框图；③ 手动分支和 PID 分支框图；④ **两组对比截图**：一组是 P 太大致振荡、一组是参数合适稳定 —— 这最能体现你理解了 PID。

## 3.8 坑与排错（实验四）

| 现象 | 原因 | 解决 |
|---|---|---|
| 传感器读数一直在 0 或不变 | AI 通道名写错；或 myDAQ 通道被别的程序占用 | 检查 DAQmx 创建虚拟通道里的 `myDAQ1/ai0` |
| 风扇完全不转 | AO 通道配置错；或 9 V 电源没开；或输出被限幅在 0 | 检查电源开关、通道名、限幅范围 |
| 刚开始能转，一会儿就报错 | **DAQmx 任务没清除**，资源没释放 | 确保程序末尾有 DAQmx 清除任务 |
| 风扇转但臂不动 / 抖动 | 平台不水平；或风扇离臂太远/太近 | 重新放平平台、检查机械结构 |
| PID 一直振荡压不住 | ① **P 太大**；② **I 太大导致积分饱和**；③ PID 输出限幅设置不当 | 先 P 减半试试；把 I 调小；检查输出限幅 0~10 |
| 切到 PID 后风扇一直满速 | 误差方向接反（SP 和 PV 接反了） | 检查 PID VI 的 setpoint / process variable 是否接对 |
| 曲线有高频毛刺 | **D 太大**，把传感器噪声放大了 | 减小 Kd，或先加个低通滤波 |
| 手动滑块在 PID 模式下没反应 | **这是正常的**，条件结构保证两个模式互锁 | — |

---

# 第 4 章　三个实验横向对比（一页看懂）

| | **实验二 音频均衡器** | **实验三 myQuake** | **实验四 myVTOL** |
|---|---|---|---|
| **一句话** | 把音乐分频段调音量 | 摇建筑模型测振动 | 用风扇把臂稳在水平 |
| **AI 用** | 无（用音频通道） | ai0, ai1 | ai0 |
| **AO 用** | 无（用音频通道） | ao0（电机） | ao0（风扇） |
| **DIO 用** | 无 | **port0（8 位设置字）** | 无 |
| **核心信号处理** | **带通滤波 + 加权求和 + 功率谱** | **低通滤波 + 峰值检测** | **PID 闭环反馈控制** |
| **频率特征** | 20 Hz ~ 10 kHz | < 10 Hz | 准静态（角度变化） |
| **关键参数** | 三个带通截止频率、320 采样 | 8 位设置字、10 Hz 低通、16~18% 起振点 | Kp / Ki / Kd、目标工作点 |
| **难点** | 通道别选错、采样数要一致 | 结构要夹紧、传感器朝向要一致、轴别选错 | PID 整定、方向别接反 |
| **成功标志** | 拉 Treble 频谱高频段抬起来 | 16~18% 时出现明显 P 波振动 | 两条曲线重合且能抗扰动 |
| **学到的核心概念** | 频域分析、滤波器 | 传感器标定、数字口配置 | **闭环控制、反馈** |

**一条主线**：三个实验其实是循序渐进地讲"**信号链**"——
**采集 → 处理 → 分析**（实验二、三）→ 再往前一步变成 **采集 → 处理 → 决策 → 回写执行器**（实验四闭环控制）。这就是虚拟仪器从"测量工具"变成"控制系统"的完整路径。

---

# 第 5 章　实验报告怎么写（照这个写不会扣分）

指导书对每个实验都要求："**描述该 VI 的功能，并在实验报告中加入前面板和程序框图的截图**"。建议统一用这个结构：

### 每个实验写 6 段

1. **概要**（3~5 行）
   实验目的 + 你做了什么 + 最终结论。例：
   > "本实验基于 NI myDAQ 与 LabVIEW 搭建了三段式音频均衡器。通过三个带通滤波器将音频分为低/中/高三段，分别用滑块加权后求和，再经总音量控制后由 AUDIO OUT 输出。实验结果表明，调节各频段滑块可显著改变输出的功率谱分布，验证了数字均衡器的原理。"

2. **实验原理**（画一张信号流图 + 2~3 个公式）
   - 实验二：写 `y(t) = V·[b·B(t) + m·M(t) + t·T(t)]` 和三个频段划分表；
   - 实验三：写设置字真值表 + "电压 ∝ 加速度"的标定关系；
   - 实验四：写 PID 公式 + 闭环框图。

3. **实验步骤**（按 Step 编号，附关键截图）
   每一步写"做了什么 + 为什么这么做"，别只抄指导书。

4. **实验结果**（**这部分最重要**）
   - 前面板截图（要能看清数值/波形）
   - 程序框图截图
   - **对比组**：实验二放"Bass 拉满前/后频谱对比"；实验三放"起振前/后波形对比"；实验四放"P 太大致振荡 vs 参数合适稳定对比"
   - 用**表格**列出关键读数

5. **结果分析 / 讨论**（体现你懂了）
   - 实验二：为什么拉 Bass 只影响低频段？为什么三段之间有缝隙？
   - 实验三：回答"Y 轴单位应该是什么"（答案见 2.7）；为什么起振需要 16~18%？为什么要 10 Hz 低通？
   - 实验四：P/I/D 三个参数各自调大调小分别导致什么现象？为什么闭环能抗扰动而开环不能？

6. **实验感想 + 遇到的问题及解决**
   写真实遇到的问题（比如"通道选错导致没声音"），比空泛的感想有价值得多。

---

# 附：开始动手前的最终 Checklist

**硬件**
- [ ] myDAQ USB 已插好，NI MAX「设备和接口」能看到设备且**自检通过**
- [ ] 需要的驱动都装了：**NI-DAQmx**（全部实验）、**NI ELVISmx**（实验三的"函数发生器"要用）
- [ ] 实验二：音频线接 **AUDIO IN**（不是 AI0），耳機接 **AUDIO OUT**
- [ ] 实验三：**12 V** 电源、电机→AO0、Accel A→AI0、Accel B→AI1、两传感器朝向一致、结构夹紧
- [ ] 实验四：**9 V** 电源（注意极性）、霍尔→AI0、风扇→AO0、平台水平

**软件**
- [ ] LabVIEW 能打开，**Ctrl+E** 能切换前面板/框图
- [ ] DAQ 助手里的**设备名**真的是你手上那块 myDAQ（可能是 Dev1 而不是 Dev2）
- [ ] 实验二两个 DAQ 助手的采样数**都是 320**
- [ ] 实验三函数发生器的 **Device** 改成实际 myDAQ 名
- [ ] 程序运行结束能正常按 Stop，DAQmx 任务有清除

---

**本次分析的中间产物**：指导书全文已提取到 `C:\Users\UserX\.zcode\workspace\default\lab_text.txt`，做题时可以直接搜关键词。

需要我把这份讲解整理成**可编辑的 Word / Markdown 文档**（方便你边做边打勾、直接往里贴截图），或者针对某一个实验展开某一部分（比如把实验四的 PID 整定做成一个"现象→原因→怎么调"的速查卡）吗？

## 👤 用户（2026-09-15 13:32）

我不理解这两个循环：
【2.1 加速度传感器的选择与量程设置部分】
   Axis(枚举) ──► 查表 ──► 位 ──┐
   Axis(枚举) ──► 查表 ──► 位 ──┼─► Build Array(8元素) ──► 布尔数组转数字 ──► DAQ Assistant(data)
                               │                                              （数字输出 port0）
                     常量: G=0, P7=1 ──┘

【2.2 信号采集部分】
   DAQ Assistant2 ──data──► [Filter 低通 10Hz] ──► 拆分 A/B ──┬─► 取波形Y分量 ─► 数组最大值 ─► Peak Reading A (V)
   （模拟输入 ai0 & ai1）                 信号→滤波后的信号    │
                                                             ├─► Waveform Chart（两路波形显示）
                                                             └─► 取波形Y分量 ─► 数组最大值 ─► Peak Reading B (V)
   前面板 "%Full Scale" 滑块 ──► NI ELVISmx Function Generator ──► 输出到 myDAQ AO0 ──► 偏心电机
   （Stop 按钮控制这个 While 循环）

<details><summary>💭 思考链（deepseek-flash）</summary>

The user is confused about the loops in 实验三. They quoted my block diagram descriptions and said "我不理解这两个循环" — actually they quoted 2.1, 2.2, and the motor control loop. So they listed three things but said "这两个循环". Probably they mean the first loop (which contains 2.1 and 2.2) vs the second loop (motor control).

Let me clarify carefully, as a total beginner. I should explain:
1. What a While loop is, and why there are two loops (not one).
2. The critical distinction: loop #1 runs at LabVIEW software speed (thousands of times/sec), loop #2 runs continuously driving the motor.
3. Why they're separate: because the motor needs a CONTINUOUS signal (the function generator must keep outputting), while the acquisition loop reads blocks of samples.
4. Actually — important technical point: in LabVIEW, two parallel While loops run independently, in parallel (multi-threaded). They don't wait for each other.
5. How data flows within each loop, step by step, in plain language.
6. Why the "handshake" via DAQ Assistant digital output: the 8-bit word only needs to be written once at the start, but since it's inside the loop it gets rewritten every iteration (harmless).

Let me also explain what "枚举" (enum) is, what happens concretely when you pick "Z" in the Axis dropdown.

Let me walk through a concrete example: Axis A = Z, Axis B = Y.

Accel A, Z轴: P0=1, P1=1, P2=G=0, P3..P6=/-随便, P7=1
Accel B, Y轴: P0..P3=/, P4=0, P5=1, P6=G=0, P7=1

So combined 8 bits: P0=1, P1=1, P2=0, P3=?, P4=0, P5=1, P6=0, P7=1

Hmm — wait. Both sensors share the SAME port0 (8 lines). Accel A uses P0-P2 (+P7), Accel B uses P4-P6 (+P7). P3 is don't care for both. So the 8-bit word configures BOTH sensors simultaneously with one write. That's the key insight! That's why it's ONE array of 8 elements, not two arrays.

That's a really important point for understanding. Let me make that clear.

So the "设置字" single byte:
- bits 0,1 = A 轴选择
- bit 2 = A 量程 G
- bit 3 = 无关
- bits 4,5 = B 轴选择
- bit 6 = B 量程 G
- bit 7 = 使能

Now "Build Array 8元素" — the array order. In LabVIEW, the boolean array to number: element [0] is the LSB. So array index 0 → P0, index 7 → P7. Yes: Boolean Array To Number treats index 0 as least significant bit.

So you build the array in order [P0, P1, P2, P3, P4, P5, P6, P7].

Then Boolean Array To Number → gives a U8 value 0-255, e.g. 1000 1011? Let's compute for A=Z, B=Y, G=0:
P0=1, P1=1, P2=0, P3=0, P4=0, P5=1, P6=0, P7=1
Binary (P7...P0) = 1 0 1 0 0 0 1 1 = 0xA3 = 163.

Good, I can give a concrete example. Let me double check: P7=1, P6=0, P5=1, P4=0, P3=0, P2=0, P1=1, P0=1 → 1010 0011 = 0xA3 = 163. Yes.

Now the "两个循环" explanation. Let me think about what the actual LabVIEW program structure is.

From the manual's 图2 (数据连续采样循环) — that's ONE While loop containing BOTH the 2.1 (setting word → DAQ Assistant digital) and 2.2 (DAQ Assistant2 analog in → filter → peak). 

And 图3 电机控制程序框图 — a SEPARATE While loop with the Function Generator.

Wait, let me re-look. In 图2, the DAQ Assistant (digital out) is inside the loop too? Looking at the crop image: there's a big rectangle border (the While loop) that encloses DAQ Assistant2, Filter, the peaks, the Waveform Chart, AND the DAQ Assistant (digital) at top. Actually the crop shows the While loop border on the left going down. The "appended array → DAQ Assistant" part is at the top, and the loop border... hmm.

Looking at the crop image again: there's a horizontal line at the bottom (loop border) and the left border. The DAQ Assistant (digital out, top right) appears to be INSIDE the loop frame — the description says "图2 程序框图中的第一个循环，其作用是...ACCELERATOR". Hmm.

The manual says: "图2 是程序框图中的第一个循环，其作用是从X、Y或者Z轴中设定选择需要进行测试的轴。DAQ助手VI会采集并在波形图中显示测量到的数据。"

So 图2 = 第一个循环 = contains BOTH the axis setting AND the acquisition. So 2.1 and 2.2 are both inside 循环①.

And 图5/图3(电机控制) = 第二个循环.

Hmm, but wait — the manual labels the motor control figure as "图5 是程序框图中的第二个循环" but the caption in the doc says "图3 电机控制程序框图". There's a numbering inconsistency in the manual itself (they call it 图5 in text, 图3 in caption). I should mention that.

Actually I already noticed: text says 图5, caption says 图3. Let me mention briefly.

Now: are the two loops INSIDE one file, running in parallel? Yes — two separate While loops placed side by side on the same block diagram, they run concurrently.

Key beginner insight: **两个 While 循环是"并行"运行的，不是"先后"执行**。LabVIEW 是多线程的，两个循环各自独立地一圈一圈转。

Now, WHY two loops instead of one?

1. **速度需求不同**：采集循环要"读一块→算→显示"，每圈几十毫秒；电机控制需要"持续输出波形"，函数发生器要一直运行。
2. **逻辑独立**：两个循环各有一个 Stop 按钮，可以单独停。
3. **互不阻塞**：如果放一个循环里，函数发生器每圈重新配置/重启会出问题。

Hmm, actually let me think about what's technically true. The NI ELVISmx Function Generator Express VI: when placed in a While loop, it (re)starts the function generation each iteration. Actually the ELVISmx Function Generator VI with "stop" — hmm.

Actually the typical usage: put the Function Generator in a While loop; each iteration it outputs the waveform continuously. Hmm, actually the ELVISmx Function Generator VI is designed to run continuously until stopped — it has its own stop terminal (stop (F) 2 shown in the diagram).

Looking at the motor control diagram (图3 电机控制程序框图): there's a box with stop(F) 2 (a "仿真信号/停止" express?), %Full Scale → NI ELVISmx Function Generator → output to while loop condition (the green stop branching to the loop's condition terminal).

So the VI keeps generating until stopped. It's in its own While loop so it can run independently.

Let me write the explanation focusing on:

**A. 两个循环分别是什么、为什么要分开**
**B. 循环①内部：上半部分（2.1）和下半部分（2.2）其实不是两个循环，是同一个循环里的两条并行数据流**  ← THIS IS THE KEY MISUNDERSTANDING. The user says "这两个循环" referring to 2.1 and 2.2 — but 2.1 and 2.2 are NOT two loops! They're two parts of ONE loop. That's likely their confusion.

Yes! Looking at the user's message: they quoted 【2.1 加速度传感器的选择与量程设置部分】 and 【2.2 信号采集部分】 and the motor part. They said "这两个循环" — probably meaning 循环① (含2.1和2.2) and 循环② (电机).

Either way, I should clarify BOTH:
- 2.1 和 2.2 是同一个循环（第一个循环）里的两条并行支路
- 第一个循环 和 第二个循环（电机）是两个真正独立的循环

That fully resolves the confusion.

Let me also explain "顺序" — in the first loop, 2.1 runs "first" in the sense that at the first iteration the digital write happens; but actually they're parallel dataflow. Important nuance: the 8-bit word must be written BEFORE (or at least at the same time as) reading, because it configures the sensor hardware. In practice, since the loop iterates many times per second, it gets re-written every iteration — so it's effectively "always configured". But strictly, on the very first iteration, there could be a race; in practice it works because the write is fast.

Hmm, actually, does DAQ Assistant write on every iteration? Yes — DAQ Assistant inside a While loop writes its data input on every iteration.

Let me also explain: why write it repeatedly instead of once? Because the user can CHANGE the axis selection while the program is running — the front panel dropdown changes → next iteration writes the new word → sensor switches axis live. That's elegant and is WHY it's inside the loop.

Great insight to include.

Now let me also carefully explain what "枚举" is and the "查表" step. Actually, looking at the block diagram, the "查表" is done via: Axis enum (U16) → 索引数组 (index array) into a constant array → 选择(Select)/布尔到数字. Or more simply: the enum value (0,1,2) is used to index into a pre-built array.

Honestly, a simpler way a student would build it: use a "Case Structure" or just "索引数组" into a 2D boolean array. The diagram shows: Axis(U16) → [索引数组图标] → [布尔选择器 with 真/假] with a blue "2" constant → produces bits.

Hmm, the blue "2" is likely a constant feeding "Build Array" (2 elements) or a numeric constant for the select. 

I'll explain it generically: 把 Axis 枚举的值（0/1/2）当索引，从一张"查找表"里取出对应的 2 位布尔值。Then note that the actual mechanism in the program might be 索引数组/选择结构, but the essential logic is the lookup.

Actually, let me reconsider — maybe I should describe a concrete simple implementation and note the figure's implementation. Since the manual is what it is, I'll explain the principle and mention what the figure does.

Let me look at the crop image once more mentally: 
- "Axis [U16]" blue enum → wire → a small yellow box with a grid icon (索引数组? no, 索引数组 icon is a box with an arrow pointing down/right)
- then → a yellow box with a sine/step shape (选择 Select? or 布尔值至(0,1)?)
- with a blue "2" constant below it

Hmm, "选择" (Select) function takes t/f/selector → output. The icon for Select is a box with a "?" shape. The icon shown has a wavy line — that's the "选择" (Select) icon? Actually LabVIEW's Select icon is a rectangle with a vertical divider and a "?"... 

Alternatively the wavy line icon = "布尔数组至数字" no.

Hmm. I think it's: 索引数组 (Index Array) → with a "2" constant... no, Index Array takes an array + index.

Maybe: Axis enum → 索引数组 (index into a 3-element array of U8 codes) → 数值 → then 拆分成布尔。

You know what, I'll describe it functionally and say "图里用的是『索引数组/选择』这类小函数，具体是哪种不重要，本质就是查表"，and give the student a clean way to build it themselves. That's genuinely more useful for a beginner.

Let me now also address: "为什么要用数组传，而不是直接传数字？" — Because DAQ Assistant 数字输出 port0 expects either a boolean array (one bool per line, 8 lines = 8 elements) or a number. The manual says "将其从布尔型转换成数据型式传入" — so they convert to number. Actually DAQ Assistant for digital port output accepts a boolean array OR a number. The manual's flow: bool array → number → DAQ Assistant "数据". 

Hmm, actually the manual says "将设定的8位设置字放入数组中，再将其从布尔型转换成数据型式传入myDAQ助手中". So: bool array → number. But in the diagram, after "appended array" (bool array) there's a "布尔数组至数字" → then → DAQ Assistant data. Yes.

Wait, but actually looking at the crop, after the 8-element array there's a small box then an arrow into DAQ Assistant. The small box = 布尔数组至数字. OK consistent.

Why convert to number? Because DAQ Assistant's digital port write takes a number (or bool array). Either works; the manual chose number. Fine — I'll just explain both are OK and the essence is the same 8 bits.

Now let me also explain the "拆分 A/B" and "取波形Y分量" chain more concretely, since the user quoted it.

And explain Waveform Chart vs Waveform Graph (图表 vs 图): 
- Waveform Chart = 图表, 逐点追加，保留历史，像"纸带记录仪"
- Waveform Graph = 图, 每次刷新整幅

In 实验二 they use 波形图 (Graph) for the spectrum; in 实验三 they use 波形图表 (Chart) for the time waveform. The manual's Chinese is loose. Let me mention it briefly since it's a common beginner confusion. Actually 实验三 图1 shows "Waveform Chart" in the diagram, and the front panel shows a chart.

Hmm, the manual for exp2 Step9 says "前面板中创建一个波形图" and the block diagram says "Waveform Graph". For exp3 the diagram says "Waveform Chart". OK, so exp2 = Graph, exp3 = Chart. Good, consistent with their function (频谱是一次算一整幅 vs 时域波形是滚动追加).

Let me write this all up now.

Structure:
1. 先纠正一个关键误解：这不是"两个循环"，是"第一个循环里两条并行支路" + "第二个循环"
2. 全局图（三个东西的位置）
3. 讲清 While 循环是什么 + LabVIEW 并行执行
4. 第一个循环逐段拆解
   4.1 上半支路（2.1）：为什么要一个字节、8位怎么分工、具体例子、为什么放在循环里
   4.2 下半支路（2.2）：数据怎么一路变成峰值和波形
   4.3 两条支路的关系：并行，不是串行；但有一个隐含的"配置在前"的因果关系
5. 第二个循环：电机控制，为什么必须独立成一个循环
6. 为什么不能合成一个循环（对比表）
7. 一句话总结 + 常见误解 Q&A

Let me use a concrete example (A=Z, B=Y) to compute the byte.

Also I should double check: is it P0 lowest bit? Boolean Array To Number: index 0 = LSB. And the array built is [P0,P1,...,P7]. So yes.

Let me write out the byte table clearly.

Example 1: A=Z, B=Y, G=0
A: P0=1,P1=1,P2=0
B: P4=0,P5=1,P6=0
P3 = 无关 → 程序中可以填 0（假）
P7 = 1
数组 = [1,1,0,0,0,1,0,1]  (index0..7)
数值 = 1*1 + 1*2 + 0*4 + 0*8 + 0*16 + 1*32 + 0*64 + 1*128 = 1+2+32+128 = 163 = 0xA3 ✓

Example 2: A=X, B=X, G=0
A X: P0=1,P1=0,P2=0
B X: P4=1,P5=0,P6=0
P3=0, P7=1
数组 = [1,0,0,0,1,0,0,1] → 1 + 16 + 128 = 145 = 0x91

Good.

Example 3: A=X, B=X, G=1 (±6g)
P2=1, P6=1 → 数组=[1,0,1,0,1,0,1,1] → 1+4+16+64+128 = 213 = 0xD5

Good.

Let me include a small table of examples.

Now writing. Should be thorough but focused on the confusion. Not as long as the previous answer, but detailed.

I should also address the user's literal quote which mixed all three parts — so I'll explicitly say: 你贴的三段其实是"两个循环"，其中 2.1 和 2.2 不是两个循环。

Let me write it.

One more thing to verify — is the digital DAQ Assistant really inside the first While loop? Let me reconsider the crop image. In crop_p15_fig2.png: I see a horizontal green dotted line at the top going from "stop (F)" across to the right and down — that's the loop's boolean wire. The While loop border: there's a visible rectangle. The DAQ Assistant (digital) at top-right is at roughly the same height as the "appended array" label. And the loop's top border... 

Actually in the crop, I see the loop border as a thin line. The bottom shows the loop border with the "1" iteration terminal (the small box with "1" and an icon at bottom left) and the "i" terminal. The left border runs down the left side. Looking at the image, the loop frame's top edge is not clearly visible in the crop, but the manual text says "图2 是程序框图中的第一个循环，其作用是从X、Y或者Z轴中设定选择需要进行测试的轴。DAQ助手VI会采集并在波形图中显示测量到的数据。" — so both are in the first loop.

Hmm, actually re-reading: "图2是程序框图中的第一个循环，其作用是从X、Y或者Z轴中设定选择需要进行测试的轴" — the loop's purpose includes the axis setting. So yes, 2.1 is inside.

I'm confident. Let me write.

Also the iteration terminal "i" appears at bottom left of the loop — in the crop there's a "1" box with a small icon which is likely the "i" iteration terminal wired to something, or a constant 1.

OK writing now.

Let me also add a "怎么自己搭" mini-guide since they'll need to build it.

I'll keep TodoWrite out — this is a single explanation task, not multi-step work. Actually the reminder suggests using it; but for a pure explanation reply it's not applicable. Skip.

</details>

### 🤖 助手（deepseek-flash，2026-09-15 13:32）

先纠正一个**最关键的误解**——你贴的这三大段，其实**不是两个循环，是「一个循环里的两条并行支路」＋「另一个循环」**：

```
┌──────────────────────────── 第一个 While 循环 ────────────────────────────┐
│                                                                            │
│  支路 ①（你写的 2.1）  传感器配置：Axis下拉 → 8位设置字 → DAQ助手(数字出port0) │
│                                                                            │
│  支路 ②（你写的 2.2）  信号采集：DAQ助手2(AI) → 低通滤波 → 拆分 → 峰值/波形   │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────── 第二个 While 循环 ────────────────────────────┐
│  %Full Scale 滑块 → 函数发生器 → AO0 → 偏心电机                            │
└────────────────────────────────────────────────────────────────────────────┘
```

**2.1 和 2.2 共享同一个循环框**（指导书原话："图 2 是程序框图中的**第一个循环**"）。它们上下摞在一起，但**不是先后执行**，而是**同时进行**。下面把它彻底讲透。

---

# 一、先搞懂三个前置概念

## 1. 什么是"While 循环框"

LabVIEW 里画一个矩形框，左下角有个 `i`（循环计数），右下角有个**条件接线端**——这就是 While 循环。

```
   ┌─────────────────────────────┐
   │  框里所有东西，一遍一遍地跑    │
 i │                             │  ⟳ 条件为"继续"→ 再跑一圈
   │                             │
   └─────────────────────────────┘
                ▲
                └── 接到 Stop 按钮：按一下 → 条件变"停" → 退出循环
```

**关键**：框**外面**的东西只执行一次；框**里面**的东西**每一圈都执行一次**，直到你按 Stop。

## 2. LabVIEW 是"并行"的，不是"从上到下"的

这是和 C/Python 最不一样的地方。框里两条**没有互相连线**的支路，**同时跑**，谁也不等谁。

```
   ┌──────────────────────────────┐
   │  支路①  ───────────────────►  │   ← 两条同时转
   │  支路②  ───────────────────►  │
   └──────────────────────────────┘
```

所以在你问的这个程序里：**"配置传感器"和"采集信号"是同时进行的**，不是"先配好再采集"。

## 3. DAQ 助手被"放进循环里"意味着什么

一个 DAQ 助手每被循环执行一次，就**真的跟硬件通信一次**：

| DAQ 助手 | 放在循环里 = 每一圈都做 |
|---|---|
| DAQ 助手（数字输出 port0） | 把 8 位数据**重新写一遍**到 DIO 口 |
| DAQ 助手 2（模拟输入 ai0/ai1） | **从卡里读一块新数据**（默认每路一点） |
| 函数发生器（第二个循环） | **持续产生波形**送到 AO0 |

> 💡 这就解释了为什么配置字要放在循环里：**这样你在程序运行中随时改前面板的 Axis 下拉框，下一圈就会写入新设置字，传感器立刻换轴**。如果放循环外面，就只有启动那一刻配置一次，中途改下拉框没反应。

---

# 二、第一个循环 · 支路①：8 位"设置字"到底在干什么

## 2.1 为什么是"1 个字节配 2 个传感器"

这是最容易卡住的地方。myDAQ 的 **DIO port0 有 8 根线，一次必须一起写**。而板上有 **A、B 两个加速度计**要配置，所以：

> **这 8 根线被"分赃"了：低 4 位管 A，高 4 位管 B，最高位 P7 是共用使能。**

```
   位号:   P7   P6   P5   P4 │ P3   P2   P1   P0
           │    └────┬────┘  │  │    └───┬───┘
           │         │       │  │        │
           │     给 B 用     │  │    给 A 用
           │  (量程+轴选择)   │  │  (轴选择+量程)
           │                 │  │
       总使能=1          废弃位   P2/P6 = 量程 G
       （A、B 共用）
```

对照指导书的表：

| 位 | 管谁 | 含义 |
|---|---|---|
| **P0, P1** | **A 传感器** | 轴选择：`10`=X，`01`=Y，`11`=Z |
| **P2** | **A 传感器** | 量程 G：0 → ±1.5 g，1 → ±6 g |
| **P3** | — | 无关位（表里写 `/`），程序里随便填 0 |
| **P4, P5** | **B 传感器** | 轴选择：`10`=X，`01`=Y，`11`=Z |
| **P6** | **B 传感器** | 量程 G：0 → ±1.5 g，1 → ±6 g |
| **P7** | **两个都要** | 使能位，**必须 = 1**，否则传感器不工作 |

**所以"8 位设置字"就是把"我想让 A 测 Z、B 测 Y、都用 ±1.5g"这一句话，翻译成 8 个 0/1**，一次写下去，两个传感器同时被配置好。

## 2.2 走一遍完整流程（具体数字）

假设你在前面板选了：**Accel A = Z 轴，Accel B = Y 轴**，量程程序里固定 G=0。

**第一步：查表，得到两个传感器的位**

- A 测 **Z**：P0=1，P1=1，P2=0(G)
- B 测 **Y**：P4=0，P5=1，P6=0(G)
- 补上：P3=0（无关，填0），P7=1（使能）

**第二步：拼成 8 元素布尔数组**（这就是框图上那个 `Build Array`，标签写着 `appended array`）

> ⚠️ **顺序很重要**：数组的**第 0 个元素对应 P0**（最低位），第 7 个元素对应 P7（最高位）。

```
数组下标:  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]
对应的位:  P0   P1   P2   P3   P4   P5   P6   P7
布尔值:    1    1    0    0    0    1    0    1
```

**第三步：布尔数组 → 数字**（`Boolean Array To Number`）

按"下标 i 的权值是 2^i"加起来：

$$1\cdot2^0 + 1\cdot2^1 + 0\cdot2^2 + 0\cdot2^3 + 0\cdot2^4 + 1\cdot2^5 + 0\cdot2^6 + 1\cdot2^7$$
$$= 1 + 2 + 32 + 128 = \mathbf{163} = \text{0xA3}$$

**第四步：把这个 163 交给 DAQ 助手（数字输出 port0）的"数据"端口**

myDAQ 把 163 展开成二进制 `1010 0011`，依次送到 DIO7~DIO0：

```
DIO7=1  DIO6=0  DIO5=1  DIO4=0  DIO3=0  DIO2=0  DIO1=1  DIO0=1
 ↑       ↑                                            ↑        ↑
使能    B量程                                      A轴高    A轴低
        B轴=01(Y)                                  → A测Z
```

**传感器硬件立刻按新配置工作。**

## 2.3 再给两个例子对照

| 你的选择 | 数组 `[P0..P7]` | 十进制 | 十六进制 |
|---|---|---|---|
| A=Z, B=Y, G=0 | `1,1,0,0,0,1,0,1` | **163** | 0xA3 |
| A=X, B=X, G=0 | `1,0,0,0,1,0,0,1` | **145** | 0x91 |
| A=X, B=X, **G=1**(±6g) | `1,0,1,0,1,0,1,1` | **213** | 0xD5 |

你可以自己在前面板把下拉框换成 X/Y/Z，观察**数组和数字的变化** —— 这是理解这张表最快的方法。（在框图里把这根线右键 → 探针，就能看到实时的值。）

## 2.4 为什么不用两个 DAQ 助手分别配 A 和 B

因为 **port0 是一个整体，8 根线必须一次性写入**。你没法"只写 P0~P2"。所以只能是：**在软件里把 8 位全算好 → 一次性写下去**。这就是"设置字"这个概念存在的原因。

> 顺带回答"为什么要转成数字"：DAQ 助手的数字口输出其实**布尔数组和数字都接受**。指导书选了"转成数字"这条路，是因为一个 0~255 的数字更紧凑、也方便你在探针里看。**本质没变，还是那 8 个 0/1。**

---

# 三、第一个循环 · 支路②：从电压到峰值，一路怎么走

这条支路是一条**瀑布式的流水线**，数据一层层往下流：

```
【第1层 采集】
DAQ 助手2（模拟输入 ai0 和 ai1）
   └─► 输出 "data"：一个"动态数据"，里面装着 2 路波形（A 和 B）
       —— 每一圈循环读一次新数据
              │
              ▼
【第2层 滤波】
Filter（低通，截止 10 Hz）
   ├─ 输入端口 "信号" ◄── 接上面来的 data
   └─ 输出端口 "滤波后的信号" → 干净的两路波形
       —— 滤掉 50Hz 工频、电机电磁噪声、传感器本底噪声
              │
              ▼
【第3层 拆分】
把"两路波形"拆成"A 一路、B 一路"，同时还要"显示波形"
       ┌──────────────┴──────────────┐
       ▼                              ▼
   A 路波形                       B 路波形
       │                              │
       │        ┌──► Waveform Chart（波形图表）◄──┐
       │        │   把两路波形都送进去画出来      │
       │        │   这就是前面板那个大图          │
       ▼        │                               ▼
【第4层 取幅值】
   取波形 Y 分量              取波形 Y 分量
   （把波形对象里的"幅值数组"抽出来，
     丢掉时间信息，只留一串电压数字）
       │                              │
       ▼                              ▼
【第5层 取峰值】
   数组最大值                数组最大值
   （从这一串电压里挑出最大的那个）
       │                              │
       ▼                              ▼
   Peak Reading A (V)        Peak Reading B (V)
   （前面板上的两个数值框）
```

## 关键点解释

**① 为什么要"取波形 Y 分量"？**
DAQ 助手吐出来的不是"一串数字"，而是一个**波形对象**（里面包含：采样起始时间 t0、采样间隔 dt、幅值数组 Y）。你想做数学运算，必须先**把 Y 数组抽出来**。

**② 为什么要"数组最大值"？**
因为这圈采到的一整块数据里，你要的是**最大的那个加速度**——也就是"这次振动晃得最厉害有多大"。这就是"**峰值检测**"。它和"波形图"是**两个不同的用途**：

| 输出 | 用途 |
|---|---|
| Waveform Chart（波形） | 看**过程**：波形长什么样、有没有周期性、A 和 B 谁大 |
| Peak Reading（峰值） | 看**数值**：这一瞬间晃动的最大值是多少 V，方便记录到实验报告里 |

**③ Chart 和 Graph 的区别**（顺带解决一个常见困惑）
- **Waveform Chart（波形图表）**：**滚动追加**，新数据接在旧数据后面，像纸带记录仪 —— 实验三用它画**时域波形**；
- **Waveform Graph（波形图）**：每次**整体刷新**，画一整幅 —— 实验二用它画**频谱**。

## 和支路①的关系：并行，但有一个隐含的因果

两条支路在框图上**没有连线，同时运行**。但有一个**隐藏的先后逻辑**：

> **必须先把设置字写下去，传感器才知道该输出什么轴的信号。如果配置字没写或写错了，支路②采回来的就是无效数据。**

程序是怎么保证的？靠自己"跑得够快"：循环每秒转几十圈，配置字**每圈都重写一遍**，所以最多第一圈的头几毫秒没配好，你根本察觉不到。

**这也是为什么指导书把这两条支路放进同一个循环**——它们共享同一个"每一圈"的节奏，配置和采集同步刷新。

---

# 四、第二个循环：为什么电机必须单独一个循环

```
   ┌──────────────── 第二个 While 循环 ────────────────┐
   │                                                    │
   │  %Full Scale 滑块(0~100) ──► NI ELVISmx           │
   │                              Function Generator ──┼──► AO0 ──► 偏心电机
   │                                    │               │
   │                              stop(F) 2  ───────────┼──► 循环条件
   └────────────────────────────────────────────────────┘
```

## 为什么不能塞进第一个循环？

| 需求 | 采集支路 | 电机控制 |
|---|---|---|
| **每圈要做什么** | 读一块数据、算峰值、刷新图表 | 持续输出波形驱动电机 |
| **节奏** | 跟着采样率走，一圈几毫秒 | 函数发生器**自己**要持续跑 |
| **谁控制停止** | Stop 按钮 | 另一个 stop(F) 2 |
| **改轴/改量程时** | 要重新配置 | 不该受影响 |

如果硬塞进一个循环：
- 电机转速会**跟着采集节奏一卡一卡**（每圈重新启动一次函数发生器，波形不连续）；
- 你按 Stop 停下来看数据，**电机也停了**（后面没法同时观察）；
- 改 Axis 下拉框时会**顺带打断电机波形**。

**分成两个循环后**：电机稳定地一直转，采集稳定地一直采，互不干扰。你需要"电机转着、同时看波形"，这正是这个实验的核心场景。

> ⚠️ 指导书自己有个小笔误：正文里把电机那部分叫"**图 5**"，但图下面的标题写的是"**图 3 电机控制程序框图**"。指的是同一张图，别被编号绕晕。
>
> ⚠️ 还有一点：两个循环**各有一个停止条件**，但程序里通常把它们接在**同一个 Stop 按钮**上——你按一次，两个循环同时退出。虽然图里显示成 `Stop` 和 `stop(F) 2` 两个接线端，其实是同一根线分出来的。

---

# 五、一张图看懂"为什么是 2 个循环、3 条支路"

```
                        ┌──────────── Stop 按钮 ────────────┐
                        │                                   │
        ┌───────────────▼─────────── 循环① ────────────────┐│
        │                                                   ││
        │  【支路 A】配置                                     ││
        │   AxisA下拉 ─┐                                     ││
        │              ├─► 查表 ─► 8位数组 ─► 转数字 ─► DAQ助手1 ││
        │   AxisB下拉 ─┘        ▲                     (数字出) ││
        │                   G=0, P7=1 常量                    ││
        │                                                     ││
        │  【支路 B】采集（与支路 A 并行，不连线）              ││
        │   DAQ助手2(AI ai0/ai1) ─► 低通10Hz ─► 拆分 ─┬─► 取Y ─► 最大值 ─► Peak A││
        │                                            ├─► 波形图表           ││
        │                                            └─► 取Y ─► 最大值 ─► Peak B││
        └─────────────────────────────────────────────────────┘│
                                                               │
        ┌────────────────────── 循环② ────────────────────────┐│
        │  %Full Scale ─► 函数发生器 ─► AO0 ─► 电机            ││
        └──────────────────────────────────────────────────────┘
```

**记忆口诀**：
> **循环① = 一条配置线 + 一条采集线，并行跑（互不连线是正常的，不是没画完）。**
> **循环② = 电机线，独立跑（因为电机要一直转，不能被采集节奏打断）。**

---

# 六、常见误解速查

| 你的疑问 | 答案 |
|---|---|
| 2.1 和 2.2 之间为什么没有连线？是不是少画了？ | **正常**。它们通过硬件（myDAQ + myQuake 板）间接耦合，软件上不需要连线。 |
| 配置和采集谁先谁后？ | 软件上同时；逻辑上配置必须在采集之前生效，靠"每圈都重写配置字"来保证。 |
| 为什么配置字要放循环里面，放外面不行吗？ | 放外面只有启动时配一次，**运行中改 Axis 下拉框就不生效**了。放里面才能实时切换轴向。 |
| 为什么两个传感器要挤在一个字节里？ | 因为 **port0 是 8 根线一个整体，必须一次全写**，必须把 A、B 的配置合起来算。 |
| 8 位里哪几位是"无关"的？ | **P3**（表里写 `/`）。填 0 即可，程序里通常直接接一个"假"常量。 |
| "布尔数组转数字"为什么下标 0 是 P0？ | LabVIEW 的 `Boolean Array To Number` 把**下标 0 当最低位**（2⁰），和 P0 对应，正好吻合。 |
| 电机为什么单独一个循环？ | 电机要**持续输出波形**；放进采集循环会跟着采集节奏一卡一卡，且按 Stop 会一起停。 |
| 两个循环怎么一起停？ | 同一个 Stop 按钮分两路接过去，按一次两边都退出。 |

---

**最有效的验证方法**：把程序跑起来，用**探针**（在框图的连线上右键 → 探针）挂在"布尔数组"和"转数字"的输出上，然后在前面板把 Axis 在 X/Y/Z 之间来回换，你会看到数组和数字**实时变化**。对照上面 2.3 那张例子表，5 分钟就能把这张 8 位表彻底吃透。

要不要我按这个逻辑，把**实验四那两个分支（手动/PID 的条件结构）**也用同样方式拆一遍？那是另一个容易卡住的点。
