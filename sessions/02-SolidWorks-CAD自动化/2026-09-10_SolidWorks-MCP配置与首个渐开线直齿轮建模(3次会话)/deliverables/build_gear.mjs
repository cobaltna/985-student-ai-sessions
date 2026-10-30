// Build an involute spur gear (m=2, z=20, 20° pressure angle) with a center bore
// and 4 lightening holes, driving the SolidWorks MCP adapter over stdio JSON-RPC.
//
//   blank Ø44 x 10  ->  tooth-space cut (1 tooth)  ->  circular pattern x20
//   ->  4x Ø5 on BCD26 + Ø10 bore  ->  verify  ->  save
import { spawn } from "node:child_process";
import { mkdirSync } from "node:fs";

const PY = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\.venv\\Scripts\\python.exe";
const SERVER = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\adapters\\claude\\server.py";
const CWD = "C:\\Users\\UserX\\Downloads\\mcp-server-solidworks-main\\adapters\\claude";
const OUT_DIR = "C:\\Users\\UserX\\.zcode\\workspace\\default\\solidworks-gear";
const PART = OUT_DIR + "\\spur_gear_m2_z20.sldprt";

// ---------------------------------------------------------------- MCP client
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
child.stderr.on("data", (d) => process.stderr.write("[srv] " + d));
let nextId = 1;
const send = (o) => child.stdin.write(JSON.stringify(o) + "\n");
const rpc = (method, params, timeoutMs = 180000) =>
  new Promise((res, rej) => {
    const id = nextId++;
    const t = setTimeout(() => { pending.delete(id); rej(new Error("timeout " + method)); }, timeoutMs);
    pending.set(id, (m) => { clearTimeout(t); res(m); });
    send({ jsonrpc: "2.0", id, method, params });
  });

const call = async (name, args) => {
  const r = await rpc("tools/call", { name, arguments: args ?? {} });
  const text = r.result?.content?.map((c) => c.text).join("\n") ?? JSON.stringify(r.error ?? r.result);
  return text;
};
const field = (t, n) => (t.match(new RegExp(n + "=([^|]*)")) ?? [, ""])[1].trim();
const geom = (t) => { const i = t.indexOf("result_geometry="); if (i < 0) return null; try { return JSON.parse(t.slice(i + 16)); } catch { return null; } };
const feats = (t) => { const m = t.match(/features=\[(.*?)\]/); return m ? m[1].split(",").map((s) => s.replace(/^'|'$/g, "").trim()).filter(Boolean) : []; };

const log = (label, text) => console.log(`\n--- ${label} ---\n${text.slice(0, 700)}`);

// ---------------------------------------------------------------- gear math
const M = 0.002, Z = 20, ALPHA = (20 * Math.PI) / 180;          // module 2 mm, 20 teeth, 20°
const rp = (M * Z) / 2, ra = rp + M, rf = rp - 1.25 * M, rb = rp * Math.cos(ALPHA);
const inv = (a) => Math.tan(a) - a;
const halfPitch = Math.PI / (2 * Z);                            // half tooth thickness at pitch circle
const invP = inv(ALPHA);
const offsetAt = (r) => halfPitch + invP - inv(Math.acos(Math.min(1, rb / r))); // half tooth angle at r
const halfTooth = Math.PI / Z;                                  // 9° — gap centred at 0°, teeth at ±9°
const RMAX = 0.0225;                                            // 0.5 mm above the Ø44 blank, avoids tangency
const N = 12;                                                   // involute segments per flank
const P = (r, a) => [+(r * Math.cos(a)).toFixed(9), +(r * Math.sin(a)).toFixed(9)];
const line = (r1, a1, r2, a2) => { const [x1, y1] = P(r1, a1), [x2, y2] = P(r2, a2); return { entity_type: "line", x1, y1, x2, y2 }; };
const arcC = (r, aFrom, aTo, dir) => { const [x1, y1] = P(r, aFrom), [x2, y2] = P(r, aTo); return { entity_type: "arc_center", cx: 0, cy: 0, x1, y1, x2, y2, direction: dir }; };

const tMax = Math.sqrt((RMAX / rb) ** 2 - 1);
const radii = Array.from({ length: N + 1 }, (_, i) => rb * Math.sqrt(1 + (tMax * (i / N)) ** 2));
const angL = radii.map((r) => -halfTooth + offsetAt(r));        // left (gap-side) flank of the −9° tooth
const angR = radii.map((r) => halfTooth - offsetAt(r));         // right flank of the +9° tooth

