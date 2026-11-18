# Design polish: MetaLab layout, ConnectX theme

Reference: metalab.com/work/midjourney, measured at 1655px. We copy its **layout, type sizes, spacing and image placement**. We don't copy its theme. Our case study is themed to our product: the cool-grey ConnectX studio.

## What MetaLab does (measured)
| Element | MetaLab | Ours (at 1440) |
|---|---|---|
| Grid | 12 columns, 24px gutter, content placed by column | Same 12 columns and 24px gutter. We keep our existing 56px outer padding (an earlier instruction). |
| Display title | 140px, weight 300, line-height 1.2, tracking −1.5% | `clamp(56px, 6.7vw, 128px)`, weight 300. Our title is a sentence, so it gets 2 lines. |
| Meta row under the title | dt 16px/500 in ink, dd 16px/400 in grey, in column slots (1, 7, 9) | The 6 hero facts as plain dt/dd pairs, 2 columns each. No uppercase micro-labels. |
| Hero media | Full-bleed, no radius | The hero product, full-bleed on the grey studio. |
| Section label | 20px/400, sentence case | Chapter labels become 20px sentence case. Number, capability and weeks become quiet grey meta. |
| Intro statement | 56px/400, line-height 1.21, tracking −2%, 10 columns, brightens on scroll | The intro becomes one 56px statement that brightens as you scroll. |
| Section statement | 40px/400, line-height 1.2, tracking −3%, starts at column 3, 6 columns wide | Chapter headings at 40px, starting at column 3, 6 columns wide. |
| Body notes | 16px, line-height 1.4, short, set beside or under media (columns 1–2 or 7–11) | Chapter copy at 16–17px in columns 7–11, under the heading. |
| Media placement | Offset to start at column 3 and run to the right edge, or full-bleed. Small notes in columns 1–2. | Scenario areas and peak price: text in columns 1–3, product in columns 4–12. |
| Vertical rhythm | About 240–320px between sections | Chapter gaps raised to about 220–260px. |
| Contact headline | 88px, weight 240 | Enquiry headline at weight 300, 88px. |

## Changes
1. **Grey theme on the whole page:**
   - Use the cool-grey studio throughout. Remove the white page.
   - Cards go back to translucent white on grey.
   - The original Tcules footer stays exactly as it is.
2. **The arc:** keep the arc under the hero, filled white-to-grey with a soft shadow on its rim, so the second section rises out of the hero.
3. **Scenario areas get distinct images:**
   - Each area uses its own camera crop of the product, its own answer and pin, and its own highlight on the render:
     - System status: floor 6 lit red, framed on the facade.
     - Forecasting: the main supply and plinth in blue, framed low.
     - Asset performance: the roof in amber, framed high.
     - Operational conditions: the site in green, framed wide.
   - The view pans between them.
   - These are static product states, not the full motion prototype.
4. **MetaLab layout layer** (new `css/layout.css`): the grid, type scale, label style, hero meta row, full-bleed hero product, chapter offsets, media offsets, rhythm and contact headline. Mobile (below 1024px) stays single-column.
5. **Less repetition:** "At a glance" is hidden, since the hero meta row now carries the same facts.

## Check
- 1440px and 390px.
- All product states work.
- No console errors.
- Committed locally, not pushed.
