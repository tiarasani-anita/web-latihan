# -*- coding: utf-8 -*-
"""Tambahkan class spotlight-card pada kartu yang sudah memiliki data-tilt."""
import io

BASE = r"C:/Users/COMPUTER/Desktop/portfolio-anita"
PATH = BASE + "/index.html"

with io.open(PATH, encoding="utf-8") as f:
    html = f.read()

# Pasangan: string lama -> string baru (tambah class spotlight-card)
repls = [
    ('class="project-card glass reveal" data-tilt>',
     'class="project-card glass reveal spotlight-card" data-tilt>'),
    ('class="skill-card glass reveal" data-tilt>',
     'class="skill-card glass reveal spotlight-card" data-tilt>'),
    ('class="cert-card glass reveal" data-tilt>',
     'class="cert-card glass reveal spotlight-card" data-tilt>'),
    ('class="about-card glass reveal gradient-border" data-tilt>',
     'class="about-card glass reveal gradient-border spotlight-card" data-tilt>'),
]

for old, new in repls:
    if old not in html:
        raise SystemExit("TIDAK KETEMU: " + old)
    html = html.replace(old, new)

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("OK. Total class spotlight-card :", html.count("spotlight-card"))
print("Total data-tilt              :", html.count("data-tilt"))

