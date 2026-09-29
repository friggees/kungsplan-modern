import { useEffect } from 'react';

/** Animate each group once; content stays visible if motion or browser support is absent. */
export function useScrollReveal() {
  useEffect(() => {
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (!('IntersectionObserver' in window)) return;
    const elements = Array.from(document.querySelectorAll<HTMLElement>(
      '.section-heading, .course-card, .intro-grid > div, .package, .about-grid > *, .reviews > .eyebrow, .reviews > h2, .review, .gallery-card, .gallery-bottom, .faq-grid > *, .cta'
    ));
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove('reveal-pending');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -24px 0px' });
    const clear = () => {
      observer.disconnect();
      elements.forEach(element => element.classList.remove('reveal-pending', 'scroll-reveal'));
    };
    const setup = () => {
      clear();
      if (preference.matches) return;
      elements.forEach(element => {
        element.classList.add('scroll-reveal');
        const siblings = Array.from(element.parentElement?.children ?? []);
        element.style.setProperty('--reveal-delay', `${Math.min(siblings.indexOf(element) % 4, 3) * 55}ms`);
        if (element.getBoundingClientRect().top >= window.innerHeight) {
          element.classList.add('reveal-pending');
          observer.observe(element);
        }
      });
    };
    setup();
    preference.addEventListener('change', setup);
    return () => { clear(); preference.removeEventListener('change', setup); };
  }, []);
}
