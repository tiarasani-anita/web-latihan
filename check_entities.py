# -*- coding: utf-8 -*-
"""Verifikasi struktur web portofolio Anita (sementara)."""
import io
import os

BASE = r"C:/Users/COMPUTER/Desktop/portfolio-anita"

def load(rel):
    with io.open(os.path.join(BASE, rel), encoding="utf-8") as f:
        return f.read()

css = load("css/style.css")
html = load("index.html")

print("== CSS ==")
print("LOGO content      :", 'content: "\\3C/\\3E";' in css)
print("GREET content     :", 'content: "\\3C hello_world \\2F \\3E";' in css)
print("neon-edge class   :", ".hero-name.neon-edge" in css)
print("dropdown menu css :", ".dropdown-menu" in css)
print("cert grid css     :", ".cert-grid" in css)
print("social icons css  :", ".ic-whatsapp" in css)

print("== HTML ==")
print("HTML length       :", len(html))
print("Project cards     :", html.count('class="project-card'))
print("Cert cards        :", html.count('class="cert-card'))
print("Timeline items    :", html.count('class="timeline-item'))
print("Python 95 skill   :", '>Python</span><span class="skill-percent">95%</span>' in html)
print("Sertifikasi teks  :", "Google Data Analytics" in html, "NASBA" in html, "Pelatihan Finance" in html)
print("Dropdown nav      :", "menu-dropdown" in html)
print("neon-edge         :", "neon-edge" in html)
print("script main       :", "js/main.js" in html)
print("script three      :", "three.min.js" in html)
print("logo icon empty   :", '<span class="logo-icon" aria-hidden="true"></span>' in html)
print("greeting empty    :", '<p class="hero-greeting neon-text" id="hero-greeting"></p>' in html)
print("No raw <hello_world:", "<hello_world" not in html)
print("No raw </> in HTML:", "</>" not in html)

# hitung jumlah id section
import re
ids = re.findall(r'<section id="([^"]+)"', html)
print("Sections          :", ids)

