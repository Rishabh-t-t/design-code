# Handoff · ConnectX case study, Iteration 6

Context for continuing this work in a new chat. Read this first, then the files it points to.

## The project
- Tcules case study for **ConnectX**, an AI-first building-energy SaaS. Audience: zero-to-one founders and semi-technical PMs. Goal: "these people are experts; I can trust them with my money".
- Story facts: the client came with two words ("energy" and "AI"). In **8 weeks, 1 MVP, 3 people** (1 designer, 2 developers) Tcules shaped the problem, designed the product, added a 3D twin mid-way, connected real data (electricity provider API from a real office building), made the twin generate itself from a parts library, tried a chat box, then flipped to AI-first (ask → the AI builds the screen, every number traceable to its meter). Ending: pilot-ready / investor demo.
- Rules: the client may be named; **no model or tech names**; numbers may be real or invented; **never mention that the MVP contract ended after week 8**. Founder quote and some facts ("15 minutes", "24+ questions", "weekly review") are placeholders to confirm.
- How the user works: **don't build unless told**; make a detailed plan when asked; this is **refinement, not rebuild**; ask clarifying questions when unsure.

## Where things live
- **Claude Design canvas** (the main workspace): https://claude.ai/artifact/BLfrt37Z8jemQtK7AVsiCv
  - Page **"Iteration 6"** (`iter6`): `Proto6.dc.html` (the live scroll prototype, canvas launch view), loader boards `I6-L1..L3`, 20 stills `I6S-01..20` (each is `Proto6` frozen with `at="<scroll>"`), `I6App.dc.html` (the polished app component).
  - Older pages: Iteration 4 (`I4App`, the UI the user likes), Iteration 5 (`Proto5`, the scroll timeline), Story v2 page (story versions v2–v5).
  - Files to read from the canvas with Artifact `read` + `path`: `project/Proto6.dc.html`, `project/I6App.dc.html`, `project/i6p.css`, `project/i6app.css`, `project/i5.css`, `project/canvas.json`. Always re-read the live `canvas.json` before publishing (the user edits the canvas) and merge.
- **Figma**: file `iZpEgPaQNgE6efe4q56Nlw` ("Case study - ConnectX"). Page "story for draft 2" holds Story v5 as editable frames plus the user's own improved opening frames (section `80:2832`).
- **GitHub**: `Rishabh-t-t/design-code`, branch `claude/cool-rubin-hrpv85` (push only here).
  - The previous live page: `src/` → `node build.mjs` → `dist/connectx-case-study.html`, copied to root `index.html`; GitHub Pages deploys via `.github/workflows/static.yml` on push to this branch.
  - Building render tools: `docs/v4/building/` (`render-white-model.html`, `tools/`).

## Iteration 6 · what the prototype does (one scroll, 100 units = one screen)
- **Loader** (timed, plays once fonts + first renders load): dark screen, cool-grey band grows 376 → 632 → 888px → full while `001 8 weeks to build` → `002 1 MVP built by` → `003 3 people`.
- **Hero** (0–140): "We build full / Working SaaS with 2 words **energy** and **AI**" (user's wording, green underline on the two words), initial brief, finished building with floor 6 lit. No rail.
- **Week 1** (175–520): floor plan as the whole background (30%), "Helped the founder define the product and the business"; "Floor 6 cooled an empty office for three weeks"; break "Building for the business" (blur veil).
- **Weeks 2–4**: floors only (render frames 30 → 75). Partial UI: three empty bottom cards (design), figures count up (real data).
- **Weeks 5–6**: second skeleton layer (75 → 114). Cards leave; "builds itself"; **Buried** = only the cost card with one red spike + callout; **Chat box** = only the chat panel with a paragraph answer.
- **Flip** (1320–1430): only "So we flipped it. **Asking** comes first." + the search box.
- **Week 7**: question types in; scan (scan + assistant + input); building finishes (→ 149) then floor 6 lights (150); answer (answer card, input, pin); source (cooling card + source popover).
- **Week 8**: break "Ready for investors", founder quote (PLACEHOLDER), "Floor 6 is now a question on Monday. Not a surprise on the bill."
- **Try it** (1995+): the full app appears for the first time, live and interactive, inside a thin-bezel rounded **monitor** (no stand). Rail hidden.
- **After the story** (normal scroll): form "Got **two words** and a hunch?" (idea, stage chips, name, email, Start a project) → Q&A (7 questions, incl. how we worked: team, weekly review + milestones W1/W3/W4/W8, ownership) → footer.
- Chrome: iteration 5 tick rail (no dots) with a glass week pill shown only while its scene text is visible; progress line bottom right. No Tcules logo/mark.

## Design system (reference style: the Volvo EX30 dashboard image the user shared = iteration 4 look)
- One family: **Manrope**, weight 500 headlines, ink `#23272E`, body `#5B616B`, labels `#8A9099`. Hero 88px, chapter 60px, UI scenes 44px, line above 20px, body 16px; letter-spacing about −2%.
- Cool greys (iteration 4): page gradient `#E5E8EC → #DFE2E6 → #E3E6EA`; translucent white cards with strong blur, no shadows; app green `#0F9160`; floor 6 red `#D84A3B`; highlighter `#2EE37A` as a bold underline, only on energy/AI, Asking, two words.
- Text starts 60px from the left; the week pill may overlap it.
- App component `I6App`: copy of `I4App` with polish (8px spacing, 24px card radius, gaps) and props `mode` (story/home/loading/answer), `parts` (comma list: top,left,right,title,ai,input,card1,card2,card3,hhead,hinput,chips,hbrief,scan,pin,src; empty = everything), `chat`, `chart`, `src`, `noai`, `notitle`, `fill`, `focus`.

## Assets
- 151 building render frames (white model, AO): blob IDs listed in `ids5.json`, used by `Proto6` as `/_blob/<id>` on the canvas. Frame 0 = plan, 22 = plan tilting, 40–75 floors, 92–114 skeleton/walls/wiring, 128 facade closing, 149 finished, 150 finished with floor 6 lit.
- 11 traced line-art frames (used in Story v5 and Figma).

## Open next step
The user asked to build Iteration 6 on GitHub as HTML, like the previous live version. Pending decision: put it at a new path (`/v6/`, keeping the current live page) or replace the root page after snapshotting the current one to a branch. Then port `Proto6` (loader, canvas frame sequence, scroll timeline, partial UI, monitor + live app, form, Q&A, footer) to plain HTML/CSS/JS; the render frames go in as image files.

Still open in the story: confirm the founder quote and placeholder facts; test other screen sizes.
