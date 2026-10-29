/* ConnectX case study — sticky scenes.
   Each scene is a tall track whose content sticks under the nav with CSS position: sticky
   (see sections.css). Nothing is pinned here: ScrollTrigger only reads progress through the track,
   so the scene stops exactly at its line and moves exactly with the scroll.
   Called by motion.js once fonts are ready: window.cxScenes.init({ lenis, EASE }). */
window.cxScenes = {
  init({ lenis }) {
    const $ = (s, c = document) => c.querySelector(s);
    const $$ = (s, c = document) => [...c.querySelectorAll(s)];
    const STICK = 96; // matches `top` on the sticky elements
    const ink = getComputedStyle(document.documentElement);
    const color = (name) => ink.getPropertyValue(name).trim();

    /* Progress runs from "content reaches its sticky line" to "track ends and it scrolls away" */
    const span = (track, sticky) => ({
      trigger: track,
      start: `top ${STICK}px`,
      end: () => `bottom ${STICK + sticky.offsetHeight}px`,
      invalidateOnRefresh: true,
    });

    /* ---------- S5 The choice: two directions merge into the chosen model ---------- */
    const track = $('[data-pin="choice"] .stage__track');
    if (track) {
      const frame = $('.stage__frame', track);
      const [dirA, dirB] = $$('.choice__dir', frame);
      const verdicts = $$('.choice__dir .choice__verdict', frame);
      const merged = $('.choice__merged', frame);
      const flow = $('.flow', frame);
      const steps = $$('.flow__step', frame);
      // steps wait in legible grey (4.6:1) and turn black as the line reaches them
      gsap.set(steps, { color: color('--ink-3') });
      gsap.set(flow, { '--flow': 0 });

      gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { ...span(track, frame), scrub: 0.4 } })
        // beat 1 → 2: verdicts step aside, the directions slide together
        .to(verdicts, { opacity: 0, y: -8, duration: 0.4 }, 0.2)
        .to(dirA, { xPercent: 26, scale: 0.9, duration: 1 }, 0.2)
        .to(dirB, { xPercent: -26, scale: 0.9, duration: 1 }, 0.2)
        // beat 3: they merge into one workspace, grey turns product blue
        .to([dirA, dirB], { opacity: 0, duration: 0.5 }, 1.05)
        .fromTo(merged, { autoAlpha: 0, scale: 0.92, y: 24 }, { autoAlpha: 1, scale: 1, y: 0, duration: 0.7 }, 1.05)
        // the merged workspace assembles its modules around the question
        .from($$('[data-mod]', merged), { opacity: 0, y: 14, scale: 0.97, stagger: 0.1, duration: 0.45 }, 1.3)
        // beat 4: the line runs through the five steps and each one darkens as it is reached
        .to(flow, { '--flow': 1, duration: 1.1 }, 1.7)
        .to(steps, { color: color('--ink'), stagger: 0.22, duration: 0.3 }, 1.7)
        .to({}, { duration: 0.4 });
    }

    /* ---------- S6 Scenario areas: the sticky list drives the workspace view ---------- */
    const stage = $('[data-pin="areas"]');
    const areas = stage && $('.areas', stage);
    if (areas) {
      const items = $$('.areas__item', areas);
      let current = -1;
      const setArea = (i) => {
        if (i === current) return;
        current = i;
        window.cxSetArea(i);
      };
      const st = ScrollTrigger.create({
        ...span(stage, areas),
        onUpdate: (self) => setArea(Math.min(items.length - 1, Math.floor(self.progress * items.length))),
      });
      setArea(0);
      items.forEach((el, n) => $('button', el).addEventListener('click', (e) => {
        e.stopPropagation();
        lenis.scrollTo(st.start + (st.end - st.start) * ((n + 0.5) / items.length), { duration: 1.2 });
      }));
    }
  },
};
