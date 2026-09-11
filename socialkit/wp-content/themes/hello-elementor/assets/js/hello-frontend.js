/**
 * AryPro Brands Solutions Frontend Script
 */
!function(){class e{constructor(){this.initSettings(),this.initElements(),this.bindEvents()}initSettings(){this.settings={selectors:{menuToggle:".site-header .site-navigation-toggle",menuToggleHolder:".site-header .site-navigation-toggle-holder",dropdownMenu:".site-header .site-navigation-dropdown"}}}initElements(){this.elements={window:window,menuToggle:document.querySelector(this.settings.selectors.menuToggle),menuToggleHolder:document.querySelector(this.settings.selectors.menuToggleHolder),dropdownMenu:document.querySelector(this.settings.selectors.dropdownMenu)}}bindEvents(){this.elements.menuToggleHolder&&!this.elements.menuToggleHolder?.classList.contains("hide")&&(this.elements.menuToggle.addEventListener("click",()=>this.handleMenuToggle()),this.elements.dropdownMenu.querySelectorAll(".menu-item-has-children > a").forEach(e=>e.addEventListener("click",e=>this.handleMenuChildren(e))))}closeMenuItems(){this.elements.menuToggleHolder.classList.remove("elementor-active"),this.elements.window.removeEventListener("resize",()=>this.closeMenuItems())}handleMenuToggle(){const e=!this.elements.menuToggleHolder.classList.contains("elementor-active");this.elements.menuToggle.setAttribute("aria-expanded",e),this.elements.dropdownMenu.setAttribute("aria-hidden",!e),this.elements.dropdownMenu.inert=!e,this.elements.menuToggleHolder.classList.toggle("elementor-active",e),this.elements.dropdownMenu.querySelectorAll(".elementor-active").forEach(e=>e.classList.remove("elementor-active")),e?this.elements.window.addEventListener("resize",()=>this.closeMenuItems()):this.elements.window.removeEventListener("resize",()=>this.closeMenuItems())}handleMenuChildren(e){const t=e.currentTarget.parentElement;t?.classList&&t.classList.toggle("elementor-active")}}document.addEventListener("DOMContentLoaded",()=>{new e})}();

// Elementor Breakpoint & Nav-Menu Error Safeguard
(function() {
  function safeguardBreakpoints() {
    try {
      if (typeof window !== 'undefined' && window.elementorFrontend && window.elementorFrontend.config && window.elementorFrontend.config.responsive) {
        var resp = window.elementorFrontend.config.responsive;
        var defaultBreakpoints = {
          mobile: { value: 767, label: "Mobile Portrait", is_enabled: true, direction: "max" },
          mobile_extra: { value: 880, label: "Mobile Landscape", is_enabled: true, direction: "max" },
          tablet: { value: 1024, label: "Tablet Portrait", is_enabled: true, direction: "max" },
          tablet_extra: { value: 1200, label: "Tablet Landscape", is_enabled: true, direction: "max" },
          laptop: { value: 1366, label: "Laptop", is_enabled: true, direction: "max" },
          desktop: { value: 1440, label: "Desktop", is_enabled: true, direction: "max" },
          widescreen: { value: 2400, label: "Widescreen", is_enabled: true, direction: "min" },
          none: { value: 0, label: "None", is_enabled: true, direction: "max" }
        };
        if (!resp.activeBreakpoints || typeof resp.activeBreakpoints !== 'object') {
          resp.activeBreakpoints = {};
        }
        Object.keys(defaultBreakpoints).forEach(function(k) {
          if (!resp.activeBreakpoints[k]) {
            resp.activeBreakpoints[k] = defaultBreakpoints[k];
          }
        });
        if (typeof Proxy !== 'undefined' && !resp.activeBreakpoints.__isProxied) {
          resp.activeBreakpoints = new Proxy(resp.activeBreakpoints, {
            get: function(target, prop) {
              if (prop === '__isProxied') return true;
              if (prop in target && target[prop] !== undefined) return target[prop];
              return { value: 1024, label: String(prop), is_enabled: true };
            }
          });
        }
      }
    } catch(e) {}
  }

  window.addEventListener('elementor/frontend/init', safeguardBreakpoints, { capture: true });
  document.addEventListener('DOMContentLoaded', safeguardBreakpoints);
  safeguardBreakpoints();
})();

// Ensure all text elements are immediately and fully visible across all browsers
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll('.elementor-invisible, .arypro-curtain-ltr, .arypro-curtain-rtl').forEach(function(el) {
    el.classList.remove('elementor-invisible');
    el.style.opacity = '1';
    el.style.visibility = 'visible';
  });
});