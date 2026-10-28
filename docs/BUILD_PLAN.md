# ConnectX case study — build plan (v2)

Status: **plan for review. Nothing is built yet.**
Scope of this round: page **layout**, **animations** and **interactions**, desktop **1024 → 1920+**.

---

## 0. Decisions

| Topic | Decision |
|---|---|
| Copy | `case-studies__ai-native-building-energy-product-connectx.md` is the source of truth. The live page copy is older and is only used as an image source. |
| Reference | Metalab › Midjourney: its structure, rhythm and motion, **inverted to light mode**. |
| Fonts | Tcules' own: **Bricolage Grotesque** (display / headings) + **Figtree** (body / labels). Swappable through one token. |
| Layout step | A scrollable **grey-box HTML page**: real copy, grid and motion, with labelled placeholder media. |
| Video | None. Every moving product moment is an **HTML component with code-driven animation**. |
| Scenarios | Only the **4 scenario areas named in the markdown** (System status, Forecasting, Asset performance, Operational conditions). The 8 individual scenarios aren't named or listed anywhere on the page → backlog item **IMP-01**. |
| Nav | A **light, case-study nav** (Metalab-style). |
| Footer | The **Tcules green footer**, rebuilt. |
| Metrics | A **placeholder metric** is allowed for now, visibly marked in the source and logged as **IMP-03**. |
| Live Twin | Embedded borderless and interactive, in a **stripped-back "floating" layout**: ConnectX top bar + 3D scene + a few floating KPI cards + a few floating detail cards (see §6). |
| Viewports | Desktop **1024 → 1920+**. Below 1024 is not designed this round → **IMP-04**. |
| Output | **One self-contained `.html` file** (see §2). |

---

## 1. What the reference does (measured)

Measured on metalab.com/work/midjourney in a headless browser:

- **Type**: only 5 sizes: 140 display · 56 intro · 40 chapter statement · 20 label · 16 body.
- **Rhythm**: Hero (giant name → credits row → full-width image that grows on scroll) → one big intro paragraph → **chapter module × 4** (label + one-line statement, then an asymmetric media composition with a narrow body column) → Outcomes (hairline-ruled stats) → "Next case study" marquee → "How can we help?" closing.
- **Motion**: smooth scroll · nav turns from a bar into a floating pill · hero image scale-up · line-masked text reveals · clipped media reveals · context cursor · drag carousel · marquee.
- **Media**: UI is never shown flat. It is placed on coloured backdrops, cropped, layered and pulled apart.

---

## 2. Output and tech

**Deliverable: a single file, `dist/connectx-case-study.html`.** You open it in a browser and it just works.
- All CSS and JS are inline.
- The **Live Twin is inside the same file**: its HTML is held in an inline `<template>` and loaded into an iframe from a same-origin Blob URL. It stays isolated from the page's styles and scripts, but no second file is needed.
- Fonts (Google Fonts) and libraries (Lenis, GSAP + ScrollTrigger + SplitText, three.js for the twin) load from CDNs at pinned versions. Images are linked from the existing Tcules Cloudinary URLs.
- **One caveat**: the file needs an internet connection to fetch fonts, libraries and images. A fully offline version (everything embedded) is possible later, at a cost of several MB → **IMP-05**.

**How I'll work**:
- I keep readable source files (`src/…`) and run a tiny Node script (`build.mjs`, no dependencies) that inlines everything into the single HTML. Both the source and the built file are committed.

```
src/index.html
src/css/tokens.css  base.css  sections.css  components.css
src/js/main.js  nav.js  cursor.js  reveal.js  marquee.js
src/js/scenes/choice.js  areas.js  peak.js  twin-bridge.js  timeline.js
src/twin/live-twin.html      (copy of ConnectX_Live_Twin.html + embed mode)
build.mjs                    → dist/connectx-case-study.html
docs/BUILD_PLAN.md
```

---

## 3. Colour and theme

### 3.1 Principles
1. **Two voices, kept apart.** The **page** speaks in Tcules' neutral black and white. The **product** (twin and HTML components) speaks in ConnectX colours (blue for normal/info, orange for alerts). Product colour never leaks into page chrome, and Tcules green never appears inside the product. That way the reader always knows whether they're looking at the studio's story or the client's product.
2. **Light, but not white.** The page sits on a soft off-white so white product cards can lift off it with shadow. That's how the "floating" look works without borders.
3. **Green is a signal, not a surface.** Tcules green `#04EC50` has a contrast of only about 1.5:1 on light backgrounds, so it is **never used for text on light**. It appears only as a fill with black text on it (about 14:1), and only in small, meaningful places. The one large green area is the footer, as on the live site, which closes the page on brand.
4. **Colour carries the story's state.** Grey means "explored / rejected", product blue means "chosen / working", orange means "needs attention", and green means "live / delivered".

