// Renders each Live Twin embed mode and saves its first frame as the instant picture the page
// shows until the live twin is ready: src/assets/twin/poster-{hero,scenario,ask}.jpg
// Usage: node tools/gen-twin-posters.mjs   (needs Playwright + Chromium; re-run when the twin changes)
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const twin = 'file://' + join(root, 'src/twin/live-twin.html');

// Viewports roughly match each host's size on the page at 1440 × 900
const SHOTS = [
  { mode: 'hero', width: 1600, height: 820 },
  { mode: 'scenario', width: 1100, height: 900 },
  { mode: 'ask', width: 1200, height: 900 },
];

const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
for (const { mode, width, height } of SHOTS) {
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto(`${twin}?embed=${mode}`, { waitUntil: 'networkidle' });
  await page.waitForSelector('#gl canvas');
  await page.waitForTimeout(4000); // let the camera settle and the KPI cards fill
  const out = join(root, `src/assets/twin/poster-${mode}.jpg`);
  await page.screenshot({ path: out, type: 'jpeg', quality: 74 });
  console.log('wrote', out);
  await page.close();
}
await browser.close();
