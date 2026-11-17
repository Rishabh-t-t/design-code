/* ConnectX case study — page behaviour that works with or without motion. */
(function () {
  const root = document.documentElement;

  /* Wireframe notes are removed from the published page (html.notes-off keeps any leftovers hidden). */

  /* Scenario areas: one setter shared by the click fallback and the sticky scene (scenes.js).
     Each area plays its scenario on the live twin next to the list. */
  const areas = [...document.querySelectorAll('.areas__item')];
  const areaIndex = document.querySelector('.areas__progress span');
  const AREA_FOCUS = ['f6', 'tariff', 'solar', 'ev'];  // system status · forecasting · asset performance · operational conditions
  function setArea(n) {
    areas.forEach((a, m) => a.classList.toggle('is-active', m === n));
    areaIndex.textContent = String(n + 1);
    const app = window.cxApp && window.cxApp('scenario');
    if (app) app.setFocus(AREA_FOCUS[n]);
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

  /* Small screens: the app-style twins render at 960px and scale to fit their box (responsive.css) */
  const scaled = [...document.querySelectorAll('.areas__view.twin-host, .peak .twin-host')];
  const fitTwins = () => scaled.forEach((el) => el.style.setProperty('--tw-s', String(el.clientWidth / 960)));
  if (window.ResizeObserver) { const ro = new ResizeObserver(fitTwins); scaled.forEach((el) => ro.observe(el)); }
  fitTwins();

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
})();
