/* ConnectX case study — motion system (Phase 2).
   Runs only when motion is allowed and the libraries loaded; otherwise the
   page stays complete and static (html.motion-off). */
(function () {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const libs = window.gsap && window.ScrollTrigger && window.SplitText && window.Lenis;
  if (reduce || !libs) {
    root.classList.remove('is-loading');
    root.classList.add('motion-off');
    return;
  }

  gsap.registerPlugin(ScrollTrigger, SplitText);
  root.classList.add('motion');

  const EASE = 'expo.out';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const token = (name) => getComputedStyle(root).getPropertyValue(name).trim();

  /* ---------- Smooth scroll ---------- */
  const lenis = new Lenis({ lerp: 0.1 });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((t) => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
  window.cxMotion = { lenis };

  /* ---------- Nav ---------- */
  const nav = $('[data-nav]');
  const chapterEl = $('[data-nav-chapter]');
  const menuBtn = $('[data-nav-menu]');
  const menu = $('#nav-menu');

  function setMenu(open) {
    menu.hidden = !open;
    menuBtn.setAttribute('aria-expanded', String(open));
    if (open) nav.classList.remove('is-hidden');
  }
  menuBtn.addEventListener('click', () => setMenu(menu.hidden));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); menuBtn.focus(); } });
  document.addEventListener('click', (e) => { if (!menu.hidden && !nav.contains(e.target)) setMenu(false); });

  /* In-page links scroll smoothly and clear the fixed nav */
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href');
    const el = id.length > 1 && document.querySelector(id);
    if (!el) return;
    e.preventDefault();
    setMenu(false);
    lenis.scrollTo(el, { offset: -96, duration: 1.4 });
    history.replaceState(null, '', id);
  });

  chapterEl.textContent = 'ConnectX';
  ScrollTrigger.create({
    trigger: '.hero', start: 'top -120px',
    onEnter: () => nav.classList.add('is-pill'),
    onLeaveBack: () => { nav.classList.remove('is-pill'); setMenu(false); },
  });
  /* Current chapter = the one crossing the middle of the screen; outside the chapters it reads "ConnectX".
     Measured on every scroll so jumps (menu links, fast scrolls) never leave a stale label. */
  const chapters = $$('[data-chapter]');
  function updateChapter() {
    const mid = innerHeight / 2;
    const sec = chapters.find((el) => { const r = el.getBoundingClientRect(); return r.top <= mid && r.bottom > mid; });
    const text = sec ? sec.dataset.chapter : 'ConnectX';
    if (chapterEl.textContent !== text) chapterEl.textContent = text;
  }
  lenis.on('scroll', updateChapter);

  /* Hide on a fast scroll down, return on any scroll up */
  lenis.on('scroll', ({ velocity, direction, scroll }) => {
    if (!menu.hidden || scroll < innerHeight) { nav.classList.remove('is-hidden'); return; }
    if (direction > 0 && velocity > 14) nav.classList.add('is-hidden');
    else if (direction < 0) nav.classList.remove('is-hidden');
  });

  /* ---------- Context cursor ---------- */
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
    root.classList.add('has-pointer');
    const cursor = $('.cursor');
    const label = $('.cursor__label');
    const xTo = gsap.quickTo(cursor, 'x', { duration: 0.35, ease: 'power3' });
    const yTo = gsap.quickTo(cursor, 'y', { duration: 0.35, ease: 'power3' });
    addEventListener('pointermove', (e) => {
      if (cursor.classList.contains('is-hidden')) { gsap.set(cursor, { x: e.clientX, y: e.clientY }); cursor.classList.remove('is-hidden'); }
      xTo(e.clientX); yTo(e.clientY);
    }, { passive: true });
    document.addEventListener('pointerover', (e) => {
      const t = e.target.closest('[data-cursor]');
      const text = t && t.dataset.cursor;
      cursor.classList.toggle('is-label', !!text);
      if (text) label.textContent = text;
    });
    document.documentElement.addEventListener('mouseleave', () => cursor.classList.add('is-hidden'));
    document.documentElement.addEventListener('mouseenter', () => cursor.classList.remove('is-hidden'));
    window.cxMotion.cursor = cursor;
  }

  /* ---------- Helpers ---------- */
  /* A batch can hold everything a long jump skipped past: show those at once,
     and stagger only what is on screen, capped so nothing waits long */
  function staggerIn(els, vars) {
    const onScreen = els.filter((el) => el.getBoundingClientRect().bottom > 0);
    const passed = els.filter((el) => !onScreen.includes(el));
    if (passed.length) gsap.set(passed, Object.fromEntries(Object.keys(vars).filter((k) => !['duration', 'ease', 'stagger', 'overwrite'].includes(k)).map((k) => [k, vars[k]])));
    if (onScreen.length) gsap.to(onScreen, { ...vars, stagger: Math.min(vars.stagger || 0, 0.6 / onScreen.length) });
  }

  function revealLines(el, { start = 'top 85%', stagger = 0.08 } = {}) {
    let played = false;
    SplitText.create(el, {
      type: 'lines', mask: 'lines', linesClass: 'split-line', autoSplit: true, aria: 'none',
      onSplit(self) {
        if (played) return undefined;
        return gsap.from(self.lines, {
          yPercent: 105, duration: 1.1, ease: EASE, stagger,
          scrollTrigger: { trigger: el, start, once: true, onEnter: () => { played = true; } },
        });
      },
    });
  }

  function brighten(el) {
    const from = token('--ink-dim');
    const to = token('--ink');
    SplitText.create(el, {
      type: 'words', autoSplit: true, aria: 'none',
      onSplit(self) {
        return gsap.fromTo(self.words, { color: from }, {
          color: to, ease: 'none', stagger: 0.1,
          scrollTrigger: { trigger: el, start: 'top 82%', end: 'bottom 55%', scrub: true },
        });
      },
    });
  }

  function countUp(el) {
    const node = [...el.childNodes].find((n) => n.nodeType === 3 && /\d/.test(n.textContent));
    if (!node) return;
    const m = node.textContent.match(/^(\s*)([\d.]+)(.*)$/s);
    if (!m) return;
    const target = parseFloat(m[2]);
    const decimals = (m[2].split('.')[1] || '').length;
    const obj = { v: 0 };
    const write = () => { node.textContent = m[1] + obj.v.toFixed(decimals) + m[3]; };
    write();
    gsap.to(obj, {
      v: target, duration: 1.6, ease: 'power3.out', onUpdate: write,
      scrollTrigger: { trigger: el, start: 'top 88%', once: true },
    });
  }

  /* ---------- Start: the hero right away, everything else once fonts are ready ----------
     The set-up is split into short tasks so the main thread never blocks for long. */
  const yieldToBrowser = () => new Promise((r) => setTimeout(r, 0));

  function startHero() {
    /* Hero: eyebrow, title line by line, then the credits line. The twin below shows its picture
       right away and fades to live on its own, so it is not part of this sequence.
       Lines re-split if the fonts arrive later, without replaying the reveal. */
    root.classList.remove('is-loading');
    let heroPlayed = false;
    SplitText.create('.hero__title', {
      type: 'lines', mask: 'lines', aria: 'none', autoSplit: true,
      onSplit(self) {
        if (heroPlayed) return undefined;
        heroPlayed = true;
        return gsap.timeline({ defaults: { ease: EASE } })
          .from('.hero__eyebrow', { opacity: 0, y: 12, duration: 0.8 }, 0)
          .from(self.lines, { yPercent: 105, duration: 1.2, stagger: 0.09 }, 0.1)
          .from('.details > .detail', { opacity: 0, y: 10, duration: 0.8, stagger: 0.06 }, 0.5);
      },
    });
  }

  /* Line breaks depend on the web fonts, so text splitting waits for them */
  async function startRest() {
    /* Pinned scenes go first so later triggers measure the pin spacing */
    if (window.cxScenes) window.cxScenes.init({ lenis, EASE });
    await yieldToBrowser();
    if (window.cxComponents) window.cxComponents.init({ EASE });
    await yieldToBrowser();

    /* Line reveals */
    $$([
      '.chapter__heading:not(.decide__lead)', '.banner__text', '.peak__text h3', '.glance__key .t-heading-m',
      '.facts__title', '.faq__title', '.related__title', '.enquiry__title', '.intro__summary',
    ].join(',')).forEach((el) => revealLines(el));
    await yieldToBrowser();

    /* Big reads brighten word by word, scrubbed */
    $$('.decide__lead').forEach(brighten);
    await yieldToBrowser();

    /* Fade-up for supporting elements */
    const fades = $$([
      '.hero__eyebrow', '.intro__links', '.glance__head > *', '.glance__key > .t-body-l', '.summary__row > *',
      '.chapter__label', '.split .copy > *', '.role-card', '.banner__cite', '.shell__caption',
      '.areas__label', '.peak__text .copy > *', '.timeline-row__title', '.timeline__step > p', '.rules__label',
      '.rules__list li > *', '.facts__item > *', '.quotes__title', '.quote',
      '.trust__list li', '.related__lead', '.related__row > *', '.enquiry__sub', '.field', '.enquiry__actions',
    ].join(','));
    gsap.set(fades, { opacity: 0, y: 24 });
    ScrollTrigger.batch(fades, {
      start: 'top 90%', once: true,
      onEnter: (els) => staggerIn(els, { opacity: 1, y: 0, duration: 0.9, ease: EASE, stagger: 0.07, overwrite: true }),
    });

    /* Footer: columns rise together once its top is on screen */
    const footerBits = $$('.footer__brand > *, .footer__col, .footer__mid > *, .footer__bottom');
    gsap.from(footerBits, {
      opacity: 0, y: 32, duration: 1, ease: EASE, stagger: 0.05,
      scrollTrigger: { trigger: '.footer', start: 'top 85%', once: true },
    });

    /* Hairline rules draw left to right */
    const rules = $$('.summary__row, .rules__list li, .faq__item, .related__row');
    rules.forEach((el) => el.classList.add('draw'));
    gsap.set(rules, { '--draw': 0 });
    ScrollTrigger.batch(rules, {
      start: 'top 92%', once: true,
      onEnter: (els) => staggerIn(els, { '--draw': 1, duration: 1.3, ease: 'expo.inOut', stagger: 0.08 }),
    });

    await yieldToBrowser();

    /* Media: clip wipe open, inner screen settles */
    $$('.shell__frame').forEach((el) => {
      const trigger = { trigger: el, start: 'top 88%', once: true };
      gsap.fromTo(el, { clipPath: 'inset(10% 6% 10% 6%)' }, {
        clipPath: 'inset(0% 0% 0% 0%)', duration: 1.5, ease: EASE, scrollTrigger: trigger,
      });
      const inner = el.querySelector('.shell__img');
      if (inner) gsap.from(inner, { scale: 1.08, duration: 1.8, ease: EASE, scrollTrigger: trigger });
    });

    /* Image shells: a light parallax inside each square */
    $$('.shell__img').forEach((img) => gsap.fromTo(img, { yPercent: -4, scale: 1.08 }, {
      yPercent: 4, scale: 1.08, ease: 'none',
      scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true },
    }));

    /* Numbers count up */
    $$('.facts__item .t-stat').forEach(countUp);
    $$('.trust__v').filter((el) => !/^\s*\d{4}\s*$/.test(el.textContent)).forEach(countUp);

    /* Next case study marquee: drifts, speeds up with scroll velocity */
    const loop = gsap.to('.next__track', { xPercent: -50, duration: 32, ease: 'none', repeat: -1 });
    let boost = 1;
    lenis.on('scroll', ({ velocity }) => { boost = Math.max(boost, 1 + Math.min(Math.abs(velocity) * 0.35, 6)); });
    gsap.ticker.add(() => {
      boost += (1 - boost) * 0.05;
      loop.timeScale(loop.timeScale() + (boost - loop.timeScale()) * 0.1);
    });
    ScrollTrigger.create({
      trigger: '.next', start: 'top bottom', end: 'bottom top',
      onToggle: (self) => (self.isActive ? loop.play() : loop.pause()),
    });

    ScrollTrigger.refresh();
  }

  /* Keyboard users never land on something still mid-reveal */
  document.addEventListener('focusin', (e) => {
    for (let el = e.target; el && el !== document.body; el = el.parentElement) {
      if (el.style.opacity !== '' && parseFloat(el.style.opacity) < 1) { gsap.killTweensOf(el); gsap.set(el, { opacity: 1, y: 0 }); }
    }
  });

  /* ---------- Carousel: drag with the mouse, arrow keys ---------- */
  const track = $('.carousel__track');
  let drag = null;
  if (track) {
  track.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    drag = { x: e.clientX, left: track.scrollLeft, moved: false };
    track.setPointerCapture(e.pointerId);
  });
  track.addEventListener('pointermove', (e) => {
    if (!drag) return;
    const dx = e.clientX - drag.x;
    if (!drag.moved && Math.abs(dx) > 4) { drag.moved = true; track.classList.add('is-dragging'); }
    if (drag.moved) track.scrollLeft = drag.left - dx;
  });
  const endDrag = () => { drag = null; track.classList.remove('is-dragging'); };
  track.addEventListener('pointerup', endDrag);
  track.addEventListener('pointercancel', endDrag);
  track.addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    e.preventDefault();
    const item = $('.carousel__item', track);
    const step = item.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 0);
    track.scrollBy({ left: e.key === 'ArrowRight' ? step : -step, behavior: 'smooth' });
  });
  }

  /* ---------- FAQ: animated height ---------- */
  $$('.faq__item').forEach((item) => {
    const body = $('.faq__a', item);
    $('summary', item).addEventListener('click', (e) => {
      e.preventDefault();
      gsap.killTweensOf(body);
      if (item.open && !item.classList.contains('is-closing')) {
        item.classList.add('is-closing');
        gsap.to(body, {
          height: 0, opacity: 0, duration: 0.5, ease: 'power3.inOut',
          onComplete: () => {
            item.open = false;
            item.classList.remove('is-closing');
            gsap.set(body, { clearProps: 'height,opacity' });
            ScrollTrigger.refresh();
          },
        });
      } else {
        item.classList.remove('is-closing');
        item.open = true;
        gsap.fromTo(body, { height: 0, opacity: 0 }, {
          height: 'auto', opacity: 1, duration: 0.6, ease: 'power3.out',
          onComplete: () => { gsap.set(body, { clearProps: 'height' }); ScrollTrigger.refresh(); },
        });
      }
    });
  });

  /* Wait for every script (scenes.js loads after this file), then for fonts — cached fonts resolve instantly */
  const domReady = document.readyState === 'loading'
    ? new Promise((r) => document.addEventListener('DOMContentLoaded', r, { once: true }))
    : Promise.resolve();
  domReady
    .then(() => Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 700))]))
    .then(startHero)
    .then(() => Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 1500))]))
    .then(startRest);
})();
