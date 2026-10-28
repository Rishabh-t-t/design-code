/* ConnectX case study — page behaviour that works with or without motion. */
(function () {
  const root = document.documentElement;

  /* Wireframe notes toggle: button or the N key */
  const notesBtn = document.querySelector('[data-notes-toggle]');
  function setNotes(on) {
    root.classList.toggle('notes-off', !on);
    notesBtn.setAttribute('aria-pressed', String(on));
    notesBtn.textContent = on ? 'Notes: on' : 'Notes: off';
  }
  notesBtn.addEventListener('click', () => setNotes(root.classList.contains('notes-off')));
  document.addEventListener('keydown', (e) => {
    if (e.key.toLowerCase() !== 'n' || /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) return;
    setNotes(root.classList.contains('notes-off'));
  });

  /* Testimonials: previous / next */
  const quotes = [...document.querySelectorAll('[data-quotes] .quote')];
  const quoteIndex = document.querySelector('[data-quotes-index]');
  let q = 0;
  function swapQuote() {
    quotes.forEach((el, n) => { el.hidden = n !== q; el.classList.toggle('is-active', n === q); });
    quoteIndex.textContent = String(q + 1);
  }
  function showQuote(i) {
    const prev = quotes[q];
    q = (i + quotes.length) % quotes.length;
    if (!root.classList.contains('motion')) { swapQuote(); return; }
    /* Crossfade: the old quote lifts away, the new one reveals line by line */
    gsap.killTweensOf(prev);
    gsap.to(prev, {
      opacity: 0, y: -16, duration: 0.35, ease: 'power2.in',
      onComplete() {
        gsap.set(prev, { clearProps: 'opacity,transform' });
        swapQuote();
        const p = quotes[q].querySelector('blockquote p');
        const split = SplitText.create(p, { type: 'lines', mask: 'lines', aria: 'none' });
        gsap.from(split.lines, { yPercent: 105, duration: 0.9, ease: 'expo.out', stagger: 0.06, onComplete: () => split.revert() });
        gsap.from(quotes[q].querySelector('.quote__by'), { opacity: 0, y: 12, duration: 0.6, delay: 0.25, ease: 'expo.out' });
      },
    });
  }
  document.querySelector('[data-quotes-prev]').addEventListener('click', () => showQuote(q - 1));
  document.querySelector('[data-quotes-next]').addEventListener('click', () => showQuote(q + 1));

  /* Scenario areas: one setter shared by the click fallback and the pinned scene (scenes.js).
     Each area also changes what the mini twin highlights. */
  const areas = [...document.querySelectorAll('.areas__item')];
  const areaIndex = document.querySelector('.areas__progress span');
  const areaStates = [...document.querySelectorAll('.areas__state')];
  const areaApp = document.querySelector('.areas__view .cx-app');
  const areaTwin = areaApp && areaApp.querySelector('.cx-twin');
  const AREA_TWIN = [
    { hot: 'hvac' },                      // System status: the exception
    { blue: 'solar' },                    // Forecasting: generation ahead
    { blue: 'battery', dim: true },       // Asset performance: one asset in focus
    {},                                   // Operational conditions: whole building, weather shown
  ];
  function setArea(n) {
    areas.forEach((a, m) => a.classList.toggle('is-active', m === n));
    areaStates.forEach((a, m) => a.classList.toggle('is-active', m === n));
    areaIndex.textContent = String(n + 1);
    if (!areaApp) return;
    areaApp.dataset.area = String(n);
    const t = AREA_TWIN[n] || {};
    ['hot', 'blue', 'dim'].forEach((k) => {
      if (t[k]) areaTwin.setAttribute('data-' + k, t[k] === true ? '' : t[k]);
      else areaTwin.removeAttribute('data-' + k);
    });
  }
  window.cxSetArea = setArea;
  setArea(0);
  areas.forEach((el, n) => el.addEventListener('click', () => setArea(n)));

  /* Enquiry form: stub submit (IMP-06), keeps the entered data */
  const form = document.querySelector('[data-enquiry]');
  form.referrer.value = document.referrer;
  form.campaign.value = new URLSearchParams(location.search).get('utm_campaign') || '';
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    const success = form.querySelector('.enquiry__success');
    const button = form.querySelector('button[type="submit"]');
    button.disabled = true;
    button.textContent = 'Sent';
    success.hidden = false;
    if (root.classList.contains('motion')) {
      gsap.from(success, { opacity: 0, y: 16, duration: 0.8, ease: 'expo.out' });
      ScrollTrigger.refresh();
    }
  });

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
})();
