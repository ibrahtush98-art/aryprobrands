import os
import re

base_dir = r"c:\Users\Admin\Documents\website generator\New folder\templatekit.tokomoo.com\socialkit"

for p in ["index.htm", "about-us/index.htm", "services/index.htm", "contact-us/index.htm"]:
    path = os.path.join(base_dir, p)
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    h_start = c.find("<header")
    h_end = c.find("</header>") + len("</header>")
    header = c[h_start:h_end]
    print(f"=== {p} ===")
    print("  Header length:", len(header))
    print("  Has 'Case Study':", "Case Study" in header)
    print("  Has 'Pricing':", "Pricing" in header)
    print("  Number of <ul:", header.count("<ul"))
    print("  Number of </ul:", header.count("</ul"))
