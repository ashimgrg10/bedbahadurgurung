/**
 * Countdown timer for "Member of Gandaki Province Assembly" term.
 *
 * Reads the target end date from the #term-countdown element's
 * data-end-date attribute (an ISO date string rendered by Django from
 * the view's context), so the date only needs to be updated in
 * portfolio/views.py — not in this file.
 */
(function () {
  const countdownEl = document.getElementById('term-countdown');
  if (!countdownEl) return;

  const endDateStr = countdownEl.dataset.endDate;
  const endDate = new Date(endDateStr + 'T00:00:00');

  const yearsEl = document.getElementById('countdown-years');
  const monthsEl = document.getElementById('countdown-months');
  const daysEl = document.getElementById('countdown-days');

  function diffYMD(from, to) {
    if (to <= from) return { years: 0, months: 0, days: 0 };

    let years = to.getFullYear() - from.getFullYear();
    let months = to.getMonth() - from.getMonth();
    let days = to.getDate() - from.getDate();

    if (days < 0) {
      months -= 1;
      const prevMonth = new Date(to.getFullYear(), to.getMonth(), 0);
      days += prevMonth.getDate();
    }
    if (months < 0) {
      years -= 1;
      months += 12;
    }
    return { years, months, days };
  }

  function update() {
    const now = new Date();
    const { years, months, days } = diffYMD(now, endDate);

    if (yearsEl) yearsEl.textContent = String(years).padStart(2, '0');
    if (monthsEl) monthsEl.textContent = String(months).padStart(2, '0');
    if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
  }

  update();
  // Once a day is sufficient, but an hourly tick keeps things correct
  // even if the tab is left open across a day boundary.
  setInterval(update, 1000 * 60 * 60);
})();
