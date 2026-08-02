# -*- coding: utf-8 -*-
"""Sesi Lanjutan 3: Kartu blog dapat diklik -> modal detail artikel.
1. Tambah atribut data-blog + tombol 'Baca Selengkapnya' pada 3 kartu blog.
2. Tambah modal blog baru di akhir halaman.
"""
import io

PATH = r"C:/Users/COMPUTER/Desktop/portfolio-anita/index.html"
html = io.open(PATH, encoding="utf-8").read()

# --- 1) Blog card 1 ---
old1 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-1"><span class="blog-emoji">🤖</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Teknologi</span>
                        <h3>Mengenal Kecerdasan Buatan di Era Modern</h3>
                        <p>Bagaimana AI mengubah cara kita bekerja, belajar, dan mengambil keputusan di berbagai bidang.</p>
                        <div class="blog-meta"><span>📅 Jan 2025</span><span>⏱ 5 mnt</span></div>
                    </div>
                </article>'''
new1 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt data-blog="1">
                    <div class="blog-thumb blog-thumb-1"><span class="blog-emoji">🤖</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Teknologi</span>
                        <h3>Mengenal Kecerdasan Buatan di Era Modern</h3>
                        <p>Bagaimana AI mengubah cara kita bekerja, belajar, dan mengambil keputusan di berbagai bidang.</p>
                        <div class="blog-meta"><span>📅 Jan 2025</span><span>⏱ 5 mnt</span></div>
                        <button class="btn btn-small blog-detail-btn" data-blog="1">Baca Selengkapnya →</button>
                    </div>
                </article>'''
assert html.count(old1) == 1, "blog card 1"
html = html.replace(old1, new1)

# --- 2) Blog card 2 ---
old2 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-2"><span class="blog-emoji">🪙</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Finance</span>
                        <h3>Panduan Investasi Emas &amp; Saham untuk Pemula</h3>
                        <p>Langkah awal membangun portofolio investasi: emas, saham lokal, hingga saham luar negeri.</p>
                        <div class="blog-meta"><span>📅 Feb 2025</span><span>⏱ 7 mnt</span></div>
                    </div>
                </article>'''
new2 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt data-blog="2">
                    <div class="blog-thumb blog-thumb-2"><span class="blog-emoji">🪙</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Finance</span>
                        <h3>Panduan Investasi Emas &amp; Saham untuk Pemula</h3>
                        <p>Langkah awal membangun portofolio investasi: emas, saham lokal, hingga saham luar negeri.</p>
                        <div class="blog-meta"><span>📅 Feb 2025</span><span>⏱ 7 mnt</span></div>
                        <button class="btn btn-small blog-detail-btn" data-blog="2">Baca Selengkapnya →</button>
                    </div>
                </article>'''
assert html.count(old2) == 1, "blog card 2"
html = html.replace(old2, new2)

# --- 3) Blog card 3 ---
old3 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-3"><span class="blog-emoji">🔗</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Web3</span>
                        <h3>Web3 &amp; Web4: Masa Depan Internet Terdesentralisasi</h3>
                        <p>Eksplorasi blockchain, smart contract, dApp, dan bagaimana Web4 membawa internet ke level berikutnya.</p>
                        <div class="blog-meta"><span>📅 Mar 2025</span><span>⏱ 6 mnt</span></div>
                    </div>
                </article>'''
new3 = '''                <article class="blog-card glass reveal-stagger spotlight-card" data-tilt data-blog="3">
                    <div class="blog-thumb blog-thumb-3"><span class="blog-emoji">🔗</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Web3</span>
                        <h3>Web3 &amp; Web4: Masa Depan Internet Terdesentralisasi</h3>
                        <p>Eksplorasi blockchain, smart contract, dApp, dan bagaimana Web4 membawa internet ke level berikutnya.</p>
                        <div class="blog-meta"><span>📅 Mar 2025</span><span>⏱ 6 mnt</span></div>
                        <button class="btn btn-small blog-detail-btn" data-blog="3">Baca Selengkapnya →</button>
                    </div>
                </article>'''
assert html.count(old3) == 1, "blog card 3"
html = html.replace(old3, new3)

# --- 4) Tambah modal blog baru setelah modal proyek ---
anchor = '''    <!-- ================= BACK TO TOP ================= -->'''
blog_modal = '''    <!-- ================= MODAL BLOG / ARTIKEL ================= -->
    <div id="blog-modal-overlay"></div>
    <div id="blog-modal" role="dialog" aria-modal="true" aria-label="Detail Artikel">
        <button class="modal-close" aria-label="Tutup">✕</button>
        <div class="modal-body" id="blog-modal-body"></div>
    </div>

    <!-- ================= BACK TO TOP ================= -->'''
assert html.count(anchor) == 1, "back to top anchor"
html = html.replace(anchor, blog_modal)

io.open(PATH, "w", encoding="utf-8", newline="").write(html)

print("OK.")
print("data-blog cards  :", html.count('data-blog="'))
print("blog-detail-btn  :", html.count('blog-detail-btn'))
print("blog modal       :", 'id="blog-modal"' in html and 'id="blog-modal-overlay"' in html)

