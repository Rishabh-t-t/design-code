/* ConnectX case study — Live Twin embed (Phase 4).
   The twin's HTML ships inside this page as JSON (#twin-src) and runs in an iframe made from a Blob.
   Until the reader engages it, a shield keeps wheel and drag on the page, so scrolling never gets trapped.
   Messages to the twin: intro · skip · pause · resume · engage {on} · scenario {id}
   Messages from it:    ready · live · scenario {id|null} · esc */
(function () {
  const root = $('[data-twin]');
  const src = document.getElementById('twin-src');
  if (!root || !src) return;
  function $(s, c = document) { return c.querySelector(s); }

  const stage = $('.twin__stage', root);
  const frame = $('[data-twin-frame]', root);
  const engageBtn = $('[data-twin-engage]', root);
  const exitBtn = $('[data-twin-exit]', root);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  let loaded = false, ready = false, introSent = false, engaged = false, visible = false;
  const queue = [];
  const send = (msg) => { if (ready) frame.contentWindow.postMessage(msg, '*'); else queue.push(msg); };

  function load() {
    if (loaded) return;
    loaded = true;
    const html = JSON.parse(src.textContent).replace('<head>', '<head><script>window.CX_EMBED = true;<\/script>');
    frame.src = URL.createObjectURL(new Blob([html], { type: 'text/html' }));
    frame.hidden = false;
  }

  window.addEventListener('message', (e) => {
    if (e.source !== frame.contentWindow) return;
    const m = e.data || {};
    if (m.cx === 'ready') {
      ready = true;
      root.classList.add('is-ready');
      queue.splice(0).forEach(send);
      if (!visible) send({ cx: 'pause' });
    }
    if (m.cx === 'live') root.classList.add('is-live');
    if (m.cx === 'esc') disengage();
    if (m.cx === 'scenario') root.dataset.scenario = m.id || '';
  });

  /* Load about one screen early; play the intro once it is properly in view; pause when off screen */
  new IntersectionObserver(([entry]) => { if (entry.isIntersecting) load(); }, { rootMargin: '100% 0px' }).observe(stage);
  new IntersectionObserver(([entry]) => {
    if (entry.intersectionRatio >= 0.45 && !introSent) { introSent = true; send({ cx: reduce ? 'skip' : 'intro' }); }
  }, { threshold: [0, 0.45] }).observe(stage);
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    send({ cx: visible ? 'resume' : 'pause' });
    if (!visible && engaged) disengage();
  }).observe(stage);

  /* Engage: the twin takes wheel, drag and keys; Exit or Esc hands them back */
  const cursor = () => window.cxMotion && window.cxMotion.cursor;
  function engage() {
    if (!ready || engaged || !root.classList.contains('is-live')) return;
    engaged = true;
    root.classList.add('is-engaged');
    document.documentElement.classList.add('twin-engaged');
    // line the twin up with the top of the screen so its own top bar is fully visible
    if (window.cxMotion) window.cxMotion.lenis.scrollTo(stage, { duration: 0.8 });
    else stage.scrollIntoView({ block: 'start' });
    stage.dataset.cursor = '';
    if (cursor()) cursor().classList.add('is-hidden');
    exitBtn.hidden = false;
    frame.tabIndex = 0;
    send({ cx: 'engage', on: true });
    frame.focus({ preventScroll: true });
  }
  function disengage() {
    if (!engaged) return;
    engaged = false;
    root.classList.remove('is-engaged');
    document.documentElement.classList.remove('twin-engaged');
    stage.dataset.cursor = 'Explore';
    exitBtn.hidden = true;
    frame.tabIndex = -1;
    send({ cx: 'engage', on: false });
    engageBtn.focus({ preventScroll: true });
  }

  engageBtn.addEventListener('click', engage);
  $('[data-twin-shield]', root).addEventListener('click', engage);
  exitBtn.addEventListener('click', disengage);
  root.querySelectorAll('[data-twin-run]').forEach((b) => b.addEventListener('click', () => {
    engage();
    send({ cx: 'scenario', id: b.dataset.twinRun });
  }));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && engaged) disengage(); });
})();
