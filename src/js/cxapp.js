/* ConnectX product, Iteration 4 (ported from the ConnectX Story Canvas: I4App + Proto4).
   One component, three places on the page:
     [data-cx="hero"]      the building assembles frame by frame, the dashboard builds around it,
                           then it is live: pick a tile or ask, it scans the building and answers in place.
     [data-cx="scenario"]  driven by the scenario list: each area scans, then answers on the building.
     [data-cx="peak"]      the peak-price question end to end (home → typing → scan → answer), with replay.
   The building is the pre-rendered white model (assets/i4/frames), the scan uses visible-surface masks
   (assets/i4/scan). All sizes are in cqi of the stage, so the whole product scales as one picture. */
(function () {
  const BASE = 'assets/i4/';
  const FRAMES = Array.from({ length: 28 }, (_, i) => `${BASE}frames/f${String(i).padStart(2, '0')}.webp`);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // answer pins sit on the raw render; the asked view moves the building 6cqi right, 3.4cqi down, ×1.06 about (53.92, 32)
  const BX = 6, BY = 3.4, BS = 1.06;
  const P = (x, y, n, v) => ({ x: (53.92 + (x - 53.92) * BS + BX).toFixed(2) + 'cqi', y: (32 + (y - 32) * BS + BY).toFixed(2) + 'cqi', n, v });
  const ANS = {
    f6: { tag: 'ANOMALY · FLOOR 6', big: '+18%', col: '#D84A3B', text: 'Floor 6 has used 18% more cooling than planned for four days. Its west glass takes full sun from 14:00.', act: 'Pre-cool at 11:00', pin: P(50.5, 20.8, 'Floor 6', '+18%'), card: { t: 'Cooling · floor 6', s: 'Against the plan', a: '16', au: 'kW', b: '+18', bu: '%' } },
    tariff: { tag: 'PEAK PRICE', big: '17:00', col: '#4A6FE3', text: 'Peak pricing starts at 17:00. Running on the battery until 20:00 avoids the highest rate.', act: 'Plan discharge', pin: P(45.6, 41.4, 'Main supply', '17:00'), card: { t: 'Today’s cost', s: 'So far today', a: '£1,284', au: 'today', b: '17:00', bu: 'peak' } },
    ev: { tag: 'EV CHARGING', big: '2 / 4', col: '#0F9160', text: 'Two chargers are drawing into the evening peak. Moving them to 21:00 gives the same range.', act: 'Reschedule', pin: P(31.4, 31.6, 'EV chargers', '2/4'), card: { t: 'EV charging', s: 'Carport, right now', a: '2/4', au: 'in use', b: '21:00', bu: 'best start' } },
    solar: { tag: 'SOLAR', big: '245 kW', col: '#0F9160', text: 'Roof and carport solar covered 81% of today’s midday load.', act: 'See the day', pin: P(48.6, 10.6, 'Roof solar', '245 kW'), card: { t: 'Solar', s: 'Roof and carport', a: '245', au: 'kW now', b: '81', bu: '% of midday' } },
  };
  const TILES = [
    { f: 'f6', n: 'Floor 6', s: 'Cooling 18% over', c: '#D84A3B', icon: 'M12 3l9 5-9 5-9-5zM3 13l9 5 9-5', q: 'Why is floor 6 using so much cooling?' },
    { f: 'tariff', n: 'Peak price', s: 'Starts at 17:00', c: '#4A6FE3', icon: 'M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18zM12 7v5l3 2', q: 'When does the peak price start?' },
    { f: 'ev', n: 'EV charging', s: '2 of 4 in use', c: '#0F9160', icon: 'M9 3v4M15 3v4M7 7h10v4a5 5 0 0 1-10 0zM12 16v5', q: 'Are the EV chargers adding to the peak?' },
    { f: 'solar', n: 'Solar', s: '245 kW right now', c: '#D9A23A', icon: 'M12 8a4 4 0 1 0 0 8a4 4 0 1 0 0-8zM12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4', q: 'How much did the solar cover today?' },
  ];
  const BRIEF = [
    { f: 'f6', tag: 'ANOMALY · FLOOR 6', col: '#D84A3B', t: 'Floor 6 is using 18% more cooling than planned.' },
    { f: 'tariff', tag: 'PEAK PRICE', col: '#4A6FE3', t: 'Peak pricing starts at 17:00. The battery can carry it.' },
    { f: 'ev', tag: 'EV CHARGING', col: '#0F9160', t: 'Two chargers will run into the evening peak.' },
  ];
  const focusOf = (q) => { const s = (q || '').toLowerCase(); if (/ev|charg/.test(s)) return 'ev'; if (/peak|price|tariff|cost/.test(s)) return 'tariff'; if (/solar|sun/.test(s)) return 'solar'; return 'f6'; };
  const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  const I = {
    back: '<path d="M19 12H5M11 6l-6 6 6 6"></path>',
    layers: '<path d="M12 3l9 5-9 5-9-5z"></path><path d="M3 13l9 5 9-5"></path>',
    bolt: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"></path>',
    battery: '<rect x="3" y="7" width="16" height="10" rx="2"></rect><path d="M21 10v4"></path><path d="M7 10v4M10 10v4"></path>',
    home: '<path d="M4 21V8l8-5 8 5v13"></path><path d="M9 21v-6h6v6"></path>',
    sun: '<circle cx="12" cy="12" r="3"></circle><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4L7 17M17 7l1.4-1.4"></path>',
    close: '<path d="M7 7l10 10M17 7L7 17"></path>',
    mic: '<rect x="9" y="3" width="6" height="12" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0M12 18v3"></path>',
    clip: '<path d="M20 12l-8 8a5 5 0 0 1-7-7l9-9a3.5 3.5 0 0 1 5 5l-9 9a2 2 0 0 1-3-3l8-8"></path>',
    cube: '<path d="M12 3l7.5 4.5v9L12 21l-7.5-4.5v-9z"></path><circle cx="12" cy="12" r="2.5"></circle>',
    report: '<rect x="4" y="5" width="16" height="14" rx="2.5"></rect><path d="M8 10h8M8 14h5"></path>',
    clock: '<circle cx="12" cy="12" r="8"></circle><path d="M12 8v4l3 2"></path>',
    expand: '<path d="M14 4h6v6M10 20H4v-6M20 4l-7 7M4 20l7-7"></path>',
    send: '<path d="M4 12l16-8-6 16-2-7z"></path>',
  };
  const svg = (k, stroke, w) => `<svg viewBox="0 0 24 24" fill="none" stroke="${stroke || '#0F1115'}" stroke-width="${w || 1.7}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${I[k]}</svg>`;
  const ib = (k, cls, label) => `<button type="button" class="ib4 ${cls || ''}" aria-label="${label}" tabindex="-1">${svg(k)}</button>`;

  function create(host) {
    const kind = host.dataset.cx;
    const S = { mode: kind === 'peak' ? 'home' : kind === 'scenario' ? 'answer' : 'dash', focus: kind === 'peak' ? 'tariff' : 'f6', q: '', fill: 1, ui: 1, idx: 27, scanDur: kind === 'hero' ? 6.4 : 4.2 };
    if (kind === 'scenario') S.q = TILES[0].q;
    let timer = 0, raf = 0;

    host.classList.add('cxv');
    host.innerHTML = `<div class="s4" role="img" aria-label="${esc(host.dataset.cxLabel || 'The ConnectX product: the building in the middle, the AI assistant on the right, live figures below.')}">
      <div class="s4__bld"></div>
      <div class="cx4"></div>
    </div>`;
    const stage = host.querySelector('.s4');
    const min = 'cxMin' in host.dataset;   // hero: only the title, the building and the assistant
    if (min) stage.classList.add('s4--min');
    const bld = host.querySelector('.s4__bld');
    const ui = host.querySelector('.cx4');
    const needed = kind === 'hero' ? FRAMES : [FRAMES[26], FRAMES[27]];
    bld.innerHTML = needed.map((src, i) => `<img src="${src}" alt="" decoding="async" ${kind === 'hero' && i > 0 && i < 26 ? 'loading="eager"' : ''} data-i="${kind === 'hero' ? i : 26 + i}">`).join('');
    const imgs = [...bld.querySelectorAll('img')];

    function setFrame(idx) {
      S.idx = idx;
      imgs.forEach((im) => { const i = +im.dataset.i; im.style.opacity = Math.max(0, 1 - Math.abs(idx - i)).toFixed(3); });
    }
    function placeBuilding() {
      const asked = S.mode === 'answer' || S.mode === 'loading';
      bld.style.opacity = S.mode === 'home' ? 0.28 : 1;
      bld.style.transform = asked ? `translate(${BX}cqi, ${BY}cqi) scale(${BS})` : min ? 'translate(-3cqi, 2.4cqi) scale(1.05)' : 'none';
      if (S.ui >= 1) setFrame(S.mode === 'answer' && S.focus === 'f6' ? 27 : 26);
    }

    function render() {
      const m = S.mode, product = m !== 'home', ans = ANS[S.focus];
      const loading = m === 'loading', answer = m === 'answer', home = m === 'home';
      const hasData = m === 'dash' || answer;
      const card = answer ? ans.card : ANS.tariff.card;
      const k = (n) => Math.round(n * S.fill);
      const scan = loading ? `<div class="scan5" aria-hidden="true" style="--scan:${S.scanDur}s">
          <i class="sg" style="-webkit-mask-image:url(${BASE}scan/ground.webp),radial-gradient(ellipse 72% 72% at 50% 69%,transparent var(--r),#000 calc(var(--r) + 8%));mask-image:url(${BASE}scan/ground.webp),radial-gradient(ellipse 72% 72% at 50% 69%,transparent var(--r),#000 calc(var(--r) + 8%))"></i>
          ${Array.from({ length: 10 }, (_, i) => `<i class="sf" style="-webkit-mask-image:url(${BASE}scan/f${i}.webp);mask-image:url(${BASE}scan/f${i}.webp);animation-name:p4-f${i}"></i>`).join('')}
        </div>` : '';
      const d = S.scanDur / 6.4;
      ui.innerHTML = `${scan}
      <div class="cx4__top">
        <span class="cx4__brand"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4 L11 12 L4 20 M20 4 L13 12 L20 20" stroke="#0F1115" stroke-width="2.6" stroke-linecap="round" fill="none"></path></svg><b>ConnectX</b></span>
        <span class="seg4"><span class="pill4 pill4--on">Twin</span><span class="pill4">Reports</span><span class="pill4">Alerts</span></span>
        <span class="cx4__tr"><span class="pill4 cx4__bpill">${svg('home', '#0F1115')}<span class="cx4__mute">Building:</span> Meridian Tower</span><span class="ib4">${svg('sun')}</span></span>
      </div>
      ${product ? `
      ${ib('back', 'cx4__back', 'Back to the dashboard')}
      <div class="cx4__lrail">${ib('layers', '', 'Floors')}${ib('bolt', '', 'Energy')}${ib('battery', '', 'Storage')}</div>
      <div class="cx4__title">
        <h3 class="h4">Meridian Tower</h3>
        <p class="sub4">Office building · 8 floors · 4,200 m²</p>
        <div class="tags4" aria-label="Floor"><span class="tag4">4</span><span class="tag4">5</span><span class="tag4 tag4--alert ${answer && S.focus === 'f6' ? 'tag4--on' : ''}">6</span><span class="tag4">7</span><span class="tag4">8</span><span class="tag4">R</span></div>
      </div>
      <div class="cx4__ai">
        <div class="c4 cx4__asst">
          <div class="cx4__ah"><span><b>AI Assistant</b><span class="lab4">${loading ? 'Looking at the building…' : answer ? esc(S.q || 'Here’s what I found') : 'How can I help you?'}</span></span><button type="button" class="ib4" data-act="close" aria-label="Close the answer">${svg('close', '#0F1115', 1.8)}</button></div>
          ${loading ? `<div class="cx4__steps">
            <span class="stp4" style="--d:0s;--e:${(1.6 * d).toFixed(2)}s"><i class="ring4"></i>Reading the plot and its supply</span>
            <span class="stp4" style="--d:${(1.6 * d).toFixed(2)}s;--e:${(5.4 * d).toFixed(2)}s"><i class="ring4"></i>Scanning the building, floor by floor</span>
            <span class="stp4" style="--d:${(5.4 * d).toFixed(2)}s;--e:${(6.2 * d).toFixed(2)}s"><i class="ring4"></i>Writing the answer</span>
          </div>` : answer ? `<div class="cx4__ans">
            <span class="cx4__tag" style="color:${ans.col}">${ans.tag}</span>
            <span class="num4 cx4__big" style="color:${ans.col}">${ans.big}</span>
            <span class="cx4__txt">${ans.text}</span>
            <div class="cx4__btns"><button type="button" class="send4">${ans.act}</button><button type="button" class="ghost4">Show the data</button></div>
          </div>` : `<div class="cx4__tiles">${TILES.map((t) => `<button type="button" class="t4 cx4__tile" data-pick="${t.f}"><span class="cx4__ti"><svg viewBox="0 0 24 24" fill="none" stroke="#0F1115" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${t.icon}"></path></svg><i style="background:${t.c}"></i></span><span><b>${t.n}</b><span class="lab4">${t.s}</span></span></button>`).join('')}</div>`}
        </div>
        <div class="c4 cx4__in">
          <label class="cx4__sr" for="cx-q-${kind}">Ask about the building</label>
          <input id="cx-q-${kind}" class="cx4__input" value="${esc(S.q)}" placeholder="Ask anything about the building…" autocomplete="off">
          <div class="cx4__inrow">${ib('mic', '', 'Voice')}${ib('clip', '', 'Attach')}${ib('cube', '', 'Twin view')}<button type="button" class="send4 cx4__send" data-act="send">Send ${svg('send', '#FFFFFF', 2)}</button></div>
        </div>
      </div>
      <div class="cx4__rrail">${ib('bolt', 'ib4--on', 'Energy')}${ib('report', '', 'Reports')}${ib('clock', '', 'History')}</div>
      <div class="cx4__cards">
        <div class="c4 cx4__card"><div class="cx4__ch"><span><b>Live load</b><span class="lab4">Whole building, right now</span></span>${ib('expand', 'cx4__ex', 'Expand')}</div>
          ${hasData ? `<span class="num4 cx4__n1" data-n="318">${k(318)}<small> kW</small></span>` : '<i class="shim4" style="height:2.8cqi;width:55%"></i>'}</div>
        <div class="c4 cx4__card"><div class="cx4__ch"><span><b>${card.t}</b><span class="lab4">${card.s}</span></span>${ib('expand', 'cx4__ex', 'Expand')}</div>
          ${hasData ? `<div class="cx4__row"><span class="t4 cx4__pillnum"><span class="num4">${answer ? card.a : '£' + k(1284).toLocaleString('en-GB')}</span><span class="lab4">${card.au}</span></span><span class="num4 cx4__n2">${card.b}<small> ${card.bu}</small></span></div>` : '<i class="shim4" style="height:2.8cqi;width:70%"></i>'}</div>
        <div class="c4 cx4__card"><div class="cx4__ch"><span><b>Battery</b><span class="lab4">Basement storage</span></span>${ib('expand', 'cx4__ex', 'Expand')}</div>
          ${hasData ? `<div class="t4 cx4__bat"><span><b>${k(78)}% charged</b><span class="lab4">Enough for tonight’s peak</span></span><span class="cx4__ok"><i></i></span></div>` : '<i class="shim4" style="height:2.8cqi;width:80%"></i>'}</div>
      </div>` : ''}
      ${home ? `<div class="cx4__home">
        <div class="cx4__hh"><span class="lab4"><span class="dot4"></span>Meridian Tower · live</span>
          <h3 class="h4">Everything’s running normally.<br><span>One thing needs a look today.</span></h3></div>
        <div class="c4 cx4__hbox">
          <div class="cx4__hrow"><label class="cx4__sr" for="cx-h-${kind}">Ask about the building</label><input id="cx-h-${kind}" class="cx4__input cx4__hin" value="${esc(S.q)}" placeholder="Ask anything about the building…" autocomplete="off"><button type="button" class="send4" data-act="send">Send ${svg('send', '#FFFFFF', 2)}</button></div>
          <div class="cx4__chips">${TILES.map((t) => `<button type="button" class="chip4" data-pick="${t.f}">#${t.n.replace(/\s+/g, '')}</button>`).join('')}</div>
        </div>
        <div class="cx4__brief">${BRIEF.map((b) => `<button type="button" class="c4 cx4__bc" data-pick="${b.f}"><span style="color:${b.col}">${b.tag}</span><span>${b.t}</span></button>`).join('')}</div>
        <span class="lab4">Modelled from the last 90 days of meter data</span>
      </div>` : ''}
      ${answer ? `<span class="pin4" style="left:${ans.pin.x};top:${ans.pin.y}"><i></i>${ans.pin.n} <em>${ans.pin.v}</em></span>` : ''}`;
      stage.dataset.mode = m;
      placeBuilding();
      applyAssembly();
    }

    /* the build-up: UI groups fade in by progress (top bar, then assistant, then cards) */
    function applyAssembly() {
      const sm = (x) => { x = Math.max(0, Math.min(1, x)); return x * x * (3 - 2 * x); };
      const a1 = sm(S.ui / 0.35), a2 = sm((S.ui - 0.2) / 0.4), a3 = sm((S.ui - 0.45) / 0.45);
      stage.style.setProperty('--a1', a1.toFixed(3)); stage.style.setProperty('--a2', a2.toFixed(3)); stage.style.setProperty('--a3', a3.toFixed(3));
    }

    function ask(f, q) {
      clearTimeout(timer);
      S.focus = f || focusOf(q); S.q = q || TILES.find((t) => t.f === S.focus).q;
      S.mode = 'loading'; render();
      timer = setTimeout(() => { S.mode = 'answer'; render(); }, (reduce ? 0.3 : S.scanDur) * 1000);
    }
    function dash() { clearTimeout(timer); S.mode = kind === 'peak' ? 'home' : 'dash'; S.q = ''; render(); }

    /* typing a question into the home box, one character at a time */
    function typeInto(text, done) {
      let n = 0;
      const step = () => {
        S.q = text.slice(0, n);
        const el = ui.querySelector('.cx4__hin') || ui.querySelector('.cx4__input');
        if (el) el.value = S.q;
        if (n++ < text.length) timer = setTimeout(step, 38 + Math.random() * 40); else timer = setTimeout(done, 450);
      };
      step();
    }

    /* events */
    ui.addEventListener('click', (e) => {
      const pick = e.target.closest('[data-pick]');
      if (pick) { const t = TILES.find((x) => x.f === pick.dataset.pick); ask(t.f, t.q); return; }
      const act = e.target.closest('[data-act]');
      if (act && act.dataset.act === 'send') { const q = (ui.querySelector('.cx4__hin') || ui.querySelector('.cx4__input') || {}).value || ''; ask(null, q || TILES[0].q); return; }
      if ((act && act.dataset.act === 'close') || e.target.closest('.cx4__back')) dash();
    });
    ui.addEventListener('input', (e) => { if (e.target.classList.contains('cx4__input')) S.q = e.target.value; });
    ui.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.classList.contains('cx4__input')) { e.preventDefault(); ask(null, e.target.value || TILES[0].q); } });

    /* fit: below 900px the stage renders at 1280px and scales down, so the product keeps its proportions */
    const fit = () => {
      const w = host.clientWidth;
      if (w && w < 900) { stage.style.width = '1280px'; stage.style.transform = `scale(${w / 1280})`; host.style.height = (w / 1.6) + 'px'; }
      else { stage.style.width = ''; stage.style.transform = ''; host.style.height = ''; }
    };
    if (window.ResizeObserver) new ResizeObserver(fit).observe(host);
    fit();

    const api = {
      kind, ask, dash, render,
      setFocus(f) { if (S.focus === f && S.mode === 'answer') return; ask(f, TILES.find((t) => t.f === f).q); },
      /* hero: the building assembles (plan → skeleton → walls → facade), then the dashboard builds around it */
      build() {
        if (reduce) { S.ui = 1; S.fill = 1; S.mode = 'dash'; render(); return; }
        S.ui = 0; S.fill = 0; S.mode = 'dash'; render(); setFrame(0);
        const t0 = performance.now(), T1 = 3600, T2 = 1500;
        const tick = (t) => {
          const e = t - t0;
          const p = Math.min(1, e / T1);
          setFrame(26 * (1 - Math.pow(1 - p, 1.6)));
          S.ui = Math.max(0, Math.min(1, (e - T1 * 0.55) / (T1 * 0.45 + T2)));
          applyAssembly();
          const f = Math.max(0, Math.min(1, (e - T1) / T2));
          if (Math.abs(f - S.fill) > 0.02 || f === 1) {
            S.fill = f;
            const n1 = ui.querySelector('.cx4__n1'); if (n1) n1.firstChild.nodeValue = String(Math.round(318 * f));
          }
          if (e < T1 + T2) raf = requestAnimationFrame(tick); else { S.ui = 1; S.fill = 1; render(); }
        };
        raf = requestAnimationFrame(tick);
      },
      /* peak: the full ask, played once in view and again on replay */
      play() {
        clearTimeout(timer); cancelAnimationFrame(raf);
        S.mode = 'home'; S.q = ''; S.focus = 'tariff'; render();
        if (reduce) { S.q = TILES[1].q; S.mode = 'answer'; render(); return; }
        timer = setTimeout(() => typeInto(TILES[1].q, () => ask('tariff', TILES[1].q)), 700);
      },
    };
    render();
    return api;
  }

  const apps = {};
  document.querySelectorAll('[data-cx]').forEach((el) => { apps[el.dataset.cx] = create(el); });
  window.cxApp = (k) => apps[k];

  /* hero builds once it is first seen; peak plays the first time it scrolls into view */
  const once = (el, fn, threshold) => {
    if (!el) return;
    if (!window.IntersectionObserver) { fn(); return; }
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { io.disconnect(); fn(); } }, { threshold });
    io.observe(el);
  };
  if (apps.hero) once(document.querySelector('[data-cx="hero"]'), () => apps.hero.build(), 0.2);
  if (apps.peak) once(document.querySelector('[data-cx="peak"]'), () => apps.peak.play(), 0.45);
  document.querySelectorAll('[data-ask-replay]').forEach((b) => b.addEventListener('click', () => apps.peak && apps.peak.play()));
})();
