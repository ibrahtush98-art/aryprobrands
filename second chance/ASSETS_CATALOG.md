# 📦 Complete Assets Catalog & Inventory Manifest

> **Folder**: `second chance/`  
> **Purpose**: Centralized archive of all newly created, extracted, and processed brand assets, imagery, vector graphics, merchandise mockups, and design system styles.  
> **Total Files**: 42 Unique Core Assets (94 items including subfolder categorizations)

---

## 📁 Directory Architecture

All assets are available directly inside `second chance/` for immediate drop-in use, and also organized neatly inside specialized subfolders:

```
second chance/
├── logos/                  # Brand identity marks, dark/light variants, SVGs, favicons
├── showcase/               # High-res service showcases, photography, UI mockups
├── merchandise/            # Branded apparel, mugs, caps, business cards, 3D office wall
├── brand_guide_slices/     # Modular slices 0–9 from the master brand guidelines
├── styles/                 # ProMedia / AryPro core design system stylesheet
├── ASSETS_CATALOG.md       # (This document) Complete asset manifest & technical specs
└── COLORS_AND_USAGE_GUIDE.md # Exhaustive website color palette & usage breakdown
```

---

## 1. Brand Identity & Logos (`logos/`)

These assets represent the dual-brand system (ProMedia Group / AryPro Solutions) optimized with transparent alpha channels and SVG vector containers for razor-sharp rendering on Retina/4K displays.

| Asset Filename | Format | Dimensions | File Size | Role & Purpose | Used In Site At |
|:---|:---:|:---:|:---:|:---|:---|
| `arypro-logo-white.png` | PNG (Alpha) | `775 × 554` | 385.4 KB | Primary logo with crisp white typography for dark navy surfaces | Header, Hero, Footer (`.elementor-location-header`) |
| `arypro-logo-dark.png` | PNG (Alpha) | `775 × 554` | 443.1 KB | Primary logo with dark navy typography for light backgrounds | Light sections, About Us page, Service detail |
| `arypro-logo.png` | PNG (Alpha) | `775 × 554` | 443.1 KB | Universal transparent logo master | Drop-in image replacement |
| `arypro-logo-white.svg` | Vector SVG | Responsive | 209 B | Responsive SVG wrapper for dark backgrounds | Scalable header elements |
| `arypro-logo-dark.svg` | Vector SVG | Responsive | 208 B | Responsive SVG wrapper for light backgrounds | Scalable light headers |
| `arypro-favicon.png` | PNG (Alpha) | `128 × 128` | 14.3 KB | Square AP monogram emblem favicon | Browser tab icon (`<link rel="icon">`) |
| `arypro-favicon.svg` | Vector SVG | `128 × 128` | 170 B | Scalable vector favicon | Modern browser SVG favicon |
| `favicon.png` | PNG (Alpha) | `128 × 128` | 14.3 KB | Universal drop-in favicon | Root favicon path |
| `favicon.svg` | Vector SVG | `128 × 128` | 170 B | Universal drop-in SVG favicon | Modern browsers |
| `promedia-logo-white.png` | PNG (Alpha) | `136 × 54` | 13.7 KB | ProMedia white logo | Legacy ProMedia dark header |
| `promedia-logo-white.svg` | Vector SVG | `520 × 120` | 209 B | ProMedia white vector logo | Vector header logo |
| `promedia-logo-dark.svg` | Vector SVG | `520 × 120` | 208 B | ProMedia navy vector logo | Vector light section logo |
| `promedia-logo-light-bg.png`| PNG (Alpha) | `251 × 103` | 30.7 KB | ProMedia logo for light backgrounds | Light header/content |
| `promedia-logo-dark-bg.png` | PNG (Alpha) | `136 × 54` | 13.7 KB | ProMedia logo for dark backgrounds | Dark header/footer |
| `promedia-favicon.png` | PNG (Alpha) | `128 × 128` | 14.3 KB | ProMedia icon mark favicon | Browser tab |
| `promedia-favicon.svg` | Vector SVG | `128 × 128` | 467 B | Vector PM icon mark | SVG favicon |
| `promedia_icon_raw.png` | PNG (Alpha) | `60 × 69` | 6.2 KB | Raw icon emblem crop | App icon / mobile touch icon |
| `promedia_logo_banner_crop.png` | PNG | `220 × 75` | 28.9 KB | Cropped logo mark from welcome banner | Editorial reference |
| `promedia_logo_team_crop.png` | PNG | `370 × 95` | 48.2 KB | Cropped logo mark from team banner | Editorial reference |
| `promedia_logo_light_raw.png` | PNG | `261 × 113` | 31.8 KB | Brand guide raw light logo crop | Guidelines reference |
| `promedia_logo_dark_raw.png` | PNG | `146 × 69` | 15.5 KB | Brand guide raw dark logo crop | Guidelines reference |

---

## 2. High-Resolution Showcase & Photography (`showcase/`)

Custom imagery capturing digital products, cinema-grade video production setups, executive agency teams, and web mockups.

