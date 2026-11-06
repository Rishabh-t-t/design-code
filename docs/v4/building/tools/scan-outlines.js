const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  await p.goto('http://localhost:8766/render.html'); await p.waitForFunction(() => window.ready);
  const r = await p.evaluate(() => {
    const TX0 = -8, TX1 = 8, TZ0 = -10, TZ1 = 6, CX1 = 10.2, CZ0 = -1.2, CZ1 = 3.2, BX = -3, BZ = 4.2, PX0 = -9, PX1 = 10.6, PZ0 = -11, PZ1 = 7.4, PL = 0.4, G = 4.5, FH = 3.6, TOP = 4.5 + 3.6 * 8;
    const P = (pts, y) => pts.map(([x, z]) => { const [u, v] = proj(x, y, z); return [Math.round(u * 1600), Math.round(v * 1000)]; });
    const rect = (x0, z0, x1, z1) => [[x0, z0], [x1, z0], [x1, z1], [x0, z1]];
    const lerpR = (a, b, t) => a.map((v, i) => v + (b[i] - v) * t);
    const plot = [-29, -22, 29, 22], pl = [PX0 - 1.3, PZ0 - 1.3, PX1 + 1.3, PZ1 + 1.3];
    const tower = [[TX0, TZ0], [TX1, TZ0], [TX1, CZ0], [CX1, CZ0], [CX1, CZ1], [TX1, CZ1], [TX1, TZ1], [BX, TZ1], [BX, BZ], [TX0, BZ]];
    const out = { site: [], floors: [] };
    for (const t of [0, 0.35, 0.65, 1]) out.site.push(P(rect(...lerpR(plot, pl, t)), t === 1 ? PL : 0.02));
    out.floors.push(P(rect(PX0, PZ0, PX1, PZ1), PL + 0.05));
    out.floors.push(P(rect(PX0, PZ0, PX1, PZ1), G - 0.35));
    for (let k = 2; k <= 9; k++) out.floors.push(P(tower, G + (k - 1) * FH - 0.35));
    out.floors.push(P(rect(-8, -10, -2.5, -4), TOP + FH));
    return out;
  });
  fs.writeFileSync(__dirname + '/scan.json', JSON.stringify(r)); console.log(r.site.length, r.floors.length); await b.close();
})();
