# -*- coding: utf-8 -*-
"""Ganti seluruh heading/identity font menjadi Sora + perkecil nama hero."""
import io
import re

CSS = "css/style.css"
HTML = "index.html"

c = io.open(CSS, encoding="utf-8").read()
h = io.open(HTML, encoding="utf-8").read()

# 1) Semua referensi heading/identity -> Sora
c = c.replace("'Syne', 'Space Grotesk'", "'Sora'")
c = c.replace("'Space Grotesk'", "'Sora'")
c = c.replace("'Syne'", "'Sora'")

# 2) Perkecil ukuran nama hero (agak lebih kecil & proporsional)
c = c.replace("font-size: clamp(2.6rem, 7.5vw, 5.2rem);",
              "font-size: clamp(2rem, 5.2vw, 3.5rem);")

# 3) Update Google Fonts link di HTML
#    Hapus Space Grotesk & Syne, sisakan Sora + Inter
h = re.sub(r'family=Space\+Grotesk[^&]*&?', '', h)
h = re.sub(r'family=Syne[^&]*&?', '', h)
if 'family=Sora' not in h:
    h = h.replace('family=Inter', 'family=Sora:wght@400;500;600;700;800&family=Inter')

io.open(CSS, "w", encoding="utf-8", newline="").write(c)
io.open(HTML, "w", encoding="utf-8", newline="").write(h)

print("CSS 'Sora' refs     :", c.count("'Sora'"))
print("CSS 'Space Grotesk' left:", c.count("Space Grotesk"))
print("CSS 'Syne' left     :", c.count("Syne"))
print("HTML Sora link      :", "family=Sora" in h)
print("HTML Space Grotesk left:", "Space Grotesk" in h)
print("HTML Syne left      :", "Syne" in h)
print("hero size updated   :", "font-size: clamp(2rem, 5.2vw, 3.5rem);" in c)

