# 🛠️ Step-by-Step Procedure: How "Our Services" Was Created

> **Document**: Technical Implementation & Procedural Blueprint for "Our Services"  
> **Location**: `second chance/OUR_SERVICES_PROCEDURE.md`  
> **Project**: AryPro Brands Solutions / ProMedia Group  
> **Author**: Engineering & Design Team  

---

## 📑 Table of Contents
1. [Overview & Strategic Goal](#1-overview--strategic-goal)
2. [Phase 1: Architecture & Structural Planning](#2-phase-1-architecture--structural-planning)
3. [Phase 2: Asset Extraction & Graphic Engineering](#3-phase-2-asset-extraction--graphic-engineering)
4. [Phase 3: Design System Tokens & Styling (CSS)](#4-phase-3-design-system-tokens--styling-css)
5. [Phase 4: Component Implementation (HTML Markup)](#5-phase-4-component-implementation-html-markup)
6. [Phase 5: Responsive Layout & Mobile Optimization](#6-phase-5-responsive-layout--mobile-optimization)
7. [Phase 6: Python Automation Scripts Used](#7-phase-6-python-automation-scripts-used)
8. [Phase 7: Step-by-Step Guide to Add or Modify a Service](#8-phase-7-step-by-step-guide-to-add-or-modify-a-service)

---

## 1. Overview & Strategic Goal

The goal of creating the **"Our Services"** section was to transform the website from a generic, stock WordPress template into a high-converting, authoritative digital agency experience.

### Key Objectives:
1. **Showcase 8 Core Specialized Divisions**: Present a structured end-to-end service offering rather than generic marketing buzzwords.
2. **Eliminate Ugly Placeholders**: Replace low-resolution stock images with tailored, high-resolution photography, merchandise mockups, and vector graphics.
3. **Establish Clear Visual Hierarchy**: Use card elevation, circular icon badges, checkmark deliverable lists, and clear CTA buttons.
4. **Drive Lead Conversion**: Connect every service card to deep-link anchor destinations (`services/index.html#talent`, `#digital`, etc.) and consultation booking forms.

---

## 2. Phase 1: Architecture & Structural Planning

The service architecture was organized into two complementary layers:

### Layer A: Homepage Overview Grid (`index.html#services`)
- **Container**: `<section class="arypro-divisions-section" id="services">`
- **Role**: High-level teaser grid displaying 8 specialized divisions with bulleted deliverables and "LEARN MORE →" links.
- **The 8 Divisions**:
  1. Marketing Talent & Content Creators (`fas fa-users-cog`)
  2. Digital Marketing & Social Strategy (`fas fa-chart-pie`)
  3. Content Production & Media (`fas fa-video`)
  4. Paid Performance Advertising (`fas fa-bullseye`)
  5. Branding & Creative Design (`fas fa-palette`)
  6. Website Development & SEO (`fas fa-laptop-code`)
  7. Social Media Setup & Audit (`fas fa-share-alt`)
  8. Printing & Merchandise (`fas fa-tshirt`)

### Layer B: Dedicated Services Page (`services/index.html`)
- **Container**: Detailed division breakdown containers with expanded scope of work, strategy descriptions, client deliverable packages, and inquiry forms.

### Layer C: Visual Case Study & Project Showcase
- High-impact visual proof cards demonstrating real deliverables:
  - **Commercial Video Production**: `assets/images/services/arypro_video_showcase.jpg`
  - **Agribusiness & Corporate Branding**: `assets/images/services/arypro_branding_showcase.jpg`
  - **Web Platform & Technology**: `assets/images/services/arypro_web_showcase.jpg`
  - **Interactive SaaS Mockup**: `assets/images/services/promedia_web_mockup.svg`

---

## 3. Phase 2: Asset Extraction & Graphic Engineering

### 1. Vector Browser Mockup (`promedia_web_mockup.svg`)
- **Problem**: Traditional screenshots have white borders that clash with dark or colored backgrounds.
- **Procedure**:
  - Authored a custom SVG browser container with rounded corners (`rx="16"`) and drop shadow.
  - Added MacOS-style traffic light window controls (🔴 `#EF4444`, 🟡 `#F59E0B`, 🟢 `#10B981`).
  - Added an interactive analytics dashboard showing `+370%` inquiry growth and `▲ 48.6k Visitors`.
  - Exported as `assets/images/services/promedia_web_mockup.svg`.

### 2. High-Resolution Photography Sourcing & Optimization
- **Script**: `extract_merch.py` and `extract_brand_assets.py` using Python PIL / Pillow.
- **Cropping & Processing**:
  - Extracted executive studio photography (`promedia_team_experts.jpg`).
  - Extracted physical brand applications: mugs, caps, business cards, apparel, and 3D office sign (`assets/images/branding/`).
  - Generated high-res Retina showcase imagery (`arypro_branding_showcase.jpg`, `arypro_video_showcase.jpg`).

---

## 4. Phase 3: Design System Tokens & Styling (CSS)

The styling rules were implemented in `assets/css/promedia-theme.css` and `index.html`:

### 1. The Section Container & Header
```css
.arypro-divisions-section {
  background-color: #F8FAFC;
  padding: 80px 20px 70px 20px;
  position: relative;
}

.arypro-section-header-center {
  text-align: center;
  max-width: 720px;
  margin: 0 auto 55px auto;
}

.arypro-pill-label {
  display: inline-block;
  background: rgba(255, 122, 0, 0.12);
  color: #FF7A00;
  font-family: 'Poppins', sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 6px 16px;
  border-radius: 20px;
  margin-bottom: 14px;
}

.arypro-section-title {
  font-family: 'Space Grotesk', 'Poppins', sans-serif;
  font-size: clamp(28px, 4vw, 42px);
  font-weight: 800;
  color: #001630;
  margin: 0 0 14px 0;
  line-height: 1.2;
}

.arypro-section-subtitle {
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  color: #64748B;
  line-height: 1.65;
  margin: 0 auto;
}
```

### 2. Responsive Grid System
```css
.arypro-divisions-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  max-width: 1280px;
  margin: 0 auto;
}

@media (max-width: 1100px) {
  .arypro-divisions-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .arypro-divisions-grid {
    grid-template-columns: 1fr;
  }
}
```

### 3. Service Card Elevation & Hover Dynamics
```css
.arypro-division-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 18px;
  padding: 30px 24px 26px 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 8px 24px rgba(0, 22, 48, 0.06);
  position: relative;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 3px Top Accent Line that reveals on hover */
.arypro-division-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #FF7A00;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.arypro-division-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 45px rgba(0, 22, 48, 0.14);
  border-color: #CBD5E1;
}

.arypro-division-card:hover::before {
  opacity: 1;
}
```

### 4. Card Icon Wrapper & Typography
```css
.arypro-card-icon-wrap {
  width: 52px;
  height: 52px;
  background: rgba(255, 122, 0, 0.12);
  color: #FF7A00;
  border-radius: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.arypro-division-card:hover .arypro-card-icon-wrap {
  background: #FF7A00;
  color: #FFFFFF;
  transform: scale(1.08);
}

.arypro-division-title {
  font-family: 'Space Grotesk', 'Poppins', sans-serif;
  font-size: 19px;
  font-weight: 700;
  color: #001630;
  margin: 0 0 12px 0;
  line-height: 1.3;
}

.arypro-division-desc {
  font-family: 'Poppins', sans-serif;
  font-size: 13.5px;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 18px;
}
```

### 5. Deliverables Checkmark List
```css
.arypro-card-deliverables {
  list-style: none;
  padding: 0;
  margin: 0 0 22px 0;
}

.arypro-card-deliverables li {
  font-family: 'Poppins', sans-serif;
  font-size: 12.5px;
  color: #334155;
  font-weight: 600;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.arypro-card-deliverables li i {
  color: #FF7A00;
  font-size: 11px;
}
```

### 6. Card Action Link
```css
.arypro-card-link {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 12px;
  font-weight: 800;
  color: #FF7A00;
  text-decoration: none;
  letter-spacing: 0.8px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.25s ease;
}

.arypro-card-link:hover {
  color: #001630;
  transform: translateX(4px);
}
```

---

## 5. Phase 4: Component Implementation (HTML Markup)

Here is the exact HTML structure used for each card:

```html
<!-- ================= SECTION: WHAT WE DO (8 MAJOR DIVISIONS) ================= -->
<section class="arypro-divisions-section" id="services">
  <div class="arypro-section-header-center">
    <span class="arypro-pill-label">Our Specialized Divisions</span>
    <h2 class="arypro-section-title">What We Do</h2>
    <p class="arypro-section-subtitle">
      We provide complete, integrated marketing and creative solutions. Explore our major divisions built to take your brand from obscurity to market leadership.
    </p>
  </div>

  <div class="arypro-divisions-grid">
    
    <!-- Division 1: Marketing Talent & Content Creators -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-users-cog"></i>
        </div>
        <h3 class="arypro-division-title">Marketing Talent &amp; Content Creators</h3>
        <p class="arypro-division-desc">
          We help businesses identify, cast, and collaborate with top-tier influencers, UGC creators, brand ambassadors, and marketing talent tailored to your target audience.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Influencer &amp; Creator Selection</li>
          <li><i class="fas fa-check"></i> UGC &amp; Ambassador Management</li>
          <li><i class="fas fa-check"></i> Campaign Direction &amp; Coordination</li>
        </ul>
      </div>
      <a href="services/index.html#talent" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 2: Digital Marketing & Social Media -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-chart-pie"></i>
        </div>
        <h3 class="arypro-division-title">Digital Marketing &amp; Social Strategy</h3>
        <p class="arypro-division-desc">
          Full-funnel management across Facebook, Instagram, TikTok, LinkedIn, and X. Strategic content planning, community engagement, and lead generation.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Strategic Channel Management</li>
          <li><i class="fas fa-check"></i> High-Engagement Content Planning</li>
          <li><i class="fas fa-check"></i> Community &amp; Lead Cultivation</li>
        </ul>
      </div>
      <a href="services/index.html#digital" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 3: Content Production & Media -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-video"></i>
        </div>
        <h3 class="arypro-division-title">Content Production &amp; Media</h3>
        <p class="arypro-division-desc">
          Commercial photography, videography, viral Reels, YouTube videos, drone cinematography, event coverage, interviews, and post-production editing.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Commercial Photography &amp; Video</li>
          <li><i class="fas fa-check"></i> Drone &amp; Aerial Cinematography</li>
          <li><i class="fas fa-check"></i> Reels, Shorts &amp; Social Video</li>
        </ul>
      </div>
      <a href="services/index.html#content" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 4: Paid Performance Advertising -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-bullseye"></i>
        </div>
        <h3 class="arypro-division-title">Paid Performance Advertising</h3>
        <p class="arypro-division-desc">
          High-ROI campaigns across Facebook, Instagram, Google, TikTok, and YouTube. Precise targeting, budget stewardship, and continuous conversion optimization.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Multi-Platform Campaign Strategy</li>
          <li><i class="fas fa-check"></i> Budget Planning &amp; Split Testing</li>
          <li><i class="fas fa-check"></i> Conversion &amp; Lead Optimization</li>
        </ul>
      </div>
      <a href="services/index.html#paid" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 5: Branding & Creative Design -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-palette"></i>
        </div>
        <h3 class="arypro-division-title">Branding &amp; Creative Design</h3>
        <p class="arypro-division-desc">
          Visual identities that command respect. Logo design, brand style guides, social media graphics, brochures, business cards, and marketing collateral.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Logo &amp; Corporate Visual Identity</li>
          <li><i class="fas fa-check"></i> Marketing Collateral &amp; Brochures</li>
          <li><i class="fas fa-check"></i> Campaign Creatives &amp; Graphics</li>
        </ul>
      </div>
      <a href="services/index.html#branding" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 6: Website Development & SEO -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-laptop-code"></i>
        </div>
        <h3 class="arypro-division-title">Website Development &amp; SEO</h3>
        <p class="arypro-division-desc">
          Modern corporate websites, landing pages, and e-commerce platforms engineered for rapid speed, mobile conversion, and top organic search rankings.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> High-Converting Business Websites</li>
          <li><i class="fas fa-check"></i> On-Page &amp; Technical SEO</li>
          <li><i class="fas fa-check"></i> Mobile-First Speed Optimization</li>
        </ul>
      </div>
      <a href="services/index.html#web" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 7: Social Media Setup & Optimization -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-share-alt"></i>
        </div>
        <h3 class="arypro-division-title">Social Media Setup &amp; Audit</h3>
        <p class="arypro-division-desc">
          Professional launch and rebuilding of profiles across Facebook, Instagram, TikTok, and LinkedIn with optimized bios, branding, and contact infrastructure.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Complete Profile Configuration</li>
          <li><i class="fas fa-check"></i> High-Resolution Cover &amp; Bio Assets</li>
          <li><i class="fas fa-check"></i> Verification &amp; Security Audits</li>
        </ul>
      </div>
      <a href="services/index.html#setup" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

    <!-- Division 8: Printing & Merchandise -->
    <div class="arypro-division-card">
      <div>
        <div class="arypro-card-icon-wrap">
          <i class="fas fa-tshirt"></i>
        </div>
        <h3 class="arypro-division-title">Printing &amp; Merchandise</h3>
        <p class="arypro-division-desc">
          Physical brand presence. Premium business cards, pull-up banners, flyers, branded corporate apparel, promotional merchandise, and office items.
        </p>
        <ul class="arypro-card-deliverables">
          <li><i class="fas fa-check"></i> Embroidered &amp; Printed Apparel</li>
          <li><i class="fas fa-check"></i> Executive Corporate Merchandise</li>
          <li><i class="fas fa-check"></i> Event Banners &amp; Large Format Print</li>
        </ul>
      </div>
      <a href="services/index.html#merch" class="arypro-card-link">LEARN MORE &rarr;</a>
    </div>

  </div>
</section>
```

---

## 6. Phase 5: Responsive Layout & Mobile Optimization

To ensure seamless viewing on all smartphones and tablets:
1. **Fluid Grid Breakpoints**:
   - `≥ 1100px`: 4 columns (`grid-template-columns: repeat(4, 1fr)`)
   - `641px – 1099px`: 2 columns (`grid-template-columns: repeat(2, 1fr)`)
   - `≤ 640px`: 1 full-width column (`grid-template-columns: 1fr`)
2. **Touch Target Sizing**:
   - Cards have equal height (`display: flex; flex-direction: column; justify-content: space-between`).
   - "LEARN MORE →" link has a minimum clickable area of `44px` on mobile screens.
3. **Adaptive Typography**:
   - Titles use CSS `clamp()` (`clamp(28px, 4vw, 42px)`) so headings scale smoothly without horizontal scrolling.

---

## 7. Phase 6: Python Automation Scripts Used

During construction, specialized workspace Python scripts automated the process:

| Script Name | Function & Role |
|:---|:---|
| `enrich_services_showcase.py` | Injected the core service sections into `index.html` and `services/index.html`, swapped stock images with branded imagery, and generated `promedia_web_mockup.svg`. |
| `extract_brand_assets.py` | Sourced and cropped imagery from high-res uploaded agency files using Pillow. |
| `extract_merch.py` | Sourced and cropped apparel, caps, mugs, and business card assets from the brand manual. |
| `apply_full_promedia_theme.py` | Enforced Poppins / Space Grotesk typography, Deep Navy and Vibrant Orange color tokens, and card hover dynamics across all pages. |

---

## 8. Phase 7: Step-by-Step Guide to Add or Modify a Service

If you need to add a new service or edit an existing one in the future, follow these 5 steps:

### Step 1: Locate the Section
Open `index.html` and navigate to `<section class="arypro-divisions-section" id="services">` (around Line 290).

### Step 2: Copy the Card Template
```html
<div class="arypro-division-card">
  <div>
    <div class="arypro-card-icon-wrap">
      <i class="fas fa-YOUR-ICON-HERE"></i>
    </div>
    <h3 class="arypro-division-title">Your Service Title</h3>
    <p class="arypro-division-desc">
      A concise 2-line explanation of the business value and outcome delivered.
    </p>
    <ul class="arypro-card-deliverables">
      <li><i class="fas fa-check"></i> Key Deliverable 1</li>
      <li><i class="fas fa-check"></i> Key Deliverable 2</li>
      <li><i class="fas fa-check"></i> Key Deliverable 3</li>
    </ul>
  </div>
  <a href="services/index.html#your-anchor" class="arypro-card-link">LEARN MORE &rarr;</a>
</div>
```

### Step 3: Choose a FontAwesome Icon
Pick any solid FontAwesome 5/6 icon from the loaded library:
- `fa-bullhorn` (PR & Communications)
- `fa-envelope-open-text` (Email Marketing & Newsletters)
- `fa-funnel-dollar` (Sales Funnels & CRM)
- `fa-shield-alt` (Brand Reputation Management)

### Step 4: Link to the Service Detail Page
Set the anchor in the `href` attribute (e.g. `services/index.html#email-marketing`) and ensure a matching `<div id="email-marketing">` exists on `services/index.html`.

### Step 5: Save & Verify
Save `index.html`. Check the live preview on `http://localhost:3000` to verify card alignment and responsive behavior.
