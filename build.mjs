// Inlines src/ into one self-contained HTML file: dist/connectx-case-study.html
// and copies it to index.html at the repo root for GitHub Pages.
// Usage: node build.mjs
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const src = join(root, 'src');
const out = join(root, 'dist', 'connectx-case-study.html');
const read = (p) => readFileSync(join(src, p), 'utf8');

let html = read('index.html');

// <link rel="stylesheet" href="css/…"> → <style>…</style>  (external URLs are left alone)
html = html.replace(/<link rel="stylesheet" href="((?!https?:)[^"]+)">/g, (_, p) => `<style>\n${read(p)}</style>`);

// <script src="js/…"></script> → <script>…</script>
html = html.replace(/<script src="((?!https?:)[^"]+)"><\/script>/g, (_, p) => `<script>\n${read(p)}</script>`);

// <!-- @inline path --> → file contents (SVGs, templates)
html = html.replace(/<!-- @inline ([^ ]+) -->/g, (_, p) => read(p).trim());

// <!-- @twin-json path --> → the Live Twin's HTML as JSON in an inert script tag.
// "</" is escaped so the payload can never close the tag early; twin.js reads it back into a Blob.
html = html.replace(/<!-- @twin-json ([^ ]+) -->/g, (_, p) =>
  `<script type="application/json" id="twin-src">${JSON.stringify(read(p)).replace(/<\//g, '<\\/')}</script>`);

mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, html);
// Root copy so GitHub Pages can serve the page at the site root
writeFileSync(join(root, 'index.html'), html);
console.log(`built ${out} (${(Buffer.byteLength(html) / 1024).toFixed(1)} KB)`);
