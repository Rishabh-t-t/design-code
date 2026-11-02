# ConnectX case study — rebuild on the Figma layout (v3)

Source of truth: Figma "Case study – ConnectX", frame **test-1** (`46:1823`).
Goal: rebuild the page's structure, type and colour on the Figma layout and keep the current experience: scroll animations, transitions, sticky scenes and live twins.
Snapshot of the previous version: branch `v2-revision-snapshot`.

---

## 0. Defaults used (your open questions from the last review)

| # | Question | Default used | Easy to change? |
|---|---|---|---|
| 1 | Faded sections (Delivered → Enquiry) | Keep their current layout; apply the new type and colour tokens | Yes |
| 2 | Hero / scenario / peak media | Keep the **live twins** inside the Figma media containers | Yes |
| 3 | Placeholder text | Fill with real copy: Company → *ConnectX*; image captions from the markdown and the image alts; banner citation lines → the chapter each banner closes; "Full Vph" → the choice scene at full viewport height | Yes |
| 4 | Chapter numbering | 01 Starting point · 02 The choice · 03 Scenarios · **04 Digital twin · 05 Demo to production · 06 How we decide** | Yes |
| 5 | Orange outlines | Working markers, not built | Yes |

---

## 1. Design system (from the Figma text styles and variables)

### Scale
- Figma is fixed at 1440. In code every value scales linearly with the viewport: **exact at 1440**, clamped at 1024 and 1920+, so the page holds from 1024 to 1920 and beyond.
- Side padding is 56 at 1440, written `clamp(32px, 3.889vw, 80px)`.
- Section content is capped at 1680 px, while the backgrounds (gradients, the grey band) stay full-bleed.

### Text styles → CSS custom properties (`--t-*`)

| Figma style | Font | Size/line (at 1440) |
|---|---|---|
| Display/Small (hero) | Bricolage Medium | 76/80 |
| Display/Large (marquee) | Bricolage Regular | 200/200 |
| Heading/Large | Bricolage Regular | 48/52 |
| Heading/Medium | Bricolage Regular | 32/40 |
| Heading/Small | Bricolage Regular | 24/32 |
| Data/Large | Bricolage Regular | 92/96 |
| Label/Large · Medium · Small | Figtree SemiBold | 20/24 · 16/20 · 12/16 |
| Body/Large · Medium · Small | Figtree Regular | 16/24 · 14/20 · 12/18 |
| Mono/Large · Medium · Small | Geist Mono | 14/20 · 12/16 · 10/16 |
| Caption | Figtree Italic | 12/18 (images), 16/24 (banner citation) |

### Colours

| Use | Token | Value |
|---|---|---|
| Ink | `--ink` | `#0B0B0B` |
| Body | `--ink-2` | `#464646` |
| Labels | `--ink-3` | `#696965` |
| Hero meta label | `--ink-meta` | `#999999` |
| Hero meta value / links | `--ink-soft` | `#666666` |
| Divider | `--line` | `#E7E7E3` |
| Brand (Live badge) | `--brand` | `#04EC50` |
| Link arrows | `--brand-ink` | `#00C23F` |
| Sand | `--sand` | `#F4EDE2` |
| Banner end | `--paper` | `#FAFAFA` |
| Choice band | `--band` | `#ECECE9` |
| Role tags | facilities / finance / sustainability | `#C74420` / `#3453BC` / `#447E61` |
| Role card | | `#FAFAFA` fill, `#DEDCD5` border, 3 px radius, shadow `2px 4px 13.6px rgb(164 183 219 / .5)` |
| Testimonial card | | white, 14 px radius |
| Monogram | | `#1A1A17`, 8 px radius |

- The page background becomes **white**; the sand gradients and grey band create the colour moments.
- Contrast is rechecked in QA. `#999` meta labels on white are 2.85:1 and fail AA. **Fallback:** the labels use `#767676` (4.54:1), which reads the same at a glance; logged as a deviation.

### Gradients and shapes
- **Hero:** linear, top → bottom, `#FFFFFF → #F4EDE2`.
- **Intro:** linear `#F4EDE2 → #FFFFFF`, plus one huge white ellipse (5812 px wide, top 16 px, centred). Its curved top edge draws the horizon between the hero's sand and the intro's white. Built as a CSS radial/ellipse shape, not an image.
- **Centred banners:** linear `#FFFFFF → #FAFAFA`.
- **The choice:** a full-viewport grey band (`--band`).

---

## 2. Structure: section by section (mirrors the Figma frames)

Every block is a `<section>` with a `.sec` inner container (side padding plus max-width). The Figma flex/grid settings map 1:1:

