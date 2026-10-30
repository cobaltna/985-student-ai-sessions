// Independent analytic check of the gear cross-section (no SolidWorks involved).
// Compares (a) the true involute profile against (b) the 12-chord polyline the model was built from,
// and predicts the volume each should produce so the SolidWorks number can be judged.
const M = 0.002, Z = 20, ALPHA = (20 * Math.PI) / 180, T = 0.01;
const rp = (M * Z) / 2, ra = rp + M, rf = rp - 1.25 * M, rb = rp * Math.cos(ALPHA);
const inv = (a) => Math.tan(a) - a;
const halfPitch = Math.PI / (2 * Z), invP = inv(ALPHA), halfTooth = Math.PI / Z;
const offsetAt = (r) => halfPitch + invP - inv(Math.acos(Math.min(1, rb / r)));
const w = (r) => halfTooth - (r <= rb ? offsetAt(rb) : offsetAt(r));   // gap half-angle at radius r (rad)

// --- polar-integral area of one clipped tooth space:  A = ∫ 2w(r)·r dr ,  rf → ra
const polarArea = (wfn, n = 200000) => {
  let a = 0, dr = (ra - rf) / n;
  for (let i = 0; i < n; i++) {
    const r0 = rf + i * dr, r1 = r0 + dr;
    a += ((2 * wfn(r0) * r0 + 2 * wfn(r1) * r1) / 2) * dr;   // trapezoid
  }
  return a;
};
const A_exact = polarArea(w);

// --- the chord model: a straight segment between sampled involute points, evaluated at radius r
const N = 12, RMAX = 0.0225;
const tMax = Math.sqrt((RMAX / rb) ** 2 - 1);
const P = Array.from({ length: N + 1 }, (_, i) => {
  const r = rb * Math.sqrt(1 + (tMax * (i / N)) ** 2);
  return { r, a: offsetAt(r) };
});
// angle of the chord (between sample i and i+1) at radius r — exact intersection of |P|=r with the line
const chordAngle = (i, r) => {
  const A = P[i], B = P[i + 1];
  const x1 = A.r * Math.cos(A.a), y1 = A.r * Math.sin(A.a), x2 = B.r * Math.cos(B.a), y2 = B.r * Math.sin(B.a);
  const dx = x2 - x1, dy = y2 - y1;
  const A2 = dx * dx + dy * dy, B2 = 2 * (x1 * dx + y1 * dy), C2 = x1 * x1 + y1 * y1 - r * r;
  const disc = Math.max(0, B2 * B2 - 4 * A2 * C2);
  const s = (-B2 + Math.sqrt(disc)) / (2 * A2);
  return Math.atan2(y1 + s * dy, x1 + s * dx);
};
const wChord = (r) => {
  if (r <= rb) return w(rb);
  for (let i = 0; i < N; i++) if (r <= P[i + 1].r) return halfTooth - chordAngle(i, r);
  return halfTooth - chordAngle(N - 1, r);
};
const A_chord = polarArea(wChord);

// --- max deviation of the chord polyline from the true involute (µm)
let maxDev = 0;
for (let i = 0; i < N; i++) {
  const A = P[i], B = P[i + 1];
  const x1 = A.r * Math.cos(A.a), y1 = A.r * Math.sin(A.a), x2 = B.r * Math.cos(B.a), y2 = B.r * Math.sin(B.a);
  for (let s = 0; s <= 1; s += 1 / 50) {
    const xm = x1 + s * (x2 - x1), ym = y1 + s * (y2 - y1);
    const r = Math.hypot(xm, ym), ang = Math.atan2(ym, xm);
    const trueAng = halfTooth - (r <= rb ? offsetAt(rb) : offsetAt(r));
    maxDev = Math.max(maxDev, Math.abs(ang - trueAng) * r);
  }
}

const A_holes = 4 * Math.PI * 0.0025 ** 2 + Math.PI * 0.005 ** 2;
const V = (Ag) => (Math.PI * ra ** 2 - Z * Ag - A_holes) * T;

console.log(`rp=${(rp * 1000).toFixed(4)} ra=${(ra * 1000).toFixed(3)} rf=${(rf * 1000).toFixed(3)} rb=${(rb * 1000).toFixed(4)} mm`);
console.log(`gap area  exact=${(A_exact * 1e6).toFixed(4)} mm²   12-chord=${(A_chord * 1e6).toFixed(4)} mm²   Δ=${((A_chord - A_exact) * 1e6).toFixed(4)} mm²`);
console.log(`max chord deviation from true involute = ${(maxDev * 1e6).toFixed(1)} µm`);
console.log(`predicted volume  exact=${(V(A_exact) * 1e9).toFixed(1)} mm³   12-chord=${(V(A_chord) * 1e9).toFixed(1)} mm³`);
console.log(`SolidWorks measured                                    = 10687.7 mm³`);
console.log(`  → vs 12-chord model: ${(((10687.7 - V(A_chord) * 1e9) / (V(A_chord) * 1e9)) * 100).toFixed(3)} %`);
console.log(`  → vs true involute : ${(((10687.7 - V(A_exact) * 1e9) / (V(A_exact) * 1e9)) * 100).toFixed(3)} %`);
