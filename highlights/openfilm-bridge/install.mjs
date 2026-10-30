#!/usr/bin/env node
/**
 * Mount (or unmount) the ZCode bridge on one of OpenFilm's agent slots.
 *
 *   node install.mjs              mount on `deepseek` (the free slot) and show the result
 *   node install.mjs --slot kimi  mount on another slot
 *   node install.mjs --remove     unmount
 *   node install.mjs --status     show what is mounted now
 *
 * OpenFilm keeps its agent choices in <userData>/agents.json:
 *   shown[<slot>] = true            the slot appears in the chat's menu
 *   disconnected                   slots listed here are switched off
 *   paths[<slot>] = <program>      a program found by hand (tried with `--version` before use)
 *
 * The slots are fixed in OpenFilm's app.asar (codex, claude, copilot, cursor, opencode,
 * codebuddy, qwen, kimi, minimax, deepseek, byok), so the bridge takes one of them.
 */
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const BRIDGE = join(HERE, 'bridge.mjs');
const DATA = process.env.OPENFILM_HOME || join(process.env.APPDATA || join(homedir(), 'AppData', 'Roaming'), 'OpenFilm');
const FILE = join(DATA, 'agents.json');
const DEFAULT_SLOT = 'deepseek';

const arg = (name, fallback = null) => {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
};
const has = (name) => process.argv.includes(name);

const SLOTS = ['codex', 'claude', 'copilot', 'cursor', 'opencode', 'codebuddy', 'qwen', 'kimi', 'minimax', 'deepseek'];

function read() {
  try {
    const raw = JSON.parse(readFileSync(FILE, 'utf8'));
    return raw && typeof raw === 'object' ? raw : {};
  } catch {
    return {};
  }
}

function write(data) {
  writeFileSync(FILE, `${JSON.stringify(data, null, 2)}\n`);
}

const mountedOn = (data) => Object.entries(data.paths ?? {})
  .filter(([, p]) => typeof p === 'string' && p.replace(/\//g, '\\').toLowerCase().endsWith('openfilm-bridge\\bridge.mjs'))
  .map(([slot]) => slot);

const show = (data) => {
  const slots = mountedOn(data);
  console.log(`agents.json : ${FILE}`);
  console.log(`bridge      : ${BRIDGE} (${existsSync(BRIDGE) ? 'present' : 'MISSING'})`);
  console.log(`mounted on  : ${slots.length ? slots.join(', ') : '(none)'}`);
  for (const slot of slots) {
    console.log(`  ${slot}: shown=${data.shown?.[slot] ?? false} disconnected=${(data.disconnected ?? []).includes(slot)}`);
  }
};

const data = read();

if (has('--status')) {
  show(data);
  process.exit(0);
}

if (has('--remove')) {
  for (const slot of mountedOn(data)) {
    if (data.paths) delete data.paths[slot];
    if (data.shown) delete data.shown[slot];
    data.disconnected = (data.disconnected ?? []).filter((id) => id !== slot);
  }
  write(data);
  console.log('unmounted.');
  show(data);
  process.exit(0);
}

const slot = arg('--slot', DEFAULT_SLOT);
if (!SLOTS.includes(slot)) {
  console.error(`unknown slot ${slot}; one of: ${SLOTS.join(', ')}`);
  process.exit(1);
}
if (!existsSync(BRIDGE)) {
  console.error(`bridge.mjs is missing at ${BRIDGE}`);
  process.exit(1);
}

data.shown = { ...(data.shown ?? {}), [slot]: true };
data.disconnected = (data.disconnected ?? []).filter((id) => id !== slot);
data.paths = { ...(data.paths ?? {}), [slot]: BRIDGE };
write(data);

console.log(`mounted on "${slot}". Restart OpenFilm; the chat's menu shows it there (bottom right).`);
show(data);
