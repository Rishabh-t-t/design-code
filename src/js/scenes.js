/* ConnectX case study — pinned scenes (Phase 2, on grey boxes).
   Called by motion.js once fonts are ready: window.cxScenes.init({ lenis, EASE }). */
window.cxScenes = {
  init({ lenis }) {
    const $ = (s, c = document) => c.querySelector(s);
    const $$ = (s, c = document) => [...c.querySelectorAll(s)];
    const NAV_CLEAR = 88; // pinned stages sit just under the floating nav

    /* ---------- S5 The choice: two directions merge into the chosen model ---------- */
    const frame = $('[data-pin="choice"] .stage__frame');
    if (frame) {
      const [dirA, dirB] = $$('.choice__dir', frame);
      const verdicts = $$('.choice__dir .choice__verdict', frame);
      const merged = $('.choice__merged', frame);
      const steps = $$('.flow__step', frame);
      steps.forEach((el) => el.classList.add('draw'));
      gsap.set(steps, { opacity: 0.15, y: 12, '--draw': 0, '--draw-c': 'var(--line-strong)' });

      gsap.timeline({
        defaults: { ease: 'none' },
        scrollTrigger: {
          trigger: frame, start: `top ${NAV_CLEAR}px`, end: '+=160%',
          pin: true, scrub: 0.6, anticipatePin: 1, refreshPriority: 2,
        },
      })
        // beat 1 → 2: verdicts step aside, the directions slide together
        .to(verdicts, { opacity: 0, y: -8, duration: 0.4 }, 0.2)
        .to(dirA, { xPercent: 26, scale: 0.9, duration: 1 }, 0.2)
        .to(dirB, { xPercent: -26, scale: 0.9, duration: 1 }, 0.2)
        // beat 3: they merge into one workspace, grey turns product blue
        .to([dirA, dirB], { opacity: 0, duration: 0.5 }, 1.05)
        .fromTo(merged, { autoAlpha: 0, scale: 0.92, y: 24 }, { autoAlpha: 1, scale: 1, y: 0, duration: 0.7 }, 1.05)
        // the merged workspace assembles its modules around the question
        .from($$('[data-mod]', merged), { opacity: 0, y: 14, scale: 0.97, stagger: 0.1, duration: 0.45 }, 1.3)
        // beat 4: the chosen model's five steps draw in
        .to(steps, { opacity: 1, y: 0, '--draw': 1, stagger: 0.22, duration: 0.6 }, 1.7)
        .to({}, { duration: 0.4 });
    }

    /* ---------- S6 Scenario areas: pinned list drives the workspace view ---------- */
    const areas = $('[data-pin="areas"] .areas');
    if (areas) {
      const items = $$('.areas__item', areas);
      let current = -1;
      const setArea = (i) => {
        if (i === current) return;
        current = i;
        window.cxSetArea(i);
      };
      const st = ScrollTrigger.create({
        trigger: areas, start: `top ${NAV_CLEAR}px`, end: `+=${items.length * 60}%`,
        pin: true, anticipatePin: 1, refreshPriority: 1,
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
