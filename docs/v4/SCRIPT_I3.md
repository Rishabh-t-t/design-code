# ConnectX case study · Iteration 3 script
## "A blank screen becomes a building that answers"

Status: draft for review. Nothing built yet. Every number here is a starting value to tune in the prototype.

---

## 0. The premise in one paragraph
The page is one continuous scroll in one white world, the product's own tone. It opens on a blank screen. Three cursors arrive: the Tcules team (one designer, two engineers). As the visitor scrolls, time moves forward and the team designs the product in front of them: first the layout, then the site plan, then a building that rises floor by floor inside the layout, then how the twin should look, how data comes in, how energy is shown, and how the AI answers. At the end time stops, the product is live, and the visitor's own cursor joins as the fourth. Then the screen goes blank again, and that blank screen is the enquiry form: *your* blank screen.

**What it must leave in the visitor's head:** *They took a blank screen to a real, working AI product, fast, and design led every step.*

---

## 1. Global rules (apply to every beat)

### 1.1 Time
- **Scroll is time.** One master timeline, 0 → 1, driven by scroll position. Scroll speed is time speed; scrolling up rewinds everything, including un-building.
- **Time ends at Live (beat 9).** After that the page is "the present": scroll moves the page, not time.
- **Pacing:** each beat has its own scroll length (below). Set pieces get **slow zones** (more scroll per change). No scroll-jacking: native scrolling, keyboard, Page Down and trackpads always work. Slow zones come from length and easing only.
- **Speed cap:** however fast someone scrolls, time can't run faster than a set maximum (smoothed with Lenis). Prevents flashing and missed beats.

### 1.2 The world
- **Base:** white with very slight gradients (warm white `#FFFDF9` ↔ cool white `#F6F8FC`), drifting slowly with time.
- **Grid:** a fine dot grid (Tcules pixel-grid texture) underneath everything. It is the "canvas" the team works on.
- **Textures:** paper grain on the plan (beat 3); faded options become backdrop texture after each choice (beats 5 and 8).
- **Hover:** every beat has one hover reaction (listed per beat). Everything hover-only also works on keyboard focus and is never required to follow the story.
- **No day/night lighting.** The building and UI are always lit the same way.

### 1.3 The sun and moon (time passing)
- A thin dotted arc sits across the top of the stage. A small **sun** (soft white disc, pale blue ring) travels along it, sets at the right, and a **moon** (pale blue crescent) rises from the left. Then the sun again.
- **Where it moves:** from beat 4 (the rise) to beat 8 (AI). About **8 passes** in total: enough to feel like many days, never countable.
- **How fast:** follows the time warp. Fast during the build stretches, slow in slow zones, parked during Live.
- **At Live:** the sun stops at the top of the arc and stays.
- **It never changes the lighting.** It is a sign of time, not a light source.

### 1.4 The team (people, speed, design-led)
- **Three labelled cursors**, like a multiplayer design tool:
  - **Designer** (blue cursor, label "Design"),
  - **Engineer** (black, label "AI + data"),
  - **Engineer** (black, label "Twin + UI").
- They do the work on screen: draw the layout, draw the plan, pull floors up, drag options, connect data lines, place panels. Their speed and overlap show *fast and together* without any number.
- Labels show roles, optionally first names (open question Q2).
- **At Live, the visitor's cursor gets a label too: "You".** The fourth collaborator.

### 1.5 The building
- One 3D model, used from beat 3 to the end. Built in parts so it can grow: plot, footprint, floors (8) one by one, roof plant, carport, battery yard, trees, sensors per floor, system emitters (solar, cooling, battery, EV).
- **Style after beat 5:** the clean 2.5D look (white walls, blue glass, balconies), as in the current SVG, but real 3D.
- **It never leaves the centre stage.**

### 1.6 The dashboard (the product UI)
- The product's real layout: top bar (ConnectX, building name, live badge), left panel (floors), right panel (insight and actions), bottom question bar, centre stage (the building).
- **It is flat HTML, fixed to the screen.** The 3D building lives inside the centre stage. The camera moves inside the stage; the UI frame doesn't tilt.
- **Its states:** outlines (2) → labels (3–4) → numbers fill (6) → charts draw (7) → AI arrangement (8) → fully live (9).

### 1.7 Colour enters with the product
Not a clock, just richness that grows with the product:
- beats 1–4: grey lines on white;
- beat 6: **blue** (data);
- beat 7: **green** (energy) and **soft orange** (attention);
- beat 8 onward: full product colour.

