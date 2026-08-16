(function () {
  'use strict';

  var root = document.documentElement;

  if (!('IntersectionObserver' in window)) {
    root.classList.remove('js');
    return;
  }

  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  if (revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08 }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  }

  var yearEls = document.querySelectorAll('[data-year]');
  if (yearEls.length) {
    var year = String(new Date().getFullYear());
    yearEls.forEach(function (el) {
      el.textContent = year;
    });
  }
})();
