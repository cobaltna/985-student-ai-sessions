---
name: github-machine
description: 本机（UserX/Windows）GitHub 工具链专属约定：gh CLI 路径与账号、github.com 代理 127.0.0.1:1088、git-bash curl 必挂须用 pwsh、大包推送参数、设备码授权流程、Release 资产 ASCII 命名。凡是涉及 GitHub 推送/克隆/gh 命令/Release 发布/授权过期/连接 reset/HTTP 000 的任务都要先读本技能。
---

# GitHub 本机工具链（实测踩坑定稿 2026-09-30）

## 网络硬规则（最重要）

- **git-bash 的 curl 连 github.com 必挂**（HTTP 000，不走代理）。GitHub HTTP API 一律用 pwsh：
  `pwsh -NoProfile -Command "Invoke-RestMethod ..."`（自动走 Windows 系统代理）。
- git 对 github.com 走全局代理 `http.https://github.com.proxy=http://127.0.0.1:1088`，
  且已全局配置 `http.https://github.com.version HTTP/1.1` + `postBuffer 524288000`
  + `lowSpeedLimit 1000` / `lowSpeedTime 60`（只作用于 github.com，别改其他域）。
  **为什么**：代理上 HTTP/2 大包易被 reset（curl 65），HTTP/1.1 实测一次成功（28MB 推送）。
- 推送仍被 reset 时：直接重试 1~2 次；再不行改 push 分批或用 `gh api` 传小文件。
- gh CLI 本身联网正常（Go 栈自选代理），`gh api` 可放心用。

## gh CLI

- 安装位置 `C:\Program Files\GitHub CLI\`，已在**系统 PATH**（新开终端直接可用）。
  **ZCode 旧会话 shell**（启动早于安装时间）需手动：
  `export PATH="$PATH:/c/Program Files/GitHub CLI"`。
- 账号 **cobaltna**（id 139681237），凭据在 gh keyring，scopes: repo/read:org/gist/workflow。
  查登录态：`gh auth status`。

## 授权过期 → 设备码流程（不要开交互窗口干等）

1. 生成设备码（用 pwsh，不是 curl）：
   `Invoke-RestMethod -Uri 'https://github.com/login/device/code' -Method Post -Body @{client_id='178c6fc778ccc68e1d6a'; scope='repo read:org gist workflow'} -Headers @{Accept='application/json'}`
   （client_id 是 gh CLI 官方公开 ID；响应含 user_code / device_code / interval）
2. `AskUserQuestion` 让用户打开 **github.com/login/device** 输入 user_code 并 Authorize。
3. 后台每 5s 轮询 `POST https://github.com/login/oauth/access_token`
   （body: client_id + device_code + `grant_type=urn:ietf:params:oauth:grant-type:device_code`），
   拿到 access_token 后写临时文件 → `gh auth login --hostname github.com --git-protocol https --with-token < 文件` → 删文件。

## Release / 仓库小抄

- **Release 资产一律用 ASCII 文件名**（中文文件名部分下载工具会编码错乱），README 下载指引同步改。
- 建仓+推送：`gh repo create <name> --public --source . --push`（先 `git branch -M main`）。
- 发版：`gh release create vX.Y <file> --title ... --notes ...`。
- topics：`gh repo edit <owner>/<repo> --add-topic ...`（小写字母/连字符）。
- gh JSON 字段名以 `gh <cmd> --json` 的报错提示为准（如 `isDraft` 而非 `isPublished`）。

## 噪音（无害，别当错误）

- `git add`/`git commit` 会刷 "LF will be replaced by CRLF" 警告（Windows autocrlf），可忽略。
- gh CLI 未加 PATH 的 shell 里 `gh` 报 command not found → 先按上面 export PATH。
