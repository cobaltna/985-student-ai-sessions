# 子代理会话 sess_subagent_agent_a2964d03-9260-40f9-879a-ee46a4875fbc

模型: GLM-5.3-Flash

## 👤 用户（2026-10-03 18:11）

你是一名嵌入式课程助教，为《轮式机器人创新实验指导书》（STC12C5A60S2 单片机四驱小车，Keil C51 开发）撰写配套"小白详解"文档的【第一章：全书导读与预备篇】，覆盖指导书的：课程信息与目录结构、第一章 实验概述、第二章 基础理论知识、第三章 实验设备与环境搭建、预备实验（硬件认识+Keil+烧录+串口调试）。读者是零基础本科生，目标是读完本章就清楚"这门课玩什么、需要什么、怎么把环境跑起来"。

必读材料（先全部读完再动笔）：
1. C:\Users\UserX\.zcode\workspace\default\robot-guide\guide_extract.txt 的第 1–217 行（你的全部范围）。
2. C:\Users\UserX\.zcode\workspace\default\robot-guide\code_text\batch1.md（img_001–img_028 的转录：BST-4WD 扩展板接口标注图、扩展板模块连线图、单片机应用系统框图、小车照片、扩展板使用说明（充电座 8.4V-12.6V、L3 电源灯/L1 低电压灯、MVCC->5V 跳线、51/Arduino 烧录开关、舵机接口 J1 接线、Arduino 跳线区 51 版不用）、Keil 各步骤界面描述、STC-ISP 界面描述、设备管理器/串口助手界面描述）。

本章结构（编号连续、顺序固定）：
1. 这本指导书怎么用（课程性质 32 学时/综合性设计性实验、适用专业、全书 11 个实验的结构地图：基础实验一~五练什么、创新实验六~十一练什么、最后报告与验收怎么考；建议的打开方式——每章对照指导书原文+本文详解）
2. 你需要准备的东西（硬件清单表：STC12C5A60S2 主控、TB6612FNG 驱动、12V 直流减速电机×4、11.1V 2200mAh 锂电、HC-SR04 超声波、TCRT5000×4 巡线、E18-D80NK×2 红外避障、光敏电阻×2、SG90 舵机、RGB 探照灯模块、按键；软件清单：Keil uVision（C51）、STC-ISP 串口烧录软件、CH340 驱动、串口调试助手；每样一句话说明是干什么的）
3. 读懂小车：整机结构（底盘/4 轮/扩展板/51 核心板/电池盒；扩展板把单片机的引脚引到哪里：IN1~IN8 传感器口、电机驱动口、舵机口 J1、RGB 灯口 J24、超声波口、串口/ISP 口；img_001/img_002/img_008 的接口说明整理成表；供电与开关：电源开关、L3 供电指示灯、L1 低电压指示灯、DC 充电 8.4V-12.6V、MVCC->5V 跳线出厂默认）
4. 第二章理论基础逐条讲透（这是本章重头，全部要给推导与例子）：
   4.1 差动驱动：左右轮速差怎么变成转向；v=(vR+vL)/2、ω=(vR−vL)/L 两式的来历（用两轮各自走过的弧长推一遍，举 L=15cm、vR=0.2m/s、vL=0.1m/s 的数字例——L 若材料未给，注明"指导书未给轴距，此处假设 15cm 仅为算例"）；对照小车的 run/left/right/spin_left/spin_right 六个函数（预告实验三）
   4.2 PWM 调速：占空比定义、平均电压=电源电压×占空比、为什么频率要 10–20kHz（指导书原话）以及本套代码实际用 50Hz 软件 PWM 的现实（低频会有轻微抖动噪声，属正常——此句若属推断请标注）
   4.3 PID：P/I/D 三项各自的作用与调参口诀（用小车巡线/直行的场景各举一个"P 大了会怎样、I 大了会怎样"的例子；说明本课程代码是开关式控制而非 PID，PID 是进阶方向）
   4.4 传感器：红外反射式（避障/巡线/跟随三个实验都靠它，讲发射-反射-接收与黑白吸收差异、阈值电位器）、超声波测距公式（距离=声速×时间/2，为什么除 2；2–400cm 量程）
5. 第三章设备与环境搭建的补充解读（组装顺序、接线前断电的为什么、CH340 驱动安装与设备管理器验证、"usb-serial ch340"字样）
6. 预备实验手把手（对应 img_003–img_027）：认识系统组成（硬件=单片机+接口电路外设、软件两层框图）→ 接线（ISP 口、串口、电池）→ Keil 建工程全流程（新建文件夹、STC12C5A60S2.H 拷到 C51\INC、New Project、选 Atmel AT89S52 的原因——STC12 与 51 兼容但 Keil 库里用 AT89S52 通用头、New .c 文件、Add Files、Options→Output→Create HEX、Build 看 0 Error）→ STC-ISP 烧录全流程（看芯片丝印、选 STC89C52/STC12 系列、COM 口、打开 .hex、先点"下载/编程"再开电源开关的时序、RX/TX 不得占用）→ 串口调试助手（选 COM、波特率、Reset 按钮重跑）→ 实验收尾断电
7. 本章小结与衔接（下一章进入实验一）

必须融入的"指导书注意"（原文笔误/不一致，语气平实）：
- 指导书 3.2.1 说安装 Keil uVision IDE，预备实验又说 Keil uVision2 IDE，界面截图是 µVision2/µVision3 混用——版本不影响操作流程。
- 烧录软件标题为 stc-isp-15xx-v6.85；指导书以选"STC89C52"为例，并注明小车上实际芯片是 STC12C5A60S2——两款都要能在列表里找到，选型以板上丝印为准。
- 指导书第二章说"PWM 频率一般 10kHz-20kHz"，而本书全部实验代码是 50Hz 软件 PWM（20ms 周期），这是教学简化，不要当成矛盾讲错方向。
- 表 3-1 中电机标 12V、电池 11.1V：工作电压以电池实际供电为准。

语言红线（违反即返工）：
- 平实、准确、克制；不过度口语化、无翻译腔。
- 禁止 emoji；禁止"让我们""接下来""总的来说""综上""希望对您有帮助"式空话；禁止空洞排比与每段强行总结。
- 每句有信息量；术语首次出现给定义；中文标点。
- 全部数字/型号/界面元素必须来自材料，禁止编造；材料没有的写"指导书未给出"；确需补充的常识性假设必须显式标注"（补充说明）"或"（算例假设）"。
- 表格只用于枚举型事实，过程性内容用段落；代码块 ```c。

输出：写入 C:\Users\UserX\.zcode\workspace\default\robot-guide\sections\01_导读与预备篇.md（UTF-8）。Markdown 层级：章 `#`、节 `##`、小节 `###`。
篇幅预期：600–900 行，宁细勿略，每句有内容，不灌水。预备实验的思考题答案由另一章负责，本章不要展开，只提示"参考答案见实验一章前"。
完成后回复：输出文件路径、总行数、融入几处"指导书注意"。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Let me start by reading the required materials. I need to read:
1. C:\Users\UserX\.zcode\workspace\default\robot-guide\guide_extract.txt lines 1-217
2. C:\Users\UserX\.zcode\workspace\default\robot-guide\code_text\batch1.md

Let me read both files first.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\robot-guide\\guide_extract.txt", "limit": 217}` → `1 [P] 轮式机器人创新实验指导书 2 [TBL 1] 3 | 课程类型：创新实践实验 适用专业：工学院各个专业（农业机械化及其自动化、农业工程、车辆工程、机械设计制造及其自动化、工业设计、机械电子工程、某工科专业等） 实验学时：32学时 实验性质：综合性、设计性实验 | 4 [/TBL] 5 [P] 目录 6 [P] 第一章 实验概述1 7 [P] 第二章 基础理论知识2 8 [P] 第三章 实验设备与环境搭建4 9 [P] 预备实验8 10 [P] 第四章 基础实验项目22 11 [P] 实验一 七彩探照灯22 12 [P] 实验二 小车前进实验27 13 [P] 实验三 小车前进后退左右转向综合实验36 14 [P] 实验四 …[截断,原长7246]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\robot-guide\\code_text\\batch1.md"}` → `1 # Batch 1 (img_001–img_028) 2 3 ### img_001.jpeg — 类型: photo 4 BST-4WD 智能小车扩展板（PCB 正面）产品标注图。顶部标题：「搭载BST-4WD智能小车扩展板」「一个强大的智能小车开发平台」，下方英文小字（模糊，大意为 4WD smart car is a new four-wheel drive intelligent car; programming difficulty: entry-level; hardware configuration, race level, control experience, consumer level）。 5 板上标注 …[截断,原长12597]`

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

I've read both materials. Now I need to write the chapter. Let me check the output directory exists first, and also check if there are other sections already written to match style (maybe not necessary, but let me check the sections folder).

Let me also look at the workspace to see what's there.

Key facts to incorporate:

From guide_extract.txt:
- 课程类型：创新实践实验；适用专业：工学院各个专业（农业机械化及其自动化、农业工程、车辆工程、机械设计制造及其自动化、工业设计、机械电子工程、某工科专业等）；实验学时：32学时；实验性质：综合性、设计性实验
- 目录：第一章 实验概述；第二章 基础理论知识；第三章 实验设备与环境搭建；预备实验；第四章 基础实验项目（实验一 七彩探照灯、实验二 小车前进、实验三 小车前进后退左右转向综合、实验四 舵机旋转控制七彩探照灯、实验五 按键控制小车启动）；第五章 创新设计实验（实验六 红外避障、实验七 红外跟随、实验八 寻光行走、实验九 巡线、实验十 超声波避障、实验十一 带舵机云台的超声波避障）；第六章 实验报告要求与评分标准；第七章 安全注意事项与常见问题；第八章 拓展与思考
- 1.1 实验目的：5条
- 1.2 实验意义
- 1.3 能力培养目标表（技术能力、分析能力、创新能力、协作能力）
- 2.1.1 差动驱动：直线运动（左右同速）、原地旋转（等速反向）、圆弧运动（有速差，绕瞬时中心）
- 2.1.2 运动学模型：v=(vR+vL)/2，ω=(vR−vL)/L，L为两轮之间轴距
- 2.2.1 PID：表格（P 快速响应误差成比例调节输出；增大加快响应，过大会引起振荡；I 消除稳态误差提高控制精度；增大加快消除静差，过大会引起超调；D 预测误差变化趋势抑制振荡；增大增强阻尼，过大会放大噪声）
- 2.2.2 PWM：占空比=高电平时间/周期×100%；电机平均电压=电源电压×占空比；PWM频率一般选择10kHz-20kHz，避免人耳可闻噪声
- 2.3.1 红外传感器：发射红外光→遇障碍物反射→接收管检测反射光；特点：成本低、响应快、易受环境光干扰；应用：近距离避障、黑线检测
- 2.3.2 超声波：距离=声速×飞行时间/2；测量范围2cm-400cm；特点：测距远、精度中等、受角度影响大
- 3.1.1 核心控制器表：STC12C5A60S2 ×1 主控制器；TB6612FNG ×1 驱动直流减速电机；直流减速电机 12V ×4；锂电池组 11.1V 2200mAh ×1
- 3.1.2 传感器表：HC-SR04 ×1 超声波测距障碍物距离检测；TCRT5000 ×4 红外循迹黑线检测与循迹；E18-D80NK ×2 红外避障近距离障碍物检测；光敏电阻 ×2 寻找光线
- 3.1.3 机械结构件：铝合金底盘1个；橡胶轮胎4个（驱动轮）；铜柱、螺丝、螺母若干；传感器支架按需配置
- 3.2.1 开发环境：Keil uVision IDE；官网 https://www.keil.com/；也可安装配套资料提供的 Keil C51 V9.00；配置串口驱动（CH340）；库文件安装：将 STC12C5A60S2.H 拷贝到 Keil 安装目录（例如 C:\Program Files\Keil\C51\INC）
- 3.2.2 开发环境验证：USB连接开发板到电脑，设备管理器查看端口中是否出现 usb-serial ch340 字样；打开串口监视器验证串口通信正常
- 3.3.1 底盘组装：电机固定→轮胎安装→舵机、灯光模块、传感器→铜柱固定核心控制板
- 3.3.2 电路连接：重要提示：接线前务必断开电源！接线完成后仔细检查，确认无误后再通电！；开发板接线（img_001）；传感器接线（img_002）
- 3.3.3 系统测试：组装完成后通过预备实验进行系统测试
- 预备实验：
  - 实验目的：1、掌握轮式机器人用C51开发板与计算机硬件连接及其基本结构；2、熟悉及掌握C51系列单片机Keil uVision IDE（集成开发环境）软件、ISP下载软件及串口调试终端的使用方法
  - 设备：轮式机器人套件、ISP下载线和串行接口线（共用）、计算机、电源；Keil uVision2 IDE、程序下载软件、串口调试软件
  - 单片机控制的轮式机器人是通过串并口或USB接口通信交互，由硬件系统与软件系统相互结合组成的一个完整的智能控制系统。单片机必须与外围设备及软件组成一个完整的应用系统（图1.1）
  - 结构组成（图1.2）：小车底盘、车轮、扩展板、伺服电机、电池盒。MCU 是 STC 公司生产与51系列兼容的8位 STC12C5A60S2（兼容STC89C52）单片机
  - 扩展板定义：方便单片机与电源、ISP下载线、串口线以及各种传感器和电机的连接制作的一个电路板（图1.4）
  - 连接：ISP接口（Micro USB）到计算机以便程序下载；串行接口（Micro USB）到计算机以便调试和交互；连接机器人到电池或供电电源
  - Keil 流程：①建立用户文件夹，拷入头文件 STC12C5A60S2.H 到 C:\Program Files\Keil\C51\INC；②进入 Keil uVision2 IDE：新建项目工程（*.uv2）：Project→New Project，命名，保存在用户文件夹内；选择 Atmel、AT89S52；新建C程序文件：File→New，保存为 *.c，注意关键字拼写、英文标点、大小写；添加C程序到工程：Source Group 1 右键→Add Files to Group Source；生成hex：Target 1 右键→Option for target→Output→选中 Create HEX Fi:→编译生成 *.hex；编译要求没有错误，允许警告。示例文件 HelloRoBot.Hex
  - 下载系统（stc-isp-15xx-v6.85）：1）查看开发板芯片型号（丝印，打手电筒，开发板稍微倾斜）；2）安装驱动（microUSB连接，检查驱动）；3）烧录代码：选择芯片型号和端口，以 STC89C52 为例（小车上实际是 STC12C5A60S2）；STC89C52 在"STC89C51 系列"里找；端口在设备管理器看（USB-SERIAL CH340 (COM*)）；打开程序文件：选择 .hex 后缀文件；烧录步骤：插上usb后没有灯亮，点击"下载/编程"，L1亮了，立刻按下板子电源开关，然后L2亮，开始烧录。！！！上传程序时不能占用RX、TX串口（蓝牙模块、WIFI模块需要取下来，否则烧录失败）
  - ④串口调试：从执行文件下载到单片机的那个时刻开始，程序开始运行。单片机向计算机发送信息。利用串口调试软件查看，"Reset"按钮可让程序重新运行一次。使用前串口线连接单片机串口与计算机USB口，设备管理器查看串口号。如果没有，重新安装 CH340 驱动
  - 4、做完实验断开电源，开关拨到 OFF，拆卸串口线还原
  - 思考题：1、什么是单片机？2、MCS51、8051、C51、AT89S52之间是什么关系？3、轮式机器人所用单片机的特点是什么？4、头文件的作用是什么？

