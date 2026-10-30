---
name: memory-web-scraping
description: Use when 爬取/抓取网页内容、处理微信公众号/微博/小红书/头条/bilibili/百度系站点内容、绕 JS 渲染墙、WebFetch 失败返回环境异常、使用 playwright persistent context、pip 安装 playwright 相关任务。含用户长期沉淀的各站点抓取特性、两步法采集策略与成功率经验。
---

# 记忆：网页爬取与内容采集（长期踩坑沉淀）

## 核心策略：两步法
1. **HTTP requests 快筛**：处理非微信/微博/头条的 URL（快，参考成功率 30/42）。
2. **playwright persistent context 兜底**：处理微信（headless=False 必免环境异常）+ 微博/头条（lo_profile）+ HTTP 失败项。

- WebFetch 在多数目标站返回「环境异常」页或混淆 JS → 直接用 playwright persistent context，别反复试 WebFetch。
- 头条/微博用 HTTP requests 返回 0 字符（JS 墙）→ 必须 playwright persistent context（headless=False + 系统 Chrome + profile 目录），无需登录，参考成功率 34/34。
- 行为模拟：随机间隔 `random.uniform(2.5, 5.0)` 秒 + 随机滚动 `mouse.wheel(0, randint(80, 300))`。
- 登录墙站点（微信、小红书）需要用户先扫码/点击验证 → 预留交互，headless=False。

## 站点特性表
| 站点 | 特性与对策 |
|---|---|
| bendibao.com | WebFetch 一律 failed → 用 sohu / bjd / 163 / beijing.gov.cn 替代 |
| haokan / yoojia.baidu | 只返回推荐框架，无正文 |
| toutiao | WebFetch 返回混淆 JS；playwright persistent context 可拿全文（视频页仅标题） |
| xiaohongshu | persistent context 也仅返回约 77 字 → 登录墙，需用户先扫码 |
| 微信 | headless=True 必触发环境异常 → headless=False 让用户点验证；图片型文章（明星活动合集）只返回标题框架无正文 |
| 头条/微博 | HTTP requests 返回 0 字符（JS 墙）→ playwright persistent context（无需登录） |
| bilibili | HTTP 可拿视频标题/描述（约 1000 字），但非完整内容 |
