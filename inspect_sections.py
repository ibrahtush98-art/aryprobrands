with open('socialkit/services/index.htm', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*>', html)
for m in matches:
    classes = [c for c in m.split() if 'elementor-element-' in c]
    print(classes)