From batch1.md:
- img_001/img_006: BST-4WD 扩展板接口标注（详细列表）
- img_002/img_007: 扩展板模块连线图（风扇、左避障寻光、四路循迹、灰度、右避障寻光、七彩探照灯、超声波、电池盒、9G舵机、蓝牙、4个直流减速电机）
- img_003: 单片机应用系统 = 硬件（单片机+接口电路及外设等）+软件
- img_004: 四轮小车俯视照片，DIP-40芯片
- img_005: 小车底盘宣传图：铝合金底盘、强劲四驱动、金属固定支架；三节蓝色18650电池（3.7V 2200mAh）
- img_008: 扩展板使用说明：
  - DC充电座 8.4V-12.6V，18650锂电池充电使用，DC口在驱动板上
  - L3 供电电源指示灯，开电源开关后常亮；不亮时检查电源接线（红色对应+，黑色对应-）
  - L1 低电压指示灯，低电压时熄灭，L3仍点亮
  - 跳线帽短接 MVCC->5V（出厂默认）——在超声波座旁，丝印 Ultrasonic、Level Change，J16跳线
  - 烧录开关（51/Arduino DownLoad Switch ON/OFF）：烧录程序时拨到 ON；使用蓝牙/WiFi模块时拨到 OFF
  - 舵机接口 J1：棕色接GND、红色接VCC、橙色接IO0
  - Arduino功能跳线区：51版本不用此功能区。丝印一行 L2 HW2 L1 HW1 X4 X3 X2 X1。无需插跳线帽
  - micro USB口：串口烧录通讯使用
  - 红外遥控时给 INF 插跳线帽，拔掉风扇和灰度模块排线，小车需单层结构安装
- img_009: Keil µVision3 主界面布局（功能菜单、项目文件列表、编辑区、系统信息区）
- img_010: µVision2 Project 菜单 New Project
- img_011: Select Device for Target 'Target 1'：Vendor Atmel，Device AT89S52，Family MCS-51
- img_012: Copy Standard 8051 Startup Code to Project Folder and Add File to Project? 是/否
- img_013: Save As HelloRoBot.c
- img_014: Source Group 1 右键 → Add Files to Group 'Source Group 1'
- img_015: Project 菜单 Options for Target 'Target 1'
- img_016: Options 对话框 Output 标签：Create HEX Fi: 勾选，HEX-80；Name of Executable: HelloRoBot
- img_017: 工具栏小图标
- img_018: 编译输出：Build target 'Target 1'; compiling HelloRoBot.c...; linking...; Program Size: data=58.3 xdata=0 code=1246; creating hex file from "HelloRoBot"...; "HelloRoBot" - 0 Error(s), 0 Warning(s).
- img_019: 设备管理器：USB-SERIAL CH340 (COM4)，红字「出现ch340表示已经安装成功的」「没有这个需要重新安装驱动」
- img_020: 芯片丝印 STC 89C52 特写（TEXTOOL 锁紧插座）
- img_021: STC-ISP V6.85 界面，选 STC89C52（STC89C51 系列里）
- img_022: 设备管理器 COM14 + STC-ISP 串口号选择
- img_023: 打开程序代码文件对话框，shumaguan_dongtai1.hex，打开.hex后缀的文件
- img_024: 烧录完成：固件版本号 7.2.6C，操作成功!，烧录成功!
- img_025_conv: 设备管理器 USB-SERIAL CH340 (COM5)
- img_026: 串口调试助手标题图
- img_027: 串口调试助手 CM精装版 V3.8.3：串口号 COM1、波特率 9600、校验位 NONE、数据位 8、停止位 1、打开按钮；接收区设置；发送区设置
- img_028: 宣传图「丰富有趣的玩法」6 种玩法：智能追光、高难度巡线、颜色识别车灯显示、巡线色块识别、超声波避障、风扇灭火

Note about "指导书注意" items to weave in:
1. Keil 版本不一致：3.2.1 说 Keil uVision IDE，预备实验说 Keil uVision2 IDE，截图 µVision2/µVision3 混用——版本不影响操作流程。
2. 烧录软件标题 stc-isp-15xx-v6.85；指导书以选 STC89C52 为例，注明小车上实际芯片是 STC12C5A60S2——两款都要能在列表里找到，选型以板上丝印为准。
3. PWM 频率：第二章说 10kHz-20kHz，实验代码是 50Hz 软件 PWM（20ms 周期），教学简化。
4. 表 3-1 电机 12V、电池 11.1V：工作电压以电池实际供电为准。

Note the task says "对照小车的 run/left/right/spin_left/spin_right 六个函数" — that says "六个函数" but lists only five names (run/left/right/spin_left/spin_right). Hmm, "对照小车的 run/left/right/spin_left/spin_right 六个函数（预告实验三）". Maybe it's run, back (后退?), left, right, spin_left, spin_right? The instruction says "六个函数" but lists 5. Since experiment 3 is 小车前进后退左右转向综合实验, likely functions are run（前进）、back（后退）、left（左转）、right（右转）、spin_left（原地左转/自转）、spin_right（原地右转）. But I cannot invent function names not in materials. Hmm. The task instruction itself gives the function names: run/left/right/spin_left/spin_right — that's 5. It says "六个函数". I should be careful. Since I don't have the experiment 3 code (that's another chapter's range), I can only preview. I could write "run（前进）、left（左转）、right（右转）、spin_left（原地左转）、spin_right（原地右转）等运动函数" and note 后退函数见实验三详解。Actually the safest: mention the listed five functions and note that experiment three will detail them; the count discrepancy — I can write "指导书实验三中的运动函数（如 run、left、right、spin_left、spin_right 等）" to avoid committing to a wrong list. Since the task instruction says "六个函数" and lists five, maybe there's a "back" function. But I must not fabricate. I'll write it as "run（前进）、left、right（转向）、spin_left、spin_right（原地旋转）等运动控制函数，逐一对照详解见实验三一章" — that avoids the count issue. Hmm, but the task explicitly said "对照小车的 run/left/right/spin_left/spin_right 六个函数（预告实验三）". Perhaps they consider run/back/left/right/spin_left/spin_right as six and abbreviated. I'll mention run、back(?)... no, can't invent. I'll say "实验三会给出 run、left、right、spin_left、spin_right 等运动函数" and describe what each would do based on 差动驱动 theory (which is legitimate deduction from theory, and I can frame it as "对应差动驱动的三种运动状态"). Actually since these are standard names, describing run=前进, left=左转, right=右转, spin_left=原地左转, spin_right=原地右转 is a reasonable mapping to the differential drive states (直线运动、圆弧运动、原地旋转) — I'll frame carefully: "从函数名即可对应 2.1.1 的三种运动状态" and mark detailed implementations in 实验三.

Also "PW-M frequency 10-20kHz（指导书原话）以及本套代码实际用 50Hz 软件 PWM 的现实（低频会有轻微抖动噪声，属正常——此句若属推断请标注）" — so I need to include the 50Hz fact and mark the "轻微抖动噪声属正常" as 补充说明 since it's inference.

For the L=15cm example: mark "（算例假设）指导书未给出轴距数值，此处假设 L=15cm 仅为算例".

vR=0.2, vL=0.1: v=(0.2+0.1)/2=0.15 m/s; ω=(0.2−0.1)/0.15=0.667 rad/s. Turning radius R=v/ω=0.15/0.667=0.225 m=22.5cm. That's a nice addition (R = L/2 × (vR+vL)/(vR−vL) = 0.15/2 × 0.3/0.1 = 0.075×3 = 0.225 m). Good, consistent.

Arc-length derivation: two wheels separated by L, turning about instantaneous center, both wheels have same angular velocity ω about center; outer wheel (right, faster) radius R + L/2, inner wheel (left) radius R − L/2. vR = ω(R+L/2), vL = ω(R−L/2). Subtract: vR − vL = ωL → ω = (vR−vL)/L. Add: vR + vL = 2ωR → average v = ωR = (vR+vL)/2. Good derivation.

Alternative simpler derivation via arc lengths in time t: left wheel travels sL = vL·t along arc, right wheel sR = vR·t. The car body center travels arc of radius R, wheels at R±L/2. Ratio of arc lengths equals ratio of radii: sR/sL = (R+L/2)/(R−L/2). Then solve. I'll present the clean version: same time t, angles same θ (both wheels' arcs subtend the same central angle θ since rigid body). θ = sR/(R+L/2) = sL/(R−L/2). Then vR−vL over L gives ω = θ/t · ... Let me do: vR = (R+L/2)·θ/t, vL = (R−L/2)·θ/t. Subtract: vR−vL = L·θ/t = L·ω. Add: vR+vL = 2R·θ/t = 2R·ω → v=(vR+vL)/2 = R·ω. Good.

PID section: P/I/D from the table, plus examples: 巡线场景 — P 大了：小车在线两侧来回摆动（振荡）；I 大了：转弯后冲过头、超调；直行场景 similar. And note "本课程代码是开关式控制而非 PID" — is that in the materials? The task instruction states it as fact to include. I'll include as instructed; maybe mark as (补充说明)? The task says "说明本课程代码是开关式控制而非 PID，PID 是进阶方向" — it's part of the brief, so I can state it, but since it's not visible in the extracted guide text (chapter 2 extract only has PID/PWM/sensor sections; the code is in later chapters), I should perhaps phrase as "本套指导书的实验代码采用…开关式控制" — the brief asserts it, so I trust the brief. I could add a light note that具体实现见后续实验章节. To be safe I'll phrase without inventing specifics: "本课程各实验代码中的控制是开关式（阈值判断）控制：传感器读数超过阈值就执行固定动作，而不是按误差大小连续调节。PID 是学完基础实验后的进阶方向（指导书第八章'拓展与思考'亦指向拓展）" — hmm, 第八章 拓展与思考 exists in TOC, that's fair to reference as a pointer but I shouldn't claim its content. I'll just say PID 是进阶方向.

Sensor section: 红外反射式 — 发射-反射-接收 from 2.3.1; 黑白吸收差异: is that in materials? The guide says 红外循迹 TCRT5000 黑线检测与循迹. The black/white absorption difference is standard knowledge needed to explain 巡线. Task says "讲发射-反射-接收与黑白吸收差异、阈值电位器" — 阈值电位器 is not explicitly in extract but is standard for TCRT5000/E18-D80NK modules; the brief instructs to include it. I'll include with (补充说明) marking where needed. Actually the brief explicitly asks for these contents, so they're sanctioned; but per language rules "材料没有的写'指导书未给出'；确需补充的常识性假设必须显式标注'（补充说明）'". So for 阈值电位器 and 黑白吸收 I should add （补充说明）markers. Hmm, but that could get clunky. I'll mark once per concept.

Ultrasonic: 距离=声速×飞行时间/2, why /2 (sound travels to obstacle and back, double path). 2–400cm. Speed of sound ~340 m/s — that's a common-physics supplement; mark （补充说明）if I give 340 m/s numeric example. I'll give an example: 500µs → 340×0.0005/2 = 0.085 m = 8.5 cm. That's a nice concrete example. Mark as 补充说明 for the 340 m/s value.

