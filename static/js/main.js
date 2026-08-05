/**
 * Site-wide interactions: sticky navbar scroll state, fade-in-on-scroll
 * reveal animations, and the back-to-top button.
 */
document.addEventListener('DOMContentLoaded', function () {
  // --- Sticky navbar shrink-on-scroll -------------------------------
  const navbar = document.getElementById('mainNavbar');
  function handleNavScroll() {
    if (!navbar) return;
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
  handleNavScroll();
  window.addEventListener('scroll', handleNavScroll, { passive: true });

  // --- Collapse mobile menu after a link is tapped -------------------
  const navCollapseEl = document.getElementById('navbarContent');
  if (navCollapseEl) {
    navCollapseEl.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.bootstrap && navCollapseEl.classList.contains('show')) {
          bootstrap.Collapse.getOrCreateInstance(navCollapseEl).hide();
        }
      });
    });
  }

  // --- Fade-in-up reveal on scroll ------------------------------------
  const revealEls = document.querySelectorAll('.fade-in-up');
  if ('IntersectionObserver' in window && revealEls.length) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // --- Back to top button ---------------------------------------------
  const backToTopBtn = document.getElementById('backToTop');
  if (backToTopBtn) {
    window.addEventListener(
      'scroll',
      function () {
        backToTopBtn.classList.toggle('show', window.scrollY > 500);
      },
      { passive: true }
    );
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- Journey portrait slider --------------------------------------
  // The slider is intentionally self-contained so the Journey section can
  // stay reusable and easy to maintain without affecting other pages.
  const journeySliders = document.querySelectorAll('[data-journey-slider]');
  const reduceMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

  journeySliders.forEach(function (slider) {
    const slides = Array.from(slider.querySelectorAll('.journey-slide'));
    const dots = Array.from(slider.querySelectorAll('.journey-dot'));
    const prevBtn = slider.querySelector('.journey-slider-btn.prev');
    const nextBtn = slider.querySelector('.journey-slider-btn.next');

    if (!slides.length) return;

    let activeIndex = 0;
    let autoplayTimer = null;

    function setActiveSlide(index) {
      const nextIndex = (index + slides.length) % slides.length;
      if (nextIndex === activeIndex) return;

      const currentSlide = slides[activeIndex];
      const nextSlide = slides[nextIndex];

      if (!currentSlide || !nextSlide) return;

      slides.forEach(function (slide) {
        slide.classList.remove('is-active');
        slide.classList.remove('is-leaving');
        slide.setAttribute('aria-hidden', 'true');
      });

      currentSlide.classList.add('is-leaving');
      currentSlide.style.visibility = 'visible';
      currentSlide.setAttribute('aria-hidden', 'false');

      window.requestAnimationFrame(function () {
        nextSlide.classList.add('is-active');
        nextSlide.style.visibility = 'visible';
        nextSlide.setAttribute('aria-hidden', 'false');
      });

      dots.forEach(function (dot, dotIndex) {
        const isActive = dotIndex === nextIndex;
        dot.classList.toggle('is-active', isActive);
        dot.setAttribute('aria-pressed', String(isActive));
      });

      window.setTimeout(function () {
        currentSlide.classList.remove('is-leaving');
      }, 900);

      activeIndex = nextIndex;
    }

    function stopAutoplay() {
      if (autoplayTimer) {
        window.clearInterval(autoplayTimer);
        autoplayTimer = null;
      }
    }

    function startAutoplay() {
      if (reduceMotionQuery.matches || slides.length < 2) return;
      stopAutoplay();
      autoplayTimer = window.setInterval(function () {
        setActiveSlide(activeIndex + 1);
      }, 4000);
    }

    function goToNext() {
      setActiveSlide(activeIndex + 1);
    }

    function goToPrev() {
      setActiveSlide(activeIndex - 1);
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        goToPrev();
        startAutoplay();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        goToNext();
        startAutoplay();
      });
    }

    dots.forEach(function (dot) {
      dot.addEventListener('click', function () {
        const targetIndex = parseInt(dot.getAttribute('data-slide-index'), 10);
        setActiveSlide(targetIndex);
        startAutoplay();
      });
    });

    slider.addEventListener('mouseenter', stopAutoplay);
    slider.addEventListener('mouseleave', startAutoplay);
    slider.addEventListener('focusin', stopAutoplay);
    slider.addEventListener('focusout', startAutoplay);
    slider.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight') {
        event.preventDefault();
        goToNext();
      } else if (event.key === 'ArrowLeft') {
        event.preventDefault();
        goToPrev();
      } else if (event.key === 'Home') {
        event.preventDefault();
        setActiveSlide(0);
      } else if (event.key === 'End') {
        event.preventDefault();
        setActiveSlide(slides.length - 1);
      }
    });

    setActiveSlide(0);
    if (!reduceMotionQuery.matches) {
      startAutoplay();
    }
  });

  // --- Contact form: front-end only, no backend processing ------------
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const feedback = document.getElementById('contactFormFeedback');
      if (feedback) {
        feedback.classList.remove('d-none');
        feedback.textContent = 'This form is a frontend placeholder — message sending is not yet connected.';
      }
    });
  }
});
