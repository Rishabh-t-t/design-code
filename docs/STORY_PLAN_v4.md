# ConnectX case study, v4: story-first rebuild (concept)

Status: **concept agreed, not built.** The live page (v3, Figma layout) is unchanged.
Visual board: https://claude.ai/artifact/5V18VkqEPCYHQpXwDbFxzx (source in `docs/v4/moodboard.src.html`).

---

## 1. The shift

| | v3 (now) | v4 (new) |
|---|---|---|
| Audience | Designers and builders | Zero-to-one founders and teams |
| Main story | How we decided what the AI controls | An idea became a real, working product, fast |
| Structure | Block by block, explained | One linear story on one continuous stage |
| Carried by | Copy | Visuals, with short lines of copy |
| Ending | Faded sections, form near the bottom | The form is the destination, straight after the quote |

## 2. Facts we can use

- **Team:** 3 people (1 designer, 2 developers).
- **Output:** 5 screens, 24+ scenarios (8 × 3 roles).
- **Rhythm (felt, never stated):** idea → shape → render in about 2 weeks, first demo at week 4, working product at week 8.
- **Day 0:** only an intent: "do something with AI and the energy of a building."
- **Real product, real data.** Don't say "live since late 2025" anywhere.

**Not used:**
- results after launch;
- a stated "8 weeks";
- the second CEO quote, which is a duplicate.

## 3. Product framing

- **Framing:** an AI-first product built around a live twin render. You ask, and the building answers.
- **Name:** to be decided.
- **Twin progression:** sketch → 2.5D → realistic render. The realistic render is being reworked by the design team.

## 4. Story frames

The story is a loop: it opens on the finished product, rewinds to nothing and builds back up to the same frame.

| Frame | What we show | Why |
|---|---|---|
| **F1 Hero** | The finished product at dusk; a question types itself; the twin lights up; glass panels land with the answer; 3 people · 5 screens · 24+ scenarios | The founder sees the bar before the story |
| **F2 Rewind** | Scroll plays the build backwards: panels retract, dusk → dawn, render → 2.5D → sketch → blank | One gesture turns a product shot into a story |
| **F3 Day zero** | Paper, faint grid, one sentence, a cursor | Founders see themselves here |
| **F4 Three questions** | Facilities, finance and sustainability cards type their questions | We start from questions, not features |
| **F5 The choice** | Direction A and Direction B merge into the chosen model | The judgement founders pay for |
| **F6–F8 Progression** | Sketch → 2.5D → realistic render, morphing in place in a short stretch of scroll | Speed is felt without being said |
| **F9 X-ray** | The screen explodes into layers (question, intent, tools, data, layout, modules, render), a pulse runs down them, then they close | Where most of the effort went; proves it's a working system |
| **F10 Missing data** | One module shows a dashed, "estimated" gap | Honesty about messy real data |
| **F11 Scenario wall** | 24 tiles light in a wave; one expands into the full view | Every path was designed, not one happy path |
| **F12 Full circle** | The rail reaches Product, dusk returns, the stage lands on the hero frame, the visitor asks | Closes the loop; the payoff |
| **F13 Team** | 3 people; design and build lanes overlapping | Why it was fast |
| **F14 How we decide** | The six rules, reframed as "how we move fast without guessing" | The process is repeatable and buyable |
| **F15 Quote** | One CEO card, unchanged | Proof |
| **F16 Form** | "Have an idea like this? Let's make it real." | Placed at the peak of trust |
| **F17** | FAQ rewritten for founders → related → footer | |

**Folded in or removed:**
- **Folded in:** at a glance → F1; digital twin → F6–F8; demo to production → F12; scenarios → F11.
- **Removed:** the centred banners, the image shells and the duplicate quote.

## 5. Visual direction

The detail is on the visual board.

- **One stage:** the building holds the screen from F1 to F12.
- **Light is the clock:** dawn (idea) → day (build) → dusk (product).
- **Parallax:** sky 0.2×, haze 0.45×, building 1×, glass UI 1.15×, copy 1.3×.
- **Glass UI:** smoke glass at dusk and light glass by day; twin state colours (blue for live, orange for alerts).
- **Type:** Bricolage Grotesque Light headlines (huge and short), Figtree body (sparse), Geist Mono labels.
- **Motion:** morphs scrubbed by scroll, arrivals 600 ms with expo out, camera 1.2 s glides, Lenis smooth scroll.

## 6. Open calls

- Smoke glass or light glass at dusk; how dark the dusk is.
- Whether the rail shows labels or only marks.
- The headline and the product name.
- Assets the design team will make: the realistic render and real sketches. Everything else is built in code.

## 7. Build plan (when approved)

| Step | Scope |
|---|---|
| **S0** | Snapshot v3 to a branch. Build v4 at `/v4/` beside the live page, so the live page stays untouched until switch-over |
| **S1** | The stage engine: one sticky full-screen stage, light timeline, parallax layers, progress rail, scroll scrubbing |
| **S2** | F1–F3: hero (live twin plus glass answer), rewind, day zero |
| **S3** | F4–F8: questions, the choice, the three-look progression (with stand-in visuals until the new render lands) |
| **S4** | F9–F12: x-ray, missing data, scenario wall, full circle with a visitor question |
| **S5** | F13–F17: team, method, quote, form, FAQ for founders |
| **S6** | QA (widths 1024–1920, performance, accessibility, reduced motion), then switch v4 to the main URL |
