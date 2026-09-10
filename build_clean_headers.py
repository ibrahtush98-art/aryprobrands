import os
import re

base_dir = r"c:\Users\Admin\Documents\website generator\New folder\templatekit.tokomoo.com\socialkit"

def make_header_html(is_subpage, active_page):
    prefix = "../" if is_subpage else ""
    logo_src = f"{prefix}wp-content/uploads/sites/58/2021/12/socialy-logo-white.png"
    
    home_active = ' aria-current="page" class="elementor-item elementor-item-active"' if active_page == "home" else ' class="elementor-item"'
    about_active = ' aria-current="page" class="elementor-item elementor-item-active"' if active_page == "about" else ' class="elementor-item"'
    services_active = ' aria-current="page" class="elementor-item elementor-item-active"' if active_page == "services" else ' class="elementor-item"'
    contact_active = ' aria-current="page" class="elementor-item elementor-item-active"' if active_page == "contact" else ' class="elementor-item"'

    menu_items = f"""<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="{prefix}index.htm"{home_active}>Home</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="{prefix}about-us/index.htm"{about_active}>About</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="{prefix}services/index.htm"{services_active}>Services</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="{prefix}contact-us/index.htm"{contact_active}>Contact Us</a></li>"""

    header_html = f"""<header data-elementor-type="header" data-elementor-id="138" class="elementor elementor-138 elementor-location-header" data-elementor-post-type="elementor_library">
		<section class="elementor-section elementor-top-section elementor-element elementor-element-a383149 elementor-hidden-tablet elementor-hidden-mobile elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="a383149" data-element_type="section" data-e-type="section" data-settings="{{"background_background":"classic"}}">
			<div class="elementor-container elementor-column-gap-no">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-21a1c3ea" data-id="21a1c3ea" data-element_type="column" data-e-type="column">
					<div class="elementor-widget-wrap elementor-element-populated">
						<section class="elementor-section elementor-inner-section elementor-element elementor-element-25e3457c elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="25e3457c" data-element_type="section" data-e-type="section">
							<div class="elementor-container elementor-column-gap-no">
								<div class="elementor-column elementor-col-16 elementor-inner-column elementor-element elementor-element-3be7f061" data-id="3be7f061" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-232f077 elementor-widget elementor-widget-image" data-id="232f077" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
											<div class="elementor-widget-container">
												<a href="{prefix}index.htm">
													<img width="346" height="100" src="{logo_src}" class="attachment-large size-large wp-image-1889" alt="AryPro" style="max-height: 44px; width: auto; object-fit: contain;">
												</a>
											</div>
										</div>
									</div>
								</div>
								<div class="elementor-column elementor-col-66 elementor-inner-column elementor-element elementor-element-6ccae9d4 elementor-hidden-phone" data-id="6ccae9d4" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-64a56ec0 elementor-hidden-tablet elementor-hidden-phone elementor-nav-menu__align-center elementor-nav-menu--dropdown-mobile elementor-nav-menu--stretch elementor-nav-menu__text-align-aside elementor-nav-menu--toggle elementor-nav-menu--burger elementor-widget elementor-widget-nav-menu" data-id="64a56ec0" data-element_type="widget" data-e-type="widget" data-widget_type="nav-menu.default">
											<div class="elementor-widget-container">
												<nav aria-label="Menu" class="elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--pointer-underline e--animation-slide">
													<ul id="menu-1-64a56ec0" class="elementor-nav-menu">
{menu_items}
													</ul>
												</nav>
												<div class="elementor-menu-toggle" role="button" tabindex="0" aria-label="Menu Toggle" aria-expanded="false">
													<i aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--open eicon-menu-bar"></i><i aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--close eicon-close"></i>
												</div>
												<nav class="elementor-nav-menu--dropdown elementor-nav-menu__container" aria-hidden="true">
													<ul id="menu-2-64a56ec0" class="elementor-nav-menu">
{menu_items}
													</ul>
												</nav>
											</div>
										</div>
									</div>
								</div>
								<div class="elementor-column elementor-col-16 elementor-inner-column elementor-element elementor-element-b1e7c66" data-id="b1e7c66" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-0380544 elementor-align-right elementor-widget elementor-widget-button" data-id="0380544" data-element_type="widget" data-e-type="widget" data-widget_type="button.default">
											<div class="elementor-widget-container">
												<div class="elementor-button-wrapper">
													<a class="elementor-button elementor-button-link elementor-size-sm" href="{prefix}contact-us/index.htm">
														<span class="elementor-button-content-wrapper">
															<span class="elementor-button-text">Get a Quote</span>
														</span>
													</a>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</section>
					</div>
				</div>
			</div>
		</section>
		<section class="elementor-section elementor-top-section elementor-element elementor-element-1021f2e elementor-hidden-desktop elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="1021f2e" data-element_type="section" data-e-type="section" data-settings="{{"background_background":"classic"}}">
			<div class="elementor-container elementor-column-gap-no">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-f5de090" data-id="f5de090" data-element_type="column" data-e-type="column">
					<div class="elementor-widget-wrap elementor-element-populated">
						<section class="elementor-section elementor-inner-section elementor-element elementor-element-6ba6831 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="6ba6831" data-element_type="section" data-e-type="section">
							<div class="elementor-container elementor-column-gap-no">
								<div class="elementor-column elementor-col-16 elementor-inner-column elementor-element elementor-element-858d243" data-id="858d243" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-c764585 elementor-widget elementor-widget-image" data-id="c764585" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
											<div class="elementor-widget-container">
												<a href="{prefix}index.htm">
													<img width="346" height="100" src="{logo_src}" class="attachment-large size-large wp-image-1889" alt="AryPro" style="max-height: 40px; width: auto; object-fit: contain;">
												</a>
											</div>
										</div>
									</div>
								</div>
								<div class="elementor-column elementor-col-16 elementor-inner-column elementor-element elementor-element-7d6fd74 elementor-hidden-mobile" data-id="7d6fd74" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-d177d70 elementor-align-right elementor-widget elementor-widget-button" data-id="d177d70" data-element_type="widget" data-e-type="widget" data-widget_type="button.default">
											<div class="elementor-widget-container">
												<div class="elementor-button-wrapper">
													<a class="elementor-button elementor-button-link elementor-size-sm" href="{prefix}contact-us/index.htm">
														<span class="elementor-button-content-wrapper">
															<span class="elementor-button-text">Get a Quote</span>
														</span>
													</a>
												</div>
											</div>
										</div>
									</div>
								</div>
								<div class="elementor-column elementor-col-66 elementor-inner-column elementor-element elementor-element-f523376" data-id="f523376" data-element_type="column" data-e-type="column">
									<div class="elementor-widget-wrap elementor-element-populated">
										<div class="elementor-element elementor-element-2b2c3a3 elementor-nav-menu__align-center elementor-nav-menu--stretch elementor-nav-menu--dropdown-tablet elementor-nav-menu__text-align-aside elementor-nav-menu--toggle elementor-nav-menu--burger elementor-widget elementor-widget-nav-menu" data-id="2b2c3a3" data-element_type="widget" data-e-type="widget" data-widget_type="nav-menu.default">
											<div class="elementor-widget-container">
												<nav aria-label="Menu" class="elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--pointer-underline e--animation-slide">
													<ul id="menu-1-2b2c3a3" class="elementor-nav-menu">
{menu_items}
													</ul>
												</nav>
												<div class="elementor-menu-toggle" role="button" tabindex="0" aria-label="Menu Toggle" aria-expanded="false">
													<i aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--open eicon-menu-bar"></i><i aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--close eicon-close"></i>
												</div>
												<nav class="elementor-nav-menu--dropdown elementor-nav-menu__container" aria-hidden="true">
													<ul id="menu-2-2b2c3a3" class="elementor-nav-menu">
{menu_items}
													</ul>
												</nav>
											</div>
										</div>
									</div>
								</div>
							</div>
						</section>
					</div>
				</div>
			</div>
		</section>
	</header>"""
    return header_html

pages = [
    ("index.htm", False, "home"),
    ("about-us/index.htm", True, "about"),
    ("services/index.htm", True, "services"),
    ("contact-us/index.htm", True, "contact")
]

for rel_p, is_sub, act in pages:
    full_p = os.path.join(base_dir, rel_p)
    with open(full_p, "r", encoding="utf-8") as f:
        html = f.read()
    
    h_start = html.find("<header")
    h_end = html.find("</header>") + len("</header>")
    
    if h_start != -1 and h_end != -1:
        new_header = make_header_html(is_sub, act)
        html = html[:h_start] + new_header + html[h_end:]
        with open(full_p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Applied clean header to: {rel_p}")