| Figma frame | Code | Layout |
|---|---|---|
| navbar | `header.nav` | flex row, space-between, centred, padding 24 |
| hero-section | `section.hero` | column: label row → title row → `.details` (flex row, gap 24; first item flex:1) → `.hero__media` (live twin, 711 px tall at 1440, full-bleed) |
| intro-section | `section.intro` | column: summary row (pt 56) → `.split` (2 columns, gap 24; left empty, right Body/Medium) → links row (gap 24, pb 112) |
| glance-section | `section.glance` | header stack (gap 16) → `.split` (gap 8): key question (16 lead + 32 heading) │ summary rows (flex column, gap 8; each row = 250 label + value, top divider) |
| item sections (×6) | `section.chapter` | chapter label row (Mono/Medium, pt 128, first chapter 72) → heading row (Heading/Large) → `.split` (left empty, right copy) → media |
| cent-text-banner (×3) | `section.banner` | flex column, centred, gap 24, padding 128 × 240, gradient; Heading/Large centred + italic citation |
| image-shells (×3) | `div.shells` | flex row, gap 24 → 2 × (1:1 shell + italic caption), padding 128 |
| choice band | `div.band` inside 02 | full-viewport grey band, **sticky**; Direction A/B + the 1→5 flow |
| scenarios-areas | `div.areas` | grid `357px 1fr`, gap 16; list (flex column, gap 8; counter pushed to the bottom) │ live twin (770 px at 1440) — **sticky** |
| peak-request | `div.peak` | grid `1fr 319px`, gap 16; live twin (ask mode) │ text (flex column, space-between: Heading/Medium at the top, copy at the bottom) |
| timeline row | `div.timeline` | flex row, gap 34: title (flex 1) + 3 milestones (flex 1) |
| how-we-decide | `section.chapter` (06) | heading = the long sentence; `.split`: numbered rule rows │ copy |
| Delivered → Enquiry | (current) | Current layout kept; new tokens; side padding moves to the shared 56 |
| Footer | (current) | Unchanged |

**Section order (new):**
nav → hero → intro → glance → 01 Starting point → banner ("The ingredients…") → shells (early concepts) → 02 The choice (band) → banner ("The dashboard stayed…") → 03 Scenarios (areas + peak) → 04 Digital twin → shells (map vs 2.5D) → banner ("The simpler look…") → 05 Demo to production → shells (request / workspace) → timeline → 06 How we decide → delivered → testimonials → FAQ → trust → related → enquiry → footer.

**Removed:** the early-concepts drag carousel, which the image shells replace (the Figma frames stay as their images).

---

## 3. What stays from the current build (behaviour)

- **Smooth scroll** (Lenis), the nav that turns into a pill, the chapter label in the pill, and the context cursor.
- **Reveals:** line reveals on headings, fade-ups, drawn hairlines (summary rows, rule rows, timeline), clip-wipe image reveals, count-ups.
- **Sticky scenes** (native `position: sticky`): the choice band and the scenario areas, with the same beats (A + B merge → chosen model → flow draws).
- **Live twins** (sandboxed, picture first, wheel passes through) in the hero, scenario and peak media containers.
- **Role-card typing.** The cards move into the **staggered** Figma arrangement; each one floats in at its own position.
- **Other interactions:** FAQ accordion, marquee, form behaviour, reduced-motion path, keyboard focus fixes.

---

## 4. Build steps (each committed and live on GitHub Pages)

| Step | Scope | Check |
|---|---|---|
| **F1 Tokens and shell** ✅ | New tokens (type, colour, spacing, scaling), base styles, shared `.sec` / `.split` / chapter-label / heading primitives, white page | Build, no console errors |
| **F2 Top of page** ✅ | Navbar, hero (gradient, title, details row, twin media), intro (sand → white, ellipse horizon, summary, split copy, links), glance | Screenshot vs Figma at 1440 |
| **F3 Chapters 01–02** ✅ | Starting point with staggered role cards, banner, image shells, the choice band (sticky, full viewport) | Sticky holds at its line with 0 jumps |
| **F4 Chapters 03–06** ✅ | Scenarios (357 + twin, sticky), flipped peak block, Digital twin and Demo shells, banners, timeline row, How we decide | Twins live, scenarios switch |
| **F5 Faded sections** ✅ | Delivered → Enquiry: tokens and padding only | Visual pass |
| **F6 Motion re-wire and QA** ✅ | Point reveals at the new markup; axe, keyboard, reduced motion, 1024–2560 widths, Lighthouse, sticky and twin regression | Same bar as v2: Accessibility/Best practices/SEO 100, Performance ≥ 85 |

---

## 5. Known deviations from Figma (by design)
- The **hero meta labels** use `#767676` instead of `#999` for contrast.
- The **scenarios and peak** grids use fixed-plus-flexible columns (`357px 1fr`, `1fr 319px`) instead of two equal columns, so the fixed widths in Figma hold across screen sizes.
- The **media containers hold live twins**, not static images, as in v2.


---

## QA results (F6, live build)

| Check | Result |
|---|---|
| Lighthouse desktop (2 runs) | Performance **82–84** · Accessibility **100** · Best practices **100** · SEO **100** · blocking time 20 ms |
| Layout shift | 0.023 overall, but **0.00001 on the page itself**: the rest comes from inside the hero twin's frame (its floating cards appearing), not from page layout |
| axe | 0 violations (after giving the three banners unique labels) |
| Keyboard | 68 stops, all visible with focus rings |
| Reduced motion | Static page, hero twin live |
| Widths 1024 → 2560 | No overflow, no errors |
| Sticky scenes | Choice band holds at the top, scenarios at 96 px, 0 jumps |
| Live twins | Hero (transparent, building-framed), scenarios and peak all work; wheel passes through |

Fixed during QA: a long jump down the page queued every skipped reveal into one staggered batch (up to ~7 s late). Skipped elements now show at once, and only what is on screen staggers (capped). Role cards no longer collide at 1024.
