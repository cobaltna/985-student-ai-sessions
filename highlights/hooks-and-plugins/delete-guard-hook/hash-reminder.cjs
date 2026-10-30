#!/usr/bin/env node
'use strict';

/*
 * no-overdefense PreToolUse 钩子（提醒式，不阻断）。
 * Bash 命令或写文件内容里出现哈希计算时，向对话注入一条提醒；
 * 每个会话最多提醒一次。任何异常都静默放行（fail-open）。
 *
 * 部署说明：本脚本放在稳定路径 ~/.zcode/hooks/hash-reminder.cjs，
 * 插件的 hooks.json 以绝对路径引用。本版本 ZCode 的 process 钩子对
 * ${CLAUDE_PLUGIN_ROOT} 模板变量和 matcher 正则 alternation 均不生效，
 * 须用简单 matcher + 绝对路径（delete-guard 同款已验证模式）。
 *
 * 输出契约（ZCode PreToolUse 钩子，严格 schema，多余 key 会被拒收）：
 *   {"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"..."}}
 * 不带 permissionDecision 即为默认放行；未命中时 stdout 留空、exit 0。
 */

const fs = require('fs');
const os = require('os');
const path = require('path');

// 只匹配哈希的实际调用（命令行工具或代码 API），不匹配纯文字提及。
const HASH_PATTERN = /\b(md5sum|sha1sum|sha256sum|sha512sum|shasum)\b|get-filehash|certutil[^\n]*hashfile|\bhashlib\b|createhash\s*\(|crypto\.subtle\.digest|openssl\s+dgst/i;

const BASH_MESSAGE = '过度防御提醒：检测到哈希计算。如果目的是对比文件是否相同或确认改动，直接用 diff、比较文件大小或看文件名即可；哈希只在任务确实要求防篡改或一致性校验时使用，而且不需要对每个文件逐个计算。如果本次计算确实是必要的，忽略本提醒。';

const WRITE_MESSAGE = '过度防御提醒：新写入的代码里包含哈希计算。请确认这段校验有真实用途（任务要求的完整性或一致性校验，且结果会被实际使用）；如果确实是必要的，忽略本提醒。';

function readStdin() {
  return new Promise((resolve) => {
    let body = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (chunk) => { body += chunk; });
    process.stdin.on('end', () => resolve(body));
    process.stdin.on('error', () => resolve(''));
  });
}

function reminderText(toolName, toolInput) {
  if (toolName === 'Bash') {
    return HASH_PATTERN.test(String(toolInput.command || '')) ? BASH_MESSAGE : null;
  }
  if (toolName === 'Write') {
    return HASH_PATTERN.test(String(toolInput.content || '')) ? WRITE_MESSAGE : null;
  }
  if (toolName === 'Edit') {
    // 只看新增内容：删除哈希代码、改动无关行都不该触发。
    return HASH_PATTERN.test(String(toolInput.new_string || '')) ? WRITE_MESSAGE : null;
  }
  return null;
}

(async () => {
  try {
    const raw = await readStdin();
    if (!raw.trim()) return;
    const event = JSON.parse(raw);
    const text = reminderText(event.tool_name, event.tool_input || {});
    if (!text) return;

    const flagDir = path.join(os.tmpdir(), 'no-overdefense');
    const flagFile = path.join(flagDir, `${event.session_id || 'session'}.flag`);
    if (fs.existsSync(flagFile)) return;
    fs.mkdirSync(flagDir, { recursive: true });
    fs.writeFileSync(flagFile, new Date().toISOString());

    process.stdout.write(JSON.stringify({
      hookSpecificOutput: {
        hookEventName: 'PreToolUse',
        additionalContext: text,
      },
    }));
  } catch {
    // 静默放行：钩子自身出错不能影响正常工具调用。
  }
})();
