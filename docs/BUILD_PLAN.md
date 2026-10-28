# ConnectX case study — build plan

Status: **plan for review. Nothing is built yet.**
Scope of this round: page **layout**, **animations** and **interactions**. Final visual polish comes later.

---

## 0. Decisions already made

| Topic | Decision |
|---|---|
| Copy | `case-studies__ai-native-building-energy-product-connectx.md` is the source of truth. The live page copy is older and is only used as an image source. |
| Reference | Metalab › Midjourney: its structure, rhythm and motion, **inverted to light mode** (light background, dark foreground). |
| Fonts | Tcules' own: **Bricolage Grotesque** (display / headings) + **Figtree** (body / UI labels). Swappable later through one token. |
| Layout deliverable | A scrollable **grey-box HTML page**: real copy, real grid, real motion, with placeholder media blocks labelled with the asset that goes there. |
| Live Twin | Embedded **borderless and fully interactive** inside the page. |
| Video | **None.** Every moving product moment is an **HTML component with code-driven animation**. |

---

## 1. What the reference actually does (measured, not guessed)

Captured from metalab.com/work/midjourney in a headless browser:

- **Type scale** (only 5 sizes): 140px display title · 56px intro paragraph · 40px chapter statement · 20px chapter label / stat caption · 16px body.
- **Rhythm**: Hero (giant name → credits row → full-width image that grows on scroll) → one big intro paragraph → **chapter module × 4** (small label + one-line statement, then an asymmetric media composition with a narrow body column tucked beside it) → Outcomes (hairline-ruled stats) → huge "Next case study" marquee → "How can we help?" closing.
- **Motion**: Lenis smooth scroll · nav turns from a full-width bar into a floating blurred pill after the hero · hero image scale-up · line-by-line masked text reveals · media reveals · a context cursor ("Hover" / "Drag") · drag carousel · marquee. Restrained everywhere else.
- **Media treatment**: UI is never shown flat. It is placed on coloured or photographic backdrops, cropped, layered and pulled apart into components.

**Light-mode translation for us:** a warm off-white page, near-black text, and the product UI placed on **soft tinted panels**. The ConnectX UI is itself light, so it needs a tinted backdrop to stand off the page, the way Metalab uses orange. Tcules green appears only as a small accent, never as large fields of colour.

---

## 2. Tech approach

- **Static, no build step**: `index.html` + `css/` + `js/`, so it can be opened locally, shared, and later ported into the Tcules Next.js site.
- Libraries from CDN, pinned versions:
  - **Lenis** (smooth scroll)
  - **GSAP 3 + ScrollTrigger** (scroll-linked motion and pinning)
  - **GSAP SplitText** (line reveals; free since GSAP 3.13)
- **Live Twin** stays its own file (`twin/live-twin.html`), loaded in a same-origin `<iframe>` with a small **embed mode** added (see §6). three.js stays inside the twin only.
- Vanilla JS modules, one file per concern (nav, cursor, reveals, each pinned scene, twin bridge).

```
/index.html
/css/tokens.css      colours, type, spacing, motion tokens
/css/base.css        reset, grid, typography
/css/sections.css    per-section layout
/css/components.css  HTML product components (Instrument Sans, product tokens)
/js/main.js          boot: Lenis + GSAP wiring, reduced-motion switch
/js/nav.js  /js/cursor.js  /js/reveal.js  /js/marquee.js
/js/scenes/choice.js  scenarios.js  peak.js  twin-bridge.js  timeline.js
/twin/live-twin.html (patched copy of ConnectX_Live_Twin.html)
/assets/img/         images (Phase 5)
/docs/BUILD_PLAN.md
```

---

## 3. Design foundations (grey-box values, to be tuned)

**Grid:** 12 columns, max width 1440, outer margin 40 / 32 / 16 (desktop / tablet / mobile), gutter 24 / 20 / 12.

**Type scale** (Metalab sizes mapped to Tcules fonts):

| Token | Desktop | Mobile | Font / weight | Used for |
|---|---|---|---|---|
| `display` | 140 / 0.95 | 64 | Bricolage 500 | Hero "ConnectX", closing heading |
| `intro` | 56 / 1.15 | 30 | Bricolage 400 | Intro paragraph, "How we decide" statement |
| `statement` | 40 / 1.2 | 26 | Bricolage 400 | Chapter statements (H2) |
| `stat` | 96 / 1 | 56 | Bricolage 400 | Facts / trust numerals |
| `label` | 20 / 1.3 | 16 | Figtree 500 | Chapter labels, captions |
| `body` | 16 / 1.45 | 16 | Figtree 400 | Body copy, narrow columns (max ~34ch beside media, ~60ch alone) |
| `meta` | 12 / 1.2 | 12 | Figtree 500, caps | Credits keys, eyebrows |

