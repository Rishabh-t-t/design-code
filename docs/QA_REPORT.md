# ConnectX case study — QA report (Phase 6)

Tested on the live GitHub Pages build: https://rishabh-t-t.github.io/design-code/
Browser: Chromium (headless, via Playwright). Other engines were not available in the test environment; see "Still to check by hand".

## Results

| Check | Result |
|---|---|
| Lighthouse, desktop preset (3 runs) | Performance **84–85** · Accessibility **100** · Best practices **100** · SEO **100** |
| Core timings | First paint 1.1–1.3 s · Largest paint 1.7–1.8 s · Blocking time 130–170 ms · Layout shift **0** |
| axe-core (every reveal played, twin iframe excluded) | **0 violations** |
| Colour contrast | **0 failures** (was 175) |
| Keyboard | 74 Tab stops from skip link to footer; every stop is visible, on screen and shows a focus ring |
| Reduced motion | Complete static page: no smooth scroll, pinning or scrub; twin skips its intro and opens live |
| Widths 1024 · 1280 · 1440 · 1920 · 2560 | No horizontal overflow, no console errors at any width |
| Console | No errors |
| Duplicate IDs | None |
| Headings | One H1; H2 per section using the markdown's anchors; H3s under their H2s |
| Images | All 10 load; responsive `srcset` (WebP/AVIF from Cloudinary); hero loads first, the rest lazily |
| Live Twin | Loads one screen early, page scroll passes over it until engaged, wheel/drag go to the twin once engaged, Exit/Esc hand back, pauses off screen |

## What the QA pass changed

1. **Contrast**
   - `--ink-3` labels moved from `#7A7A7A` (3.86:1) to `#696965` (4.96:1 on the page, ≥4.58:1 on every panel tint).
   - Words waiting to brighten use `--ink-dim` `#8A8A86` (3.12:1). It's only used on 40–64 px text, which counts as large text.
   - Small product text on soft fills uses the product's darker blue `#2F51B8` and orange `#C4471C`.
   - Flow steps wait in legible grey instead of at 15% opacity.
   - The form's "Optional" label and the wireframe notes now pass AA.
2. **ARIA** — the text-splitting library no longer puts `aria-label` on `<p>` elements (not allowed by ARIA).
3. **Keyboard**
   - An element that is still fading in becomes visible the moment it receives focus.
   - The twin's call-to-action is `inert` while it is hidden.
4. **Performance**
   - The hero intro starts as soon as the page is parsed.
   - The rest of the motion set-up waits for fonts and runs in short tasks. Blocking time dropped from 250 ms to about 150 ms.
5. **Favicon** — an inline SVG removes the `/favicon.ico` 404.

## Known limits (by design or out of scope)

- **Performance:** most remaining main-thread time is GSAP start-up and splitting text into lines. The page is about 485 KB, and about 230 KB of that is the Live Twin, which only runs when you reach it.
- **The twin's intro speed:** its clock advances per frame. On machines without a graphics card it plays slowly (about 20 s in the headless test, about 6 s on a normal laptop). Skip intro is always available.
- **Screen readers and the twin:** the twin is a canvas-based 3D view. Its floating cards and buttons are real HTML, but the 3D scene itself has no text alternative beyond the section caption.
- **Wireframe notes:** the pink notes and the Notes button are still in the page for review. Remove them before launch (IMP-10).
- **Desktop only:** 1024 px and up (IMP-04).

## Still to check by hand

- **Safari and Firefox** (desktop):
  - Lenis smooth scroll;
  - `clip-path` reveals;
  - container-query sizing in the product mocks;
  - `mix-blend-mode` on the compare images;
  - the twin's WebGL.
- **Trackpad gestures:** a horizontal swipe on the concepts carousel, and a pinch over the engaged twin.
- **A real screen reader** (VoiceOver or NVDA) through the pinned scenes and the FAQ.
- **A real GPU:** the twin's frame rate while a scenario plays.

## Re-running

The QA scripts used for this pass live outside the repo, in the session scratchpad. Lighthouse can be re-run on any machine with Chrome:

```bash
npx lighthouse https://rishabh-t-t.github.io/design-code/ --preset=desktop --view
```
