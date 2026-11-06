const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('http://localhost:8766/render.html'); await p.waitForFunction(() => window.ready, null, { timeout: 60000 });
  const G = 4.5, FH = 3.6, TOP = G + FH * 8;
  const jobs = [['m-ground', 'ground', 0, 0], ['m-f0', 'band', -0.1, G - 0.35]];
  for (let k = 1; k <= 8; k++) jobs.push(['m-f' + k, 'band', G + (k - 1) * FH - 0.35, G + k * FH - 0.35]);
  jobs.push(['m-f9', 'band', TOP - 0.35, TOP + FH + 4]);
  for (const [name, kind, y0, y1] of jobs) {
    const u = await p.evaluate(([k, a, c]) => window.renderMask('done', k, a, c), [kind, y0, y1]);
    fs.writeFileSync(__dirname + '/out/' + name + '.png', Buffer.from(u.split(',')[1], 'base64'));
  }
  console.log('errors', errs.slice(0, 5)); await b.close();
})();
