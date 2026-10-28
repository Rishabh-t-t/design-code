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
  function revealLines(el, { start = 'top 85%', stagger = 0.08 } = {}) {
    let played = false;
    SplitText.create(el, {
      type: 'lines', mask: 'lines', linesClass: 'split-line', autoSplit: true,
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
    const from = token('--ink-4');
    const to = token('--ink');
    SplitText.create(el, {
      type: 'words', autoSplit: true,
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

  /* ---------- Start once fonts are ready (line breaks depend on them) ---------- */
  let started = false;
  function start() {
    if (started) return;
    started = true;

    /* Hero: title by character, credits, then the media */
    const media = $('.hero__media');
    const gutter = () => parseFloat(getComputedStyle($('.hero .wrap')).paddingLeft);
    gsap.set(media, { clipPath: `inset(0px ${gutter()}px 0px ${gutter()}px round 24px)` });
    $$('.hero__credit').forEach((el) => el.classList.add('draw'));
    gsap.set('.hero__credit', { '--draw': 0 });
    root.classList.remove('is-loading');

    const name = SplitText.create('.hero__name', { type: 'lines,chars', mask: 'lines' });
    gsap.timeline({ defaults: { ease: EASE } })
      .from(name.chars, { yPercent: 110, duration: 1.2, stagger: 0.035 }, 0)
      .from('.hero__eyebrow', { opacity: 0, y: 12, duration: 0.8 }, 0.1)
      .to('.hero__credit', { '--draw': 1, duration: 1.2, stagger: 0.08 }, 0.35)
      .from('.hero__credit > *', { opacity: 0, y: 14, duration: 0.8, stagger: 0.04 }, 0.45)
      .from('.hero__h1', { opacity: 0, y: 14, duration: 0.8 }, 0.6)
      .from(media, { opacity: 0, y: 48, duration: 1.4 }, 0.55);

    /* Hero media opens to full-bleed as the page scrolls */
    gsap.fromTo(media,
      { clipPath: () => `inset(0px ${gutter()}px 0px ${gutter()}px round 24px)` },
      {
        clipPath: 'inset(0px 0px 0px 0px round 0px)', ease: 'none',
        scrollTrigger: { start: 0, end: () => innerHeight * 0.75, scrub: true, invalidateOnRefresh: true },
      });
    gsap.fromTo('.hero__media .ph__screen', { scale: 0.94 }, {
      scale: 1, ease: 'none',
      scrollTrigger: { start: 0, end: () => innerHeight * 0.75, scrub: true },
    });

    /* Pinned scenes go first so later triggers measure the pin spacing */
    if (window.cxScenes) window.cxScenes.init({ lenis, EASE });
    if (window.cxComponents) window.cxComponents.init({ EASE });

    /* Line reveals */
    $$([
      '.chapter__head .t-statement', '.chapter__pull', '.sub__head h3', '.glance__row--key dd',
      '.facts__title', '.faq__title', '.related__title', '.enquiry__title', '.quote.is-active blockquote p',
    ].join(',')).forEach((el) => revealLines(el));

    /* Big reads brighten word by word, scrubbed */
    $$('.intro__text .t-intro, .decide__lead').forEach(brighten);

    /* Fade-up for supporting elements */
    const fades = $$([
      '.intro__links', '.glance__head', '.glance__row dt', '.glance__row:not(.glance__row--key) dd', '.glance__services',
      '.chapter__label', '.chapter__body > p', '.role-card', '.carousel__caption', '.stage__caption',
      '.areas__nav > .t-meta', '.sub__body > p', '.compare__item > .t-meta', '.compare__item figcaption',
      '.demo__media figcaption', '.timeline__title', '.timeline__step > p', '.decide__h2', '.decide__defs > .t-meta',
      '.defs li > *', '.decide__body > p', '.facts__row > *', '.quotes__title', '.quote__by', '.quotes__controls',
      '.trust__list li', '.related__lead', '.related__row > *', '.enquiry__sub', '.field', '.enquiry__actions',
    ].join(','));
    gsap.set(fades, { opacity: 0, y: 24 });
    ScrollTrigger.batch(fades, {
      start: 'top 90%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.9, ease: EASE, stagger: 0.07, overwrite: true }),
    });

    /* Footer: columns rise together once its top is on screen */
    const footerBits = $$('.footer__brand > *, .footer__col, .footer__mid > *, .footer__bottom');
    gsap.from(footerBits, {
      opacity: 0, y: 32, duration: 1, ease: EASE, stagger: 0.05,
      scrollTrigger: { trigger: '.footer', start: 'top 85%', once: true },
    });

    /* Hairline rules draw left to right */
    const rules = $$('.glance__row, .defs li, .facts__row, .faq__item, .related__row, .timeline__step');
    rules.forEach((el) => el.classList.add('draw'));
    gsap.set(rules, { '--draw': 0 });
    ScrollTrigger.batch(rules, {
      start: 'top 92%', once: true,
      onEnter: (els) => gsap.to(els, { '--draw': 1, duration: 1.3, ease: 'expo.inOut', stagger: 0.08 }),
    });

    /* Media: clip wipe open, inner screen settles */
    $$('.carousel__item, .sub__media, .compare__ph, .demo__ph, .areas__view').forEach((el) => {
      const trigger = { trigger: el, start: 'top 88%', once: true };
      gsap.fromTo(el, { clipPath: 'inset(12% 5% 12% 5% round 24px)' }, {
        clipPath: 'inset(0% 0% 0% 0% round 24px)', duration: 1.5, ease: EASE, scrollTrigger: trigger,
      });
      const inner = !el.classList.contains('areas__view') && el.querySelector('.ph__screen, .cx-app');
      if (inner) gsap.from(inner, { scale: 1.08, duration: 1.8, ease: EASE, scrollTrigger: trigger });
    });

    /* Demo image: light parallax */
    gsap.fromTo('.demo__ph .ph__screen', { y: -40 }, {
      y: 40, ease: 'none',
      scrollTrigger: { trigger: '.demo__ph', start: 'top bottom', end: 'bottom top', scrub: true },
    });

    /* Digital twin: the explored direction steps back, the chosen one comes forward */
    gsap.timeline({ scrollTrigger: { trigger: '.compare', start: 'top 80%', end: 'bottom 50%', scrub: true } })
      .to('.compare__item--explored', { opacity: 0.55, scale: 0.95, y: 24, transformOrigin: '50% 100%', ease: 'none' }, 0)
      .fromTo('.compare__item--chosen', { y: 64 }, { y: 0, ease: 'none' }, 0);

    /* Numbers count up */
    $$('.facts__row .t-stat').forEach(countUp);
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

  /* ---------- Carousel: drag with the mouse, arrow keys ---------- */
  const track = $('.carousel__track');
  let drag = null;
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
    .then(() => Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 1500))]))
    .then(start);
})();
