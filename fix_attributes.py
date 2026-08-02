# -*- coding: utf-8 -*-
"""Tambahkan atribut data-tilt/spotlight pada kartu & kelas magnetic pada tombol hero."""
import io
import os

BASE = r"C:/Users/COMPUTER/Desktop/portfolio-anita"
PATH = os.path.join(BASE, "index.html")

with io.open(PATH, encoding="utf-8") as f:
    html = f.read()

# 1. Tambah data-tilt pada kartu proyek
proj_old = '<div class="project-card glass reveal">'
proj_new = '<div class="project-card glass reveal" data-tilt>'
assert html.count(proj_old) == 12, f"project-card count = {html.count(proj_old)}"
html = html.replace(proj_old, proj_new)

# 2. Tambah data-tilt pada kartu keahlian
skill_old = '<div class="skill-card glass reveal">'
skill_new = '<div class="skill-card glass reveal" data-tilt>'
assert html.count(skill_old) == 16, f"skill-card count = {html.count(skill_old)}"
html = html.replace(skill_old, skill_new)

# 3. Tambah data-tilt pada kartu sertifikasi
cert_old = '<div class="cert-card glass reveal">'
cert_new = '<div class="cert-card glass reveal" data-tilt>'
assert html.count(cert_old) == 4, f"cert-card count = {html.count(cert_old)}"
html = html.replace(cert_old, cert_new)

# 4. Tambah data-tilt pada kartu tentang (about-card)
about_old = '<div class="about-card glass reveal gradient-border">'
about_new = '<div class="about-card glass reveal gradient-border" data-tilt>'
assert html.count(about_old) == 1, f"about-card count = {html.count(about_old)}"
html = html.replace(about_old, about_new)

# 5. Tambah kelas magnetic pada tombol hero
btn1_old = '<a href="#proyek" class="btn btn-primary">'
btn1_new = '<a href="#proyek" class="btn btn-primary magnetic">'
assert html.count(btn1_old) == 1
html = html.replace(btn1_old, btn1_new)

btn2_old = '<a href="#kontak" class="btn btn-outline">'
btn2_new = '<a href="#kontak" class="btn btn-outline magnetic">'
assert html.count(btn2_old) == 1
html = html.replace(btn2_old, btn2_new)

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("OK.")
print("data-tilt project :", html.count('class="project-card glass reveal" data-tilt>'))
print("data-tilt skill   :", html.count('class="skill-card glass reveal" data-tilt>'))
print("data-tilt cert    :", html.count('class="cert-card glass reveal" data-tilt>'))
print("data-tilt about   :", html.count('class="about-card glass reveal gradient-border" data-tilt>'))
print("magnetic buttons  :", html.count('btn btn-primary magnetic'), html.count('btn btn-outline magnetic'))

