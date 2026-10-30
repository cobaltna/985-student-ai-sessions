#!/usr/bin/env node
/**
 * ACP ↔ ZCode bridge.
 *
 * OpenFilm's desktop chat talks ACP (Agent Client Protocol) over stdio. ZCode has no ACP
 * server; it has a headless one-shot mode:
 *
 *   node zcode.cjs -p "<prompt>" --output-format stream-json --cwd <dir> [--resume sess_…] [--mode …]
 *
 * which emits newline-delimited JSON events (model.streaming / tool.updated / turn.completed /
 * result) and exits. This bridge is an ACP agent: it keeps one ZCode session id per ACP session
 * and, for each prompt, runs that command, streaming its events back as ACP session updates.
 *
 * No dependencies. Diagnostics go to stderr only; stdout is exclusively ACP JSON-RPC.
 */
import { spawn } from 'node:child_process';
import { randomUUID } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { homedir, tmpdir } from 'node:os';
import { basename, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const STATE_FILE = join(HERE, 'sessions.json');
const ATTACH_DIR = join(tmpdir(), 'openfilm-zcode-attach');
const SHIM_BIN = join(HERE, 'bin');

/* OpenFilm starts this file with its own Electron binary as Node; ZCode is best run by a real Node */
function systemNode() {
  if (process.env.ZCODE_NODE) return process.env.ZCODE_NODE;
  const candidates = [
    join(process.env.ProgramFiles || 'C:\\Program Files', 'nodejs', 'node.exe'),
    join(process.env.LOCALAPPDATA || '', 'Programs', 'nodejs', 'node.exe'),
  ];
  for (const c of candidates) { try { if (existsSync(c)) return c; } catch { /* next */ } }
  return process.execPath;
}
const NODE = systemNode();
/** true when the runner is an Electron binary that needs ELECTRON_RUN_AS_NODE to behave as Node */
const NODE_IS_ELECTRON = NODE === process.execPath && Boolean(process.versions.electron);

const ZCODE = process.env.ZCODE_CLI
  || join(process.env.LOCALAPPDATA || '', 'Programs', 'ZCode', 'resources', 'glm', 'zcode.cjs');

const PROTOCOL_VERSION = 1;
const KEEP_STATE_DAYS = 30;
const PROMPT_ARG_MAX = 20000; // beyond this the prompt travels as an attached file
const RESULT_TEXT_MAX = 20000;

/**
 * An ACP agent's `--version` (OpenFilm tries a chosen program with it before using it).
 * Also lets the file be started by any Node, Electron-as-Node included.
 */
if (process.argv.slice(2).some((a) => a === '--version' || a === '-v')) {
  process.stdout.write('0.16.9 (zcode-acp bridge)\n');
  process.exit(0);
}

const log = (...a) => process.stderr.write(`[zcode-acp] ${a.join(' ')}\n`);

/* ── state ─────────────────────────────────────────────────────────────── */

const loadState = () => {
  try {
    const raw = JSON.parse(readFileSync(STATE_FILE, 'utf8'));
    return raw && typeof raw.sessions === 'object' ? raw : { sessions: {} };
  } catch {
    return { sessions: {} };
  }
};
const state = loadState();

function saveState() {
  const cutoff = Date.now() - KEEP_STATE_DAYS * 86400_000;
  for (const [id, s] of Object.entries(state.sessions)) {
    if (!s || (s.at ?? 0) < cutoff) delete state.sessions[id];
  }
  try {
    mkdirSync(HERE, { recursive: true });
    writeFileSync(STATE_FILE, `${JSON.stringify(state, null, 2)}\n`);
  } catch (e) {
    log('could not save state:', e.message);
  }
}

/** ACP session id → { cwd, zcode, mode, at } */
const sessions = new Map();

function sessionOf(id) {
  if (sessions.has(id)) return sessions.get(id);
  const kept = state.sessions[id];
  if (!kept) return null;
  const s = { id, cwd: kept.cwd, zcode: kept.zcode ?? null, mode: kept.mode ?? 'yolo', at: Date.now(), child: null };
  sessions.set(id, s);
  return s;
}

function remember(s) {
  s.at = Date.now();
  /* the app opens throwaway sessions in its own probe folder to ask "signed in?": not worth keeping */
  if (/[\\/]openfilm-agent-probe$/i.test(s.cwd)) return;
  state.sessions[s.id] = { cwd: s.cwd, zcode: s.zcode, mode: s.mode, at: s.at };
  saveState();
}

/* ── ACP wire ──────────────────────────────────────────────────────────── */

const write = (msg) => process.stdout.write(`${JSON.stringify(msg)}\n`);
const reply = (id, result) => write({ jsonrpc: '2.0', id, result });
const fail = (id, code, message) => write({ jsonrpc: '2.0', id, error: { code, message } });
const notify = (method, params) => write({ jsonrpc: '2.0', method, params });

function update(sessionId, u) {
  notify('session/update', { sessionId, update: u });
}
function chunk(sessionId, kind, text, messageId) {
  if (!text) return;
  update(sessionId, {
    sessionUpdate: kind,
    content: { type: 'text', text },
    ...(messageId ? { messageId } : {}),
  });
}

/* ── ZCode process ─────────────────────────────────────────────────────── */

const TOOL_KIND = {
  Read: 'read', Write: 'edit', Edit: 'edit', MultiEdit: 'edit', NotebookEdit: 'edit', ApplyPatch: 'edit',
  Glob: 'search', Grep: 'search', Bash: 'execute',
  WebFetch: 'fetch', WebSearch: 'fetch',
  TodoWrite: 'other', Task: 'other', ExitPlanMode: 'other',
};

function toolTitle(name, input = {}) {
  const file = input.file_path || input.path || input.notebook_path;
  switch (name) {
    case 'Bash': return `$ ${String(input.command ?? '').replace(/\s+/g, ' ').trim().slice(0, 160) || 'command'}`;
    case 'Grep': return `Search for ${JSON.stringify(String(input.pattern ?? '').slice(0, 80))}`;
    case 'Glob': return `Find files ${String(input.pattern ?? '').slice(0, 80)}`;
    case 'WebFetch': return `Fetch ${String(input.url ?? '').slice(0, 120)}`;
    case 'WebSearch': return `Search the web: ${String(input.query ?? '').slice(0, 120)}`;
    case 'Task': return `Delegate: ${String(input.description ?? '').slice(0, 120)}`;
    case 'TodoWrite': return 'Update the plan';
    case 'ExitPlanMode': return 'Finish planning';
    default: return file ? `${name} ${basename(file)}` : name;
  }
}
const toolLocations = (input = {}) => {
  const file = input.file_path || input.path || input.notebook_path;
  return typeof file === 'string' && file ? [{ path: file }] : undefined;
};

/**
 * ZCode's own CLI needs ZCODE_BUILTIN_PROVIDER_CONFIG_FILE, which only ZCode's process tree sets.
 * When the bridge runs inside OpenFilm that variable is missing, so find the newest one on disk.
 */
function builtinProviderConfig() {
  const base = join(homedir(), '.zcode', 'v2', 'runtime', 'provider', `${process.platform === 'win32' ? 'windows' : process.platform}-${process.arch === 'arm64' ? 'aarch64' : 'x86_64'}`);
  let versions = [];
  try { versions = readdirSync(base).sort().reverse(); } catch { return null; }
  for (const v of versions) {
    let endpoints = [];
    try { endpoints = readdirSync(join(base, v)).filter((e) => e.startsWith('endpoint-')); } catch { continue; }
    for (const e of endpoints) {
      const file = join(base, v, e, 'zcode-builtin.json');
      if (existsSync(file)) return file;
    }
  }
  return null;
}

function childEnv() {
  const env = { ...process.env };
  if (NODE_IS_ELECTRON) env.ELECTRON_RUN_AS_NODE = '1';
  else delete env.ELECTRON_RUN_AS_NODE;
  delete env.ELECTRON_NO_ATTACH_CONSOLE;
  /* outside ZCode's own process tree these are not set: the built-in provider config is what -p needs first */
  if (!env.ZCODE_BUILTIN_PROVIDER_CONFIG_FILE) {
    const found = builtinProviderConfig();
    if (found) env.ZCODE_BUILTIN_PROVIDER_CONFIG_FILE = found;
    else log('no zcode-builtin.json found: ZCode may refuse to start');
  }
  if (!env.ZCODE_PERSONAL_PROVIDER_CONFIG_FILE) {
    const personal = join(homedir(), '.zcode', 'v2', 'provider_config.json');
    if (existsSync(personal)) env.ZCODE_PERSONAL_PROVIDER_CONFIG_FILE = personal;
  }
  /* the `openfilm` command first: an ASCII-safe shim, as the app's own .cmd mangles this profile's non-ASCII path */
  env.PATH = [SHIM_BIN, env.PATH].filter(Boolean).join(';');
  return env;
}

function killTree(child) {
  if (!child || child.exitCode !== null) return;
  if (process.platform === 'win32' && child.pid) {
    try {
      spawn('taskkill', ['/pid', String(child.pid), '/T', '/F'], { stdio: 'ignore', windowsHide: true });
      return;
    } catch { /* fall through */ }
  }
  try { child.kill('SIGTERM'); } catch { /* gone */ }
}

/** Prompt blocks → one text + the files to attach. */
function buildPrompt(blocks, s) {
  const parts = [];
  const files = [];
  for (const b of Array.isArray(blocks) ? blocks : []) {
    if (!b || typeof b !== 'object') continue;
    if (b.type === 'text' && typeof b.text === 'string') parts.push(b.text);
    else if (b.type === 'resource_link' && typeof b.uri === 'string') parts.push(`[file: ${b.uri}]`);
    else if (b.type === 'resource' && b.resource) {
      const r = b.resource;
      if (typeof r.text === 'string') parts.push(`[${r.uri ?? 'file'}]\n${r.text}`);
      else if (typeof r.uri === 'string') parts.push(`[file: ${r.uri}]`);
    } else if (b.type === 'image' && typeof b.data === 'string') {
      files.push(saveImage(b));
    } else if (b.type === 'audio') {
      /* ZCode takes no audio on the command line */
    }
  }
  return { text: parts.join('\n\n').trim(), files: files.filter(Boolean) };
}

function saveImage(block) {
  try {
    const ext = ({ 'image/png': 'png', 'image/jpeg': 'jpg', 'image/webp': 'webp', 'image/gif': 'gif' })[block.mimeType] ?? 'png';
    mkdirSync(ATTACH_DIR, { recursive: true });
    const file = join(ATTACH_DIR, `image-${randomUUID()}.${ext}`);
    writeFileSync(file, Buffer.from(String(block.data).replace(/^data:[^,]*,/, ''), 'base64'));
    return file;
  } catch (e) {
    log('image skipped:', e.message);
    return null;
  }
}

/**
 * One prompt: run ZCode, stream its events as ACP updates, resolve with the ACP stop reason.
 * @returns {Promise<'end_turn'|'cancelled'|'max_tokens'>}
 */
function runTurn(s, blocks) {
  return new Promise((resolve, reject) => {
    let { text, files } = buildPrompt(blocks, s);
    const cleanup = [];
    if (!text && !files.length) {
      resolve('end_turn');
      return;
    }
    if (text.length > PROMPT_ARG_MAX) {
      /* Windows caps a command line at ~32k: the message travels as a file the model reads */
      const file = join(ATTACH_DIR, `message-${randomUUID()}.md`);
      mkdirSync(ATTACH_DIR, { recursive: true });
      writeFileSync(file, text, 'utf8');
      cleanup.push(file);
      files = [file, ...files];
      text = 'The attached file is the message to act on: read it and follow it, then do what it says.';
    }
    const args = ['-p', text, '--output-format', 'stream-json', '--cwd', s.cwd];
    if (s.mode) args.push('--mode', s.mode);
    if (s.zcode) args.push('--resume', s.zcode);
    for (const f of files) args.push('--attach', f);

    const child = spawn(NODE, [ZCODE, ...args], {
      cwd: s.cwd,
      env: childEnv(),
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    });
    s.child = child;

    let buffer = '';
    let stderr = '';
    let sawText = false;
    let finished = null;   // the `result` payload
    let turnEnd = null;    // the `turn.completed` payload
    let cancelled = false;
    let settled = false;

    const finish = (fn, value) => {
      if (settled) return;
      settled = true;
      for (const f of cleanup) { try { rmSync(f, { force: true }); } catch { /* ignore */ } }
      if (s.child === child) s.child = null;
      fn(value);
    };

    const onEvent = (ev) => {
      const p = ev.payload ?? {};
      switch (ev.type) {
        case 'model.streaming': {
          switch (p.kind) {
            case 'text_delta':
              sawText = true;
              chunk(s.id, 'agent_message_chunk', p.delta, p.assistantMessageId);
              break;
            case 'reasoning_delta':
              chunk(s.id, 'agent_thought_chunk', p.delta, p.assistantMessageId);
              break;
            case 'tool_call': {
              const input = p.input ?? {};
              update(s.id, {
                sessionUpdate: 'tool_call',
                toolCallId: p.toolCallId ?? randomUUID(),
                title: toolTitle(p.toolName ?? 'tool', input),
                name: p.toolName,
                kind: TOOL_KIND[p.toolName] ?? 'other',
                status: 'pending',
                ...(toolLocations(input) ? { locations: toolLocations(input) } : {}),
                rawInput: input,
              });
              break;
            }
            default:
              break;
          }
          break;
        }
        case 'tool.updated': {
          if (p.kind === 'started') {
            update(s.id, { sessionUpdate: 'tool_call_update', toolCallId: p.toolCallId, status: 'in_progress' });
          } else if (p.kind === 'result') {
            const r = p.result ?? {};
            let content = typeof r.content === 'string' ? r.content : r.content ? JSON.stringify(r.content) : '';
            if (content.length > RESULT_TEXT_MAX) content = `${content.slice(0, RESULT_TEXT_MAX)}\n… (${content.length - RESULT_TEXT_MAX} more characters)`;
            update(s.id, {
              sessionUpdate: 'tool_call_update',
              toolCallId: p.toolCallId,
              status: r.success === false ? 'failed' : 'completed',
              ...(content ? { content: [{ type: 'content', content: { type: 'text', text: content } }] } : {}),
              rawOutput: r.success === false ? r : { duration: p.duration ?? null },
            });
          }
          break;
        }
        case 'session.titleUpdated':
        case 'session.updated':
        case 'checkpoint.created':
        case 'streamRecovery.updated':
        case 'turn.started':
          if (ev.sessionId && !s.zcode) { s.zcode = ev.sessionId; remember(s); }
          break;
        case 'turn.completed':
          turnEnd = p;
          if (ev.sessionId) { s.zcode = ev.sessionId; remember(s); }
          break;
        case 'result':
          finished = p;
          if (p.sessionId) { s.zcode = p.sessionId; remember(s); }
          break;
        default:
          if (ev.sessionId && !s.zcode) { s.zcode = ev.sessionId; remember(s); }
          break;
      }
    };

    const onLine = (line) => {
      const t = line.trim();
      if (!t) return;
      let ev;
      try { ev = JSON.parse(t); } catch { return; }
      if (ev && typeof ev === 'object' && ev.type) onEvent(ev);
      else if (ev && typeof ev === 'object' && ev.error) {
        log('zcode said:', JSON.stringify(ev.error).slice(0, 500));
      }
    };

    child.stdout.setEncoding('utf8');
    child.stdout.on('data', (d) => {
      buffer += d;
      let i;
      while ((i = buffer.indexOf('\n')) >= 0) {
        const line = buffer.slice(0, i);
        buffer = buffer.slice(i + 1);
        onLine(line);
      }
    });
    child.stderr.setEncoding('utf8');
    child.stderr.on('data', (d) => { stderr = (stderr + d).slice(-8000); });

    child.once('error', (e) => finish(reject, new Error(`ZCode could not start: ${e.message}`)));
    child.once('close', (code) => {
      if (buffer.trim()) onLine(buffer);
      if (cancelled) return finish(resolve, 'cancelled');
      const said = finished ?? null;
      const bad = turnEnd && turnEnd.resultType && turnEnd.resultType !== 'success';
      if (bad) return finish(reject, new Error(String(turnEnd.error ?? turnEnd.message ?? `ZCode ended the turn with ${turnEnd.resultType}.`)));
      if (!said && code !== 0) {
        const why = stderr.trim().split(/\r?\n/).filter(Boolean).slice(-6).join('\n');
        return finish(reject, new Error(why || `ZCode exited with code ${code}.`));
      }
      /* a turn that said nothing in words (only tools): the final answer is still worth saying */
      if (!sawText && said?.response) chunk(s.id, 'agent_message_chunk', said.response);
      finish(resolve, 'end_turn');
    });

    s.cancel = () => {
      cancelled = true;
      killTree(child);
    };
    s.turnDone = () => { s.cancel = null; };

    /* a session closed under us: stop the work */
    s.stop = () => { cancelled = true; killTree(child); };
  }).finally(() => { s.cancel = null; s.turnDone = null; });
}

/* ── methods ───────────────────────────────────────────────────────────── */

const MODES = [
  { id: 'yolo', name: 'YOLO', description: 'Run everything without asking (ZCode’s default for -p).' },
  { id: 'build', name: 'Build', description: 'ZCode’s build mode.' },
  { id: 'edit', name: 'Edit', description: 'ZCode’s edit mode.' },
  { id: 'plan', name: 'Plan', description: 'Plan only; change nothing.' },
];

/** The slot this bridge is mounted on keeps its own label; this shows what actually answers. */
const MODEL_OPTION = (current = 'zcode') => ({
  id: 'model',
  name: 'Model',
  category: 'model',
  type: 'select',
  currentValue: current,
  options: [
    { value: 'zcode', name: 'ZCode', description: 'ZCode CLI with the model ZCode is set to.' },
  ],
});

const methods = {
  initialize() {
    return {
      protocolVersion: PROTOCOL_VERSION,
      agentCapabilities: {
        loadSession: false,
        promptCapabilities: { image: true, audio: false, embeddedContext: false },
        mcpCapabilities: { http: false, sse: false },
        sessionCapabilities: { resume: {} },
      },
      agentInfo: { name: 'zcode', title: 'ZCode', version: process.env.ZCODE_VERSION || '0.16.9' },
      authMethods: [],
    };
  },

  authenticate() { return {}; },

  'session/new'(params) {
    const id = `sess_${randomUUID()}`;
    const s = {
      id,
      cwd: typeof params?.cwd === 'string' && params.cwd ? params.cwd : process.cwd(),
      zcode: null,
      mode: 'yolo',
      at: Date.now(),
      child: null,
    };
    sessions.set(id, s);
    remember(s);
    return { sessionId: id, modes: { currentModeId: 'yolo', availableModes: MODES }, configOptions: [MODEL_OPTION()] };
  },

  'session/resume'(params) {
    const id = params?.sessionId;
    const s = sessionOf(id) ?? {
      id, cwd: params?.cwd ?? process.cwd(), zcode: null, mode: 'yolo', at: Date.now(), child: null,
    };
    if (typeof params?.cwd === 'string' && params.cwd) s.cwd = params.cwd;
    sessions.set(id, s);
    remember(s);
    return { modes: { currentModeId: s.mode, availableModes: MODES }, configOptions: [MODEL_OPTION()] };
  },

  'session/close'(params) {
    const s = sessions.get(params?.sessionId);
    if (s?.stop) s.stop();
    sessions.delete(params?.sessionId);
    delete state.sessions[params?.sessionId];
    saveState();
    return {};
  },

  'session/set_mode'(params) {
    const s = sessionOf(params?.sessionId);
    if (s && typeof params?.modeId === 'string') {
      s.mode = params.modeId;
      remember(s);
      update(s.id, { sessionUpdate: 'current_mode_update', currentModeId: s.mode });
    }
    return {};
  },

  'session/set_config_option'(params) {
    if (params?.configId === 'model') return { configOptions: [MODEL_OPTION(params.value)] };
    return { configOptions: [MODEL_OPTION()] };
  },

  async 'session/prompt'(params) {
    const s = sessionOf(params?.sessionId);
    if (!s) throw Object.assign(new Error(`No session ${params?.sessionId}`), { code: -32602 });
    if (typeof params.cwd === 'string' && params.cwd) s.cwd = params.cwd;
    return { stopReason: await runTurn(s, params?.prompt) };
  },
};

const notifications = {
  'session/cancel'(params) {
    const s = sessions.get(params?.sessionId);
    if (s?.cancel) s.cancel();
  },
};

/* ── main loop ─────────────────────────────────────────────────────────── */

let chain = Promise.resolve();
function handle(msg) {
  const hasId = Object.prototype.hasOwnProperty.call(msg, 'id') && msg.id !== null && msg.id !== undefined;
  const { method, params, id } = msg;

  const note = notifications[method];
  if (note && !hasId) {
    try { note(params); } catch (e) { log('notification failed:', method, e.message); }
    return;
  }
  const fn = methods[method];
  if (!fn) {
    if (hasId) fail(id, -32601, `Method not found: ${method}`);
    return;
  }
  chain = chain.then(async () => {
    try {
      const result = await fn(params ?? {});
      if (hasId) reply(id, result ?? {});
    } catch (e) {
      log('request failed:', method, e?.message ?? String(e));
      if (hasId) fail(id, typeof e?.code === 'number' ? e.code : -32603, e instanceof Error ? e.message : String(e));
    }
  }).catch(() => {});
}

let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (d) => {
  input += d;
  let i;
  while ((i = input.indexOf('\n')) >= 0) {
    const line = input.slice(0, i);
    input = input.slice(i + 1);
    const t = line.trim();
    if (!t) continue;
    let msg;
    try { msg = JSON.parse(t); } catch { log('not JSON:', t.slice(0, 200)); continue; }
    if (msg && typeof msg === 'object' && typeof msg.method === 'string') handle(msg);
    else if (msg && typeof msg === 'object' && msg.id !== undefined) {
      /* a response to something we did not ask: ignore */
    }
  }
});

const shutdown = () => {
  for (const s of sessions.values()) { if (s.stop) s.stop(); }
  saveState();
  process.exit(0);
};
process.stdin.on('end', shutdown);
process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
process.on('uncaughtException', (e) => log('uncaught:', e?.stack ?? String(e)));
process.on('unhandledRejection', (e) => log('unhandled:', e?.stack ?? String(e)));

log(`ready (node ${process.version}, zcode ${existsSync(ZCODE) ? ZCODE : 'NOT FOUND'})`);