| Asset Filename | Format | Dimensions | File Size | Role & Purpose | Used In Site At |
|:---|:---:|:---:|:---:|:---|:---|
| `arypro_branding_showcase.jpg` | JPEG | `1200 × 896` | 680.1 KB | High-end corporate brand merchandise & stationery mockup | Services showcase: **Branding & Identity System** |
| `arypro_video_showcase.jpg` | JPEG | `1200 × 896` | 764.7 KB | 4K cinema camera production in professional studio | Services showcase: **Video & Media Production** |
| `arypro_web_showcase.jpg` | JPEG | `1376 × 768` | 582.5 KB | Responsive SaaS dashboard on modern laptop screen | Services showcase: **Web Development & Cloud Tech** |
| `promedia_team_hero.jpg` | JPEG | `720 × 900` | 187.2 KB | High-energy agency leadership & creative team photo | Hero side panel & About Us page |
| `promedia_welcome_banner.jpg` | JPEG | `720 × 480` | 102.4 KB | Official agency welcome banner with studio backdrop | About Us & Contact banners |
| `promedia_team_experts.jpg` | JPEG | `720 × 459` | 125.2 KB | Team collaboration & strategic planning session | Agency culture section |
| `promedia_office_studio.jpg` | JPEG | `360 × 480` | 51.5 KB | Modern studio workstation setup with editing gear | Studio tour & office highlight |
| `promedia_web_mockup.svg` | Vector SVG | `800 × 520` | 7.8 KB | Alpha-transparent browser window with live lead dashboard (+370% growth graph) | Tech service showcase & hero interactive mockup |

---

## 3. Tangible Brand Merchandise & Collateral (`merchandise/`)

Extracted directly from the physical application section of the agency brand guide.

| Asset Filename | Format | Dimensions | File Size | Role & Purpose | Used In Site At |
|:---|:---:|:---:|:---:|:---|:---|
| `promedia_branded_apparel.jpg` | JPEG | `391 × 266` | 50.3 KB | Photographer wearing agency hoodie with camera & mug | Merchandise & Agency apparel section |
| `promedia_brand_applications.jpg` | JPEG | `460 × 77` | 13.8 KB | Full panoramic banner of all branded swag & stationery | Brand collateral showcase slider |
| `promedia_business_cards.jpg` | JPEG | `161 × 77` | 5.2 KB | Luxury corporate business cards with orange edge gilding | Identity deliverables list |
| `promedia_3d_wall.jpg` | JPEG | `105 × 77` | 4.1 KB | 3D corporate office reception wall sign | Agency environment feature |
| `promedia_branded_mug.jpg` | JPEG | `83 × 77` | 3.0 KB | Ceramic matte agency coffee mug | Promotional collateral feature |
| `promedia_branded_cap.jpg` | JPEG | `111 × 77` | 3.6 KB | Embroidered athletic corporate cap | Promotional merchandise showcase |

---

## 4. Brand Guidelines Modular Slices (`brand_guide_slices/`)

Sequential crops from the comprehensive master brand manual, detailing spacing, minimum clear space, typography rules, color swatches, and logo isolation.

| Asset Filename | Format | Dimensions | File Size | Content Highlight |
|:---|:---:|:---:|:---:|:---|
| `guide_slice_0.jpg` | JPEG | `460 × 102` | 4.2 KB | Brand manual cover & title block |
| `guide_slice_1.jpg` | JPEG | `460 × 102` | 1.5 KB | Brand philosophy & core vision statement |
| `guide_slice_2.jpg` | JPEG | `460 × 103` | 1.4 KB | Brand mission pillars & market positioning |
| `guide_slice_3.jpg` | JPEG | `460 × 102` | 6.4 KB | Logo anatomy, geometry, and grid construction |
| `guide_slice_4.jpg` | JPEG | `460 × 103` | 9.5 KB | Primary color palette swatches & hex specifications |
| `guide_slice_5.jpg` | JPEG | `460 × 102` | 9.2 KB | Secondary color palette & gradient formulas |
| `guide_slice_6.jpg` | JPEG | `460 × 102` | 9.2 KB | Typography rules & font pairing hierarchy |
| `guide_slice_7.jpg` | JPEG | `460 × 103` | 1.9 KB | Minimum clear space & safe exclusion zone |
| `guide_slice_8.jpg` | JPEG | `460 × 102` | 3.6 KB | Incorrect logo usage & forbidden distortions |
| `guide_slice_9.jpg` | JPEG | `460 × 103` | 5.7 KB | Physical merchandise applications & summary |

---

## 5. Design System Stylesheet (`styles/`)

| Asset Filename | Format | File Size | Role & Purpose |
|:---|:---:|:---:|:---|
| `promedia-theme.css` | CSS | 28.6 KB | Complete CSS override stylesheet containing Poppins typography declarations, header styling, hero wave blending, service card animations, button glow states, responsive breakpoint overrides, and footer styling. |

---

## 💡 How to Use These Assets

1. **For Web Development**:  
   Reference any asset from the relative path `assets/images/...` or directly from `second chance/...`.
2. **For Social Media & Pitch Decks**:  
   High-resolution JPEGs (`arypro_branding_showcase.jpg`, `arypro_video_showcase.jpg`, `arypro_web_showcase.jpg`) can be used directly in Keynote, PowerPoint, and Figma presentations at full 1080p/4K resolution.
3. **For Print & Production**:  
   Vector SVGs (`promedia-logo-white.svg`, `promedia-logo-dark.svg`, `promedia_web_mockup.svg`) scale infinitely without pixelation and can be imported into Adobe Illustrator or CorelDraw.