### 1.8 Words
- One caption per beat, top left of the stage, under 8 words, Bricolage Light about 44 px. It fades in at the start of the beat and holds to the end.
- Captions are real HTML headings (`h2`), so the story is readable by search engines and screen readers in order.
- No other copy in the story, except labels that belong to the product UI.

### 1.9 The rail
- A slim vertical rail on the right with stage names: **Blank · Layout · Plan · Rise · Look · Data · Energy · AI · Live**.
- Mark spacing matches scroll length, so the long stretches look long.
- Clicking a mark jumps there (fade, not rewind).

### 1.10 Navigation
- Minimal: Tcules logo left, "Start a project" right. It appears after beat 1, so the first frame is pure.

---

## 2. The beats

Scroll lengths are in viewport heights (vh). Story total ≈ 1,640 vh (about 16 screens), then about 3–4 screens of "present".

| # | Beat | Scroll | Cumulative |
|---|---|---|---|
| 1 | Blank | 100 | 0–100 |
| 2 | Layout | 120 | 100–220 |
| 3 | Plan | 120 | 220–340 |
| 4 | Rise | 220 | 340–560 |
| 5 | Look | 160 | 560–720 |
| 6 | Data | 180 | 720–900 |
| 7 | Energy | 140 | 900–1040 |
| 8 | AI | 200 | 1040–1240 |
| 9 | Live | 160 | 1240–1400 |
| 10 | Your blank screen | 240 | 1400–1640 |
| 11 | Credits (normal page) | — | — |

---

### Beat 1 · Blank (0–100 vh)
- **Camera:** none yet. Flat, straight on.
- **On screen:** white, the dot grid barely visible, a blinking text cursor in the centre. Then the three team cursors glide in from the edges and stop near the centre, as if looking at the empty page.
- **Sun/moon:** the dotted arc draws itself across the top, empty.
- **Caption:** *It started with a blank screen.*
- **Hover:** the grid dots near the visitor's cursor lift slightly (a soft ripple).
- **Handoff to 2:** the Designer cursor clicks; a line shoots out from the click point along the grid.
- **First paint:** this frame is pure HTML/CSS; no 3D needed. It must be ready in under 1 s.
- **Reduced motion:** static frame, cursors in place.
- **Risk:** too empty to hook. *Mitigation:* the cursors moving on arrival give life within 1 second; the caption poses the story.

### Beat 2 · Layout (100–220 vh)
- **Camera:** flat.
- **On screen:** the cursors draw the product layout from the grid, all in grey outline:
  - top bar first (Designer);
  - left floor panel (Twin + UI engineer);
  - right insight panel;
  - question bar along the bottom (AI + data engineer);
  - the centre stage as an empty rounded rectangle.
  
  Placeholder labels type in: *ConnectX*, *Meridian Tower*, *Floors*, *Insight*, *Ask…*
- **Caption:** *First, a place for answers to live.*
- **Hover:** hovering a panel outline thickens it slightly and shows its name.
- **Handoff to 3:** the Designer cursor moves into the empty centre stage and starts drawing.
- **Gap to solve:** the layout must sit at its final screen position from now on. Every later beat uses the same frame, so its proportions need deciding now (desktop 16:9 and phone).
- **Confusion risk:** "Is this a website template?" *Mitigation:* the labels ConnectX and Meridian Tower appear immediately.

### Beat 3 · Plan (220–340 vh)
- **Camera:** 3D starts here, but locked straight down (top view), aligned so the 3D plane looks exactly like part of the flat drawing.
- **On screen:** inside the centre stage, the cursors draw the site from above on a paper-grain texture:
  - plot outline;
  - building footprint;
  - carport with parking bays;
  - battery yard;
  - paths;
  - trees as circles.
  
  Small grey labels appear next to each.
- **Caption:** *Then the building, from above.*
- **Hover:** hovering a part of the plan highlights it and shows its label more strongly.
- **Handoff to 4:** the Twin + UI cursor grabs the footprint's edge and drags it upward. The camera starts to tilt.
- **Technical note:** this is a 3D scene rendered in orthographic top view. The "drawn line" look comes from a line material with dash offset driven by time.
- **Confusion risk:** a top-down plan is abstract. *Mitigation:* labels plus the caption.

