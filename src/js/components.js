/* ConnectX case study — product component motion (Phase 3).
   Called by motion.js once fonts are ready: window.cxComponents.init({ EASE }).
   Without motion the components render in their finished state. */
window.cxComponents = {
  init({ EASE }) {
    const $ = (s, c = document) => c.querySelector(s);
    const $$ = (s, c = document) => [...c.querySelectorAll(s)];

    /* Types `el`'s text in. The untyped rest stays in the layout (transparent), so nothing reflows. */
    function typer(el) {
      const full = el.textContent;
      const caret = el.parentElement.querySelector('.cx-caret');
      el.textContent = '';
      const on = document.createElement('span');
      const off = document.createElement('span');
      off.className = 't-off';
      el.append(on);
      if (caret) el.append(caret);
      el.append(off);
      const render = (n) => { on.textContent = full.slice(0, n); off.textContent = full.slice(n); };
      render(0);
      return { length: full.length, render };
    }

    /* ---------- C1 Role cards: each need types in, staggered ---------- */
    $$('.role-card').forEach((card, i) => {
      const t = typer($('[data-type]', card));
      const proxy = { n: 0 };
      gsap.to(proxy, {
        n: t.length, duration: t.length * 0.035, ease: 'none', delay: 0.5 + i * 0.35,
        onUpdate: () => t.render(Math.round(proxy.n)),
        onComplete: () => setTimeout(() => card.classList.add('is-typed'), 1200),
        scrollTrigger: { trigger: '.roles__list', start: 'top 80%', once: true },
      });
    });

    /* ---------- C5 Peak-price assembly: plays once on enter, then can replay ---------- */
    const peak = $('[data-peak]');
    if (peak) {
      const q = typer($('[data-peak-q]', peak));
      const ask = $('.cx-askbar', peak);
      const twin = $('.cx-twin', peak);
      const replay = $('[data-peak-replay]', peak);
      const twinAttrs = { blue: twin.getAttribute('data-blue'), hot: twin.getAttribute('data-hot') };
      const lightTwin = (on) => {
        Object.entries(twinAttrs).forEach(([k, v]) => (on ? twin.setAttribute('data-' + k, v) : twin.removeAttribute('data-' + k)));
      };
      const proxy = { n: 0 };

      const tl = gsap.timeline({
        paused: true,
        onStart: () => { replay.hidden = true; ask.classList.remove('is-typed'); },
        onComplete: () => { ask.classList.add('is-typed'); replay.hidden = false; },
      })
        .add(() => lightTwin(false), 0)
        .fromTo(proxy, { n: 0 }, { n: q.length, duration: q.length * 0.03, ease: 'none', onUpdate: () => q.render(Math.round(proxy.n)) }, 0.2)
        .from($$('[data-peak-step]', peak), { opacity: 0, x: -8, duration: 0.45, stagger: 0.35, ease: EASE }, '>0.15')
        .from($$('[data-mod]', peak), { opacity: 0, y: 18, scale: 0.97, duration: 0.7, stagger: 0.14, ease: EASE }, '>-0.1')
        .add(() => lightTwin(true), '<0.15')
        .fromTo($$('.cx-draw', peak), { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: 1.2, stagger: 0.15, ease: 'power2.inOut' }, '<0.3')
        .from($$('.cx-bars__row i', peak), { scaleX: 0, duration: 0.9, stagger: 0.2, ease: EASE }, '<0.2');

      // Start hidden: render the first frame now, play when it scrolls into view
      q.render(0);
      lightTwin(false);
      tl.progress(0.0001).pause();
      ScrollTrigger.create({ trigger: peak, start: 'top 70%', once: true, onEnter: () => tl.play(0) });
      replay.addEventListener('click', () => tl.restart());
    }

    /* ---------- C6 Timeline: the line fills with scroll, nodes fill as it reaches them ---------- */
    const timeline = $('.timeline');
    if (timeline) {
      const fill = $('.timeline__fill', timeline);
      const steps = $$('.timeline__step', timeline);
      const stops = () => {
        const box = timeline.getBoundingClientRect();
        return steps.map((s) => (s.getBoundingClientRect().left - box.left) / box.width);
      };
      let at = stops();
      ScrollTrigger.addEventListener('refreshInit', () => { at = stops(); });
      gsap.fromTo(fill, { scaleX: 0 }, {
        scaleX: 1, ease: 'none',
        scrollTrigger: {
          trigger: timeline, start: 'top 85%', end: 'top 40%', scrub: 0.5,
          onUpdate: (self) => steps.forEach((s, i) => s.classList.toggle('is-reached', self.progress >= at[i] + 0.01)),
        },
      });
    }
  },
};
