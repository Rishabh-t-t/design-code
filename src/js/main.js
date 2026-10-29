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

  /* Scenario areas: one setter shared by the click fallback and the sticky scene (scenes.js).
     Each area plays its scenario on the live twin next to the list. */
  const areas = [...document.querySelectorAll('.areas__item')];
  const areaIndex = document.querySelector('.areas__progress span');
  const AREA_SCENARIO = ['anomaly', 'clouds', 'ev', 'outage'];  // status · forecasting · asset performance · operating conditions
  function setArea(n) {
    areas.forEach((a, m) => a.classList.toggle('is-active', m === n));
    areaIndex.textContent = String(n + 1);
    const twin = window.cxTwin && window.cxTwin('scenario');
    if (twin) twin.send({ cx: 'scenario', id: AREA_SCENARIO[n] });
  }
  window.cxSetArea = setArea;
  areas.forEach((el, n) => el.addEventListener('click', () => setArea(n)));
  document.addEventListener('DOMContentLoaded', () => setArea(0));

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
