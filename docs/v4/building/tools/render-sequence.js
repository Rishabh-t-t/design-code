const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const [from, to, step = 1] = process.argv.slice(2).map(Number);
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('http://localhost:8766/render.html'); await p.waitForFunction(() => window.ready, null, { timeout: 60000 });
  fs.mkdirSync(__dirname + '/seq', { recursive: true });
  for (let i = from; i <= to; i += step) {
    const n = String(i).padStart(3, '0');
    const u1 = await p.evaluate((i) => window.renderFrame(i), i); fs.writeFileSync(`${__dirname}/seq/q${n}.png`, Buffer.from(u1.split(',')[1], 'base64'));
    const u2 = await p.evaluate((i) => window.renderFrameAO(i), i); fs.writeFileSync(`${__dirname}/seq/q${n}-ao.png`, Buffer.from(u2.split(',')[1], 'base64'));
  }
  console.log('done', from, to, 'errors', errs.slice(0, 5)); await b.close();
})();
