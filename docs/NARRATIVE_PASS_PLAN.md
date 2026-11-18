# ConnectX MVP case study: narrative and visual pass

**Goal:** the page stays a ConnectX story, but every section quietly proves a Tcules capability (product definition, product strategy, product design, development). It shows, not claims. Less text. Visuals move one way only: rough → decided → polished → live.

---

## Phase 1: fixes from the feedback list (no narrative risk)

| # | Change | Where |
|---|---|---|
| 1.1 | Hide "What the MVP delivered", "For founders" (ch 06) and the founder testimonial. They're kept in the code with `hidden`, so they can come back. | `src/index.html` |
| 1.2 | Move the contact form directly below the FAQ, before trust and related work. | `src/index.html` |
| 1.3 | Restore the original Tcules footer exactly: brand green, black text, original buttons. | `src/css/theme.css` (remove the footer overrides) |
| 1.4 | Hero: no build-up animation. Show the final render at once (a light placeholder until it has decoded, then swap). The dashboard appears ready. | `src/js/cxapp.js` |
| 1.5 | Bring back the white arc under the hero. | `src/css/theme.css` (un-hide `.intro__horizon`, white) |
| 1.6 | White backgrounds where the earlier design was white: the page, the intro under the arc, banners and chapters. Cool grey stays only around the product (hero studio, product panels, band). Cards and quotes on white get a light-grey surface. | `src/css/theme.css` |
| 1.7 | Remove the "See how we scoped it" and "Start your MVP" links. | `src/index.html` |
| 1.8 | Check that the side padding matches the earlier design across sections and the hero product. | CSS check |

## Phase 2: fix the visual story

| # | Change |
|---|---|
| 2.1 | **Riskiest call:** remove the Direction A/B mockups, the merge animation and the horizontal 5-step flow. Show the choice with the real product in a static row: "Assistant beside a dashboard" and "Chat only" (both as real ConnectX UI frames, muted), then "We chose both", which is the product itself. Each frame gets one verdict line. No scroll pin. |
| 2.2 | **Design that ships:** remove the map and early-twin brainstorm images. Replace them with close-ups of the finished product: the scan, the answer and its pin, and the home screen, all live component states at product quality. Keep the "In v1 / Left for later" scope block. |
| 2.3 | Early concepts stay only in chapter 01, as "what ConnectX had at kickoff". |
| 2.4 | Chapter 05: drop the two demo stills. The timeline and mid-page CTA carry the build story. |

## Phase 3: copy and implied capability

| # | Change |
|---|---|
| 3.1 | Capability tag on each chapter label: 01 Product definition · 02 Product strategy · 03 Product definition · 04 Product design · 05 Development. |
| 3.2 | Each chapter becomes one short paragraph in "we did" voice, with product mechanics removed. The remaining "For founders" callouts are removed. |
| 3.3 | Intro becomes one line. At a glance becomes 4 rows (Team, Timeline, What we did, Outcome). FAQ becomes 4 questions. One banner quote at most. |
| 3.4 | One-line caption under the hero product: "Designed and built by Tcules, live since late 2025." |
| 3.5 | Make sure the proof reads strongly in the hero fact strip and the chapter 05 timeline, since results and the testimonial are hidden. |

## How each phase ships
- Each phase is built, checked at 1440px and 390px, and committed locally on its own.
- Nothing goes live until it's approved.