const toothSpace = [];
toothSpace.push(line(rf, angL[0], rb, angL[0]));                            // radial root -> base, left
for (let i = 1; i <= N; i++) toothSpace.push(line(radii[i - 1], angL[i - 1], radii[i], angL[i]));
toothSpace.push(arcC(RMAX, angL[N], angR[N], 1));                           // tip clearance arc, CCW
for (let i = N; i >= 1; i--) toothSpace.push(line(radii[i], angR[i], radii[i - 1], angR[i - 1]));
toothSpace.push(line(rb, angR[0], rf, angR[0]));                            // base -> radial root, right
toothSpace.push(arcC(rf, angR[0], angL[0], -1));                            // root arc, CW

const holeSegs = [0, 90, 180, 270].map((deg) => {
  const a = (deg * Math.PI) / 180;
  return { entity_type: "circle", cx: +(0.013 * Math.cos(a)).toFixed(9), cy: +(0.013 * Math.sin(a)).toFixed(9), radius: 0.0025 };
});
holeSegs.push({ entity_type: "circle", cx: 0, cy: 0, radius: 0.005 });

// analytic cross-section: blank disc − 20 tooth spaces − holes
const poly = [];
toothSpace.forEach((s) => {
  if (s.entity_type === "line") poly.push([s.x1, s.y1]);
});
const shoelace = (pts) => Math.abs(pts.reduce((a, [x, y], i) => { const [X, Y] = pts[(i + 1) % pts.length]; return a + (x * Y - X * y); }, 0)) / 2;
const gapArea = shoelace(poly);
const netArea = Math.PI * ra ** 2 - Z * gapArea - (4 * Math.PI * 0.0025 ** 2 + Math.PI * 0.005 ** 2);
const expectVol = netArea * 0.01;

console.log(`gear: m=${M * 1000}mm z=${Z} | rp=${(rp * 1000).toFixed(3)} ra=${(ra * 1000).toFixed(3)} rf=${(rf * 1000).toFixed(3)} rb=${(rb * 1000).toFixed(4)} mm`);
console.log(`gap area=${(gapArea * 1e6).toFixed(3)} mm² | tooth-space entities=${toothSpace.length} | predicted volume=${(expectVol * 1e9).toFixed(1)} mm³`);

// ---------------------------------------------------------------- run
await rpc("initialize", { protocolVersion: "2026-07-28", capabilities: {}, clientInfo: { name: "gear-builder", version: "1" } });
send({ jsonrpc: "2.0", method: "notifications/initialized" });

mkdirSync(OUT_DIR, { recursive: true });

log("ensure_ready", await call("ensure_ready"));
log("open_new_part", await call("open_new_part"));

// 1) Ø44 blank
log("create_sketch (blank)", await call("create_sketch", { plane: "Front Plane" }));
log("circle Ø44", await call("add_sketch_entity", { entity_type: "circle", cx: 0, cy: 0, radius: ra }));
const blank = await call("extrude_feature", { feature_type: "boss", depth: 0.01 });
log("extrude blank", blank);

// 2) one tooth space, cut through
log("create_sketch (tooth space)", await call("create_sketch", { plane: "Front Plane" }));
const tsRes = await call("add_sketch_entities", { segments: JSON.stringify(toothSpace) });
log("tooth-space profile", tsRes);
const cut = await call("extrude_feature", { feature_type: "cut", through: true });
log("cut tooth space", cut);
const cutName = feats(cut)[0];

// 3) 20x circular pattern about the part axis (Top ∩ Right = Z)
const axis = await call("add_reference_geometry", { type: "axis", entity1_name: "Top Plane", entity1_type: "PLANE", entity2_name: "Right Plane", entity2_type: "PLANE" });
log("reference axis", axis);
const axisName = feats(axis)[0];
const pat = await call("create_pattern", { pattern_type: "circular", feature_name: cutName, axis_name: axisName, count: Z, angle: 360, equal_spacing: true });
log("circular pattern", pat);
const patGeom = geom(pat);

// 4) holes
log("create_sketch (holes)", await call("create_sketch", { plane: "Front Plane" }));
log("4x Ø5 + Ø10 bore", await call("add_sketch_entities", { segments: JSON.stringify(holeSegs) }));
const holes = await call("extrude_feature", { feature_type: "cut", through: true });
log("cut holes", holes);

// 5) verify + save
const mp = await call("analyze_model", { analysis_type: "mass_properties" });
log("mass properties", mp);
const geo = await call("analyze_model", { analysis_type: "geometry" });
log("geometry", geo);
const tree = await call("analyze_model", { analysis_type: "features" });
log("feature tree", tree.slice(0, 1200));
log("save", await call("save_document", { file_path: PART }));

const vol = Number((mp.match(/volume=([\d.eE+-]+)/) ?? [, "NaN"])[1]);
console.log(`\n=== predicted ${(expectVol * 1e9).toFixed(1)} mm³ vs SolidWorks ${(vol * 1e9).toFixed(1)} mm³ | error ${(((vol - expectVol) / expectVol) * 100).toFixed(4)} % ===`);
child.kill();
process.exit(0);