### 3.2 Tokens

**Page (Tcules)**

| Token | Value | Use |
|---|---|---|
| `--bg` | `#F3F3F1` | Page background (Tcules' `#F2F2F2` with a slight warm shift so the twin's ground `#F2F1ED` blends in) |
| `--surface` | `#FFFFFF` | Cards, form fields, floating panels |
| `--ink` | `#0B0B0B` | Headings, display text |
| `--ink-2` | `#464646` | Body copy (Tcules value), 9.5:1 contrast on `--bg` |
| `--ink-3` | `#7A7A7A` | Labels, captions, inactive text (4.6:1, passes AA) |
| `--ink-4` | `#B5B5B2` | Text before it is revealed in the scroll-brightening effect; decorative only |
| `--line` | `#DCDCD8` | Hairline rules |
| `--line-strong` | `#0B0B0B` | Active rules (timeline fill, active list item) |
| `--brand` | `#04EC50` | Tcules green: "Live" pill, focus ring halo, cursor dot, footer field |
| `--brand-ink` | `#000000` | Text on green |

**Media backdrops** (Metalab's orange fields, made light): low-chroma tints from the product palette, so screens sit on a related colour:

| Token | Value | Use |
|---|---|---|
| `--tint-blue` | `#E6ECF8` | Workspace and dashboard shots (matches product blue) |
| `--tint-stone` | `#ECEAE4` | Early concepts, the "explored" side (neutral = past) |
| `--tint-sage` | `#E4EDE6` | Production / live moments (a faint green echo) |
| `--placeholder` | `#D9D9D5` | Grey-box blocks in Phase 1 |

**Product (ConnectX, taken from the twin file)**: `--cx-blue #4D7CFF` · `--cx-blue-soft #EEF2FF` · `--cx-orange #FF6B3D` · `--cx-orange-soft #FFF3EE` · `--cx-amber #F5A524` · `--cx-ink #1A1A17` · `--cx-panel #FBFAF7`. Fonts: Instrument Sans + Geist Mono, **inside product components only**.

**Elevation (the floating look):**
- `--shadow-float`: a soft two-layer shadow (`0 1px 2px rgb(0 0 0/.06), 0 12px 32px -8px rgb(20 20 40/.14)`).
- `--shadow-lift`: a stronger version for hover and the active state.
- No borders on floating cards; 14px radius, matching the product.

### 3.3 Theme rules
- **Light only.** There's no dark mode, and the page ignores the system dark setting.
- In the twin section, the page background fades to the twin's ground over 200px of scroll, so there's no seam. In embed mode the twin's `--ground` is set to the page `--bg`.
- Every text colour pair is checked for WCAG AA in Phase 6.

---

## 4. Grid and type (1024 → 1920+)

**Container:**
- Fluid 12 columns.
- Outer margin `clamp(32px, 3.2vw, 64px)`, gutter `clamp(16px, 1.4vw, 28px)`.
- Text never stretches too wide: reading blocks are capped by column count (body copy at about 60ch).
- Above 1920 the content area stops growing at **1760px**, centred; full-bleed media keeps going edge to edge.

**Type** scales smoothly between 1024 and 1920 with `clamp()`:

| Token | @1024 | @1440 | @1920+ | Font |
|---|---|---|---|---|
| `display` | 104 | 140 | 168 | Bricolage 500, tracking −0.03em |
| `intro` | 40 | 56 | 64 | Bricolage 400 |
| `statement` | 30 | 40 | 48 | Bricolage 400 |
| `stat` | 72 | 96 | 112 | Bricolage 400 |
| `label` | 17 | 20 | 22 | Figtree 500 |
| `body` | 16 | 16 | 18 | Figtree 400 / 1.5 |
| `meta` | 12 | 12 | 13 | Figtree 600, caps, +0.06em |

**Spacing:** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192. Space between chapters is `clamp(128px, 12vw, 224px)`.

**Motion tokens:**
- `--ease-out: cubic-bezier(.16,1,.3,1)`
- `--ease-io: cubic-bezier(.65,0,.35,1)`
- Durations 0.4 / 0.8 / 1.2s; stagger 0.08 (lines) / 0.12 (cards); reveal distance 24px.
- Reveals trigger when the element's top reaches 85% of the viewport and play once.

Checked at **1024×768, 1280×800, 1440×900, 1920×1080, 2560×1440**.

---

## 5. Global components and interactions

1. **Smooth scroll**: Lenis, synced to ScrollTrigger.
2. **Light nav**:
   - At the top: a thin bar with the Tcules logo on the left, "Case study · ConnectX" in the centre and "Start a project" on the right (black button).
   - After the hero: becomes a **floating centred pill** (white at 80% opacity with blur and `--shadow-float`) showing the logo, the current chapter ("03 · Scenarios") and a menu button.
   - The menu opens a small panel: chapter links + Work / Services / About.
   - Hides on fast scroll down and reappears on scroll up.
3. **Context cursor**: a small black dot that grows into a labelled pill: "Drag" over carousels, "Explore" over the twin before it's engaged, "Read" over related cards. The normal cursor comes back once the twin is engaged.
4. **Line reveal** with SplitText and masks, used on H2s, the intro and statements.
5. **Media reveal**: a `clip-path: inset()` wipe plus an inner 1.08 → 1 scale; parallax of ±40px on large media only.
6. **Chapter module** in 3 variants (A: body left, media right · B: media full width, body below · C: media left, body right).
7. **Tcules footer**, rebuilt:
   - A green field with the logo and "Modern products, designed and engineered as one."
   - "Connect now" (black button).
   - Link columns: Services, Expertise, Work, Insights, Lab, Company.
   - Socials, the "Beyond Interfaces" subscribe card, and the address / legal row.
   - Motion: the columns stagger up as the footer enters.

---

## 6. Live Twin embed: "floating" layout

**What's kept** (embed mode `?embed=1`, set via the Blob URL):
- **ConnectX top bar** (brand, Meridian Tower, Home / Live twin / Reports, system pill, clock, role switcher). Kept as is.
- **The 3D scene**, full-bleed, with the twin's ground colour set to the page background.
- **3–4 floating KPI cards** (live load, solar, battery state of charge, grid import). These are small white cards with `--shadow-float`, placed over the scene and drifting slightly with idle motion (±3px). They update live from the twin's data.
- **2–3 floating detail cards**: the asset detail card when an asset is clicked, the current scenario card, and one alert card. Each enters with a soft rise.
- **Scenario chips**: a small floating row to run Peak tariff, Grid outage, EV rush, and others.

**What's hidden in embed mode:** the fixed right rail (Asset / Alerts / Ask tabs), the decision log, the power-flow panel and the scenario sidebar list. Their information comes through the floating cards instead.

**Page side:**
- **Lazy load**: the iframe is created about 1 viewport before the section, with a poster image shown until then.
- **Intro**: the "Building a digital twin" loader plays the first time the section comes into view; "Skip intro" stays.
- **Engage model**:
  - Before engaging, a centred floating pill reads "Explore the live twin", and **page scroll passes straight through** (the twin's wheel-zoom is off).
  - Clicking engages it: wheel and drag control the twin, and an "Exit ✕" pill appears. Esc, clicking Exit, or scrolling past the section hands control back.
- **Performance**: a `postMessage` bridge pauses the twin's render loop when it's off-screen.
- **Size**: 100vh, minimum 680px, full-bleed, no frame.

The twin file is changed only behind the embed flag. The standalone twin is unchanged.

---

## 7. Section-by-section spec

**L** = layout · **M** = media · **Mo** = motion · **I** = interaction · **C#** = HTML component (see §8).

### S1 Hero
- **L**:
  - Eyebrow "Case study · ConnectX".
  - **"ConnectX"** at display size.
  - Credits row in 4 columns: Company · Sector: Building energy · Our role · Status: a **green "Live" pill** + "since late 2025".
  - The SEO H1 at label size beneath the credits.
  - Full-width media.
- **M**: `CX_Hero` on `--tint-blue`.
- **Mo**: the title reveals per character on load and the credits stagger in. On scroll, the media scales from 0.86 to 1 and its corner radius goes from 24 to 0, becoming full-bleed.

### S2 Intro
- **L**: the 3 intro lines as one paragraph at intro size across 10 columns, then two links ("Follow the product choice ↓", "Browse all case studies").
- **Mo**: line reveal, then the words brighten from `--ink-4` to `--ink` as you scroll (scrubbed).

### S3 At a glance (#case-context)
- **L**: a ruled 2-column definition list (Product, Our role, Key question, What we delivered, Scenario areas, Digital twin). The Key question is promoted to statement size. A "Related services" link row sits underneath.
- **Mo**: the rules draw left to right and the rows stagger in.

### S4 Chapter 01: Starting point (#starting-point), variant A
- **L**: label · statement · body copy.
- **M**:
  - **C1 Role cards**: three floating cards: Facilities operator ("Which exception needs action?"), Finance leader ("What will this cost, and what's the forecast?"), Sustainability lead ("Are we on track for our target?"). The wording is taken from the markdown's description of each team.
  - Then the pull line, then the **early concepts drag carousel** on `--tint-stone`. Caption from the markdown.
- **Mo**: in C1 the questions type in, staggered. Carousel items reveal with the clip wipe.
- **I**: drag or arrow keys on the carousel; a slight lift on hovering a card.

### S5 Chapter 02: The choice (#choice). Pinned, about 250vh
- **L**: label · statement · body copy, then the pinned stage.
- **M**: **C2 Two directions** (A: dashboard + assistant / B: chat builds the view) → **C3 Chosen model flow** (Conversation → Known situation → Permitted tools → Modules + twin → Workspace stays open).
- **Colour story**: A and B start in grey (`--tint-stone`, "explored"). As they merge, the result turns **product blue** ("chosen").
- **Mo** (scrubbed, 4 beats):
  1. A and B side by side with one-line verdicts.
  2. They slide together.
  3. They merge into one workspace.
  4. The 5 flow steps draw in, and the closing line appears.

### S6 Chapter 03: Scenarios (#turning-adaptation-into-scenarios). Pinned, about 300vh
- **L**: label · statement · body copy (the markdown copy says "eight" and is kept as is). Then a pinned split, 5 / 7 columns:
  - **Left: the 4 scenario areas** as a large ruled list: System status · Forecasting · Asset performance · Operational conditions.
  - **Right: C4 Workspace states**: one product workspace mock that changes as each area becomes active:
    - **Status**: an exception card in orange; one asset highlighted in the mini twin.
    - **Forecasting**: a forecast chart module.
    - **Asset performance**: one asset in focus with the others dimmed.
    - **Operational conditions**: an operating-conditions module.
  - These are visual states, with **no invented scenario text**: module titles only.
- **Mo**: the active area turns `--ink` with a black rule while the rest stay `--ink-3`. The workspace modules cross-fade and re-arrange. A progress marker shows "2 / 4".
- **I**: clicking an area scrolls to its step.
- **Sub-section, "A peak-price request…"** (variant B):
  - **C5 Peak-price assembly**:
    1. The question types into the ask bar.
    2. Resolver steps tick: intent → data → tools.
    3. The affected assets light up in the mini twin.
    4. Modules assemble: affected assets, the data behind the suggestion, and what the action changes (all three named in the markdown), plus the battery action card.
  - Plays on enter, with a replay button.

### S7 Chapter 04: Digital twin (#designing-the-digital-twin), variant C
- **L**: label · statement · body copy. Then a **compare strip**: "Explored" (map view and realistic image, desaturated, on `--tint-stone`) next to "Chosen: 2.5D" (`Section_5_Image_1`, on `--tint-blue`). Caption. Then the **Live Twin** (§6).
- **Mo**: the explored side dims and slides back while the chosen side comes forward. The background fades into the twin.

### S8 Chapter 05: Demo to production (#the-demonstration-ran-in-code-on-interim-data), variant B
- **L**: label · statement · body copy. Then the full-width `Section_4_Image` on `--tint-blue` with its caption. Then **C6 Timeline**: Product work → Demo → Production.
- **Colour story**: the line fills black, and the last node becomes the **green "Live" pill** ("since late 2025").
- **Mo**: clip-path reveal plus parallax on the image; the timeline fill is scrubbed and the nodes pop as it reaches them.

### S9 Chapter 06: How we decide (#chat-is-an-interaction-mode-not-a-complete-produ)
- **L**: the statement at intro size, then a ruled list of the 6 things defined per scenario, then the closing paragraph.
- **Mo**: words brighten with scroll; the rules draw in.

### S10 What the work delivered (Metalab's "Outcomes")
- **L**: 3 hairline-ruled rows with stat numerals:
  - **8**: scenarios defined (from the markdown)
  - **4**: scenario areas (from the markdown)
  - **[placeholder metric]**: e.g. "**60%** faster to the right view" (illustrative). Marked `data-placeholder` in the source → **IMP-03**.
- **Mo**: count-up and the rules draw in.

### S11 Testimonials
- One large quote at statement size with attribution, "1 / 2" and previous/next controls; crossfade with a line reveal; keyboard accessible.

### S12 FAQ
- A 4-item accordion with hairline rules. FAQPage structured data is kept. Height animates and the plus rotates into a cross.

### S13 Trust strip
- 2017 · 90+ projects · 19 countries · 4.8 on Clutch (13 reviews), with count-up.

### S14 Next case study
- The line "Other AI products where people check the model's work".
- A huge marquee "Next case study • BuildTwin •" with a floating BuildTwin card over it.
- A secondary row: Eden AI · Product Design · ClimateTech & energy.
- The marquee speeds up with scroll velocity; hovering the card scales its image and the cursor shows "Read".

### S15 Enquiry
- Display-size heading plus subline.
- A 3-field form on white floating fields (Email · What are you working on? · URL, optional).
- "Send enquiry" (black) and "See available times" (text link).
- Success state from the markdown, keeping what was typed. The form submits to a stub in this prototype.
- Motion: the heading line-reveals and the fields stagger in.

### S16 Tcules footer (§5.7)

---

## 8. HTML components (replacing video)

All are built in the ConnectX product style: Instrument Sans + Geist Mono, product tokens, white floating cards.

| ID | Component | Section | What animates |
|---|---|---|---|
| C1 | Role question cards | S4 | Questions type in; avatars pop |
| C2 | Two directions | S5 | Panels slide, overlap and merge; grey → blue |
| C3 | Chosen model flow | S5 | 5 steps draw along a connecting line |
| C4 | Workspace states (4 areas) | S6 | Modules cross-fade and re-arrange per area |
| C5 | Peak-price assembly | S6 | Ask → resolver → assets light → modules assemble |
| C6 | Demo → production timeline | S8 | Fill, nodes, green "Live" pill |

---

## 9. Accessibility, SEO, performance

- **Reduced motion**: no smooth scroll, pinning or scrub, just short fades. The full copy is in the HTML, so it reads without JS.
- One H1, H2s with the markdown anchors, visible focus (black ring + green halo), labelled form fields, alt text from the markdown's media bindings.
- Meta tags and OG from the frontmatter; JSON-LD for WebPage, BreadcrumbList and FAQPage.
- Only transform / opacity / clip-path are animated. The twin loads lazily and pauses off-screen.

---

## 10. Build phases and review checkpoints

| Phase | Output | You review |
|---|---|---|
| **P1 Foundation + grey-box layout** ✅ | Build script, tokens (incl. colour), grid, type, light nav, Tcules footer, all sections with real copy and labelled grey blocks. No motion. | Layout, hierarchy, spacing, colour usage |
| **P2 Motion system** ✅ | Smooth scroll, reveals, nav pill, cursor, both pinned scenes (on grey boxes), marquee, count-ups, accordion, reduced motion. | Feel, timing, pacing |
| **P3 HTML components** ✅ | C1–C6 built and animated. | Each component's story |
| **P4 Live Twin embed** ✅ | Embed mode, floating layout, lazy load, engage/exit, pause. | Interaction model |
| **P5 Assets** ✅ | Real images on tint panels. | Composition |
| **P6 QA** | Screenshots at 1024 / 1280 / 1440 / 1920 / 2560, contrast check, keyboard and reduced-motion passes, Lighthouse. | Sign-off |

Every phase rebuilds `dist/connectx-case-study.html` and is committed to `claude/cool-rubin-hrpv85`.

---

## 11. Improvements backlog (come back to these)

Note: product mock values inside C2, C4 and C5 (318 kW, 262 kW, 17:00, battery health) are illustrative, consistent with the Live Twin's sample data. Confirm or replace them before launch (IMP-08).


| ID | Item | Why it's deferred |
|---|---|---|
| **IMP-01** | Name the **8 scenarios** and their details (request, intent, data, modules, twin behaviour, next action); extend S6 from 4 areas to 8 scenarios. | Not in the markdown; no placeholders allowed |
| **IMP-02** | Swap the S1/S15 fonts for a display serif (Metalab-style), if wanted. | Tcules fonts kept for now |
| **IMP-03** | Replace the **placeholder metric** in S10 with a real, approved figure. | No metric available yet |
| **IMP-04** | Tablet and mobile layouts (< 1024), including a full-screen twin overlay. | Desktop-only this round |
| **IMP-05** | A fully offline single file (embedded fonts, libraries and images). | Size cost; CDN for now |
| **IMP-06** | Form wired to the CMS record + notify, and the scheduling link. | Prototype uses a stub |
| **IMP-07** | Port into the Tcules Next.js site. | After design sign-off |
| **IMP-09** | Replace the two embedded Figma concept frames (carousel 3 and 4) with exports hosted on Cloudinary, so the page is lighter. | They only exist in Figma today; embedded as WebP (~60 KB) |
| **IMP-08** | Confirm or replace the illustrative values in the product mocks (C2, C4, C5). | Sample values, consistent with the Live Twin |