**Colour tokens** (light):
`--bg #F6F5F1` (close to the twin's `#F2F1ED`, so the embed blends in) · `--bg-2 #EEECE6` · `--ink #0F0F0D` · `--ink-2 #5F5D57` · `--ink-3 #9A978F` · `--line #DEDBD3` · `--accent` Tcules green (sampled from the site footer) · media panel tints: `--tint-sky #E7EDF7`, `--tint-sand #EFE8DC`, `--tint-sage #E5ECE3` · grey-box placeholder `#D9D7D1`.

**Spacing scale:** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192. Space between chapters: 192 desktop / 96 mobile.

**Motion tokens:**
- `--ease-out: cubic-bezier(.16,1,.3,1)` (expo-out, used for most reveals)
- `--ease-io: cubic-bezier(.65,0,.35,1)` (scrubbed / pinned scenes)
- Durations: 0.4 (UI), 0.8 (reveals), 1.2 (large media)
- Stagger: 0.08 (lines), 0.12 (cards)
- Reveal distance: 24px
- Default trigger: element top at 85% of the viewport, played once

---

## 4. Global components and interactions

1. **Smooth scroll** with Lenis, synced to the ScrollTrigger ticker. Switched off when reduced motion is on.
2. **Nav**:
   - At the top of the page: a full-width bar (Tcules logo · Work / Services / Expertise / Insights / Lab / About · "Start a project").
   - After the hero: shrinks into a **floating centred pill** with a blurred light glass background.
   - Hides on fast scroll down and reappears on scroll up.
   - Shows a chapter progress indicator ("03 / Eight scenarios").
3. **Context cursor** (pointer devices only): a small dot that grows into a labelled pill over interactive areas:
   - "Drag" over carousels
   - "Explore" over the twin
   - "Read" over related-case cards
   - The normal cursor comes back inside the twin once it's engaged.
4. **Line reveal**: H2s, the intro and the statements are split into lines, and each line slides up from behind a mask with a stagger.
5. **Media reveal**: frames open with a `clip-path: inset()` wipe while the content inside scales from 1.08 to 1. Light parallax (±40px) on large media only.
6. **Chapter module** (reused six times): label · statement · media composition · narrow body column, in 3 layout variants (A: body left, media right; B: media full width with body below; C: media left, body right) so chapters don't repeat.
7. **Footer**: the existing Tcules green footer, rebuilt so the page feels part of the site.

---

## 5. Section-by-section spec

Notation: **L** = layout · **M** = media (Phase 1 placeholder → final) · **Mo** = motion · **I** = interaction.

### S1 Hero
- **L**:
  - Eyebrow "Case study · ConnectX" (meta).
  - **"ConnectX"** at display size, left-aligned, across the full width.
  - A credits row in 4 columns: Company: ConnectX · Sector: Building energy · Our role: Product definition, interaction design, coded demo → production · Status: **Live since late 2025**.
  - Below that, a full-width media block at 16:9.
  - The SEO H1 (*"ConnectX AI energy product: a plain-language question opens the right workspace"*) sits at label size beneath the credits, so the visual title stays short like Metalab's.
- **M**: the hero image (`CX_Hero_4800x2000`) on a tint panel.
- **Mo**:
  - On load, the title reveals per character and the credits fade up with a stagger.
  - On scroll, the media scales from 0.86 to 1, its corner radius goes from 24 to 0, and it becomes full-bleed.
- **I**: none.

### S2 Intro
- **L**: the 3 intro lines from the markdown as **one 56px paragraph** spanning 9 columns. Below it, two text links: "Follow the product choice ↓" (anchor to #choice) and "Browse all case studies".
- **Mo**: line reveal, then the words brighten from `--ink-3` to `--ink` as the paragraph scrolls past (scrubbed).

### S3 At a glance (#case-context)
- **L**: a 2-column definition list with hairline rules (Product, Our role, Key question, What we delivered, Scenario areas, Digital twin). The "Key question" row is promoted to statement size as the section's pull line. "Related services" sits as a small link row underneath.
- **Mo**: the rules draw from left to right and the rows stagger in.

### S4 Chapter 01: Starting point (#starting-point)
- **L** (variant A): label "Starting point" · statement *"Three teams asking different energy questions."* · body copy. Then:
  - **C1: Role question cards**: three cards (Facilities operator / Finance leader / Sustainability lead), each with an avatar chip and the question that role asks.
  - The closing line *"The ingredients were there…"* as a pull line.
  - **Early concepts carousel**: draggable, using the two `Section_2` images plus Figma's early "Good Afternoon, Sarah" and building-overview frames. Caption: *"ConnectX's early product concepts."*
- **Mo**: in C1, each card's question **types itself in** as the card enters, staggered across the three. The carousel images reveal with the clip-path wipe.
- **I**: drag the carousel (with "Drag" cursor and keyboard arrows); hovering a card lifts it slightly.

### S5 Chapter 02: The choice (#choice). Pinned scene 1
- **L**: label · statement *"An assistant beside the dashboard, or conversation that builds it."* · body copy. Then a **pinned stage about 250vh tall**:
  - **C2: Two directions**:
    - Panel A: a fixed dashboard with an AI chat column.
    - Panel B: chat on its own, assembling KPI cards.
  - **C3: Chosen model flow**: Conversation → Match to a known situation → Permitted tools fetch data → Assemble modules + twin view → Workspace stays open.
- **Mo** (scrubbed with scroll, 4 beats):
  1. Panels A and B sit side by side, each with a one-line verdict ("Familiar, but fixed" / "Adaptive, but nowhere to keep working").
  2. They slide together and overlap.
  3. They merge into one workspace.
  4. The C3 flow draws its 5 steps along a connecting line, and the closing line appears: *"The dashboard stayed, and chat became one way to build the right version of it."*
- **Mobile**: not pinned. The beats stack vertically, each with its own reveal.

### S6 Chapter 03: Eight scenarios (#turning-adaptation-into-scenarios). Pinned scene 2
- **L**: label · statement *"Eight scenarios made the adaptive workspace testable."* · body copy. Then a **pinned split** (5 / 7 columns):
  - **Left**: the list of 8 scenarios, grouped under the 4 areas (System status / Forecasting / Asset performance / Operational conditions).
  - **Right**: **C4: Scenario spec card**, with 6 rows: *Request · Intent detected · Data required · Interface modules · Twin behaviour · Next action*.
- **Mo**: as you scroll, the active list item highlights, and the spec card's rows update one after another (the old value slides up, the new one in). A progress bar shows "3 / 8".
- **I**: clicking a list item jumps to its scroll position.
- **Sub-section: "A peak-price request, with everything needed to act"** (not pinned, variant B):
  - **C5: Peak-price assembly**: a small product UI on a tint panel.
- **C5 motion** (plays once on enter, with a replay button):
  1. The question types into the ask bar: *"Price spikes at 17:00, what should we do?"*
  2. Resolver steps tick: Intent → Data → Tools.
  3. The affected assets light up in a mini twin diagram.
  4. KPI tiles and a battery action card slide into a grid, each tile labelled with *why it's there*.

### S7 Chapter 04: Digital twin (#designing-the-digital-twin)
- **L** (variant C): label · statement *"A 2.5D view that explains the system."* · body copy. Then:
  - **Compare strip**: "Explored: realistic 3D / maps" (the map-view and realistic images, desaturated) next to "Chosen: 2.5D explanation layer" (`Section_5_Image_1`).
  - Caption from the markdown.
  - Then the **Live Twin feature** (§6): full-bleed, borderless, 100vh, starting with the twin's own "Building a digital twin" loader the first time it's seen.
- **Mo**: in the compare strip, the "Explored" side dims and slides back as the "Chosen" side comes forward. The twin section fades the page background into the twin's ground colour so there's no visible edge.
- **I**: see §6.

### S8 Chapter 05: Demo to production (#the-demonstration-ran-in-code-on-interim-data)
- **L** (variant B): label · statement *"From coded demo to production-ready module."* · body copy. Then:
  - The full-width workspace image (`Section_4_Image`), captioned *"The coded demo, shown with sample data."*
  - **C6: Timeline**: 3 steps, Product work → Demo → Production, *live since late 2025*.
- **Mo**: the image reveals with clip-path plus parallax. The timeline line fills with scroll, and each node pops and reveals its text as the fill reaches it. The last node pulses once in Tcules green ("Live").

### S9 Chapter 06: How we decide (#chat-is-an-interaction-mode-not-a-complete-produ)
- **L**: label · statement at **intro size (56px)**, like Metalab's big read: *"We decide what the conversation controls and what stays on screen."* Below it, the 6 things defined per scenario as a ruled list (request · data · permitted tools · what the screen shows · the action · the way back from a mistake). Then the closing paragraph.
- **Mo**: the words brighten with scroll; the list rules draw in with a stagger.

### S10 Facts (Metalab's "Outcomes", with no invented metrics)
- **L**: heading *"What the work delivered"*, then 3 rows with hairline rules: **8** · scenarios defined · **4** · scenario areas · **Late 2025** · live in production.
- **Mo**: numbers count up, and the rules draw in.

### S11 Testimonials (#testimonials)
- **L**: one large quote at statement size, with attribution (Pratik Ghoshal, CEO, ConnectX), plus "1 / 2" and previous/next controls.
- **Mo / I**: crossfade between the quotes with a line reveal. Auto-advance is off; arrows, swipe and keyboard all work.

### S12 FAQ (#faq)
- **L**: a 4-item accordion, 8 columns wide, with hairline rules. The FAQPage structured data from the frontmatter is kept.
- **Mo**: height animates open and closed and the plus rotates into a cross. Keyboard accessible.

### S13 Trust strip
- **L**: one row: Founded **2017** · **90+** projects · Clients in **19** countries · **4.8** on Clutch (13 reviews, linked).
- **Mo**: count-up on enter.

### S14 Related → Next case study (#related)
- **L**:
  - The line *"Other AI products where people check the model's work"*.
  - A **huge marquee** reading "Next case study • BuildTwin •" with a BuildTwin card overlapping it, Metalab-style.
  - Underneath: a secondary row (Eden AI case · Product Design · ClimateTech & energy).
- **Mo / I**: the marquee drifts constantly and speeds up with scroll velocity. Hovering the card scales its image, and the cursor shows "Read".

### S15 Enquiry (#enquiry)
- **L**:
  - Display-size heading: *"Tell us what your AI product should be able to answer"*, with the subline.
  - A 3-field form: Email · What are you working on? · Product or company URL (optional).
  - "Send enquiry" as the primary button and "See available times" as a secondary link.
  - Success state: *"Your enquiry has reached us / We'll reply within one business day."*, keeping what was typed.
  - Hidden context fields: route, placement, case.
- **Mo**: the heading line-reveals and the fields rise in with a stagger. Submitting morphs the button into the success state. In this prototype the form is wired to a stub, not the CMS.

### S16 Footer
The Tcules green footer, as on the live site.

---

## 6. Live Twin embed: technical spec

The twin is a 3,000-line single file (three.js r149) with Home, Live and Reports views, 6 scenarios, roles, a loader, and a `window.__cx` API. It already has a mobile layout and a no-WebGL fallback.

**Changes to a copy (`twin/live-twin.html`), only when `?embed=1` is in the URL:**
1. **Borderless**: the twin keeps its own product chrome (ConnectX top bar, panels), because that is the product, but loses any outer framing. Its background matches the page token, so the iframe edge is invisible.
2. **Scroll safety**: the twin currently uses the mouse wheel to zoom (`preventDefault`), which would trap page scrolling. In embed mode, wheel zoom only works once the reader has **engaged** the twin.
3. **Pause / resume**: a `postMessage` bridge lets the page stop the render loop while the twin is off-screen, saving battery and GPU.
4. **Loader**: the "Building a digital twin" intro plays when the section first comes into view, not on page load. "Skip intro" stays.
5. **Events out**: the twin tells the page when a scenario starts or ends, so the page can show a caption.

**Page side:**
- **Lazy load**: the iframe is injected when the section is about 1 viewport away, with a static poster image shown until then.
- **Engage model**:
  - Before engaging, an overlay pill reads "Explore the live twin" with three suggested chips ("Run peak tariff", "Grid outage", "Ask a question"), and the page scrolls straight past.
  - Clicking engages the twin: the overlay fades, the cursor returns to normal and wheel/drag control the twin. A small "Exit ✕" button appears, and Esc also exits.
  - Scrolling out of the section disengages it automatically.
- **Size**: 100vh (minimum 720px) on desktop, full-bleed.
- **Mobile**: a full-width poster plus an "Open the live twin" button that opens the same embed full-screen in an overlay. A twin squeezed into a scrolling page on a phone would fight touch scrolling.
- **Reduced motion**: the loader is skipped and the twin opens in its static Live view.

---

## 7. HTML components that replace video

All are built in the **ConnectX product style** (Instrument Sans + Geist Mono and the twin's colour tokens), so they read as "the product" against the Tcules-styled page.

| ID | Component | Section | What animates |
|---|---|---|---|
| C1 | Role question cards | S4 | Questions type in; avatars pop |
| C2 | Two directions | S5 | Panels slide, overlap and merge (scrubbed) |
| C3 | Request → workspace flow | S5 | 5 steps draw along a connecting line |
| C4 | Scenario spec card | S6 | Rows swap per active scenario |
| C5 | Peak-price assembly | S6 | Ask → resolver steps → assets light → modules assemble |
| C6 | Demo → production timeline | S8 | Line fills, nodes reveal, "Live" pulse |

In Phase 1 these are grey-box rectangles of the right size with labels. They're built properly in Phase 3.

---

## 8. Responsive

- Breakpoints: ≥1280 desktop · 1024 small desktop · 768 tablet · <768 mobile. Each breakpoint is checked at 1440 / 1024 / 768 / 390.
- On mobile both pinned scenes (S5, S6) are unpinned and become stacked, step-by-step reveals.
- On mobile the hero title scales with the viewport (`clamp`) so "ConnectX" always fits on one line.
- On touch devices the custom cursor is off; carousels use native swipe.
- No horizontal scroll at any width.

---

## 9. Accessibility, SEO, performance

- **Reduced motion**: Lenis off, no pinning, no scrub. Content appears with a short fade. Everything stays readable without JS: the server HTML holds the full copy, and JS only adds motion.
- **Semantics**: one H1, H2 per section using the markdown anchors, the FAQ marked as `<details>`-style accessible disclosure, visible focus states, labelled form fields, and alt text from the markdown's media bindings.
- **SEO**: meta tags from the frontmatter (title, description, canonical, OG/Twitter), plus JSON-LD for WebPage, BreadcrumbList and FAQPage.
- **Performance budget**:
  - Page JS without the twin is under 120 KB gzipped.
  - Images in WebP/AVIF with `srcset`.
  - The twin loads lazily and pauses when off-screen.
  - Only `transform` / `opacity` / `clip-path` are animated.
  - Target: Lighthouse performance ≥ 85 on desktop with the twin section not yet loaded.

---

## 10. Build phases and review checkpoints

| Phase | Output | You review |
|---|---|---|
| **P1 Foundation + grey-box layout** | Tokens, grid, type, nav, footer, all 16 sections with real copy and labelled grey placeholders. No motion. | Layout, hierarchy, spacing, section order |
| **P2 Motion system** | Lenis, line and media reveals, nav pill, cursor, both pinned scenes on grey boxes, marquee, count-ups, accordion, reduced-motion path. | Feel, timing, pacing |
| **P3 HTML components** | C1–C6 built and animated. | Each component's story |
| **P4 Live Twin embed** | Patched twin, lazy load, engage/exit, pause, mobile overlay. | Interaction model |
| **P5 Assets** | Real images placed on tint panels (live-page Cloudinary images + Figma exports). | Visual composition |
| **P6 QA** | Playwright screenshots at 4 widths, reduced-motion pass, keyboard pass, Lighthouse, cross-browser smoke test. | Sign-off |

Each phase is committed to `claude/cool-rubin-hrpv85` and shared as a link you can scroll.

---

## 11. Out of scope for this round
- Final art direction (colour of tint panels, image crops): rough in P5, refined later.
- CMS / form backend wiring and scheduling integration.
- Porting into the production Next.js site.
- New copy. Only structural tweaks are proposed, flagged in review.

---

## 12. Open questions (answers change the build)
1. **The 8 scenarios**: the markdown names the 4 areas but not the 8 scenarios. The twin has 6 (Clouds & rain, Clear sky, EV rush, Grid outage, Floor anomaly, Peak tariff). What are the 8 names, and what are their request/intent/data/modules/twin/action values?
2. **Nav and footer**: rebuild the Tcules site nav and green footer (assumed), or use a lighter, case-study-only nav like Metalab's?
3. **Facts row (S10)**: is "8 scenarios · 4 areas · live since late 2025" acceptable, or is there a real metric you can share?
4. **Twin chrome**: inside the embed, keep the ConnectX product top bar (assumed), or hide it so only the 3D scene and its panels show?
