!function(){class e{constructor(){this.initSettings(),this.initElements(),this.bindEvents()}initSettings(){this.settings={selectors:{menuToggle:".site-header .site-navigation-toggle",menuToggleHolder:".site-header .site-navigation-toggle-holder",dropdownMenu:".site-header .site-navigation-dropdown"}}}initElements(){this.elements={window:window,menuToggle:document.querySelector(this.settings.selectors.menuToggle),menuToggleHolder:document.querySelector(this.settings.selectors.menuToggleHolder),dropdownMenu:document.querySelector(this.settings.selectors.dropdownMenu)}}bindEvents(){this.elements.menuToggleHolder&&!this.elements.menuToggleHolder?.classList.contains("hide")&&(this.elements.menuToggle.addEventListener("click",()=>this.handleMenuToggle()),this.elements.dropdownMenu.querySelectorAll(".menu-item-has-children > a").forEach(e=>e.addEventListener("click",e=>this.handleMenuChildren(e))))}closeMenuItems(){this.elements.menuToggleHolder.classList.remove("elementor-active"),this.elements.window.removeEventListener("resize",()=>this.closeMenuItems())}handleMenuToggle(){const e=!this.elements.menuToggleHolder.classList.contains("elementor-active");this.elements.menuToggle.setAttribute("aria-expanded",e),this.elements.dropdownMenu.setAttribute("aria-hidden",!e),this.elements.dropdownMenu.inert=!e,this.elements.menuToggleHolder.classList.toggle("elementor-active",e),this.elements.dropdownMenu.querySelectorAll(".elementor-active").forEach(e=>e.classList.remove("elementor-active")),e?this.elements.window.addEventListener("resize",()=>this.closeMenuItems()):this.elements.window.removeEventListener("resize",()=>this.closeMenuItems())}handleMenuChildren(e){const t=e.currentTarget.parentElement;t?.classList&&t.classList.toggle("elementor-active")}}document.addEventListener("DOMContentLoaded",()=>{new e})}();

/**
 * AryPro Global One-Sided Curtain Text Reveal Engine
 * Smoothly unrolls/wipes text across the entire website from one side (LTR or RTL)
 */
(function() {
  function initAryProCurtainReveal() {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

    var textSelectors = [
      '.elementor-heading-title',
      'h1:not(.screen-reader-text)',
      'h2',
      'h3',
      'h4',
      '.elementor-text-editor > p',
      '.elementor-testimonial-content',
      '.arypro-faq-title',
      '.arypro-faq-subtitle',
      '.arypro-faq-q-text',
      '.beliefs-ed-heading',
      '.beliefs-ed-desc',
      '.belief-category-tag',
      '.arypro-section-kicker'
    ].join(', ');

    var textElements = document.querySelectorAll(textSelectors);
    if (!textElements.length) return;

    var count = 0;
    textElements.forEach(function(el) {
      // Exclude navigation menus, skip links, buttons, and form inputs
      if (el.closest('.elementor-nav-menu') || 
          el.closest('.elementor-button') || 
          el.closest('.skip-link') || 
          el.closest('.elementor-menu-toggle') ||
          el.closest('.arypro-floating-whatsapp') ||
          el.closest('form')) {
        return;
      }

      if (!el.classList.contains('arypro-curtain-ltr') && !el.classList.contains('arypro-curtain-rtl')) {
        // Alternating logic: Check column placement or index to decide one-sided wipe direction
        var column = el.closest('.elementor-column') || el.closest('.beliefs-ed-row') || el.closest('.arypro-faq-card');
        var isRtl = false;

        if (column && column.parentElement) {
          var siblings = Array.from(column.parentElement.children);
          var colIdx = siblings.indexOf(column);
          if (colIdx % 2 === 1) isRtl = true;
        } else {
          if (count % 2 === 1) isRtl = true;
        }

        if (isRtl) {
          el.classList.add('arypro-curtain-rtl');
        } else {
          el.classList.add('arypro-curtain-ltr');
        }

        // Add subtle staggered delay for siblings
        if (el.nextElementSibling && (el.nextElementSibling.matches('p') || el.nextElementSibling.matches('h3') || el.nextElementSibling.matches('h4'))) {
          el.nextElementSibling.classList.add('arypro-curtain-delay-1');
        }

        count++;
      }
    });

    // IntersectionObserver for sleek scroll-triggered curtain unmasking
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-curtain-visible');
          } else {
            var rect = entry.target.getBoundingClientRect();
            if (rect.top > (window.innerHeight || document.documentElement.clientHeight)) {
              entry.target.classList.remove('is-curtain-visible');
            }
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -25px 0px'
      });

      document.querySelectorAll('.arypro-curtain-ltr, .arypro-curtain-rtl').forEach(function(el) {
        observer.observe(el);
      });
    } else {
      // Fallback
      document.querySelectorAll('.arypro-curtain-ltr, .arypro-curtain-rtl').forEach(function(el) {
        el.classList.add('is-curtain-visible');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAryProCurtainReveal);
  } else {
    initAryProCurtainReveal();
  }
})();