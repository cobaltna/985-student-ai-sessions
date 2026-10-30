// v2 — same involute spur gear (m=2, z=20, 20°, 10 mm thick, Ø10 bore, 4x Ø5 on BCD26),
// but the flanks are true through-point SPLINES instead of 12 chords, plus root fillets.
// Expected volume (analytic, true involute) = 10690.3 mm³ + fillets.
import { spawn } from "node:child_process";

const PY = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\.venv\\Scripts\\python.exe";
const SERVER = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\adapters\\claude\\server.py";
const CWD = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\adapters\\claude";
const OUT_DIR = "C:\\Users\\UserX\\.zcode\\workspace\\default\\solidworks-gear";
const PART = OUT_DIR + "\\spur_gear_m2_z20.sldprt";

const child = spawn(PY, [SERVER], { cwd: CWD, stdio: ["pipe", "pipe", "pipe"] });
let buf = ""; const pending = new Map();
child.stdout.on("data", (d) => {
  buf += d.toString(); let i;
  while ((i = buf.indexOf("\n")) >= 0) {
    const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1);
    if (!line) continue;
    let m; try { m = JSON.parse(line); } catch { continue; }
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  }
});
child.stderr.on("data", (d) => { if (process.env.SW_VERBOSE) process.stderr.write("[srv] " + d); });
let nextId = 1;
const send = (o) => child.stdin.write(JSON.stringify(o) + "\n");
const rpc = (method, params, timeoutMs = 180000) => new Promise((res, rej) => {
  const id = nextId++;
  const t = setTimeout(() => { pending.delete(id); rej(new Error("timeout " + method)); }, timeoutMs);
  pending.set(id, (m) => { clearTimeout(t); res(m); });
  send({ jsonrpc: "2.0", id, method, params });
});
const call = async (name, args) => {
  const r = await rpc("tools/call", { name, arguments: args ?? {} });
  if (r.result?.isError) throw new Error(`${name} FAILED -> ${JSON.stringify(r.result).slice(0, 900)}`);
  return r.result?.content?.map((c) => c.text).join("\n") ?? JSON.stringify(r.error ?? r.result);
};
const feats = (t) => { const m = t.match(/features=\[(.*?)\]/); return m ? m[1].split(",").map((s) => s.replace(/^'|'$/g, "").trim()).filter(Boolean) : []; };
const log = (l, t) => console.log(`\n--- ${l} ---\n${t.slice(0, 500)}`);

// ------------------------------------------------------------------ geometry
const M = 0.002, Z = 20, ALPHA = (20 * Math.PI) / 180, THICK = 0.01;
const rp = (M * Z) / 2, ra = rp + M, rf = rp - 1.25 * M, rb = rp * Math.cos(ALPHA);
const inv = (a) => Math.tan(a) - a;
const halfPitch = Math.PI / (2 * Z), invP = inv(ALPHA), halfTooth = Math.PI / Z;
const offsetAt = (r) => halfPitch + invP - inv(Math.acos(Math.min(1, rb / r)));
const RMAX = 0.0225, N = 16;
const R = (x) => +x.toFixed(9);
const P = (r, a) => [R(r * Math.cos(a)), R(r * Math.sin(a))];
const tMax = Math.sqrt((RMAX / rb) ** 2 - 1);
const radii = Array.from({ length: N + 1 }, (_, i) => rb * Math.sqrt(1 + (tMax * (i / N)) ** 2));
const angL = radii.map((r) => -halfTooth + offsetAt(r));
const angR = radii.map((r) => halfTooth - offsetAt(r));
const flatL = radii.map((r, i) => P(r, angL[i])).flat();            // base -> tip
const flatR = radii.map((r, i) => P(r, angR[i])).reverse().flat();   // tip -> base: reverse the PAIRS
const tipL = P(RMAX, angL[N]), tipR = P(RMAX, angR[N]);
const baseL = P(rb, angL[0]), baseR = P(rb, angR[0]);
const rootL = P(rf, angL[0]), rootR = P(rf, angR[0]);

const contour = [
  { entity_type: "line", x1: rootL[0], y1: rootL[1], x2: baseL[0], y2: baseL[1] },          // radial root->base
  { entity_type: "spline", points: flatL },                                // involute flank
  { entity_type: "arc_center", cx: 0, cy: 0, x1: tipL[0], y1: tipL[1], x2: tipR[0], y2: tipR[1], direction: 1 },
  { entity_type: "spline", points: flatR },                                // mirrored flank, back down
  { entity_type: "line", x1: baseR[0], y1: baseR[1], x2: rootR[0], y2: rootR[1] },
  { entity_type: "arc_center", cx: 0, cy: 0, x1: rootR[0], y1: rootR[1], x2: rootL[0], y2: rootL[1], direction: -1 },
];
const holeSegs = [0, 90, 180, 270].map((deg) => {
  const a = (deg * Math.PI) / 180;
  return { entity_type: "circle", cx: R(0.013 * Math.cos(a)), cy: R(0.013 * Math.sin(a)), radius: 0.0025 };
}).concat([{ entity_type: "circle", cx: 0, cy: 0, radius: 0.005 }]);