### Beat 4 · Rise (340–560 vh) · **Set piece 1**
- **Camera:** tilts slowly from top view (90°) to three-quarter (about 35°) over the first half. Then a slow orbit of about 25° around the building.
- **On screen:** the building rises **slowly**, floor by floor (8 floors plus roof), from the footprint. Grey, untextured, clean. The carport, battery yard and trees rise too. The cursors work around it: one pulls floors up, one places the roof plant, one adds balconies.
- **Sun/moon:** starts moving. About 3 passes in this beat.
- **Dashboard:** still outlines, labels in place, no numbers.
- **Backdrop:** the gradient warms very slightly at the top, like sky. It is the first sense of depth.
- **Caption:** *One floor at a time.*
- **Slow zone:** the last 60 vh (the roof going on and the camera completing its orbit).
- **Hover:** hovering a floor lifts it 2–3 px and shows "Floor 4".
- **Handoff to 5:** the building finishes. Three cards slide in around it.
- **Confusion risk:** "Is this a construction story?" *Mitigation:* no cranes or materials, just geometry extruding from a drawing, inside a software layout, moved by cursors.

### Beat 5 · Look (560–720 vh)
- **Camera:** slow orbit continues; small pushes towards each option.
- **On screen:** three cards appear around the building, each a way the twin could look:
  1. **Realistic 3D** (render-like);
  2. **Map view** (top-down satellite style);
  3. **2.5D** (clean, simple).
  
  As each card highlights, the building briefly takes on that look. Realistic and map fade out (*"hides the data"*, *"loses the building"*). 2.5D is chosen: the building settles into its clean final look (white walls, blue glass).
- **The faded options** shrink and drift into the backdrop as faint images (texture, not content).
- **Caption:** *Real enough to trust. Simple enough to read.*
- **Slow zone:** the moment 2.5D is chosen.
- **Hover:** hovering a card previews that look on the building.
- **Handoff to 6:** small dots (sensors) appear on each floor of the chosen building.
- **Assets needed:** a realistic look (material set) and a map look. *Open: use the real early concept images (Q3).*
- **Confusion risk:** visitors may think all three looks are product features. *Mitigation:* the caption and the clear fade of the rejected two.

### Beat 6 · Data (720–900 vh)
- **Camera:** pushes in to floor 6 (close three-quarter), then eases back slightly.
- **On screen:**
  - sensors light on each floor;
  - fine lines come in from the edges of the stage carrying data, labelled at the edge: *Meters*, *Building systems*, *Tariffs*, *Weather*;
  - they flow into the building as moving dots;
  - floor 7's line is **dashed**, labelled *Estimated from 14 days*.
  
  The dashboard number cards fill in one by one: live load, solar, battery, anomalies.
- **Colour:** **blue** enters for the first time (the data lines and live numbers).
- **Sun/moon:** 2 passes.
- **Caption:** *Then the data. Even what's missing.*
- **Hover:** hovering a data line shows what it carries and how often.
- **Handoff to 7:** the camera eases back; the roof solar panels begin to glow.
- **Attention gap:** the building and the dashboard both change. *Rule:* the 3D change happens first, then the matching card fills 300 ms later, so the eye moves from cause to effect.
- **Truth check:** data sources and the estimation rule must match the real product (Q4).

### Beat 7 · Energy (900–1040 vh)
- **Camera:** pulls back to the whole site, slightly higher.
- **On screen:** systems light up in turn: roof solar, cooling on floors, the battery yard, EV chargers in the carport. Energy **flows visibly** between them as soft animated paths: sun → roof → battery → floors → cars. The load-vs-price chart draws itself in the right panel. Floor 6 shows a soft orange glow (too much load).
- **Colour:** **green** (energy flowing) and **soft orange** (attention) join the blue.
- **Sun/moon:** 2 passes.
- **Caption:** *Then the energy: where it comes from, where it goes.*
- **Hover:** hovering a system shows its live value and where its energy is going.
- **Handoff to 8:** the question bar at the bottom wakes up: its outline turns solid and the cursor starts blinking in it.
- **Confusion risk:** too many moving flows. *Rule:* at most 3 flows animate at once; others are static lines.

### Beat 8 · AI (1040–1240 vh) · **Set piece 2**
- **Camera:** settles into the **hero framing** (three-quarter, building slightly left of centre, panels around).
- **On screen:**
  1. Two ghost layouts flash across the dashboard, one after the other: *assistant beside a dashboard* and *chat only*. They slide together and merge into the real layout. This is the A/B decision.
  2. The AI + data cursor types a question in the question bar: *"Why is floor 6 using so much today?"*
  3. Floor 6 highlights in the building; the camera pushes in slightly.
  4. The panels **rearrange themselves around the answer**: an insight card (*+38%, west glazing in full sun*), a load chart, an action (*Pre-cool at 11:00*).
