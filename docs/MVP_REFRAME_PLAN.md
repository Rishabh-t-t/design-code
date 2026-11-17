# ConnectX: reframing as an MVP case study (plan)

## 1. Updated understanding

**What the page is today:** a product case study ("Designing an AI workspace that answers building energy questions") with six chapters: starting point, the choice, scenarios, digital twin, demo to production, how we decide. It is live at rishabh-t-t.github.io/design-code, built from `src/` with `node build.mjs` into the root `index.html`. Pushing to `claude/cool-rubin-hrpv85` deploys it.

**Goal:** the same project, told as an MVP story for pre-seed and seed founders (PMs second). The message is "Tcules takes an AI idea to a live product, fast, and design is what makes it work."

**Confirmed facts (from you)**
- The whole MVP took **8 weeks**: about **4 weeks to the coded demo**, then **4 weeks from demo to production**.
- The demo led to **2 investor meetings**.
- Team: **1 designer and 2 developers** from Tcules.
- **Left out of v1:** complex, custom-built live twins. Instead, the team **pre-built a set of high-quality building twins** that v1 uses. This was quicker and more reliable, and custom live twins stay on the roadmap.
- Still true from the current page: 8 scenarios across 4 areas, the hybrid chat-plus-workspace model, the simplified 2.5D twin, live since late 2025, the CEO quotes.

**Dummy numbers (you'll replace these).** Each one is tagged `data-dummy` in the HTML so it's easy to find:
| Where | Dummy value |
|---|---|
| Hero fact strip, "Stage" | Pre-seed |
| Results, "Faster to the right view" | 60% (was already a placeholder) |
| Results, "Pilot buildings live" | 3 |
| Results, "Questions answered in month one" | 1,200+ |

**Rules carried over from the earlier handoff (`docs/HANDOFF_ITERATION6.md`)**
- No AI model or technology names in the copy.
- Never mention that the MVP contract ended after week 8. "Production in weeks 5–8, live since late 2025" is fine.
- Refine the existing page. Don't rebuild it.

## 2. Approach

Keep the existing design system, layout, live twins, animations and images. Change the **story, copy and structure**, plus a few small new components. All edits are in `src/`, then rebuild.

## 3. Section-by-section changes

| # | Section | Now | MVP version |
|---|---|---|---|
| 0 | `<head>`, meta, JSON-LD | Product framing | MVP title, description and FAQ schema |
| 1 | Nav chapter menu | 6 product chapters | 6 MVP chapters with new names |
| 2 | **Hero** | "Designing an AI workspace…" plus Company, Sector, Role, Status | **"From an AI idea to a live energy product in 8 weeks"** plus Company, Stage*, Timeline (8 weeks), Team (1 designer, 2 devs), Status (Live) |
| 3 | Intro | Product summary | Founder-framed summary, with links "See how we scoped it ↓" and "Start your MVP ↗" |
| 4 | At a glance | Product, role, deliverables | **"The MVP at a glance":** the key question ("Could an AI-first energy idea be proved and shipped in 8 weeks?"), then Team, Timeline, What shipped, Left out of v1, Outcome |
| 5 | 01 Starting point | Three teams' questions | **"A bold idea, and a real risk of building the wrong thing"**, keeping the role cards, plus a new *For founders* note |
| 6 | 02 The choice | Direction A vs B | **"The riskiest call: chat beside the dashboard, or chat that builds it"**, with the same band animation plus a *For founders* note |
| 7 | 03 Scenarios | 8 scenarios | **"We cut 'an AI that can do anything' down to eight scenarios"**, the same live twin and peak-price block, plus a *For founders* note |
| 8 | 04 Digital twin | 2.5D twin | **"Design that ships: a simpler twin, pre-built for v1"**, plus a new **In v1 / Left for later** scope block (pre-built twins vs custom live twins) |
| 9 | 05 Demo to production | 3-step timeline | **"Demo in 4 weeks. Live 4 weeks later."** The demo leads to 2 investor meetings. The timeline becomes **4 steps with weeks**: W1–2 Define and decide → W3–4 Coded demo → W5–8 Production → Live |
| 10 | 06 How we decide | Method (6 rules) | **"What founders can take from this":** 4 lessons, plus a "built to grow one scenario at a time" paragraph (removes the duplicated paragraph) |
| 11 | Results | 8 / 4 / 60% placeholder | **"What the MVP delivered":** 4 stats (8 weeks, 2 investor meetings, 8 scenarios, 60%*), plus a second row (3 pilot buildings*, 1,200+ questions*) |
| 12 | Quotes | 2 near-duplicate quotes | **1 founder quote**, large and single |
| 13 | FAQ | 4 product questions | **5 MVP questions:** how long, who was on the team, design or build too, what was left out, can you do this for pre-seed |
| 14 | Trust, related | Keep | Keep |
| 15 | Enquiry | "Tell us what your AI product should answer" | **"Have an AI product idea? Let's prove it in code."** with a field "What's your idea?" |

\* dummy value

## 4. New or changed components (small CSS additions in `page.css`)
- `.fnote`: a *For founders* callout with a brand-green rule and a label, inside the copy column.
- `.scope`: a two-column **In v1 / Left for later** block.
- `.timeline--4`: the timeline grid with 4 steps instead of 3.
- `.facts__list--4` and a second facts row.
- `.quotes__grid--single`: one large quote.

## 5. Build and check
1. Edit `src/index.html` and `src/css/page.css`.
2. Run `node build.mjs`, which writes `dist/` and the root `index.html`.
3. Preview locally in the browser at 1440px and 1280px. The current page is desktop-only (no mobile layout), and this change keeps that scope.
4. Check the live twins, animations and count-ups, and that there are no console errors.
5. Show screenshots for approval.

## 6. Publishing (only after approval)
1. Snapshot the current live version to branch `v3-product-casestudy-snapshot` so it can be restored.
2. Commit to `claude/cool-rubin-hrpv85` and push. GitHub Pages redeploys in about 1 minute.
3. Check the live URL.

## 7. Open questions (not blocking)
- The earlier handoff says ConnectX came with just two words, "energy" and "AI." That's a strong founder hook, but the current page says early concepts existed. It isn't used here unless you confirm it.
- Should the canonical URL and slug change (for example to `…/mvp-ai-energy-product-connectx`)? They stay as they are for now.