const FIL = 0.0005;   // 0.5 mm root fillet
const filletArea = 40 * (FIL * 1000) ** 2 * (1 - Math.PI / 4);   // mm² added back by 40 root fillets
const expect = 10690.3;   // mm³ — true involute, no root fillets
console.log(`contour entities=${contour.length} | expected ${expect.toFixed(1)} mm³ (true involute, sharp roots)`);

// ------------------------------------------------------------------ build
await rpc("initialize", { protocolVersion: "2026-07-28", capabilities: {}, clientInfo: { name: "gear", version: "2" } });
send({ jsonrpc: "2.0", method: "notifications/initialized" });

log("ensure_ready", await call("ensure_ready"));
log("open_new_part", await call("open_new_part"));
log("sketch (blank)", await call("create_sketch", { plane: "Front Plane" }));
await call("add_sketch_entity", { entity_type: "circle", cx: 0, cy: 0, radius: ra });
log("blank Ø44 x 10", await call("extrude_feature", { feature_type: "boss", depth: THICK }));

log("sketch (tooth space)", await call("create_sketch", { plane: "Front Plane" }));
log("spline profile", await call("add_sketch_entities", { segments: JSON.stringify(contour) }));
let filleted = 0;
for (const [tag, v] of [["+", rootR], ["-", rootL]]) {
  try { log(`root fillet ${tag}`, await call("add_sketch_entity", { entity_type: "fillet", vx: v[0], vy: v[1], radius: FIL })); filleted++; }
  catch (e) { console.log(`\n--- root fillet ${tag}: FAILED (kept sharp) ---\n${e.message.slice(0, 200)}`); }
}

const cut = await call("extrude_feature", { feature_type: "cut", through: true });
log("cut tooth space", cut);
const cutName = feats(cut)[0];

const axis = await call("add_reference_geometry", { type: "axis", entity1_name: "Top Plane", entity1_type: "PLANE", entity2_name: "Right Plane", entity2_type: "PLANE" });
const axisName = feats(axis)[0];
log("axis", axis);
log("20x circular pattern", await call("create_pattern", { pattern_type: "circular", feature_name: cutName, axis_name: axisName, count: Z, angle: 360, equal_spacing: true }));

log("sketch (holes)", await call("create_sketch", { plane: "Front Plane" }));
await call("add_sketch_entities", { segments: JSON.stringify(holeSegs) });
log("cut holes", await call("extrude_feature", { feature_type: "cut", through: true }));

const mp = await call("analyze_model", { analysis_type: "mass_properties" });
log("mass properties", mp);
const geo = await call("analyze_model", { analysis_type: "geometry" });
log("geometry", geo);
const faces = await call("analyze_model", { analysis_type: "faces" });
console.log("\n--- cylindrical faces by radius ---");
const radiiSeen = new Map();
for (const m of faces.matchAll(/radius":\s*([\d.eE+-]+)/g)) { const v = (+m[1] * 1000).toFixed(4); radiiSeen.set(v, (radiiSeen.get(v) ?? 0) + 1); }
console.log([...radiiSeen.entries()].map(([r, n]) => `${r} mm x${n}`).join(" | ") || faces.slice(0, 400));
log("feature tree", (await call("analyze_model", { analysis_type: "features" })).slice(0, 600));
const vol = Number((mp.match(/volume=([\d.eE+-]+)/) ?? [, "NaN"])[1]) * 1e9;
const ref = filleted === 2 ? expect + filletArea * THICK * 1000 : expect;   // mm³
const errPct = ((vol - ref) / ref) * 100;
console.log(`\n=== ${filleted}/2 root fillets applied | expected ${ref.toFixed(1)} mm³ | SolidWorks ${vol.toFixed(1)} mm³ | error ${errPct.toFixed(4)} % ===`);

if (Math.abs(errPct) > 0.1) {
  console.log("*** verification FAILED (|error| > 0.1%) — NOT saving ***");
  child.kill(); process.exit(1);
}
log("save", await call("save_document", { file_path: PART }));
child.kill();
process.exit(0);