- **Sun/moon:** last pass, slowing down.
- **Caption:** *Then the AI. Not a chat window. An answer, in place.*
- **Slow zone:** from the question typing to the answer landing.
- **Hover:** none during the answer, to keep the moment clean.
- **Handoff to 9:** the three team cursors step back to the edges. The sun slows to the top of its arc.
- **Technical note:** panel rearrangement uses GSAP Flip on the HTML panels, synced to the 3D highlight.

### Beat 9 · Live (1240–1400 vh) · **Set piece 3**
- **Time stops.** The sun parks at the top of the arc. Everything goes still for a beat (about 30 vh of nothing moving).
- **Then:**
  - a small badge appears in the top bar: **Live · real data**;
  - the visitor's cursor gets its label, **You**;
  - the question bar invites them: *Ask it something*, with 3 suggestions (cost today, wasted energy, carbon target).
- **The visitor can:**
  - pick a suggestion or type, and see a scripted answer play on the building and panels;
  - hover any floor or system to see its live value;
  - drag a time-of-day slider (the product's own feature) and watch the building's values change.
- **Caption:** *Live. Ask it something.*
- **Scroll:** stays native. The section is long enough to play in; scrolling on continues the page.
- **Handoff to 10:** when the visitor scrolls on, the team cursors come back and the camera begins to pull back.
- **Truth check:** the questions and answers must come from the real product (Q6). *Open: live twin or scripted (Q7).*

### Beat 10 · Your blank screen (1400–1640 vh) · **Set piece 4**
- **Camera:** pulls back. The whole product (layout and building) shrinks to one frame on the big grid, the same grid as beat 1.
- **On screen, in order:**
  1. **The team:** the three cursors expand into small profile cards next to the product frame (role, first name, photo or monogram).
  2. **The quote:** the client's words appear on the canvas as a comment, like a design-tool comment pinned to the product frame, with the CEO's name.
  3. **The clear:** the product frame drifts up and away. The canvas is blank again: white, grid, one blinking cursor. Full circle.
  4. **The form:** fields draw themselves on the blank canvas as the visitor reaches them, the same way the layout drew in beat 2.
     - *What should your product answer?* (the visitor's question from beat 9 is prefilled if they asked one)
     - *Email*
     - *Company or product URL* (optional)
     - **Send**, with *See available times* beside it.
- **Caption:** *Your blank screen?*
- **Hover:** fields glow as in beat 2.
- **After sending:** the three team cursors gather around the form, and one leaves a comment: *We'll reply within a day.*

### Beat 11 · Credits (normal page)
- Same white world, grid fading out, normal scrolling, no 3D.
- **Contents:**
  - FAQ for founders (accordion), styled as "questions on the canvas";
  - related work (BuildTwin, Eden AI);
  - the Tcules footer.

---

## 3. Confusions this frame can create, and how we prevent them
| # | Confusion | Where | Prevention |
|---|---|---|---|
| C1 | "Is this a construction company?" | Beats 3–4 | No cranes or materials; the building extrudes from a drawing inside a software layout, moved by cursors |
| C2 | "Is ConnectX the building or the product?" | Beats 2–4 | The top bar says ConnectX from beat 2; the building sits inside the product |
| C3 | "Whose cursors are these?" | Beat 1 | Role labels from the start; Tcules logo in the nav from beat 2; profile cards in beat 10 |
| C4 | "Is this a real product or a concept?" | Beat 9 | The **Live · real data** badge; the visitor can use it |
| C5 | "Am I meant to click things while scrolling?" | Beats 1–8 | Only small hover reactions during the story; a clear invitation only at Live |
| C6 | "What do the sun and moon mean?" | Beats 4–8 | Subtle on purpose; read as "time passing". If testing shows it's missed, add a soft hint in one caption |
| C7 | "Are the three looks product features?" | Beat 5 | The rejected two visibly fade and drift into the background |
| C8 | "Is the AI a chatbot?" | Beat 8 | The ghost "chat only" layout is rejected; the answer lands in the building and panels |
| C9 | "Where's the studio in all this?" | Throughout | The cursors are the studio; the nav, team cards and form are Tcules |
| C10 | "How long did this take?" | Throughout | Never stated; felt through the pace, the sun/moon passes and the cursors' speed |
| C11 | "What's estimated data?" | Beat 6 | A short label on the dashed line; full detail on hover |
| C12 | "I scrolled up and it's un-building. Did I break it?" | Any | That's the mechanic; it reads as rewind because everything reverses together |

---

## 4. Transition gaps and complexities
| # | Gap | Difficulty | Plan |
|---|---|---|---|
| T1 | 2D drawing (beats 1–2) → 3D plan (beat 3) must look like one surface | Medium | Orthographic top-view camera aligned pixel-exact with the HTML layout; same line weight and colour |
| T2 | Top view → three-quarter tilt while the UI frame stays flat | Medium | The 3D canvas is clipped to the centre stage; only the camera inside moves |
| T3 | Building changes look in beat 5 (realistic, map, 2.5D) | High | Three material sets on one model, blended by a shader value; the map look as a texture swap on the ground plus top camera |
| T4 | Cursors doing real work (dragging floors, drawing lines) | Medium | Cursor paths authored as curves on the timeline; each action triggers the matching 3D/HTML change |
| T5 | 3D change → matching dashboard card (cause before effect) | Low | 300 ms offset rule, all on the master timeline |
| T6 | Panels rearranging around the AI answer | Medium | GSAP Flip on HTML panels, synced with the 3D highlight |
| T7 | Time stops at Live, scroll keeps going | Medium | The master timeline ends at beat 9's start; beat 9+ use normal ScrollTriggers |
| T8 | Product frame shrinks to the big grid (beat 10) | Medium | Scale the whole layout (HTML + canvas) as one group; the grid behind continues |
| T9 | Rewind through everything | Low–medium | Everything is a pure function of time; no one-way triggers in the story |
| T10 | Phone layout | High | Separate vertical composition: building on top, panels stacked below; pre-rendered sequences for beats 4, 5, 8 |
| T11 | Reduced motion | Low | One still per beat, crossfading |
| T12 | Hover vs keyboard | Low | Every hover reaction also on focus; nothing essential is hover-only |

---

## 5. Open questions
Each has a default I will use unless you say otherwise.

| # | Question | Owner | Default |
|---|---|---|---|
| Q1 | Show the product name ConnectX and the client name in the UI? | You | Yes |
| Q2 | Cursor labels: roles only, or first names too? | You | Roles plus first names |
| Q3 | The rejected twin looks: use the real early concept images, or make new realistic and map looks? | You | Make new looks in the same style, so the quality holds |
| Q4 | The real data sources and the estimation rule | You | Meters, building systems, tariffs, weather; estimate from 14 days |
| Q5 | The real dashboard panels and numbers | You | Live load, solar, battery, anomalies; load-vs-price chart; insight card |
| Q6 | 3–10 real questions with real answers | You | The three from the moodboard |
| Q7 | Live section: embed the real live twin, or a scripted copy? | Both | Scripted on the live twin's engine, restyled |
| Q8 | Sound, off by default with a toggle? | You | No sound in iteration 3 |
| Q9 | A headline above the story for search engines and sharing? | Both | A hidden page heading plus the first caption visible |
| Q10 | Is ~16 screens of story the right length? | Both | Start here, tune in the prototype |
| Q11 | Phones: the same story in a vertical layout? | Both | Yes, with pre-rendered sequences for heavy beats |
| Q12 | Who makes the 3D building? | You | Me in code from the existing geometry, upgraded |
| Q13 | Team photos or monograms in beat 10? | You | Monograms until photos exist |
| Q14 | Quote as a canvas comment with the CEO's name? | You | Yes |
| Q15 | Prefill the form with the visitor's question from Live? | You | Yes |
| Q16 | The FAQ answers and offer terms | You | Drafts marked [Confirm] |

---

## 6. What iteration 3 (the draft) will contain
On the canvas, as a new column on the Website page:
1. **System sheet:** the global rules in one board (time, world, sun/moon, cursors, colour entry, rail, words).
2. **Ten beat boards:** each with the start, middle and end frame at real size, the caption, camera note, hover note and handoff.
3. **The four set pieces at finished quality:** Rise (4), Look (5), AI (8), Live (9), with the Live board interactive.
4. **Confusions and open questions:** one board each, so decisions can be ticked off.

After that review we decide what changes before a coded prototype of beats 1–4.