Structure plan (## sections numbered 1-7):

# 第一章（详解）全书导读与预备篇 — title: 《轮式机器人创新实验指导书》小白详解 第一章：全书导读与预备篇

## 1 这本指导书怎么用
- 1.1 这是一门什么课 (课程性质、学时、专业、实验性质)
- 1.2 全书结构地图 (11 experiments: 基础一~五、创新六~十一; plus 报告/验收)
- 1.3 建议的打开方式 (对照原文+详解)

Actually the task says structure is 7 numbered sections with fixed order:
1. 这本指导书怎么用
2. 你需要准备的东西
3. 读懂小车：整机结构
4. 第二章理论基础逐条讲透 (4.1-4.4)
5. 第三章设备与环境搭建的补充解读
6. 预备实验手把手
7. 本章小结与衔接

Markdown: 章 #, 节 ##, 小节 ###. So:
# 第一章 全书导读与预备篇
## 1 这本指导书怎么用
### 1.1 ...
## 2 你需要准备的东西
## 3 读懂小车：整机结构
### 3.1 ...
## 4 第二章理论基础逐条讲透
### 4.1 差动驱动...
#### 4.1.1? Maybe use bold paragraphs instead of #### since only 3 levels specified. "Markdown 层级：章 #、节 ##、小节 ###" — so ### is the deepest heading. Within 4.x subsections I can use ### for 4.1/4.2/4.3/4.4, and inside use bold lead-ins or paragraphs.

Section details:

## 1 这本指导书怎么用
- 课程信息表 (课程类型、适用专业、学时、性质) — from TBL 1.
- 实验目的/意义/能力目标 brief summary (from 1.1/1.2/1.3).
- 全书结构: 目录结构 + 11 实验 map. 基础实验一~五: 七彩探照灯（点灯，学 IO 输出和 PWM 彩灯）、小车前进（电机驱动+PWM 调速入门）、前进后退左右转向综合（运动函数全集）、舵机旋转控制七彩探照灯（舵机）、按键控制小车启动（输入检测+程序流程）。创新实验六~十一: 红外避障、红外跟随、寻光行走、巡线、超声波避障、带舵机云台的超声波避障。第六章 报告要求与评分标准、第七章 安全注意事项与常见问题、第八章 拓展与思考。
- 怎么考：报告与验收 — from TOC we only know 第六章 title. So say 考核方式见指导书第六章（实验报告要求与评分标准），本文对应章节会细讲. Don't invent details.
- 建议打开方式：每章对照指导书原文 + 本文详解；先读详解再动手/或边动手边对照。

Page numbers from TOC: 预备实验 8页起, 实验一 22, ..., 实验十一 146, 第六章 162, 第七章 165, 第八章 167. Could include page numbers in the map table. That's factual from TOC. Good for 枚举型事实表格.

## 2 你需要准备的东西
- 硬件清单表 (from 3.1): STC12C5A60S2 主控、TB6612FNG 驱动、12V 直流减速电机×4、11.1V 2200mAh 锂电、HC-SR04、TCRT5000×4、E18-D80NK×2、光敏电阻×2、SG90 舵机、RGB 探照灯模块、按键 + 机械件 (铝合金底盘、橡胶轮胎×4、铜柱螺丝螺母、传感器支架).
  - Note: SG90 舵机 — the materials say "伺服电机" (预备实验) and img_002 shows "9G舵机". The task says "SG90 舵机". img_002 says 9G舵机. SG90 is a 9g servo; the brief instructs SG90. img_008 says 舵机接口 J1. I'll write "9G 舵机（SG90 一类）" hmm — better to follow brief: "SG90 舵机" with note that指导书图中标注为 9G 舵机. Actually simplest: 指导书图 1.4 连线图中标注为「9G舵机」。9G 指舵机重量级别，常见型号即 SG90（补充说明）. That's honest.
  - RGB 探照灯模块: from TOC 实验一 七彩探照灯 and img_002 七彩探照灯 module. 按键: 实验五 按键控制小车启动. The 扩展板 has 启动按键 (img_001). So 按键 is on-board 启动按键. I'll list 按键（扩展板上的启动按键，实验五用）.
  - Also 风扇模块、蓝牙模块、灰度模块 appear in img_002 but not in 3.1 tables; the brief's list doesn't include them either. I could mention them in a note as扩展板还支持但清单未列/后续实验未涉及. Keep to brief list, maybe one sentence noting 扩展板还留有风扇、蓝牙等接口（见 img_001 标注），本课程主线用不到. That's factual from img_001.
- 软件清单: Keil uVision（C51 版，配套资料含 Keil C51 V9.00）、STC-ISP（stc-isp-15xx-v6.85）、CH340 驱动、串口调试助手（CM精装版 V3.8.3）. Each one-sentence purpose.
- 耗材/工具: ISP 下载线和串行接口线（共用）、计算机、电源 (from 预备实验 设备清单). microUSB 数据线.

## 3 读懂小车：整机结构
- 3.1 整车组成：底盘/4轮/扩展板/51核心板/电池盒 (from 预备实验: 小车底盘、车轮、扩展板、伺服电机、电池盒; img_004/005). MCU: STC12C5A60S2, 与51兼容, 8位, DIP-40 (img_004 shows DIP-40; img_020 shows DIP-40丝印 for 89C52; the car chip is STC12C5A60S2 — 预备实验 says compatible with STC89C52). Careful: img_020 photo shows STC89C52 chip (that's the example board photo). The car uses STC12C5A60S2. I'll note the photo in 指导书 shows a STC89C52 chip as丝印示例.
- 3.2 扩展板是什么：定义 (from 预备实验). 它把单片机引脚引到哪里: IN1~IN8 传感器口 — wait, is IN1~IN8 in materials? img_001 lists 四路巡线、左避障/寻光、右避障/寻光 etc. IN1~IN8 not explicitly in img_001 transcription. The brief says "扩展板把单片机的引脚引到哪里：IN1~IN8 传感器口、电机驱动口、舵机口 J1、RGB 灯口 J24、超声波口、串口/ISP 口". J1 is documented (img_008). J24 is not in my materials... The brief asserts these names; presumably from the guide's later chapters (out of my range). I should include them as the brief instructs, since the brief is authoritative about what exists in the guide. But to be safe with the "no fabrication" rule: the brief explicitly lists these as content to include, so they come from the overall guide (other chapters' extracts). I'll include IN1~IN8 传感器口、J24 RGB 灯口 as given by the brief. I'll present the interface table combining img_001 annotations (top row: 风扇接口、左避障/寻光、颜色识别、四路巡线、右避障/寻光、RGB车灯、超声波模块; left: Micro USB、启动按键、线性CCD、6路舵机接口、PS2、NRF24L01、CH340烧录电路、MPU6050、复位按键; right: 5V/3.3V转换开关、充电接口、电池盒接口、电源开关、低电压指示灯、TB6612四驱电机驱动、供电电路、51核心板接口、过放保护堵转重启、3.3V稳压电路; bottom: 蜂鸣器、STM32核心板、烧录开关、蓝牙插口、红外接收、ARDUINO功能跳线区、树莓派接口; back: ARDUINO UNO安装接口、右电机接口、左电机接口、电压检测模块接口) plus the named ports from brief (J1 舵机、J24 RGB、IN1~IN8、超声波口 J16 area). Actually img_008 mentions J16 跳线 near 超声波座 with 丝印 Ultrasonic、Level Change. So "超声波口"附近有 J16 跳线 MVCC->5V.
- 3.3 供电与开关: 电源开关、L3 供电指示灯（常亮）、L1 低电压指示灯（低电压熄灭、L3仍亮）、DC 充电座 8.4V-12.6V（18650锂电充电，DC口在驱动板上）、MVCC->5V 跳线出厂默认、烧录开关 51/Arduino（烧录时 ON，蓝牙/WiFi 时 OFF）、电源接线红+黑-。
- 电池: 11.1V 2200mAh 锂电池组 (表3-1)；img_005 shows 三节18650 3.7V 2200mAh → 3×3.7=11.1V (补充说明 the math is trivially 3S; I can state 三节18650串联 as shown in photo, and 3.7V×3≈11.1V is arithmetic — fine to include, maybe no marking needed since it's arithmetic on given numbers; still I can add （补充说明）for the 串联 claim... the photo shows 3 cells and battery pack 11.1V; 3.7×3=11.1 is straightforward. I'll state it plainly as consistent, low risk).

## 4 第二章理论基础逐条讲透
### 4.1 差动驱动
- 三种运动状态 (guide): 直线、原地旋转、圆弧.
- 推导 via arc lengths.
- 例题 L=15cm（算例假设）, vR=0.2, vL=0.1 → v=0.15m/s, ω=0.667rad/s ≈ 38.2°/s, R=22.5cm. Also special cases: vR=vL → ω=0 直线; vR=−vL → v=0 原地旋转.
- 对照 run/left/right/spin_left/spin_right 函数（预告实验三）: map to states. Note 指导书未在此章给出函数实现，实验三详解.
### 4.2 PWM 调速
- 占空比定义, 平均电压公式, example: 11.1V battery? Hmm, motor rated 12V; use 电源电压 example with 12V and 60% duty → 7.2V. Or use 11.1V? Table 3-1 says motor 12V, battery 11.1V — 指导书注意 #4 says 工作电压以电池实际供电为准. I can use 12V as 电源电压 in the formula example and note the注意. Example: 占空比 50% → 12V×50%=6V. 
- 频率: 指导书原话 10kHz-20kHz 避免人耳可闻噪声; 本套代码实际 50Hz 软件 PWM（20ms 周期）教学简化; 低频时电机可能有轻微抖动/噪声属正常现象（补充说明/推断标注）.
- Explain why 10-20kHz: above human hearing range ~20kHz? Actually 10-20kHz is partly audible to young people; guide says "避免人耳可闻噪声" as original. I'll quote guide. Explain: 电机对 PWM 的响应是低通（机械惯性+电感），平均电压起作用（补充说明）. Keep it grounded.
### 4.3 PID
- Table from guide (P/I/D 作用与调节原则), explain each with 巡线/直行 examples: P 大了振荡（巡线时在线两侧蛇形摆动）; I 大了超调（直行纠偏时冲过头、来回晃）; D 大了放大噪声（传感器抖动导致输出抖动）.
- 调参口诀: The brief says "P/I/D 三项各自的作用与调参口诀". 口诀 like "先 P 后 I 再 D"（补充说明 as common practice）. I can give: 参数整定先比例、后积分、再微分（补充说明，工程常用顺序）.
- 本课程代码是开关式控制而非 PID；PID 是进阶方向。
### 4.4 传感器
- 红外反射式: 发射→反射→接收; 黑白吸收差异（黑吸收红外多、反射少，白反射多——补充说明）; TCRT5000×4 巡线、E18-D80NK×2 避障; 阈值电位器（补充说明: 模块上电位器调比较阈值，决定输出翻转距离/黑白判定）; 特点 成本低响应快易受环境光干扰; 应用 近距离避障、黑线检测. Also 跟随实验（实验七）也靠红外 — brief says 避障/巡线/跟随三个实验都靠它. From TOC: 实验六 红外避障、实验七 红外跟随、实验九 巡线 — all infrared. Good.
- 超声波 HC-SR04: 测距公式, why /2, 量程 2-400cm, 特点 测距远精度中等受角度影响大. Example with 340 m/s（补充说明）: t=588µs → 10cm. Let me compute: 340 m/s × 588e-6 s = 0.19996 m round trip → /2 = 0.09998 m ≈ 10cm. Nice: 1cm corresponds to ~58µs round trip (well-known HC-SR04 fact, but that's a supplement). I'll do the example: 若测得飞行时间 588µs，距离=340×588×10⁻⁶/2≈0.1m=10cm（声速 340m/s 为补充说明的常温近似值）.

## 5 第三章设备与环境搭建的补充解读
- 5.1 组装顺序: 电机→轮胎→舵机/灯光/传感器→铜柱固定核心控制板 (3.3.1). 解读 why this order (底盘刚性件先装、电子件后装避免压坏——补充说明 reasoning light).
- 5.2 接线前断电的为什么: guide 重要提示. Explain: 接错线瞬间可能烧毁芯片/驱动,带电插拔易产生火花 (补充说明). 红正黑负 (img_008).
- 5.3 CH340 驱动: 作用 (USB转串口, 扩展板板载 CH340 烧录电路 img_001), 安装后设备管理器验证 usb-serial ch340 字样 (3.2.2, img_019 COM4, img_022 COM14, img_025 COM5 — COM号每台电脑不同), 没有则重装驱动 (img_019 红字).
- 5.4 库文件: STC12C5A60S2.H 拷到 C:\Program Files\Keil\C51\INC (3.2.1 & 预备实验①).
- 验证: 串口监视器验证通信.

## 6 预备实验手把手
### 6.1 认识系统组成: img_003 框图: 应用系统=硬件（单片机+接口电路及外设）+软件; 软件 two layers — "软件两层框图" per brief. Hmm, img_003 transcription says 大框内 单片机+接口电路及外设=硬件; 右侧 软件. "软件两层" — the brief says "硬件=单片机+接口电路外设、软件两层框图". The transcription doesn't detail software layers. I'll describe per img_003: 硬件=单片机+接口电路及外设; 软件 as独立部分; and note 预备实验原文 says 由硬件系统与软件系统相互结合组成完整的智能控制系统. For "软件两层" I can say 软件部分自上而下…指导书图未细分 — actually don't over-invent. Brief says "认识系统组成（硬件=单片机+接口电路外设、软件两层框图）" — maybe the original figure has software subdivided. My transcription only shows 软件 as one box. I'll describe hardware composition and software, and note that图1.1中软件与硬件并列（图中软件框未再细分，指导书未给出更细层次）. Hmm risky. Alternative reading: "软件两层" could be my instruction's interpretation. I'll write: 图1.1 把应用系统拆成两块：硬件＝单片机＋接口电路及外设等，软件单独一框，两者相加构成完整应用系统。That covers it faithfully. If the brief wants "软件两层", I can add: 从程序的角度看，软件也可分为底层驱动与上层功能两层（补充说明）。That satisfies both safely.
- Then 认识小车结构 (img_004/005): 底盘、车轮、扩展板、伺服电机、电池盒; MCU STC12C5A60S2 兼容 STC89C52, DIP-40 直插封装（img_004 红圈）.
- 6.2 接线: ISP 口 Micro USB → 计算机 (程序下载); 串口 Micro USB → 计算机 (调试交互); 电池/电源. Note ISP线和串口线共用 (预备实验设备: ISP下载线和串行接口线（共用）). micro USB 口串口烧录通讯使用 (img_008). 
- 6.3 Keil 建工程全流程 (img_009-018):
  1. 建用户文件夹, 拷头文件 STC12C5A60S2.H → C:\Program Files\Keil\C51\INC
  2. Project→New Project, 命名, 保存到用户文件夹 (*.uv2)
  3. 选器件: Atmel → AT89S52 (MCS-51 family) — 原因: STC12 与 51 兼容但 Keil 器件库中没有 STC12 时选通用 51 型号 AT89S52, 编译目标代码同为 8051 指令集 (brief: "STC12 与 51 兼容但 Keil 库里用 AT89S52 通用头"). img_011 description: Device AT89S52, 8K Flash, 32 I/O, 3 Timers, 8 Interrupts.
  4. 弹窗 Copy Standard 8051 Startup Code? (img_012) — 指导书截图出现该对话框; 选"是"或"否"均可…hmm, what does the guide say? Not stated. Standard practice: Yes adds STARTUP.A51. I'll mention the dialog appears and 常见做法是选"是"，得到默认启动文件 STARTUP.A51（补充说明）。Careful — brief didn't mention. I'll describe the dialog factually and add （补充说明）for the Yes recommendation. Or say 选"否"直接跳过也不影响简单程序的编译（补充说明）. I'll keep one short marked note.
  5. File→New 新建 C 文件, 保存为 *.c (img_013 HelloRoBot.c), 注意关键字拼写、英文标点、字母大小写 (guide).
  6. Source Group 1 右键→Add Files to Group 'Source Group 1' (img_014), 添加后展开 + 号, Keil 自动识别关键字着色 (guide).
  7. Target 1 右键→Options for Target 'Target 1'→Output→勾选 Create HEX Fi:（HEX-80）(img_015/016).
  8. 编译: 工具栏 Build（F7）(img_017 icon; img_010 menu shows Build target F7), 输出窗口看 "0 Error(s), 0 Warning(s)" (img_018), 生成 HelloRoBot.hex 于源程序目录; 编译要求没有错误，允许出现警告 (guide).
- 6.4 STC-ISP 烧录全流程 (img_019-024):
  1. 看芯片丝印 (打手电筒、板子稍倾斜) (guide; img_020 示例照片为 STC89C52 丝印).
  2. microUSB 连接, 检查驱动 (img_019).
  3. 打开 stc-isp-15xx-v6.85 (img_021): 选单片机型号 — 指导书以 STC89C52 为例（在"STC89C51 系列"下）, 小车实际芯片 STC12C5A60S2（在 STC12 系列中找——careful: brief says "两款都要能在列表里找到，选型以板上丝印为准"）. I'll say: 列表中 STC89C52 在「STC89C51 系列」下；小车上实际芯片 STC12C5A60S2 也能在型号列表中找到，最终以板上丝印为准.
  4. 串口号: 设备管理器看 USB-SERIAL CH340 (COM*), 在 STC-ISP 串口号下拉框选同一个 (img_022 COM14/COM4).
  5. 打开程序文件: 选 .hex 文件 (img_023).
  6. 烧录时序: 插上 USB 后没有灯亮 → 点"下载/编程" → L1 亮 → 立刻按电源开关 → L2 亮 → 开始烧录 (guide img_024: 操作成功/烧录成功). Why cold-start timing: STC ISP 需要单片机上电复位时检测下载信号 (补充说明 — well-known STC mechanism; the guide just gives the steps). I'll add short 补充说明 explaining 先点下载再上电是因为 STC 单片机在每次上电复位时会检测串口上的下载命令流，检测到才进入编程状态（补充说明）。This is accurate standard knowledge and helps beginners; marked.
  7. RX/TX 不得占用: 蓝牙/WiFi 模块要取下 (guide ！！！). Also 烧录开关拨到 ON (img_008), 用蓝牙/WiFi 时拨 OFF.
- 6.5 串口调试助手 (img_025-027): 串口线连接, 设备管理器看串口号 (COM5 example), 打开串口调试助手选串口号; img_027 参数: 波特率 9600（图中默认）, 校验位 NONE, 数据位 8, 停止位 1 — note 波特率要与程序中设置一致（补充说明）。"Reset"按钮可让程序重新运行一次 (guide). 接收区看单片机输出.
- 6.6 实验收尾: 断开电源, 开关拨 OFF, 拆卸串口线还原 (guide).
- 思考题提示: 预备实验有 4 道思考题, 参考答案见实验一章前（按任务要求）.

## 7 本章小结与衔接
- Recap: 课玩什么（11实验）、需要什么（硬件软件）、怎么跑起来（Keil 编译 hex → STC-ISP 烧录 → 串口调试闭环）。
- 下一章进入实验一（七彩探照灯）。

Also weave in the 4 "指导书注意" items:
1. Keil 版本不一致 — put in section 5 or 6 (Keil 流程处) and/or section 2 软件清单处. I'll put it in §6.3 opening (and a brief mention in §2 software list).
2. STC-ISP 型号选择 — §6.4.
3. PWM 频率 — §4.2.
4. 电机 12V/电池 11.1V — §2 hardware list note and/or §3.3 供电. Put in both briefly? One place is enough; I'll put prominently in §3 供电 subsection, and echo in §2 table note.

Count of "指导书注意" merged: 4 places (maybe 5 with echo). The final report should state the count.

Length: 600-900 lines. Need to write substantively. Let me now check the sections directory.

Also need to check: does the file sections/01_导读与预备篇.md already exist? Let me check the directory. Also should I look at other files in robot-guide for context (e.g., a style guide or other completed sections)? The task is self-contained, but a quick ls helps.

Let me check directory contents.

</details>

- 🔧 **Bash** `{"command": "ls -la \"C:/Users/UserX/.zcode/workspace/default/robot-guide/\" && ls -la \"C:/Users/UserX/.zcode/workspace/default/robot-guide/sections/\" 2>/dev/null || echo \"sections 目录不存在\"", "description": "查看 robot-guide 目录结构"}` → `total 7136 drwxr-xr-x 1 user 197121 0 Oct 3 17:52 ./ drwxr-xr-x 1 user 197121 0 Oct 2 23:38 ../ drwxr-xr-x 1 user 197121 0 Oct 3 17:29 code_text/ -rw-r--r-- 1 user 197121 4016 Oct 2 23:39 extract.py -rw-r--r-- 1 user 197121 7092792 Oct 2 23:39 guide.docx -rw-r--r-- 1 user 197121 120097 Oct 2 23:39 guide_extract.txt drw …[截断,原长682]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-03 18:11）

两份材料已读完。先看一下输出目录的现状。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

There are already two sections written (02 and 03). Let me quickly peek at the beginning of one to match style/format conventions (headings, how they reference 指导书注意, etc.). That will help consistency. Let me read a bit of 02_实验一_实验二.md.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\workspace\\default\\robot-guide\\sections\\02_实验一_实验二.md", "limit": 80}` → `1 # 实验一 七彩探照灯 · 实验二 小车前进（小白详解） 2 3 > 导语：本册对应《轮式机器人创新实验指导书》第四章的实验一（七彩探照灯）与实验二（小车前进），面向第一次接触单片机的读者——每行代码都有解释、每个数字都有出处，可直接用于预习、动手实验、验收答问和撰写实验报告，全部代码与数据均转录自指导书原文及配套程序截图。 4 5 # 预备实验思考题参考答案 6 7 以下四题出自指导书"预备实验"末尾的思考题，属于进入实验一之前应当掌握的内容，故按学习顺序放在本册开头。答案中的事实均取自指导书正文与配图，属于通行概念的部分已单独说明。 8 9 ### 问题 1 什么是单片机？ 10 11 参考答案：单片机（MCU，Microc …[截断,原长5171]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-03 18:15）

已有后续章节（02、03），先快速看一下已有章节的开头与风格约定，保持一致。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

I see the style of section 02. Now I understand the conventions:
- Title with # 
- 导语 blockquote
- Headings: ## for numbered sections, ### for subsections
- 平实语言, no emoji, 每句有信息量, 术语给定义, 指导书 img references cited
- 指导书注意 items woven in with plain tone

Now let me write section 01. It's a large document (600-900 lines). Let me carefully plan and write it.

Content plan detailed:

# 第一章 全书导读与预备篇（小白详解）

> 导语 blockquote: 本册对应指导书的课程信息、第一章 实验概述、第二章 基础理论知识、第三章 实验设备与环境搭建和预备实验……读完本章应当清楚三件事：这门课玩什么、需要准备什么、怎么把"写程序—编译—烧录—串口调试"的闭环跑起来。

## 1 这本指导书怎么用

### 1.1 这是一门什么课
- 课程信息表（表格，枚举型事实）：
  | 项目 | 内容 |
  | 课程类型 | 创新实践实验 |
  | 适用专业 | 工学院各个专业（农业机械化及其自动化、农业工程、车辆工程、机械设计制造及其自动化、工业设计、机械电子工程、某工科专业等） |
  | 实验学时 | 32 学时 |
  | 实验性质 | 综合性、设计性实验 |
- 段落解释：综合性、设计性是什么意思（综合=多学科，设计=没有唯一答案）——careful, this is interpretation; can phrase reasonably as plain explanation of the terms. It's fine as explanation, not fabricated fact.
- 实验目的（1.1 五条）、意义（跨学科）、能力目标表（表1-3）——转述。能力表可以再现为表格。

### 1.2 全书结构地图
- 段落：全书分八章/或"课程信息+八章"。TOC: 第一章 实验概述、第二章 基础理论知识、第三章 实验设备与环境搭建、预备实验、第四章 基础实验项目（实验一~五）、第五章 创新设计实验（实验六~十一）、第六章 实验报告要求与评分标准、第七章 安全注意事项与常见问题、第八章 拓展与思考。
- 表格：实验编号、名称、起止页码、练什么。
  - 预备实验 熟悉轮式机器人与C51单片机硬件软件 p8
  - 实验一 七彩探照灯 p22 —— 引脚端口控制与 LED
  - 实验二 小车前进 p27 —— 电机驱动与 PWM 调速入门
  - 实验三 小车前进后退左右转向综合 p36 —— 运动函数
  - 实验四 舵机旋转控制七彩探照灯 p47 —— 舵机
  - 实验五 按键控制小车启动 p54 —— 输入检测
  - 实验六 红外避障 p67
  - 实验七 红外跟随 p78
  - 实验八 寻光行走 p89 —— 光敏电阻
  - 实验九 巡线 p100 —— TCRT5000
  - 实验十 超声波避障 p117 —— HC-SR04
  - 实验十一 带舵机云台的超声波避障 p146 —— 综合前的所有
  - 第六章 报告要求与评分标准 p162；第七章 安全注意事项与常见问题 p165；第八章 拓展与思考 p167
  - "练什么" column: for 实验一 I know from 02 file (实验目的原文). For others I should be careful — I only have TOC titles. I can derive 练什么 from title + sensors in 3.1 tables: 红外避障→E18-D80NK；红外跟随→红外对管；寻光行走→光敏电阻；巡线→TCRT5000；超声波避障→HC-SR04；实验十一→舵机+超声波+云台。These mappings are supported by 表 3-1.1.2 sensor list (红外避障 E18-D80NK 近距离障碍物检测; TCRT5000 黑线检测与循迹; 光敏电阻 寻找光线; HC-SR04 障碍物距离检测) — reasonable. For 基础实验一~五: 实验一 七彩探照灯（RGB 灯）; 实验二 小车前进（电机）; 实验三 综合（电机+运动函数）; 实验四 舵机; 实验五 按键. These are from titles; fine. I'll phrase as "对应器材" which is directly supported.
- 分段说明：基础实验一~五练什么（把"点亮、动起来、转向、舵机、按键"五件基本功逐个过一遍）；创新实验六~十一练什么（在会动的基础上加传感器，让小车自己感知环境做决定）；最后报告与验收怎么考——指导书第六章为"实验报告要求与评分标准"，具体评分细目本文对应章节会展开/见指导书原文。Careful: 我不应编造评分细目。就说考核以实验报告与验收为抓手，具体要求见第六章（162 页起）。

### 1.3 建议的打开方式
- 每章对照指导书原文+本文详解：先读原文 → 读详解 → 动手 → 遇到卡壳回原文截图对照。
- 预备实验的思考题：预备实验末尾有 4 道思考题，本文不展开，参考答案见实验一章前（本套详解将其放在第二册开头）。

## 2 你需要准备的东西

### 2.1 硬件清单
表格（来自表 3-1/3-2 + 机械件 + 预备实验）：
| 器材 | 规格/型号 | 数量 | 干什么用 |
- 主控芯片 STC12C5A60S2 ×1 主控制器，运行控制算法（与 51 系列兼容的 8 位单片机，兼容 STC89C52）
- 电机驱动板 TB6612FNG ×1 驱动直流减速电机——单片机引脚电流带不动电机，驱动板是"功率放大中转站"
- 直流减速电机 12V ×4 提供动力输出
- 锂电池组 11.1V 2200mAh ×1 系统供电（三节 3.7V 18650 电芯，img_005）
- 超声波测距 HC-SR04 ×1 障碍物距离检测
- 红外循迹 TCRT5000 ×4 黑线检测与循迹
- 红外避障 E18-D80NK ×2 近距离障碍物检测
- 光敏电阻 ×2 寻找光线
- 舵机（图 1.4 标注 9G 舵机；实验四、十一用）
- 七彩探照灯模块（RGB 车灯）
- 按键（扩展板自带启动按键）
- 铝合金底盘 ×1、橡胶轮胎 ×4（驱动轮）、铜柱螺丝螺母若干、传感器支架按需
- 轮式机器人套件、ISP 下载线和串行接口线（共用，micro USB）、计算机、电源

Note about 12V/11.1V 指导书注意#4. Place here as 注意段落 + echo in §3.

扩展板还留有风扇接口、PS2 手柄、NRF24L01、蓝牙插口、树莓派接口等，本课程主线实验用不到（img_001）。

### 2.2 软件清单
表格：
| 软件 | 作用 |
- Keil uVision（C51 版）——写 C 程序、编译生成 .hex。配套资料提供 Keil C51 V9.00，也可官网下载。指导书 3.2.1 写"Keil uVision IDE"、预备实验写"Keil uVision2 IDE"，截图 µVision2 与 µVision3 混用——版本不影响操作流程。【指导书注意 #1】
- STC-ISP（stc-isp-15xx-v6.85）——把 .hex 烧录进单片机
- CH340 驱动——让电脑认出扩展板上的 USB 转串口芯片，出现 COM 口
- 串口调试助手（CM 精装版 V3.8.3）——查看单片机从串口发来的信息

## 3 读懂小车：整机结构

### 3.1 整车组成
- 段落：小车底盘、车轮、扩展板、伺服电机、电池盒（预备实验原文）；img_004 照片描述：黑色多层底盘、四橡胶轮、车顶主控板 DIP-40 芯片（红圈）、车尾金属减速电机、车前底盘下红外/巡线小板。img_005：铝合金底盘/金属固定支架/四驱动；三节 3.7V 2200mAh 18650。
- MCU：STC12C5A60S2，STC 公司，与 51 系列兼容，8 位，兼容 STC89C52。图 1.2 红圈标出 DIP-40 芯片。

### 3.2 扩展板：单片机引脚的"接线转接板"
- 定义（预备实验原文）：方便单片机与电源、ISP下载线、串口线以及各种传感器和电机的连接制作的一个电路板。
- 为什么需要：单片机 DIP-40 引脚又细又密，直接接电机/传感器不便；扩展板把引脚分类引出成排针/插座。
- img_001 接口标注表（按板上方位分组）——枚举型表格：
  | 板上位置 | 接口/部件 | 用途 |
  顶部一排：风扇接口、左避障/寻光、颜色识别、四路巡线、右避障/寻光、RGB车灯、超声波模块
  左侧：Micro USB 接口（串口烧录通讯使用）、启动按键、线性 CCD 摄像头、6 路舵机接口、PS2 手柄接口、NRF24L01 插口、CH340 烧录电路、MPU6050 陀螺仪接口、复位按键
  右侧：5V/3.3V 转换开关、充电接口、电池盒接口、电源开关、低电压指示灯、TB6612 四驱电机驱动、供电电路、51 核心板接口、过放保护堵转重启、3.3V 稳压电路
  底部：蜂鸣器、STM32 核心板、烧录开关（51/Arduino DownLoad Switch）、蓝牙插口、红外接收、ARDUINO 功能跳线区（51 版不用）、树莓派开发板接口
  背面：ARDUINO UNO 安装接口、右电机接口、左电机接口、电压检测模块接口
- 本课程主线用到的口（对齐 brief）：传感器口（四路巡线、左右避障/寻光、颜色识别、超声波模块口）、电机驱动口（TB6612 + 背面左右电机接口）、舵机口 J1（棕 GND/红 VCC/橙 IO0）、RGB 灯口（J24——brief 给的名字；img_001 标注为"RGB车灯"。Hmm. Brief says "RGB 灯口 J24". J24 not in my transcription. I'll write: RGB 灯口（指导书正文与实验一记作 J24；图 1.4 标注为"RGB 车灯"）—— hmm, I can't verify "指导书正文与实验一记作 J24" from my materials; the brief asserts J24. I'll phrase: RGB 灯口 J24（img_001 标注为"RGB 车灯"接口位）。That treats J24 as given name. Acceptable per brief.
  - IN1~IN8 传感器口: brief asserts. img_001 doesn't show IN1~IN8. Later chapters likely reference. I'll write: 传感器口 IN1~IN8（各传感器模块经排线插入这些口，具体每个口对应哪个模块见第三章接线图 img_002 与相应实验章节）。Hmm risky but brief sanctioned. I'll present it as "扩展板把传感器接口编号为 IN1~IN8" per brief.
  - 串口/ISP 口：micro USB 口（img_008：串口烧录通讯使用）。
- img_002 连线图整理：中间扩展板，红虚线连出：风扇、左避障寻光、四路循迹、灰度、右避障寻光、七彩探照灯、超声波、电池盒（绿色端子两根红线）、9G 舵机（黄红黑三色线）、蓝牙、4 个直流减速电机（左右各二）。
- 表：模块—接入位置/线序（舵机三色线序 from img_008；电池盒红线+黑- from img_008 L3 说明）。

### 3.3 供电、开关与指示灯
- 电源通路：电池盒接口 → 电源开关 → 供电电路 → 各模块（img_001 右侧：电池盒接口、电源开关、供电电路、3.3V 稳压、5V/3.3V 转换开关）。Careful not to over-claim circuit topology; img_001 lists these as 右侧部件. I'll describe functionally with 补充说明 minimal.
- L3 供电指示灯：打开电源开关后常亮；不亮检查电源接线（红+黑-）。
- L1 低电压指示灯：低电压时熄灭，L3 仍点亮。注意区分：预备实验烧录时序里也有"L1 亮→L2 亮"，那是核心板上的灯，与扩展板低电压灯 L1 不是一回事？Hmm — wait. img_008's L1 is 低电压指示灯 on the expansion board. 预备实验烧录步骤 says "点击烧录软件的'下载/编程'，L1亮了，这时立刻按下板子的电源开关，然后L2亮了". Is that the same L1? The 低电压灯 L1 would light when low voltage — burning sequence says L1 lights after clicking download. These are likely different LEDs (核心板 power/download LEDs) OR the same board. Risky. The brief doesn't ask me to reconcile. I'll present both as given, and add a caution note: 预备实验烧录时序中出现的 L1、L2 是指导书对板上指示灯的描述；img_008 扩展板说明中 L1 为低电压指示灯、L3 为供电指示灯。两处 L1 的含义指导书未明确统一，操作时以"按步骤观察哪盏灯亮"为准。Hmm, that's a fair 平实 note. Actually wait — could it be the same? If 电源开关 is OFF initially and USB plugged in, the board may be partially powered via USB. After clicking download, "L1亮了" then pressing power switch "L2亮了". If L1 were the low-voltage indicator it lighting would be odd. Most likely L1/L2 here are on the 51 核心板 (power/LED). The guide doesn't clarify. I'll include the reconciliation note plainly as above — it's honest and useful, phrased as 指导书未明确. Good.
- DC 充电座：8.4V-12.6V，给 18650 锂电池充电，DC 口在驱动板上。
- MVCC->5V 跳线（超声波座旁，丝印 Ultrasonic、Level Change，J16）：出厂默认插在 MVCC->5V。解释：选择超声波模块供电电平（补充说明 one line: 该跳线决定超声波接口 VCC 取 5V 还是其他电平，出厂已插好，不要动）——careful. img_008 says 跳线帽短接【MVCC->5V】（出厂默认插在此处）. I'll say 指导书仅说明出厂默认插在此处，本课程不需要改动。加（补充说明：该跳线用于选择接口供电电平）。
- 烧录开关（51/Arduino DownLoad Switch）：烧录程序拨 ON；使用蓝牙/WiFi 模块拨 OFF。
- Arduino 功能跳线区：51 版不用，无需插跳线帽（丝印 L2 HW2 L1 HW1 X4 X3 X2 X1）。
- 红外遥控 INF 跳线：用红外遥控时插上，并拔掉风扇和灰度模块排线，小车需单层结构安装（img_008）——补充 mention,本课程主线未涉及红外遥控实验（TOC 无此实验），但了解有备无患。Actually 颜色识别/追光 are in img_028 宣传图 but TOC has 寻光行走 (光敏电阻). I'll mention briefly.
- 电池参数：表 3-1 电机 12V、电池 11.1V 2200mAh；img_005 显示三节 3.7V 2200mAh 18650（3.7×3≈11.1V，串联成组——补充说明）。工作电压以电池实际供电为准【指导书注意 #4】：电机标称 12V 指额定电压，实际由 11.1V 电池供电，转速、PWM 计算时按实际电源理解。实验代码中的速度参数以实测调校为准——careful, don't over-claim. Just: 指导书表 3-1 中电机标 12V、电池 11.1V，两者并不矛盾：12V 是电机额定电压，小车实际工作电压以电池为准。
- 电源开关 OFF 省电（预备实验第4条：系统不使用时没有消耗电能，电池可以用得更久）。

## 4 第二章理论基础逐条讲透

引言段：第二章很短（指导书第 2–4 页），三小节：运动学、控制、传感器。这节逐条展开，给出推导、例子和与本套代码的对应关系。

### 4.1 差动驱动：左右轮速差怎么变成转向
- 4.1.1 三种运动状态（指导书原文三条）→ 各自生活化解释。
- 为什么四轮小车也能用两轮公式：四驱车四个轮子左右各二，同侧电机并联同速（补充说明？）——hmm. 指导书公式 for 两轮差动。小车的四个电机由 TB6612 双通道驱动，左侧两轮同速、右侧两轮同速 → 等效为两轮模型。TB6612 is dual H-bridge (常识)。Is that in materials? img_001: TB6612 四驱电机驱动. TB6612FNG is 双路驱动 — common knowledge, mark （补充说明）: TB6612FNG 内含两路 H 桥，左两个电机并联一路、右两个并联一路，因此四轮车在运动学上仍可按"左右各一虚拟轮"的两轮差动模型处理（补充说明）。Reasonable and helpful; marked.
- 推导（弧长法）：
  设车体刚体，转弯时整车绕瞬时中心 O 转过角度 θ，用时 t。左右轮与 O 的距离差半个轴距 L/2。轮子不打滑时，轮子走过的弧长 = 其到 O 的距离 × θ。
  外侧轮（右轮 vR）弧长 sR=(R+L/2)θ，内侧 sL=(R−L/2)θ。
  两式相减：sR−sL = Lθ；除以 t：vR−vL = L·(θ/t) = Lω → ω=(vR−vL)/L。
  两式相加除 2：(sR+sL)/2 = Rθ → v=(vR+vL)/2 = ωR。
  前提：轮子与地面不打滑、左右轮半径相同（补充说明）。
- 数字例（算例假设）：指导书未给出轴距，此处假设 L=15cm 仅为算例。vR=0.2m/s、vL=0.1m/s：
  v=(0.2+0.1)/2=0.15 m/s
  ω=(0.2−0.1)/0.15=0.667 rad/s（约 38.2°/s：0.667×180/π≈38.2——arithmetic fine）
  转弯半径 R=v/ω=0.225 m=22.5cm，绕左侧方向转（右快左慢 → 向左转）。
  特例：vR=vL=v → ω=0 直线；vR=−vL → v=0 原地旋转（指导书"左右两轮转速大小相等、方向相反"）。
- 对照运动函数（预告实验三）：run（前进：左右同速直线）、left/right（圆弧：一侧快一侧慢）、spin_left/spin_right（原地旋转：一侧正转一侧反转）。指导书第二章未给出这些函数，函数实现与代码逐行讲解见实验三详解。Brief says "六个函数" but lists five; I'll say "run、left、right、spin_left、spin_right 等运动函数" avoiding the count. Hmm, brief explicitly: "对照小车的 run/left/right/spin_left/spin_right 六个函数（预告实验三）". To be safe: "实验三将给出 run（前进）、left（左转）、right（右转）、spin_left（原地左转）、spin_right（原地右转）等运动控制函数" — "等"字兼容第六个（可能是后退函数）。Good.

### 4.2 PWM 调速
- 问题引入：单片机引脚只有 0/1 两态，怎么输出"中间电压"？→ 快速开关，时间平均。
- 占空比定义（指导书原文）：占空比 = 高电平时间 / 周期 × 100%。
- 平均电压公式（指导书原文）：电机平均电压 = 电源电压 × 占空比。例：电源 12V（表 3-1 电机额定）、占空比 60% → 平均 7.2V。若按 11.1V 电池实际供电，60% 对应约 6.7V（呼应指导书注意 #4——11.1×0.6=6.66）。Good, uses both.
- 为什么用 PWM 而不是降压电路：简单、高效（晶体管全开全关损耗小）——补充说明，one line, marked.
- 频率：指导书原话 "PWM频率一般选择10kHz-20kHz，避免人耳可闻噪声"。解释：频率太低，电机转速会在一个周期内波动，且开关噪声落入人耳可闻范围（补充说明解释）；选 10–20kHz 使噪声移出可闻频段。
- 现实：本套指导书全部实验代码用 50Hz 软件 PWM（周期 20ms），与第二章"10kHz–20kHz"不一致——这是教学简化【指导书注意 #3】：50Hz 在软件上容易实现（配合延时函数数时间），不依赖定时器/PCA 硬件资源，便于初学者看懂每行代码；代价是低速时电机可能有轻微抖动和可闻的嗡嗡声，属正常现象（补充说明，属推断性经验）。方向提醒：先学会软件 PWM 的思想，进阶再迁移到定时器硬件 PWM（第八章拓展方向——careful: don't claim 第八章内容。say "进阶方向"）。
- 软件 PWM 怎么工作预告：在一个 20ms 周期里，前 X ms 给高电平、其余给低电平，X 越大占空比越大。实验二详解将逐行看代码。

### 4.3 PID：从"开关控制"到"连续调节"
- 场景引入：巡线时小车偏了 3cm，怎么决定轮速差给多少？最朴素：偏了就打方向——开关式（bang-bang）；更好的做法：按偏差大小成比例给——引入 PID。
- 误差定义 e = 期望值 − 实际值。
- P（比例）：输出 ∝ e。作用（指导书表）：快速响应误差，成比例调节输出；增大加快响应，过大会引起振荡。例（巡线）：P 小 → 回线慢、弯道跟不上冲出线；P 大 → 一偏就猛打，冲过线心又反向猛打，蛇形摆动（振荡）。
- I（积分）：输出 ∝ e 的累计。作用：消除稳态误差，提高控制精度；增大加快消除静差，过大会引起超调。例（直行）：两电机有个体差异，同样 PWM 左轮略慢，小车持续向右缓偏——纯 P 需要一直存在一个小偏差才抵得住（稳态误差）；I 把这点"老偏差"攒起来加码，最终零偏差也能走直。但 I 大了：偏差已经纠正后，攒的量还没放掉，继续推 → 冲过头（超调），来回晃。
- D（微分）：输出 ∝ e 的变化率。作用：预测误差变化趋势，抑制振荡；增大增强阻尼，过大会放大噪声。例：偏差正在快速减小（马上就要回到线上了），D 提前"踩刹车"，防止冲过。D 大了：传感器读数毛刺被放大，输出跟着乱抖。
- 调参口诀：先 P 后 I 再 D：先把 P 调到能跟上弯道、略有一点摆动，再加小量 I 消静差，最后加 D 压振荡（补充说明，工程常用整定顺序）。指导书表格给出"增大…过大会…"的原则，口诀是它的操作化（补充说明）。
- 现实定位：本课程各实验代码采用开关式控制——传感器输出只有"检测到/没检测到"两态，程序据此执行固定动作（如发现障碍就转向），不计算误差连续量。开关式实现简单、够用；PID 是进阶方向，想深入可结合第八章"拓展与思考"与自动控制课程学习——careful: I said careful about 第八章. TOC has 第八章 拓展与思考. Saying "可结合指导书第八章'拓展与思考'" implies its content covers PID — unverified. I'll say: PID 属于指导书"拓展与思考"一章指向的进阶内容——no, still claims. Just: PID 是这门课的进阶方向，本文在实验详解中不再展开 PID 代码。Simple.

### 4.4 传感器：小车的"眼睛"
- 共同框架：物理量 → 传感器 → 电信号 → 单片机读入判断。
- 4.4.1 红外反射式（TCRT5000、E18-D80NK）：
  - 工作原理（指导书原文）：发射红外光→遇障碍物反射→接收管检测反射光。
  - 反射与吸收：白色/近处表面反射红外强，黑色表面吸收红外多、反射弱——TCRT5000 巡线正是靠黑线吸光、白底反光区分（补充说明 for the physics, though 应用：黑线检测 is guide原文）。
  - 输出形式：模块输出开关量（有反射/无反射）→ 适合开关式控制。Hmm — is this in materials? TCRT5000 modules typically digital output. 补充说明 mark. Keep one line.
  - 阈值电位器：模块上的电位器设定比较阈值，旋钮决定"多远的反射算检测到/黑白分界点"，环境光变化或传感器高度变化后需要重新调（补充说明）。
  - 特点（指导书原文）：成本低、响应快、易受环境光干扰。解释环境光干扰：太阳光/灯光里也含红外成分，会叠加到接收管（补充说明解释）。应用（指导书原文）：近距离避障、黑线检测。对应实验六（红外避障 E18-D80NK×2）、实验七（红外跟随）、实验九（巡线 TCRT5000×4）——三个实验都靠红外反射式。
  - E18-D80NK vs TCRT5000 差异：E18-D80NK 是漫反射式光电开关，检测距离可达 80cm（型号里的 80 即 0.8m——careful, D80 means 80cm detection. This is standard knowledge; mark 补充说明）。Hmm, E18-D80NK detection range 3-80cm adjustable. I'll say 检测距离远大于 TCRT5000（型号中"D80"即量程 80cm，可在几厘米到 80cm 间调节——补充说明）。Table 3-1 says 近距离障碍物检测. Fine.
- 4.4.2 超声波（HC-SR04）：
  - 原理（指导书原文）：测量声波飞行时间。发射超声→遇障碍物反射→接收。
  - 公式：距离 = 声速 × 飞行时间 / 2。为什么除 2：声波走的是"去+回"双程，飞行时间是双程时间。
  - 数字例：常温声速约 340 m/s（补充说明数值），若单片机测得往返 588 µs，距离 = 340×588×10⁻⁶/2 ≈ 0.1 m = 10 cm。反过来 1 cm 距离对应约 58 µs 往返（同例推算——it's the same example inverted, arithmetic OK: t = 2d/v = 0.02/340 = 58.8µs）。
  - 量程（指导书原文）：2cm–400cm。解释盲区：太近回波与发射波混叠（补充说明——careful, guide only says range. The "why min 2cm" is inference; mark or omit. I'll mark （补充说明）briefly.)
  - 特点（指导书原文）：测距远、精度中等、受角度影响大。解释受角度影响：障碍物表面斜的话，回波反射到别的方向，接收不到或测远（补充说明解释）。对应实验十、十一。

## 5 第三章设备与环境搭建的补充解读

### 5.1 组装顺序与为什么
- 指导书 3.3.1 四步：电机固定→轮胎→舵机/灯光/传感器→铜柱固定核心控制板。
- 解读：先装"重的、机械的"，再装"怕压的、电子的"；核心板最后用铜柱架起，避免与底盘金属短路（补充说明 for reasoning）。传感器支架按需配置。
- 组装完成后 3.3.3：通过预备实验进行系统测试——即先别急着跑实验一，先确认烧录、串口通。

### 5.2 接线前务必断电：为什么
- 指导书原文（表 3-9 提示框）：接线前务必断开电源！接线完成后仔细检查，确认无误后再通电！
- 解释：带电插拔/接错瞬间，电源正负短接或电源接到信号脚，可能烧毁传感器、驱动芯片甚至主控芯片；锂电池内阻小、短路电流大（补充说明）。断电接线 + 通电前查线，成本最低的安全措施。红+ 黑-（img_008）。

### 5.3 CH340 驱动：装没装好怎么看
- CH340 是什么：USB 转串口芯片，扩展板板载"CH340 烧录电路"（img_001），电脑通过它把 USB 口虚拟成一个串口（COM 口）（补充说明 one line for 定义——brief says 软件清单 one-sentence purposes include CH340 driver; a definition is warranted）。
- 安装来源：指导书 3.2.1"配置串口驱动（CH340）"，配套资料提供。
- 验证：micro USB 线连接开发板与电脑 → 我的电脑右键→属性→设备管理器→端口（COM 和 LPT）→ 出现"USB-SERIAL CH340 (COMx)"字样即成功（img_019：COM4；img_022：COM14；img_025：COM5——COM 号每台电脑不同，与占用无关，记下自己机器上的即可）。没有该条目 → 重新安装驱动（img_019 红字标注）。
- 再验证：打开串口监视器/串口调试助手验证串口通信正常（3.2.2）。

### 5.4 头文件安装（软件环境的最后一步）
- STC12C5A60S2.H → C:\Program Files\Keil\C51\INC（3.2.1 与预备实验①）。作用一句话：声明该芯片寄存器地址；不拷，编译报错找不到文件。

## 6 预备实验手把手

引言：预备实验是"实验之前的实验"，目的两条（指导书原文转述）：①掌握开发板与计算机硬件连接及基本结构；②熟悉 Keil IDE、ISP 下载软件、串口调试终端。设备：轮式机器人套件、ISP 下载线和串行接口线（共用）、计算机、电源。

### 6.1 认识系统组成
- 图 1.1（img_003）：单片机应用系统 = 硬件 + 软件；硬件 = 单片机 + 接口电路及外设等。原文：单片机控制的轮式机器人是通过串并口或USB接口通信交互，由硬件系统与软件系统相互结合组成的一个完整的智能控制系统。单片机必须与外围设备及软件组成一个完整的应用系统。
- 软件部分的两层（补充说明）：底层驱动（直接操作寄存器/延时/串口）与上层功能逻辑（按实验要求组织动作）——本套实验代码即按此组织（careful: don't claim code structure. Just say 概念上可分两层（补充说明））。Hmm brief says "软件两层框图" as part of认识系统组成. img_003 transcription shows 软件 as one box. I'll write: 图 1.1 中"软件"画成与硬件并列的一整框；从内容上可再分两层——底层是驱动程序（读写寄存器、延时、串口收发），上层是功能逻辑（小车该做什么）（补充说明）。OK.
- 图 1.2/1.3（img_004/005）：结构组成五件套 + MCU 介绍（STC12C5A60S2，兼容 STC89C52，DIP-40 红圈）。

### 6.2 第一步：接线
三条（指导书列表）：
1. ISP 接口（Micro USB）→ 计算机：程序下载用；
2. 串行接口（Micro USB）→ 计算机：调试和交互用；
3. 连接机器人到电池或供电电源。
说明：ISP 线与串口线共用一根 micro USB 线（预备实验设备清单"共用"；img_008"micro USB口，串口烧录通讯使用"）。板上 micro USB 只有一个口时如何既烧录又调试——指导书按两步进行，本预备实验先接 ISP 口烧录，再看串口输出（补充说明？）Hmm risky. The 预备实验 step ③ says 用串口调试软件查看单片机输出信息 and step ④ says 使用串口调试助手之前，首先使用串口线将单片机的串口与计算机的USB口相连. So sequence: burn via ISP connection, then connect serial for viewing. Two Micro USB ports likely (img_001 shows one Micro USB 接口标注…扩展板标注列表 has "Micro USB接口" once). img_008 says micro USB口串口烧录通讯使用 (single port used for both). So the same port serves ISP download and serial comm — 烧录和串口调试共用一个 USB 口，不同阶段用不同软件访问（补充说明）。That's consistent with "共用" in 设备清单. I'll phrase carefully: 预备实验设备清单注明"ISP下载线和串行接口线（共用）"，img_008 也说明 micro USB 口用于"串口烧录通讯"——即同一根线、同一个口，烧录阶段跑 STC-ISP、调试阶段跑串口助手，不需要来回换线。Good, grounded.
- 电源：电池盒两根红线经绿色接线端子接入（img_002），红+黑-（img_008）。

### 6.3 第二步：Keil 建工程全流程
开头【指导书注意 #1】版本问题段。
步骤（每步给界面细节 from img_009–018）：
0. 准备：建用户文件夹（方便管理程序）；拷 STC12C5A60S2.H 到 C:\Program Files\Keil\C51\INC。
1. 认识界面（img_009 µVision3 布局）：功能菜单（顶部菜单栏/工具栏）、项目文件列表（左侧 Project Workspace）、编辑区（右侧）、系统信息区（底部 Output Window）。
2. 新建工程：Project→New Project...（img_010，状态栏提示 Create a new project）→ 命名、保存在用户文件夹 → 工程文件为 *.uv2。
3. 选器件：Select Device for Target 'Target 1'（img_011）：Vendor=Atmel、Device=AT89S52、Family=MCS-51。
   为什么选 Atmel 的 AT89S52 而不是 STC12C5A60S2【关键解释，brief 要求】：本车芯片 STC12C5A60S2 与 51 系列兼容（预备实验原文"兼容 STC89C52"），Keil 的编译目标是 8051 指令集；器件库里选 AT89S52（同为 51 内核）即可生成正确的目标代码，AT89S52 仅充当"告诉编译器这是 51 内核"的通用模板；STC12 特有的寄存器由拷入的 STC12C5A60S2.H 提供定义，不依赖器件库选择。Hmm — is "Keil 器件库没有 STC12" in materials? It's the reason implied by brief ("STC12 与 51 兼容但 Keil 库里用 AT89S52 通用头"). I'll phrase as brief does, with one 补充说明 if needed. Actually brief states the reason directly; I can present it as the reason without extra marking since brief sanctions it. But careful precision: standard fact is Keil C51's device database doesn't include STC parts (older versions), so you pick a generic 8051. The header file provides SFR definitions. I'll write: 选 AT89S52 的原因：STC12C5A60S2 与 51 系列指令兼容，Keil 器件库中直接使用同为 51 内核的 AT89S52 作为目标器件，编译出的 8051 目标代码即可在 STC12 上运行；STC12 特有的寄存器定义由 STC12C5A60S2.H 头文件补上，与器件库选择无关（补充说明：这是 51 兼容芯片开发的通行做法）。
4. 弹窗（img_012）"Copy Standard 8051 Startup Code to Project Folder and Add File to Project?"：问是否把 8051 标准启动代码拷进工程。选"是"会得到 STARTUP.A51（补充说明：启动代码完成上电后的基本初始化，简单程序选"是"或"否"都能编译运行，本课程示例未依赖其修改）— hmm, "本课程示例未依赖其修改" is unverifiable. Just: 初学阶段任选其一均可，常见做法选"是"（补充说明）。Keep it minimal.
5. 新建 C 文件：File→New → 输入程序 → Save As（img_013：HelloRoBot.c，保存在 Chapter 1 目录）→ 注意关键字拼写、英文标点、字母大小写（指导书原文强调）。
6. 添加到工程：工程树 Target 1→Source Group 1 右键→Add Files to Group 'Source Group 1'（img_014）→ 选中 .c 文件添加；Source Group 1 前出现 + 号，展开可见文件；Keil 自动以不同颜色识别关键字，帮助少犯错（指导书原文）。
7. 配置生成 HEX：Target 1 右键→Options for Target 'Target 1'（img_015）→ Output 标签（img_016）→ 勾选 Create HEX Fi:（HEX 格式下拉为 HEX-80，Name of Executable 默认 HelloRoBot）→ 确定。这一步不做，编译不会产出 .hex——烧录软件找不到文件。
8. 编译：工具栏 Build（菜单 Project→Build target，快捷键 F7，img_017 为工具栏图标）→ 底部 Output Window 的 Build 标签看结果（img_018 逐行）：
   ```c
   Build target 'Target 1'
   compiling HelloRoBot.c...
   linking...
   Program Size: data=58.3 xdata=0 code=1246
   creating hex file from "HelloRoBot"...
   "HelloRoBot" - 0 Error(s), 0 Warning(s).
   ```
   解读每行：编译→链接→给出存储占用→生成 hex→错误/警告统计。标准：编译要求没有错误产生，允许出现警告（指导书原文）。hex 与 .c 同目录。代码块 should be ``` not ```c for a log — brief says 代码块 ```c. The build log isn't C code; I'll use plain ``` for the log and ```c where actual C appears (if any). Brief said 代码块 ```c — I think that's a style directive for code; for build log plain ``` is more accurate. I'll use ```c only for C snippets. Do I include any C snippet in this chapter? Maybe a minimal HelloRoBot-style example? The 预备实验 in guide doesn't show code content. Section 02 has actual experiment code. For this chapter, a tiny illustrative snippet could help (e.g., showing #include). But risk of fabrication — the guide's HelloRoBot program content is not in my materials. Better to avoid inventing program content. I can show a "骨架" example clearly marked as 示意（补充说明）? Safer to skip actual program code entirely; use the build log as the only code block. Fine.
9. 常见错误提示：分号用了中文标点、大小写写错等（呼应指导书"注意程序关键字的拼写、英文标点、字母的大小写"）。Don't invent specific error messages. Keep general.

### 6.4 第三步：STC-ISP 烧录全流程
【指导书注意 #2】段：烧录软件标题为 stc-isp-15xx-v6.85；指导书以选"STC89C52"为例，并注明小车上实际芯片是 STC12C5A60S2——两款都要能在型号列表里找到，选型以板上丝印为准。
1. 看芯片丝印：打手电筒、开发板稍微倾斜（指导书技巧）；img_020 是丝印特写示例（STC 89C52、35I-PDIP40），注意该照片为示例开发板，本车芯片应为 12C5A60S2 字样。
2. 连接与驱动检查：micro USB 连单片机与电脑，设备管理器确认 CH340（img_019）。
3. 打开 STC-ISP（img_021）：单片机型号下拉框 → STC89C52 在「STC89C51 系列」下；本车选 STC12C5A60S2（在 STC12 系列中——careful: img_021 dropdown shows STC89C51 系列 etc; STC12 series exists in STC-ISP lists but not shown in transcription. Brief says "两款都要能在列表里找到". I'll say 两款都能在型号下拉列表中找到。）
4. 选串口号：设备管理器查 USB-SERIAL CH340 (COMx)（img_022 左：COM14；右：STC-ISP 串口号下拉选中同一项）。
5. 打开程序文件：选 .hex 后缀文件（img_023，示例文件 shumaguan_dongtai1.hex，红字"打开.hex后缀的文件"）。注意：选工程目录下刚生成的 HelloRoBot.hex。
6. 烧录时序（img_024 前的关键操作，指导书原文）：插上 USB 后没有灯亮 → 点击"下载/编程" → L1 亮 → 立刻按下板子电源开关 → L2 亮 → 开始烧录 → 信息区出现"操作成功!"即烧录成功（img_024 红字"烧录成功!"，并显示固件版本号、代码长度校验和等信息）。
   为什么"先点下载再上电"（补充说明）：STC 系列单片机在上电复位的瞬间检测串口上是否有下载命令流，检测到才进入编程状态；所以软件先进入等待状态，再靠"上电"这个动作触发下载。若先上电，程序已开始运行，软件再点下载就连不上了——需要断电重新来一遍。This is standard STC behavior; mark （补充说明）. It's genuinely helpful.
   顺带：烧录开关拨到 ON（img_008：51/Arduino DownLoad Switch，烧录程序时拨 ON；用蓝牙/WiFi 模块时拨 OFF）。
7. RX/TX 红线（指导书原文"！！！"）：上传程序时不能占用 RX、TX 串口——蓝牙模块、WIFI 模块都要取下来，否则会烧录失败。解释：RX/TX 是串口收发两根线，烧录也走这两根线，外设插在上面会把数据流"抢走"（补充说明一句）。
8. 烧录成功的标志（img_024）：右侧显示"单片机型号: STC89C52、固件版本号: 7.2.6C、操作成功!"等；"成功计数"加一。
   Hmm — img_024 shows STC89C52 firmware 7.2.6C. Fine to transcribe as the screenshot content.

### 6.5 第四步：串口调试助手看输出
- 原理一句话：从 hex 下载到单片机那一刻起程序就开始运行，单片机向计算机发送信息（指导书原文④）。
- 步骤：串口线连接（同一个 micro USB 口）→ 设备管理器看串口号（img_025_conv：USB-SERIAL CH340 (COM5)）→ 若没有该条目，重装 CH340 驱动（指导书原文）→ 打开串口调试助手（img_027：CM 精装版 V3.8.3）→ 串口号选刚记下的 COM → 波特率、校验位 NONE、数据位 8、停止位 1 与程序中的设置一致才能正确显示（img_027 界面默认 9600-8-N-1；波特率具体值以实验程序代码为准——补充说明）→ 打开串口 → 接收区显示单片机输出。
- "Reset"按钮：可让下载到单片机内的程序重新运行一次（指导书原文）；改程序重新烧录后，或想从头看一遍输出时用它。
- 发送区：可向单片机发数据，交互用（预备实验目的提到"调试和交互"）。Careful — img_027 has 发送区设置. Fine to mention lightly.

### 6.6 实验收尾
- 指导书原文第 4 步：做完实验断开电源，将开关拨到关闭档（OFF），系统在不使用时没有消耗电能，电池可以用得更久。拆卸串口线还原。
- 加一条工作习惯（补充说明）：关电源前先关串口助手/烧录软件？No, unnecessary. Keep to guide + maybe 断电顺序不需要讲究，重点是断电后再拆线?Hmm — don't invent. Just restate guide.

### 6.7 预备实验的思考题
- 4 道题列出（指导书原文四题），本文不展开答案，参考答案见实验一章前（第二册开头）。

## 7 本章小结与衔接
- 三问三答小结：玩什么（32 学时、11 个实验：基础五+创新六，从点灯到带云台的超声波避障）；需要什么（硬件清单+四个软件）；怎么跑起来（Keil 写 C 编译成 hex → STC-ISP 烧录 → 串口助手看输出，一遍闭环，后面每个实验都重复）。
- 衔接：下一章进入实验一（七彩探照灯）——第一个真正的程序，从点亮一只 RGB 灯开始。预备实验思考题答案见实验一章前。

Length estimate: aiming ~700-800 lines. Tables count as lines. Let me write it now, being careful with:
- 中文标点
- No emoji, no 让我们/接下来/总的来说/综上/希望对您有帮助
- No 空洞排比/每段总结
- 术语首现定义
- （补充说明）（算例假设）标注
- 指导书注意 4 处

One more check: brief says "预备实验（硬件认识+Keil+烧录+串口调试）" and item 6 lists "认识系统组成（硬件=单片机+接口电路外设、软件两层框图）". OK covered.

Also brief item 3: "扩展板把单片机的引脚引到哪里：IN1~IN8 传感器口、电机驱动口、舵机口 J1、RGB 灯口 J24、超声波口、串口/ISP 口；img_001/img_002/img_008 的接口说明整理成表". I'll make a combined table: 本课程主线接口表:
| 接口 | 板上标注/丝印 | 接什么 | 备注 |
- 串口/ISP 口: micro USB（CH340 烧录电路）| 烧录+串口调试 | img_008
- 传感器口 IN1~IN8 | — | 各传感器模块排线 | brief given
- 电机驱动口 | TB6612 四驱电机驱动（正面）/左、右电机接口（背面）| 4 个直流减速电机 | img_001
- 舵机口 J1 | 丝印 Servo | 9G 舵机，棕 GND/红 VCC/橙 IO0 | img_008
- RGB 灯口 J24 | 标注"RGB 车灯" | 七彩探照灯模块 | img_001（J24 编号见实验一——careful. I'll write 编号 J24 为指导书实验章节所用——can't verify. Alternative: just "RGB 灯口（J24）" without sourcing claim. The brief gives J24; I include it as given. OK.)
- 超声波口 | 标注"超声波模块"，旁边 J16 跳线 MVCC->5V | HC-SR04 | img_001/008
- 四路巡线口 | 标注"四路巡线" | TCRT5000×4 | img_001/002
- 左/右避障寻光口 | 标注"左避障/寻光""右避障/寻光" | E18-D80NK、光敏电阻 | img_001/002
- 电池盒接口 | 绿色接线端子 | 11.1V 电池组 | img_002/008
- 烧录开关 | 51/Arduino DownLoad Switch | 烧录拨 ON，蓝牙/WiFi 拨 OFF | img_008

Good. For IN1~IN8, phrase: 扩展板把外接传感器/外设的接口按 IN1~IN8 编号引出（各实验章节给出每个口对应的模块；图 1.4 标注图按功能分区标注为四路巡线、左右避障/寻光、颜色识别、RGB 车灯、超声波模块等）。Hmm, this blends. Simpler: state per brief: 传感器口 IN1~IN8——各传感器模块通过排线插到这些编号接口上，具体分配见后续实验详解。Accept.

Wait — actually, let me reconsider whether IN1~IN8 might conflict with section 02/03 which are already written. Let me grep those files for "IN1" and "J24" to align terminology. Good idea for consistency.

Also check how 02/03 refer to PWM frequency (50Hz) and 轴距 assumptions, to stay consistent.

Let me grep.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/.zcode/workspace/default/robot-guide/sections\" && grep -n \"IN1\\|IN2\\|IN3\\|J24\\|J16\\|J1\\b\" *.md | head -40", "description": "检索已完成章节中的接口编号提法"}` → `02_实验一_实验二.md:94:接线说明：指导书正文"LED_R连接到主控板上的数字EA口，LED_G和LED_B分别接在主控板上的ALE和PSEN"对应上表前三行——EA、ALE、PSEN 是这三个引脚在传统 8051 里的名字，本实验把它们用作 P4.6、P4.5、P4.4。扩展板侧接口在主控板原理图中为接插件 J24（XH2.54 4P），2、3、4 脚分别为 LED B、LED G、LED R 信号（img_036），1 脚未标注信号名，按共阴模块应接公共地，以扩展板丝印为准。模块上 R、G、B 三根信号线由 L1、L2 两只 LED 共用，所以两盏灯始终显示同一颜色。 02_实验一_实验二.md:111:主控板原理图（i …[截断,原长5053]`

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-03 18:15）

写作前先与已完成章节做术语对齐（IN1~IN8、J24、PWM 频率等提法）。

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Good, consistent terminology confirmed:
- J24 = RGB 灯接口（XH2.54 4P 接插件）
- J1 = 舵机接口
- 舵机 SG90 confirmed in 03 file ("舵机 SG90 需连接到舵机接口 J1 上")
- TB6612 dual H-bridge, A路一侧 B路另一侧 — consistent with my planned 补充说明
- run() function exists; 03 file has run with time param etc.

Let me also check what the 02/03 files say about 50Hz PWM and 轴距 (L) and whether they mention IN1~IN8 anywhere. From grep, no IN1~IN8 hits. So the brief's "IN1~IN8 传感器口" doesn't appear in later chapters. I should be careful: since no other chapter references IN1~IN8, including it as fact could be inconsistent. The brief explicitly asks for it though: "扩展板把单片机的引脚引到哪里：IN1~IN8 传感器口、电机驱动口、舵机口 J1、RGB 灯口 J24、超声波口、串口/ISP 口". I'll include IN1~IN8 but hedge appropriately: the BST-4WD expansion board routes sensors via numbered headers — hmm. Actually, wait. Since the brief instructs it, presumably the coordinator knows the full guide (later chapters, e.g., 实验六~十一 extracts) mention IN1~IN8. The later chapters I have are only 实验一~五 which don't use IN1~IN8 (those experiments use P2/P0/P4 directly). Innovation experiments (六~十一) likely reference IN1~IN8 for sensor interfaces. So including it is safe per brief. I'll phrase: "扩展板把常用传感器接口编号为 IN1~IN8 引出（各传感器具体插哪个口，见第六~十一章详解与第三章接线图）" — hmm, but I don't have evidence for "编号为 IN1~IN8". The brief says "IN1~IN8 传感器口". I'll just write it plainly as the brief instructs: 传感器口 IN1~IN8。

Let me quickly check the 50Hz PWM statement in 02 file and any 轴距 mention.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/.zcode/workspace/default/robot-guide/sections\" && grep -n \"50Hz\\|50 Hz\\|20ms\\|20 ms\\|轴距\\|10kHz\\|10 kHz\\|SG90\\|9G\" *.md | head -30", "description": "检索已完成章节中 PWM 频率、轴距、舵机型号提法"}` → `02_实验一_实验二.md:372:**PWM（脉宽调制）**：大白话：让引脚反复"开—关—开—关"，开的时间占比不同，等效给出去的"劲"就不同——像快速开关水龙头，水流平均压力由开的时间比例决定。准确表述：PWM 用数字输出产生方波，占空比 = 高电平时间 ÷ 周期 × 100%，电机平均电压 = 电源电压 × 占空比（指导书第二章 2.2.2）。第二章还指出 PWM 频率一般选 10kHz–20kHz 以避开人耳可闻噪声；本实验的软件 PWM 只有 50Hz，是教学实现的折中，调速刻度也只有 21 档（push_val 取 0–20）。 02_实验一_实验二.md:439:- 周期 = 20 × 1ms = 20ms，频率 =  …[截断,原长3501]`

> ⚠️ 该条助手消息出错: {"name": "AiSdkModelAdapterError", "data": {"message": "Model request was cancelled.", "code": "model_request_cancelled", "attribution": {"source": "runtime", "reason": "cancelled", "errorPhase": "str …[截断,原长407]

<details><summary>💭 `zcode-general-purpose` 思考链（GLM-5.3-Flash）</summary>

Everything is consistent with my plan. Now I'll write the chapter. Target 600–900 lines. Let me write carefully, in full, with the structure agreed. I'll compose the complete Markdown file now.

Key discipline:
- 中文标点（，。：；（）"" —— use full-width）
- No emoji
- No forbidden phrases
- Terms defined at first occurrence
- All numbers/models from materials; missing → "指导书未给出"; supplements marked （补充说明）or （算例假设）
- Tables only for enumerative facts
- 代码块 ```c for C code (only build log as plain text — I'll use plain ``` for the log since it's compiler output, not C; the brief said 代码块 ```c which I read as "use fenced code blocks, C where applicable")

Structure with headings:
# 第一章 全书导读与预备篇（小白详解）
> 导语
## 1 这本指导书怎么用
### 1.1 这是一门什么课
### 1.2 全书结构地图
### 1.3 建议的打开方式
## 2 你需要准备的东西
### 2.1 硬件清单
### 2.2 软件清单
### 2.3 一句话总览：哪些器材对应哪些实验 (maybe merge; optional)
## 3 读懂小车：整机结构
### 3.1 整车组成与主控芯片
### 3.2 扩展板：把单片机的引脚"翻译"成好接的插座
### 3.3 供电、开关与指示灯
## 4 第二章理论基础逐条讲透
### 4.1 差动驱动：左右轮速差怎么变成转向
### 4.2 PWM 调速：用开关的"时间占比"调电压
### 4.3 PID：从开关式控制到连续调节
### 4.4 传感器：小车的"眼睛"
## 5 第三章设备与环境搭建的补充解读
### 5.1 组装顺序
### 5.2 为什么接线前必须断电
### 5.3 CH340 驱动：装没装好怎么看
### 5.4 头文件安装
## 6 预备实验手把手
### 6.0 实验目的与器材
### 6.1 认识系统组成
### 6.2 第一步：接线
### 6.3 第二步：Keil 建工程全流程
### 6.4 第三步：STC-ISP 烧录
### 6.5 第四步：串口调试助手
### 6.6 实验收尾
### 6.7 预备实验思考题
## 7 本章小结与衔接

Now write. I'll aim for roughly 750 lines. Let me be thorough but every sentence must carry information.

A few numeric checks:
- ω = (0.2−0.1)/0.15 = 0.1/0.15 = 0.6667 rad/s. Degrees: 0.6667 × 57.2958 ≈ 38.2°/s. ✓
- R = v/ω = 0.15/0.6667 = 0.225 m = 22.5 cm. ✓
- 12V × 60% = 7.2V. ✓ 11.1 × 60% = 6.66 ≈ 6.7V. ✓
- Ultrasonic: t=588µs, d = 340 × 588e-6 / 2 = 0.09996 m ≈ 10 cm. ✓ 1cm ↔ 2×0.01/340 = 58.8 µs. ✓
- Full spin example: 原地旋转 vR=0.1, vL=−0.1, L=0.15 → ω=0.2/0.15=1.333 rad/s, 一圈 2π/1.333 ≈ 4.71 s. Could add as second 算例. Nice.
- 直线: vR=vL=0.15 → v=0.15, ω=0.

For the derivation, present clean:
设整车绕瞬时中心 O 转弯，右轮在外、左轮在内（右转时相反），轴距 L，车体中心到 O 的距离 R。刚体转弯时，左右轮在时间 t 内转过的角度相同，都是 θ。不打滑时每个轮子走过的弧长 = 它到 O 的距离 × θ：
右轮：sR = (R + L/2)·θ
左轮：sL = (R − L/2)·θ
两边同除以 t 得速度（v=s/t），…
相减：vR − vL = L·(θ/t)。θ/t 正是整车绕 O 转动的角速度 ω（单位 rad/s）。→ ω=(vR−vL)/L
相加取平均：v=(vR+vL)/2 = R·ω。R=v/ω 即转弯半径。

Also explain "瞬时中心"：转向那一刻小车整体绕某个点转，这个点此刻不动，叫瞬时中心（指导书"机器人绕瞬时中心做圆周运动"）。

For run/left/right/spin_left/spin_right mapping — grounded in 02/03 files: run() exists in experiment 2; experiment 3 has 运动函数 with time param. I'll phrase: "实验三将给出 run（前进）、left（左转）、right（右转）、spin_left（原地左转）、spin_right（原地右转）等运动控制函数" — matches brief's function list.

PWM section: mention 调速刻度 0–20 → 占空比 5%–100%? From 02: push_val 0–20, initial 5 (25%), run sets 10 (50%). I can preview: 实验二代码的占空比刻度是 0–20 档。That's cross-referencing chapter 02's content; it's part of the same book series, fine to preview as "实验二详解将看到". Keep it as a forward pointer with the fact from the companion file. Since the brief for THIS chapter says "对照小车的…预告实验三" — forward pointers are wanted. But careful: this chapter's scope is 指导书 chapters 1-3 + 预备实验; referencing 实验二 code facts is allowed as preview since the whole project is one series and 02 file already exists. I'll keep such previews brief and accurate.

指导书注意 #4 wording: "表 3-1 中电机标 12V、电池 11.1V：工作电压以电池实际供电为准。" Put in §2.1 (after hardware table) and use in §4.2 example.

指导书注意 #1: Keil version — put in §2.2 software table note + §6.3 opening. Count as one merge (possibly two mentions). I'll count "处" as distinct placements: I'll deliberately place the four notes at clearly findable spots:
1. §6.3 开头（Keil 版本）
2. §6.4 开头（STC-ISP 型号）
3. §4.2（PWM 频率）
4. §2.1 硬件清单后（电机 12V/电池 11.1V）
That's 4 merges; I may echo #4 briefly in §4.2 without re-counting.

Also the L1/L2/L3 lamp ambiguity note — I'll include as an extra 平实 clarification in §3.3 (not counted among the four assigned notes, but it is also a 指导书 observation). The brief's four assigned notes are the ones to report; extra clarifications fine.

Thinking question list (4 questions from guide). And note "参考答案见实验一章前".

Now — about "表 3-1" numbering: The extract shows TBL 6 as 核心控制器 table in 3.1.1. The brief calls it 表 3-1. I'll refer to "第三章硬件清单表（指导书表 3-1）" loosely as "指导书 3.1 节的硬件清单表". Safer: "第三章 3.1 节的设备表". The brief says 表 3-1; I'll use that once: "指导书表 3-1（3.1.1 核心控制器）". OK.

Page numbers from TOC: use in the map table. 实验一 22、实验二 27、实验三 36、实验四 47、实验五 54、实验六 67、实验七 78、实验八 89、实验九 100、实验十 117、实验十一 146、第六章 162、第七章 165、第八章 167、预备实验 8。✓

For 实验八 寻光行走: 光敏电阻 ×2 功能"寻找光线" (表 3-2). ✓ For 实验七 红外跟随: no dedicated sensor listed in 3.1 tables... 红外循迹 TCRT5000 或避障 E18-D80NK could serve; guide TOC only says 红外跟随. img_028 宣传图 shows 智能追光 etc. For the map table "对应器材" column, for 实验七 I'll write 红外传感器（反射式）without specifying model, or "红外反射式传感器（型号见实验七详解）". Hmm. Actually E18-D80NK ×2 "近距离障碍物检测" — 跟随 typically uses the same pair. But to avoid fabrication: for 实验七 write "红外反射式传感器（红外避障/循迹同类，详见实验七）". Actually simpler and safest: the column header "对应器材" only fill where directly supported by 3.1 tables: 实验一→七彩探照灯模块（img_002）；实验二/三→直流减速电机×4＋TB6612；实验四→舵机；实验五→按键；实验六→E18-D80NK×2；实验七→红外反射式传感器；实验八→光敏电阻×2；实验九→TCRT5000×4；实验十→HC-SR04；实验十一→HC-SR04＋舵机云台。实验七's 红外反射式传感器 is directly implied by title "红外跟随" and 2.3.1 红外传感器 应用. Fine.

Also, brief item: "最后报告与验收怎么考" — from TOC 第六章 实验报告要求与评分标准. I can also mention 1.3 能力表 mentions 成果汇报 via 分组实验/任务分配/成果汇报. And 实验意义 mentions 分组实验. I'll say: 课程考核落在第六章"实验报告要求与评分标准"，即以实验报告和现场验收为抓手；每个实验详解末尾会提示报告要点。Hmm "每个实验详解末尾会提示报告要点" — is that true of 02/03? Let me not claim structure of other chapters. Just: 具体的报告格式与评分细目以第六章为准，本文不提前展开。

One more thing: the brief says section 1 should cover "课程性质 32 学时/综合性设计性实验、适用专业、全书 11 个实验的结构地图：基础实验一~五练什么、创新实验六~十一练什么、最后报告与验收怎么考；建议的打开方式". Covered.

Also 导语 should mention 本册定位 and prerequisite.

Writing style guardrails: avoid starting sections with "接下来". Use plain statements. Avoid per-paragraph summaries.

Let me also double check "servo motor 伺服电机" in 预备实验 结构组成: "小车底盘、车轮、扩展板、伺服电机、电池盒" — 舵机=伺服电机, I'll note 伺服电机即舵机（servo）—03 file uses 舵机（servo，伺服舵机）. Fine: "伺服电机（即舵机，servo）".

电池盒: img_002 shows 三格电池盒 via 绿色接线端子 two red lines; img_005 shows 3×18650 3.7V 2200mAh. 表3-1 says 锂电池组 11.1V 2200mAh. Consistent story: 三节 3.7V 18650 串联 ≈11.1V（补充说明 for 串联 statement — actually arithmetic 3×3.7=11.1 makes 串联 evident; I'll state "三节 3.7V 2200mAh 的 18650 电芯，3.7V×3=11.1V，即表 3-1 的 11.1V 电池组" and mark （补充说明：三节串联成组）. The multiplication is factual arithmetic from materials. I'll keep one light （补充说明）.

充电: DC 充电座 8.4V-12.6V 18650 锂电池充电使用，注意此 DC 口在驱动板上。Li-ion 3S charging voltage 12.6V = 4.2×3 — I can note 充电电压范围 8.4V–12.6V 正对应三串锂电的充电电压区间（补充说明）。Maybe too deep; one short parenthetical is fine, marked. Actually 8.4V would be 2S charging... 8.4–12.6V range covers 2S–3S. Saying "正对应三串" for the upper end only. I'll say: 该范围上限 12.6V 即三节串联锂电充满时的电压（4.2V×3）——hmm 4.2 not in materials. Too deep; skip. Just present the range as-is.

Now the L1/L2 burning-sequence LEDs vs L1 low-voltage indicator: I'll write the clarification in §6.4 where the sequence appears, cross-referencing §3.3. Phrase: "这里的 L1、L2 是指导书预备实验对板上指示灯的叫法；扩展板使用说明（图 1.4 之 img_008）中 L1 又是低电压指示灯、L3 是供电指示灯，两处 L1 指导书未说明是否同一盏。操作时不必纠结名称，按'点下载→哪盏亮→按电源开关→哪盏再亮'的顺序观察即可。" Good, 平实.

Length management: I'll write ~730-800 lines. Let me draft the full text now in one Write call. I need to be careful with 中文标点 throughout and UTF-8 (Write tool writes UTF-8 by default).

Also headings: brief wants 小节 ### max depth. I'll use bold paragraphs (like **X**：) inside subsections as 02/03 do.

Draft now. I'll write the content mentally section by section and then output.

Line count estimation: my content will likely be ~750 lines with tables and blank lines. Good.

One more consideration: "表格只用于枚举型事实，过程性内容用段落" — my tables: 课程信息表、实验地图表、能力目标表、硬件清单表、软件清单表、扩展板接口标注表、本课程主线接口表、供电指示灯表(maybe paragraph instead—指示灯 is enumerative, table ok)、PID 表、编译输出(log as code block not table)、串口助手参数表(maybe paragraph)。OK.

PID 表 from guide (控制项/作用/参数调节原则) reproduce + expand in text.

Now write.

</details>

### 🤖 助手（`zcode-general-purpose` GLM-5.3-Flash，2026-10-03 18:20）

两份必读材料已读完，与已完成章节（02、03）的术语（J24、J1、SG90、TB6612 双路、50Hz 软件 PWM、push_val 0–20 刻度）已核对一致。现在撰写第一章。
