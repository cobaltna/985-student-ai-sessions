#!/usr/bin/env node
/**
 * ACP client used to test the bridge without OpenFilm: initialize, session/new, a prompt with a
 * tool call, a second prompt that must remember the first, cancel, close.
 *
 *   node acp-test.mjs [--cwd DIR] [--cancel]
 */
import { spawn } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const arg = (name, fallback = null) => {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
};

const cwd = arg('--cwd', process.cwd());
const cancelTest = process.argv.includes('--cancel');

const child = spawn(process.execPath, [join(HERE, 'bridge.mjs')], {
  stdio: ['pipe', 'pipe', 'pipe'],
  env: { ...process.env, ZCODE_CLI: process.env.ZCODE_CLI || undefined },
});

child.stderr.setEncoding('utf8');
child.stderr.on('data', (d) => process.stderr.write(`  [bridge] ${d}`));
child.stdout.setEncoding('utf8');

let nextId = 1;
const pending = new Map();
let buffer = '';

child.stdout.on('data', (d) => {
  buffer += d;
  let i;
  while ((i = buffer.indexOf('\n')) >= 0) {
    const line = buffer.slice(0, i).trim();
    buffer = buffer.slice(i + 1);
    if (!line) continue;
    let msg;
    try { msg = JSON.parse(line); } catch { console.log('  << not JSON:', line.slice(0, 200)); continue; }
    if (msg.id !== undefined && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(new Error(`${msg.error.code}: ${msg.error.message}`));
      else resolve(msg.result);
      continue;
    }
    if (msg.method === 'session/update') {
      const u = msg.params.update ?? {};
      switch (u.sessionUpdate) {
        case 'agent_message_chunk': process.stdout.write(u.content?.text ?? ''); break;
        case 'agent_thought_chunk': (globalThis.thoughts ??= []).push(u.content?.text ?? ''); break;
        case 'tool_call': console.log(`\n  [tool ${u.kind}] ${u.title}`); break;
        case 'tool_call_update':
          if (u.status) console.log(`  [tool ${u.status}] ${u.toolCallId?.slice(0, 12)}`);
          break;
        default: console.log(`\n  [${u.sessionUpdate}]`); break;
      }
    }
  }
});

const rpc = (method, params) => new Promise((resolve, reject) => {
  const id = nextId++;
  pending.set(id, { resolve, reject });
  child.stdin.write(`${JSON.stringify({ jsonrpc: '2.0', id, method, params })}\n`);
});
const note = (method, params) => child.stdin.write(`${JSON.stringify({ jsonrpc: '2.0', method, params })}\n`);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const run = async () => {
  console.log('→ initialize');
  const init = await rpc('initialize', {
    protocolVersion: 1,
    clientCapabilities: { fs: { readTextFile: false, writeTextFile: false }, terminal: false },
    clientInfo: { name: 'acp-test', version: '0' },
  });
  console.log('  agentInfo:', JSON.stringify(init.agentInfo), 'caps:', JSON.stringify(init.agentCapabilities));

  console.log('→ session/new');
  const { sessionId, modes } = await rpc('session/new', { cwd, mcpServers: [] });
  console.log('  session:', sessionId, 'modes:', modes?.availableModes?.map((m) => m.id).join(','));

  console.log('\n→ prompt 1 (tool call + memory)');
  const r1 = await rpc('session/prompt', {
    sessionId,
    prompt: [{ type: 'text', text: 'Create a file named acp-bridge-test.txt containing exactly: BRIDGE-OK. Then reply with just: DONE' }],
  });
  console.log(`\n  stopReason: ${r1.stopReason}`);

  console.log('\n→ prompt 2 (same ACP session: must remember)');
  const r2 = await rpc('session/prompt', {
    sessionId,
    prompt: [{ type: 'text', text: 'What exact word did you put in acp-bridge-test.txt? Reply with only that word.' }],
  });
  console.log(`\n  stopReason: ${r2.stopReason}`);

  if (cancelTest) {
    console.log('\n→ prompt 3 (cancelled after 3s)');
    const slow = rpc('session/prompt', {
      sessionId,
      prompt: [{ type: 'text', text: 'Count slowly from 1 to 200, one number per line, no tools.' }],
    });
    await sleep(3000);
    console.log('  cancelling…');
    note('session/cancel', { sessionId });
    const r3 = await slow.catch((e) => ({ stopReason: `error: ${e.message}` }));
    console.log(`\n  stopReason: ${r3.stopReason}`);
  }

  console.log('\n→ session/close');
  await rpc('session/close', { sessionId });
  console.log('done');
  child.stdin.end();
};

run().catch((e) => {
  console.error('\nFAILED:', e.message);
  child.kill();
  process.exit(1);
});
