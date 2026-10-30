---
name: minecraft-bedrock-dev
description: Minecraft 基岩版（Bedrock Edition）模组/Add-On 开发辅助，规定"本地官方文档优先、网络兜底"的检索流程。凡是涉及基岩版行为包/资源包、Script API（@minecraft/server、@minecraft/ui 等模块）、方块/实体/物品 JSON 组件、manifest、loot table、Molang、动画/模型等规范或官方 API 的查询、编写、排错，都要先加载本 skill——即使没明说"查文档"。触发词：基岩版、Bedrock、addon、行为包、资源包、Script API、@minecraft。
---

# Minecraft 基岩版开发：文档检索流程

## 核心规则：先本地查找，后网络搜索

本机有一份爬取好的基岩版官方创作者文档快照（约 900 个 md，含 Script API 全量类/接口参考）：

```
C:\Users\UserX\Downloads\minecraft-crawl-grammer\minecraft_docs\markdown
```

查询任何模组代码规范、API 签名、JSON 字段、事件名时，**先用 Glob/Grep 搜这个目录**，确认本地没有答案或答案过时，才上网搜索。这样更快、且内容与官方文档一致。

## 第一步：搜本地文档

目录是扁平结构，文件名为 `<标题>_<8位hash>.md`（空格→`_`，`@`→`_`，标题被截断过）。hash 无法记忆，**永远用通配符匹配文件名，用 Grep 搜内容**：

- 按类型找 API 参考：`*_Class_*.md`（约 400 个类）、`*_Interface_*.md`、`*_Module_*.md`
- 例：找 `EntityHealthComponent` → Glob `**/EntityHealthComponent_Class_*.md`
- 找模块总览：`__minecraft_server__Module_*.md`、`__minecraft_common__Module_*.md`
- 按主题找教程/规范：Glob `*BLOCKS_DOCUMENTATION*`、`*ADDONS_DOCUMENTATION*`、`*manifest*`、`*Molang*` 等
- 按字段/事件名搜内容：Grep 关键词（如 `"minecraft:destructible"`、`playerInteractWithEntity`），列出命中文件再 Read

建议组合拳：Glob 缩小文件 → Read 命中文件；拿不准标题时直接 Grep 内容，能一次搜全 905 个文件。Grep 的 path 直接给该目录即可；不要在 bash 里 `grep pattern *.md`——900+ 文件展开传参会报 Argument list too long，用递归形式或 Grep 工具。

## 第二步：网络兜底

仅当本地搜不到、或怀疑快照过时（爬取快照不跟随最新版本，新 API/实验性特性可能缺失）才上网。优先官方源：

- Microsoft Learn 创作者文档：`learn.microsoft.com/minecraft/creator`
- Script API 参考（同站 Command/Script 部分）；bedrock.dev、wiki.bedrock.dev 可作补充

上网查到后，若发现本地快照明显滞后（例如某 API 已废弃/新增），在回答里提醒用户一句。

## 回答要求

- 引用本地文档时给出文件路径，方便用户点开核对。
- 涉及具体 API 时以本地文档中的签名为准，不要凭训练记忆默写 API——基岩版 API 迭代快、弃用多。
