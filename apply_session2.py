# -*- coding: utf-8 -*-
"""Sesi Lanjutan 2: perubahan HTML
- Meta Open Graph / Twitter / theme-color
- Tombol Download CV (hero & kontak)
- Preloader persentase
- Kelas reveal-stagger pada kartu blog & layanan
"""
import io

PATH = r"C:/Users/COMPUTER/Desktop/portfolio-anita/index.html"
html = io.open(PATH, encoding="utf-8").read()

# 1) Meta tags SEO & sharing
old_meta = '<meta name="description" content="Portofolio Anita Tiara Sani - Anak Informatika, Web Developer, App Developer, Data Analyst, Finance & Accounting Enthusiast.">'
new_meta = old_meta + '''
    <meta name="theme-color" content="#070b16">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Anita Tiara Sani | Portofolio Anak Informatika">
    <meta property="og:description" content="Portofolio Anita Tiara Sani - Anak Informatika, Web Developer, App Developer, Data Analyst, Finance & Accounting Enthusiast.">
    <meta property="og:url" content="https://anitatiara25.github.io/portfolio-anita/">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Anita Tiara Sani | Portofolio Anak Informatika">
    <meta name="twitter:description" content="Portofolio Anita Tiara Sani - Anak Informatika, Web Developer, App Developer, Data Analyst, Finance & Accounting Enthusiast.">'''
assert html.count(old_meta) == 1, "meta description"
html = html.replace(old_meta, new_meta)

# 2) Tombol Download CV di hero
old_btns = '<a href="#proyek" class="btn btn-primary magnetic">🚀 Lihat Proyek</a>\n                <a href="#kontak" class="btn btn-outline magnetic">💬 Hubungi Saya</a>'
new_btns = old_btns + '\n                <a href="cv.pdf" download class="btn btn-download magnetic">📄 Download CV</a>'
assert html.count(old_btns) == 1, "hero buttons"
html = html.replace(old_btns, new_btns)

# 3) Preloader persentase
old_pre = '<p class="preloader-text">Memuat Portofolio...</p>'
new_pre = old_pre + '\n            <p class="preloader-percent" id="preloader-percent">0%</p>'
assert html.count(old_pre) == 1, "preloader text"
html = html.replace(old_pre, new_pre)

# 4) Tombol Download CV di section kontak (di dalam contact-info, setelah menu-panel)
old_contact = '''                            </div>
                        </div>
                    </div>
                </div>

                <form class="contact-form glass reveal gradient-border" id="contact-form">'''
new_contact = '''                            </div>
                        </div>
                    </div>
                <a href="cv.pdf" download class="btn btn-download btn-full magnetic" style="margin-top:14px;">📄 Download CV</a>
                </div>

                <form class="contact-form glass reveal gradient-border" id="contact-form">'''
assert html.count(old_contact) == 1, "contact menu-panel close"
html = html.replace(old_contact, new_contact)

# 5) Kartu blog: reveal -> reveal-stagger
old_blog = '<article class="blog-card glass reveal spotlight-card" data-tilt>'
new_blog = '<article class="blog-card glass reveal-stagger spotlight-card" data-tilt>'
assert html.count(old_blog) == 3, "blog cards"
html = html.replace(old_blog, new_blog)

# 6) Kartu layanan: reveal -> reveal-stagger
old_svc = 'service-card glass reveal spotlight-card'
new_svc = 'service-card glass reveal-stagger spotlight-card'
assert html.count(old_svc) == 6, "service cards"
html = html.replace(old_svc, new_svc)

io.open(PATH, "w", encoding="utf-8", newline="").write(html)

print("OK.")
print("Meta og:title          :", 'property="og:title"' in html)
print("Meta twitter:card      :", 'name="twitter:card"' in html)
print("Meta theme-color       :", 'name="theme-color"' in html)
print("CV hero                :", 'btn btn-download magnetic">📄 Download CV</a>' in html)
print("CV kontak              :", 'btn btn-download btn-full magnetic' in html)
print("Preloader percent      :", 'id="preloader-percent"' in html)
print("Blog reveal-stagger    :", html.count('blog-card glass reveal-stagger'))
print("Service reveal-stagger :", html.count('service-card glass reveal-stagger'))

