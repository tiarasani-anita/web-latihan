# -*- coding: utf-8 -*-
"""Verifikasi menyeluruh proyek portofolio Anita: konsistensi HTML/CSS/JS."""
import io
import os
import re

BASE = r"C:/Users/COMPUTER/Desktop/portfolio-anita"

def load(rel):
    with io.open(os.path.join(BASE, rel), encoding="utf-8") as f:
        return f.read()

html = load("index.html")
css = load("css/style.css")
js = load("js/main.js")

print("=== 1. FUNGSI INIT DI DOMCONTENTLOADED ===")
defined = set(re.findall(r"function (init\w+)\(", js))
called = set(re.findall(r"\b(init\w+)\(\);", js))
print("Terdefinisi :", len(defined))
print("Terpanggil  :", len(called))
print("Tidak dipanggil :", sorted(defined - called) or "-")
print("Dipanggil, tak terdefinisi :", sorted(called - defined) or "-")

print()
print("=== 2. KONSISTENSI data-blog (HTML vs JS) ===")
btn_blog = set(re.findall(r'data-blog="(\d+)"', html))
blog_start = js.find("const blogData")
blog_end = js.find("function openBlog")
js_blog = set(re.findall(r"^\s*(\d+): \{", js[blog_start:blog_end], re.M))
print("HTML:", sorted(btn_blog, key=int))
print("JS  :", sorted(js_blog, key=int))
print("Mismatch:", sorted(btn_blog ^ js_blog, key=int) or "tidak ada")

print()
print("=== 3. KONSISTENSI data-project (HTML vs JS) ===")
btn_proj = set(re.findall(r'data-project="(\d+)"', html))
proj_start = js.find("const projectData")
proj_end = js.find("function openModal")
js_proj = set(re.findall(r"^\s*(\d+): \{", js[proj_start:proj_end], re.M))
print("HTML:", sorted(btn_proj, key=int))
print("JS  :", sorted(js_proj, key=int))
print("Mismatch:", sorted(btn_proj ^ js_proj, key=int) or "tidak ada")

print()
print("=== 4. KESEIMBANGAN TAG HTML ===")
ok = True
for tag in ["div", "section", "button", "ul", "li", "nav", "form", "span", "h1", "h2", "h3", "p", "article", "footer", "header", "a"]:
    # abaikan <a ...> yang self-closing atau void? <a> selalu berpasangan
    open_n = len(re.findall(r"<%s[\s>]" % tag, html))
    close_n = len(re.findall(r"</%s>" % tag, html))
    if open_n != close_n:
        print("  TAG MISMATCH %s: open=%d close=%d" % (tag, open_n, close_n))
        ok = False
print("  Semua tag seimbang" if ok else "  ADA MISMATCH")

print()
print("=== 5. SECTION ID ===")
ids = re.findall(r'<section id="([^"]+)"', html)
print("Jumlah section:", len(ids))
print(ids)

print()
print("=== 6. ELEMEN UNIK / ID DUPLIKAT ===")
all_ids = re.findall(r'id="([^"]+)"', html)
dupes = {x for x in all_ids if all_ids.count(x) > 1}
print("ID duplikat:", sorted(dupes) or "tidak ada")

print()
print("=== 7. REFERENSI CLASS DI CSS ===")
css_classes = set(re.findall(r"\.([a-zA-Z][\w-]*)", css))
# class yang dipakai di HTML
html_classes = set()
for m in re.finditer(r'class="([^"]+)"', html):
    for c in m.group(1).split():
        html_classes.add(c)
# class penting yang dipakai HTML tapi tidak terdefinisi di CSS
important = html_classes
missing = []
for c in sorted(important):
    # cari sebagai .c atau .c:  atau .c[  atau .c,
    if not re.search(r"\.%s(?![a-zA-Z0-9_-])" % re.escape(c), css):
        missing.append(c)
print("Class dipakai di HTML :", len(html_classes))
print("Class TIDAK ada di CSS:", missing if missing else "tidak ada (atau via CSS lain)")

print()
print("=== 8. MODAL PROYEK & BLOG ===")
print("Modal proyek :", 'id="project-modal"' in html, 'id="project-modal-overlay"' in html)
print("Modal blog   :", 'id="blog-modal"' in html, 'id="blog-modal-overlay"' in html)
print("btn detail proyek :", html.count("project-detail-btn"))
print("btn detail blog   :", html.count("blog-detail-btn"))

print()
print("=== 9. ASSET EKSTERNAL ===")
print("three.min.js :", "three.min.js" in html)
print("main.js      :", "js/main.js" in html)
print("style.css    :", "css/style.css" in html)
print("cv.pdf ada   :", os.path.exists(os.path.join(BASE, "cv.pdf")))

print()
print("=== 10. CUSTOM CURSOR & PRELOADER ===")
print("cursor-dot/ring :", 'id="cursor-dot"' in html, 'id="cursor-ring"' in html)
print("preloader       :", 'id="preloader"' in html, 'id="preloader-percent"' in html)

print()
print("SELESAI VERIFIKASI.")

