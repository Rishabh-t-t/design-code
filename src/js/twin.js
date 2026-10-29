/* ConnectX case study — live twins (revision R3).
   Every [data-twin="hero|scenario|ask"] on the page runs the real ConnectX twin (#twin-src, shipped in the
   page as JSON) in a borderless iframe made from a Blob, in that embed mode.
   - A picture of the first frame shows instantly; the live twin fades in over it on its first frame.
   - Frames are created about one screen early, paused off screen, and unloaded when far away.
   - The wheel inside a twin is handed back to the page, so scrolling never gets trapped.
   Messages to a twin:  pause · resume · scenario {id} · ask {q}
   Messages from it:    ready · frame · wheel {dx, dy, dm} · scenario {id|null} */
(function () {
  const src = document.getElementById('twin-src');
  const hosts = [...document.querySelectorAll('[data-twin]')];
  if (!src || !hosts.length) return;

  let html = null;
  const twinHtml = () => html || (html = JSON.parse(src.textContent));

  /* Hand the wheel back to the page: through Lenis when it runs (same smoothing as anywhere else), else natively */
  function pageWheel({ dx, dy, dm }) {
    const unit = dm === 1 ? 16 : dm === 2 ? innerHeight : 1;
    if (window.cxMotion) {
      window.dispatchEvent(new WheelEvent('wheel', { deltaX: dx, deltaY: dy, deltaMode: dm, bubbles: true, cancelable: true }));
    } else {
      window.scrollBy(dx * unit, dy * unit);
    }
  }

  const twins = hosts.map((host) => {
    const t = {
      host,
      mode: host.dataset.twin,
      frame: null,
      ready: false,
      queue: [],
      last: {},          // last message per kind, replayed after a reload (e.g. the current scenario)
      visible: false,
      send(msg) {
        if (msg.cx === 'scenario' || msg.cx === 'ask') t.last[msg.cx] = msg;
        if (t.ready) t.frame.contentWindow.postMessage(msg, '*'); else t.queue.push(msg);
      },
    };

    t.load = () => {
      if (t.frame) return;
      const f = document.createElement('iframe');
      f.className = 'twin-frame';
      f.title = host.dataset.twinTitle || 'ConnectX live digital twin of Meridian Tower';
      f.setAttribute('tabindex', '-1');
      // A sandboxed frame gets an opaque origin, so Chrome can run it in its own process:
      // the twin's 3D work then never blocks the page's thread. postMessage still works.
      f.setAttribute('sandbox', 'allow-scripts');
      const page = twinHtml().replace('<head>', `<head><script>window.CX_EMBED = { mode: '${t.mode}' };<\/script>`);
      f.src = URL.createObjectURL(new Blob([page], { type: 'text/html' }));
      host.appendChild(f);
      t.frame = f;
    };

    t.unload = () => {
      if (!t.frame) return;
      URL.revokeObjectURL(t.frame.src);
      t.frame.remove();
      t.frame = null; t.ready = false; t.queue = [];
      host.classList.remove('is-live');
    };

    t.onMessage = (m) => {
      if (m.cx === 'ready') {
        t.ready = true;
        const pending = t.queue.splice(0);
        // after a reload, restore what the page last asked for
        Object.values(t.last).forEach((msg) => { if (!pending.includes(msg)) pending.push(msg); });
        pending.forEach((msg) => t.frame.contentWindow.postMessage(msg, '*'));
        if (!t.visible) t.frame.contentWindow.postMessage({ cx: 'pause' }, '*');
      }
      if (m.cx === 'frame') host.classList.add('is-live');
      if (m.cx === 'wheel') pageWheel(m);
      if (m.cx === 'scenario') host.dataset.scenario = m.id || '';
    };

    /* Load about a screen early; unload when more than about three screens away */
    new IntersectionObserver(([e]) => { if (e.isIntersecting) t.load(); }, { rootMargin: '100% 0px' }).observe(host);
    new IntersectionObserver(([e]) => { if (!e.isIntersecting) t.unload(); }, { rootMargin: '300% 0px' }).observe(host);
    /* Draw only while on screen */
    new IntersectionObserver(([e]) => {
      t.visible = e.isIntersecting;
      if (t.ready) t.frame.contentWindow.postMessage({ cx: t.visible ? 'resume' : 'pause' }, '*');
    }).observe(host);
    return t;
  });

  window.addEventListener('message', (e) => {
    const t = twins.find((x) => x.frame && e.source === x.frame.contentWindow);
    if (t) t.onMessage(e.data || {});
  });

  /* Peak-price block: ask the question once it is properly in view; Replay asks again */
  const askTwin = twins.find((t) => t.mode === 'ask');
  if (askTwin) {
    const Q = { cx: 'ask', q: 'The price peaks at 17:00. What should we do?' };
    let asked = false;
    new IntersectionObserver(([e]) => {
      if (e.intersectionRatio >= 0.5 && !asked) { asked = true; askTwin.send(Q); }
    }, { threshold: [0, 0.5] }).observe(askTwin.host);
    const replay = document.querySelector('[data-ask-replay]');
    if (replay) replay.addEventListener('click', () => askTwin.send(Q));
  }

  /* Other scripts drive a twin by mode: window.cxTwin('scenario').send({ cx: 'scenario', id: 'anomaly' }) */
  window.cxTwin = (mode) => twins.find((t) => t.mode === mode);
})();
