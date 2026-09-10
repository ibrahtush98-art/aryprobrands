import os
import re

css_file = r"c:\Users\Admin\Documents\website generator\New folder\templatekit.tokomoo.com\socialkit\wp-content\themes\hello-elementor\assets\css\promedia-theme.css"

with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Replace or update the Services section in promedia-theme.css
start_marker = "/* SERVICES PAGE (elementor-2087) MASTER OVERRIDE */"
idx = css.find(start_marker)
if idx != -1:
    # find the comment open before it
    comment_start = css.rfind("/* =", 0, idx)
    if comment_start != -1:
        css = css[:comment_start].strip()
    else:
        css = css[:idx].strip()

smaller_cards_css = """
/* ==========================================================================
   /* SERVICES PAGE (elementor-2087) MASTER OVERRIDE */
   Compact, Sleek, Executive Proportions & Brand Palette
   ========================================================================== */

/* Page Canvas */
.elementor-2087 {
  background-color: #FFFFFF !important;
  font-family: 'Poppins', 'Space Grotesk', sans-serif !important;
}

/* 1. Hero Section (elementor-element-2e5d3505) */
.elementor-2087 .elementor-element-2e5d3505,
.elementor-element-2e5d3505 {
  background: linear-gradient(135deg, #001630 0%, #082142 50%, #001630 100%) !important;
  color: #FFFFFF !important;
  padding: 6.5em 0em 7.5em 0em !important;
  position: relative !important;
}

.elementor-element-2e5d3505 .elementor-heading-title,
.elementor-element-2e5d3505 h1,
.elementor-element-318b617f .elementor-heading-title {
  color: #FFFFFF !important;
  font-family: 'Space Grotesk', 'Poppins', sans-serif !important;
  font-weight: 800 !important;
  font-size: clamp(32px, 4.5vw, 48px) !important;
  letter-spacing: -0.5px !important;
}

.elementor-element-2e5d3505 p,
.elementor-element-7bf47675 p {
  color: #E2E8F0 !important;
  font-size: 16px !important;
  line-height: 1.65 !important;
  max-width: 640px !important;
  margin: 0 auto !important;
}

.elementor-element-2e5d3505 .elementor-shape-fill {
  fill: #FFFFFF !important;
}

/* 2. Overview Section (elementor-element-1be2b82b) */
.elementor-2087 .elementor-element-1be2b82b {
  background-color: #FFFFFF !important;
  padding: 50px 0 60px 0 !important;
}

.elementor-2087 .elementor-element-48269de9 .elementor-heading-title {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
  font-size: clamp(24px, 3vw, 34px) !important;
  line-height: 1.25 !important;
  margin-bottom: 16px !important;
}

.elementor-2087 .elementor-element-324a4d18 p {
  color: #475569 !important;
  font-size: 14.5px !important;
  line-height: 1.65 !important;
  margin-bottom: 20px !important;
}

.elementor-2087 .elementor-element-6c236ed1 .elementor-button {
  background-color: #FF7A00 !important;
  color: #FFFFFF !important;
  border-radius: 25px !important;
  font-weight: 700 !important;
  padding: 10px 24px !important;
  font-size: 13.5px !important;
  border: 1px solid #FF7A00 !important;
  box-shadow: 0 4px 15px rgba(255, 122, 0, 0.35) !important;
  transition: all 0.3s ease !important;
}

.elementor-2087 .elementor-element-6c236ed1 .elementor-button:hover {
  background-color: #001630 !important;
  color: #FFFFFF !important;
  border-color: #001630 !important;
  transform: translateY(-2px) !important;
}

.elementor-2087 .elementor-element-5690ac43 img {
  border-radius: 18px !important;
  box-shadow: 0 16px 36px rgba(0, 22, 48, 0.12) !important;
}

/* Compact Overview Counter Card */
.elementor-2087 .elementor-element-64d8f067 {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  box-shadow: 0 8px 24px rgba(0, 22, 48, 0.08) !important;
  padding: 16px 22px !important;
  max-width: 440px !important;
  margin-top: 18px !important;
}

.elementor-2087 .elementor-element-64d8f067 > .elementor-container {
  display: flex !important;
  align-items: center !important;
}

.elementor-2087 .elementor-element-2576e208 {
  flex: 0 0 60px !important;
  width: 60px !important;
  max-width: 60px !important;
}

.elementor-2087 .elementor-element-47fe5014 img {
  width: 46px !important;
  height: 46px !important;
  max-width: 46px !important;
  object-fit: contain !important;
}

.elementor-2087 .elementor-element-14d51646 {
  flex: 1 1 auto !important;
  padding-left: 16px !important;
}

.elementor-2087 .elementor-element-42e83afb .elementor-counter-number,
.elementor-2087 .elementor-element-42e83afb .elementor-counter-number-suffix {
  color: #FF7A00 !important;
  font-weight: 800 !important;
  font-size: 28px !important;
  line-height: 1.1 !important;
}

.elementor-2087 .elementor-element-8c159b6 .elementor-heading-title {
  color: #001630 !important;
  font-weight: 700 !important;
  font-size: 14px !important;
  margin-top: 2px !important;
}

/* 3. Solutions Section Header (elementor-element-ebc9f7d) */
.elementor-2087 .elementor-element-ebc9f7d {
  background-color: #F8FAFC !important;
  padding: 65px 0 75px 0 !important;
}

.elementor-2087 .elementor-element-76142360 .elementor-heading-title {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
  font-size: clamp(26px, 3.5vw, 36px) !important;
  text-align: center !important;
  margin-bottom: 35px !important;
}

/* 4. Sleek, Compact Solutions Cards (9ee1616, 33bd931c, 4d256d94) */
.elementor-2087 .elementor-element-9ee1616,
.elementor-2087 .elementor-element-33bd931c,
.elementor-2087 .elementor-element-4d256d94 {
  background: #FFFFFF !important;
  border-radius: 18px !important;
  border: 1px solid #E2E8F0 !important;
  box-shadow: 0 6px 24px rgba(0, 22, 48, 0.06) !important;
  overflow: hidden !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  margin-bottom: 22px !important;
  max-width: 940px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

.elementor-2087 .elementor-element-9ee1616 > .elementor-container,
.elementor-2087 .elementor-element-33bd931c > .elementor-container,
.elementor-2087 .elementor-element-4d256d94 > .elementor-container {
  display: flex !important;
  flex-direction: row !important;
  align-items: stretch !important;
  min-height: auto !important;
}

.elementor-2087 .elementor-element-9ee1616:hover,
.elementor-2087 .elementor-element-33bd931c:hover,
.elementor-2087 .elementor-element-4d256d94:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 16px 36px rgba(0, 22, 48, 0.12) !important;
  border-color: #CBD5E1 !important;
}

/* Solutions Card Left Graphic Panel - Streamlined width & padding */
.elementor-2087 .elementor-element-231883aa,
.elementor-2087 .elementor-element-394459ad,
.elementor-2087 .elementor-element-71eb1f62 {
  background: linear-gradient(135deg, #001630 0%, #082142 100%) !important;
  border-radius: 18px 0 0 18px !important;
  flex: 0 0 190px !important;
  width: 190px !important;
  max-width: 190px !important;
  min-height: 100% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 24px !important;
}

.elementor-2087 .elementor-element-231883aa .elementor-widget-wrap,
.elementor-2087 .elementor-element-394459ad .elementor-widget-wrap,
.elementor-2087 .elementor-element-71eb1f62 .elementor-widget-wrap {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.elementor-2087 .elementor-element-231883aa img,
.elementor-2087 .elementor-element-394459ad img,
.elementor-2087 .elementor-element-71eb1f62 img {
  width: 70px !important;
  height: 70px !important;
  max-width: 70px !important;
  max-height: 70px !important;
  object-fit: contain !important;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25)) !important;
}

/* Solutions Card Right Content Column - Balanced spacing */
.elementor-2087 .elementor-element-4aefa621,
.elementor-2087 .elementor-element-7c8d13e8,
.elementor-2087 .elementor-element-667de51e {
  background-color: #FFFFFF !important;
  border-radius: 0 18px 18px 0 !important;
  flex: 1 1 auto !important;
  width: calc(100% - 190px) !important;
  padding: 24px 32px 22px 32px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
}

.elementor-2087 .elementor-icon-box-wrapper {
  margin-bottom: 0 !important;
}

.elementor-2087 .elementor-icon-box-title,
.elementor-2087 .elementor-icon-box-title a {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
  font-size: 20px !important;
  margin-bottom: 6px !important;
  line-height: 1.3 !important;
}

.elementor-2087 .elementor-icon-box-description {
  color: #475569 !important;
  font-size: 13.5px !important;
  line-height: 1.55 !important;
  margin-bottom: 14px !important;
}

/* Horizontal Deliverables Badges */
.elementor-2087 .elementor-icon-list-items {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 6px 20px !important;
  margin-bottom: 14px !important;
  padding: 0 !important;
}

.elementor-2087 .elementor-icon-list-item {
  padding-bottom: 0 !important;
  margin-bottom: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
}

.elementor-2087 .elementor-icon-list-icon i,
.elementor-2087 .elementor-icon-list-icon svg {
  color: #FF7A00 !important;
  fill: #FF7A00 !important;
  font-size: 13px !important;
  margin-right: 6px !important;
}

.elementor-2087 .elementor-icon-list-text {
  color: #1E293B !important;
  font-weight: 600 !important;
  font-size: 13px !important;
}

/* Compact CTA Button */
.elementor-2087 .elementor-element-e9c9c18 .elementor-button,
.elementor-2087 .elementor-element-76eb06 .elementor-button,
.elementor-2087 .elementor-element-21f86e10 .elementor-button {
  background-color: #FF7A00 !important;
  color: #FFFFFF !important;
  border-radius: 25px !important;
  font-weight: 700 !important;
  font-size: 12.5px !important;
  padding: 8px 20px !important;
  border: 1px solid #FF7A00 !important;
  box-shadow: 0 3px 10px rgba(255, 122, 0, 0.3) !important;
  transition: all 0.25s ease !important;
  margin-top: 2px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  width: auto !important;
}

.elementor-2087 .elementor-element-e9c9c18 .elementor-button:hover,
.elementor-2087 .elementor-element-76eb06 .elementor-button:hover,
.elementor-2087 .elementor-element-21f86e10 .elementor-button:hover {
  background-color: #001630 !important;
  color: #FFFFFF !important;
  border-color: #001630 !important;
  box-shadow: 0 6px 18px rgba(0, 22, 48, 0.2) !important;
  transform: translateY(-2px) !important;
}

/* Mobile Responsiveness for Solution Cards */
@media (max-width: 767px) {
  .elementor-2087 .elementor-element-9ee1616 > .elementor-container,
  .elementor-2087 .elementor-element-33bd931c > .elementor-container,
  .elementor-2087 .elementor-element-4d256d94 > .elementor-container {
    flex-direction: column !important;
  }
  .elementor-2087 .elementor-element-231883aa,
  .elementor-2087 .elementor-element-394459ad,
  .elementor-2087 .elementor-element-71eb1f62 {
    width: 100% !important;
    max-width: 100% !important;
    flex: 0 0 100px !important;
    border-radius: 18px 18px 0 0 !important;
    padding: 16px !important;
  }
  .elementor-2087 .elementor-element-4aefa621,
  .elementor-2087 .elementor-element-7c8d13e8,
  .elementor-2087 .elementor-element-667de51e {
    width: 100% !important;
    border-radius: 0 0 18px 18px !important;
    padding: 20px 20px !important;
  }
}

/* 5. Middle Showcase Banner (elementor-element-73c18419) */
.elementor-2087 .elementor-element-73c18419,
.elementor-element-73c18419 {
  background: linear-gradient(135deg, #001630 0%, #082142 50%, #001630 100%) !important;
  color: #FFFFFF !important;
  padding: 5em 0em 4.5em 0em !important;
  position: relative !important;
}

.elementor-element-73c18419 .elementor-shape-top .elementor-shape-fill {
  fill: #F8FAFC !important;
}

.elementor-element-73c18419 .elementor-heading-title,
.elementor-element-73c18419 h2,
.elementor-element-73c18419 h3,
.elementor-element-73c18419 h5 {
  color: #FFFFFF !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
}

.elementor-element-73c18419 p,
.elementor-element-73c18419 .elementor-testimonial-content {
  color: #E2E8F0 !important;
  font-size: 15px !important;
  line-height: 1.65 !important;
}

.elementor-element-73c18419 .elementor-testimonial-name {
  color: #FFFFFF !important;
  font-weight: 700 !important;
  font-size: 15px !important;
}

.elementor-element-73c18419 .elementor-testimonial-job {
  color: #FF7A00 !important;
  font-weight: 600 !important;
  font-size: 13.5px !important;
}

.elementor-element-73c18419 .elementor-testimonial-image img {
  width: 60px !important;
  height: 60px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
}

.elementor-element-73c18419 .elementor-counter-number,
.elementor-element-73c18419 .elementor-counter-number-suffix {
  color: #FF7A00 !important;
  font-weight: 800 !important;
  font-size: 36px !important;
}

.elementor-element-73c18419 .elementor-divider-separator {
  border-color: rgba(255, 255, 255, 0.15) !important;
}

.elementor-element-73c18419 .elementor-button {
  background-color: #FF7A00 !important;
  color: #FFFFFF !important;
  border-color: #FF7A00 !important;
  border-radius: 25px !important;
  font-weight: 700 !important;
  font-size: 13px !important;
  padding: 10px 24px !important;
  box-shadow: 0 4px 15px rgba(255, 122, 0, 0.35) !important;
}

.elementor-element-73c18419 .elementor-button:hover {
  background-color: #FFFFFF !important;
  color: #001630 !important;
  border-color: #FFFFFF !important;
  transform: translateY(-2px) !important;
}

/* 6. Lower Logos & Brands Section (elementor-element-6d344411) */
.elementor-2087 .elementor-element-6d344411,
.elementor-element-6d344411 {
  background-color: #FFFFFF !important;
  background-image: none !important;
  padding: 50px 0 65px 0 !important;
}

.elementor-element-6d344411 .elementor-shape-top .elementor-shape-fill {
  fill: #001630 !important;
}

.elementor-element-6d344411 .elementor-heading-title {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
}

/* 7. Articles & Blog Section (Compact Cards) */
.elementor-2087 .elementor-element-4812c941 {
  padding: 50px 0 60px 0 !important;
}

.elementor-2087 .elementor-element-436d3aca .elementor-heading-title {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 800 !important;
  font-size: clamp(22px, 3vw, 30px) !important;
}

.elementor-2087 .elementor-post {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 18px rgba(0, 22, 48, 0.05) !important;
  transition: all 0.3s ease !important;
  padding-bottom: 16px !important;
}

.elementor-2087 .elementor-post:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 28px rgba(0, 22, 48, 0.12) !important;
  border-color: #CBD5E1 !important;
}

.elementor-2087 .elementor-post__thumbnail {
  height: 160px !important;
  overflow: hidden !important;
}

.elementor-2087 .elementor-post__thumbnail img {
  height: 160px !important;
  width: 100% !important;
  object-fit: cover !important;
  transition: transform 0.35s ease !important;
}

.elementor-2087 .elementor-post:hover .elementor-post__thumbnail img {
  transform: scale(1.05) !important;
}

.elementor-2087 .elementor-post__text {
  padding: 14px 18px 0 18px !important;
}

.elementor-2087 .elementor-post__title,
.elementor-2087 .elementor-post__title a {
  color: #001630 !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 700 !important;
  font-size: 15.5px !important;
  line-height: 1.35 !important;
  margin-bottom: 6px !important;
  transition: color 0.2s ease !important;
}

.elementor-2087 .elementor-post__title a:hover {
  color: #FF7A00 !important;
}

.elementor-2087 .elementor-post__meta-data {
  color: #94A3B8 !important;
  font-size: 12px !important;
  margin-bottom: 8px !important;
}

.elementor-2087 .elementor-post__read-more {
  color: #FF7A00 !important;
  font-weight: 700 !important;
  font-size: 12.5px !important;
}

.elementor-2087 .elementor-element-952a28b .elementor-button,
.elementor-2087 .elementor-element-775ba8cb .elementor-button {
  background-color: #FF7A00 !important;
  color: #FFFFFF !important;
  border-radius: 25px !important;
  font-weight: 700 !important;
  font-size: 12.5px !important;
  padding: 8px 20px !important;
}

.elementor-2087 .elementor-element-952a28b .elementor-button:hover,
.elementor-2087 .elementor-element-775ba8cb .elementor-button:hover {
  background-color: #001630 !important;
  color: #FFFFFF !important;
}
"""

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css + "\n" + smaller_cards_css)

print("Applied compact, smaller card styles to promedia-theme.css.")
