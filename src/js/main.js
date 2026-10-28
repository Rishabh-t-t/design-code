/* ConnectX case study — Phase 1 behaviour (no motion yet). */
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
  function showQuote(i) {
    q = (i + quotes.length) % quotes.length;
    quotes.forEach((el, n) => { el.hidden = n !== q; el.classList.toggle('is-active', n === q); });
    quoteIndex.textContent = String(q + 1);
  }
  document.querySelector('[data-quotes-prev]').addEventListener('click', () => showQuote(q - 1));
  document.querySelector('[data-quotes-next]').addEventListener('click', () => showQuote(q + 1));

  /* Scenario areas: static selection until the pinned scene arrives in Phase 2 */
  const areas = [...document.querySelectorAll('.areas__item')];
  const areaIndex = document.querySelector('.areas__progress span');
  areas.forEach((el, n) => el.addEventListener('click', () => {
    areas.forEach((a) => a.classList.toggle('is-active', a === el));
    areaIndex.textContent = String(n + 1);
  }));

  /* Enquiry form: stub submit (IMP-06), keeps the entered data */
  const form = document.querySelector('[data-enquiry]');
  form.referrer.value = document.referrer;
  form.campaign.value = new URLSearchParams(location.search).get('utm_campaign') || '';
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    form.querySelector('.enquiry__success').hidden = false;
    form.querySelector('button[type="submit"]').disabled = true;
  });

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
})();
