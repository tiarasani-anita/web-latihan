# -*- coding: utf-8 -*-
"""Perbaiki preloader-logo: ganti literal </> dengan entity yang benar."""
import io
import os

BASE = r"C:/Users/COMPUTER/Desktop/portfolio-anita"
PATH = os.path.join(BASE, "index.html")

AMP = chr(38)  # ampersand, dibangun via chr agar tidak ter-decode oleh tool
LT = chr(60)   # <
GT = chr(62)   # >

with io.open(PATH, encoding="utf-8") as f:
    html = f.read()

old = '<span class="preloader-logo">' + LT + '/' + GT + '</span>'
entity = AMP + 'lt;' + '/' + AMP + 'gt;'
new = '            <span class="preloader-logo">' + entity + '</span>'

assert html.count(old) == 1, "target string not found or not unique"

html = html.replace(old, new)

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Done. Raw </> count now:", html.count("</>"))
print("Entity present     :", entity in html)

