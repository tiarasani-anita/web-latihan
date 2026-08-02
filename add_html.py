# -*- coding: utf-8 -*-
"""Tambahkan elemen HTML baru: live clock, custom cursor, section dots,
   scroll percent, toast, services, testimonials, blog, FAQ."""
import io

PATH = "index.html"
html = io.open(PATH, encoding="utf-8").read()

marks = {}

# ---------- 1. Live Clock di navbar (setelah weather widget) ----------
clock_html = '''
                <!-- Live Clock WIB -->
                <div class="live-clock" id="live-clock" title="Waktu lokal Anda">
                    <span class="clock-icon">🕒</span>
                    <span class="clock-time" id="clock-time">--:--:--</span>
                </div>
'''
anchor = '<!-- Toggle Tema -->'
assert anchor in html
html = html.replace(anchor, clock_html + '\n' + anchor)

# ---------- 2. Fixed elements: cursor, section dots, scroll %, toast ----------
fixed_html = '''
    <!-- Custom Cursor -->
    <div class="cursor-dot" id="cursor-dot"></div>
    <div class="cursor-ring" id="cursor-ring"></div>

    <!-- Section Navigation Dots -->
    <nav class="section-dots" id="section-dots" aria-label="Navigasi section"></nav>

    <!-- Scroll Percentage Bubble -->
    <div class="scroll-percent" id="scroll-percent">0%</div>

    <!-- Toast Container -->
    <div class="toast-container" id="toast-container"></div>

'''
anchor = '<!-- ================= NAVBAR ================= -->'
assert anchor in html
html = html.replace(anchor, fixed_html + anchor)

# ---------- 3. Section LAYANAN setelah Tentang ----------
services_html = '''
    <!-- ================= LAYANAN ================= -->
    <section id="layanan" class="section">
        <div class="container">
            <div class="section-header reveal">
                <h2 class="section-title neon-edge-sm">Layanan <span class="gradient-text">Saya</span></h2>
                <div class="section-line"></div>
                <p class="section-sub reveal">Solusi digital modern untuk kebutuhan Anda</p>
            </div>

            <div class="services-bento">
                <div class="service-card glass reveal spotlight-card bento-wide" data-tilt>
                    <div class="service-icon">🌐</div>
                    <h3>Web Development</h3>
                    <p>Website modern, responsif, cepat, dan SEO-friendly — dari landing page hingga aplikasi web lengkap.</p>
                    <div class="service-tags"><span>HTML</span><span>CSS</span><span>JS</span><span>PHP</span></div>
                </div>
                <div class="service-card glass reveal spotlight-card" data-tilt>
                    <div class="service-icon">📱</div>
                    <h3>App Development</h3>
                    <p>Pengembangan aplikasi mobile lintas platform dengan pengalaman pengguna yang mulus.</p>
                    <div class="service-tags"><span>React Native</span><span>Flutter</span></div>
                </div>
                <div class="service-card glass reveal spotlight-card" data-tilt>
                    <div class="service-icon">📊</div>
                    <h3>Data Analytics</h3>
                    <p>Transformasi data mentah menjadi insight bisnis melalui visualisasi dan analisis mendalam.</p>
                    <div class="service-tags"><span>Python</span><span>SQL</span><span>Power BI</span></div>
                </div>
                <div class="service-card glass reveal spotlight-card" data-tilt>
                    <div class="service-icon">🎨</div>
                    <h3>UI/UX Design</h3>
                    <p>Desain antarmuka yang indah, intuitif, dan berfokus pada kebutuhan pengguna.</p>
                    <div class="service-tags"><span>Figma</span><span>Prototype</span></div>
                </div>
                <div class="service-card glass reveal spotlight-card" data-tilt>
                    <div class="service-icon">🔐</div>
                    <h3>Cyber Security</h3>
                    <p>Audit keamanan, enkripsi data, dan perlindungan aplikasi dari ancaman siber umum.</p>
                    <div class="service-tags"><span>Audit</span><span>Enkripsi</span><span>Best Practice</span></div>
                </div>
                <div class="service-card glass reveal spotlight-card bento-wide" data-tilt>
                    <div class="service-icon">💹</div>
                    <h3>Financial &amp; Trading Tech</h3>
                    <p>Solusi teknologi untuk investasi emas, saham lokal &amp; asing, crypto, blockchain, Web3, dan Web4.</p>
                    <div class="service-tags"><span>Python</span><span>API</span><span>Web3</span><span>dApp</span></div>
                </div>
            </div>
        </div>
    </section>

'''
anchor = '<!-- ================= KEAHLIAN ================= -->'
assert anchor in html
html = html.replace(anchor, services_html + anchor)

# ---------- 4. Section BLOG setelah Sertifikasi ----------
blog_html = '''
    <!-- ================= BLOG / ARTIKEL ================= -->
    <section id="blog" class="section">
        <div class="container">
            <div class="section-header reveal">
                <h2 class="section-title neon-edge-sm">Blog &amp; <span class="gradient-text">Artikel</span></h2>
                <div class="section-line"></div>
            </div>

            <div class="blog-grid">
                <article class="blog-card glass reveal spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-1"><span class="blog-emoji">🤖</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Teknologi</span>
                        <h3>Mengenal Kecerdasan Buatan di Era Modern</h3>
                        <p>Bagaimana AI mengubah cara kita bekerja, belajar, dan mengambil keputusan di berbagai bidang.</p>
                        <div class="blog-meta"><span>📅 Jan 2025</span><span>⏱ 5 mnt</span></div>
                    </div>
                </article>
                <article class="blog-card glass reveal spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-2"><span class="blog-emoji">🪙</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Finance</span>
                        <h3>Panduan Investasi Emas &amp; Saham untuk Pemula</h3>
                        <p>Langkah awal membangun portofolio investasi: emas, saham lokal, hingga saham luar negeri.</p>
                        <div class="blog-meta"><span>📅 Feb 2025</span><span>⏱ 7 mnt</span></div>
                    </div>
                </article>
                <article class="blog-card glass reveal spotlight-card" data-tilt>
                    <div class="blog-thumb blog-thumb-3"><span class="blog-emoji">🔗</span></div>
                    <div class="blog-body">
                        <span class="blog-cat">Web3</span>
                        <h3>Web3 &amp; Web4: Masa Depan Internet Terdesentralisasi</h3>
                        <p>Eksplorasi blockchain, smart contract, dApp, dan bagaimana Web4 membawa internet ke level berikutnya.</p>
                        <div class="blog-meta"><span>📅 Mar 2025</span><span>⏱ 6 mnt</span></div>
                    </div>
                </article>
            </div>
        </div>
    </section>

'''
anchor = '<!-- ================= PROYEK ================= -->'
assert anchor in html
html = html.replace(anchor, blog_html + anchor)

# ---------- 5. Section TESTIMONI setelah Proyek ----------
testimonial_html = '''
    <!-- ================= TESTIMONI ================= -->
    <section id="testimoni" class="section">
        <div class="container">
            <div class="section-header reveal">
                <h2 class="section-title neon-edge-sm">Kata <span class="gradient-text">Mereka</span></h2>
                <div class="section-line"></div>
            </div>

            <div class="testimonial-carousel reveal" id="testimonial-carousel">
                <div class="testimonial-track" id="testimonial-track">
                    <div class="testimonial-slide">
                        <div class="testimonial-card glass gradient-border">
                            <div class="testimonial-quote">❝</div>
                            <p class="testimonial-text">"Anita sangat profesional dan cepat. Website yang dibuatnya modern, responsif, dan sesuai dengan kebutuhan bisnis kami."</p>
                            <div class="testimonial-author">
                                <div class="testimonial-avatar">RS</div>
                                <div>
                                    <h4>Raka Saputra</h4>
                                    <span>Founder · Startup Tech</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-slide">
                        <div class="testimonial-card glass gradient-border">
                            <div class="testimonial-quote">❝</div>
                            <p class="testimonial-text">"Kemampuan analisis datanya luar biasa! Insight yang disajikan sangat membantu pengambilan keputusan di perusahaan kami."</p>
                            <div class="testimonial-author">
                                <div class="testimonial-avatar">DN</div>
                                <div>
                                    <h4>Dewi Nugraha</h4>
                                    <span>Data Lead · E-Commerce</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-slide">
                        <div class="testimonial-card glass gradient-border">
                            <div class="testimonial-quote">❝</div>
                            <p class="testimonial-text">"Aplikasi catatan keuangan yang dibuat Anita sangat membantu saya mengelola keuangan pribadi. UI-nya bersih dan mudah dipakai."</p>
                            <div class="testimonial-author">
                                <div class="testimonial-avatar">BF</div>
                                <div>
                                    <h4>Bima Firmansyah</h4>
                                    <span>Freelancer</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-slide">
                        <div class="testimonial-card glass gradient-border">
                            <div class="testimonial-quote">❝</div>
                            <p class="testimonial-text">"Kolaborasi dengan Anita sangat menyenangkan. Ide kreatifnya dan pemahaman tentang Web3 &amp; blockchain melampaui ekspektasi."</p>
                            <div class="testimonial-author">
                                <div class="testimonial-avatar">SL</div>
                                <div>
                                    <h4>Salsabila Lestari</h4>
                                    <span>Project Manager · Fintech</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-nav">
                    <button class="testimonial-arrow" id="testimonial-prev" aria-label="Sebelumnya">←</button>
                    <div class="testimonial-dots" id="testimonial-dots"></div>
                    <button class="testimonial-arrow" id="testimonial-next" aria-label="Berikutnya">→</button>
                </div>
            </div>
        </div>
    </section>

'''
anchor = '<!-- ================= PENDIDIKAN & PENGALAMAN ================= -->'
assert anchor in html
html = html.replace(anchor, testimonial_html + anchor)

# ---------- 6. Section FAQ sebelum Kontak ----------
faq_html = '''
    <!-- ================= FAQ ================= -->
    <section id="faq" class="section">
        <div class="container">
            <div class="section-header reveal">
                <h2 class="section-title neon-edge-sm">FAQ <span class="gradient-text">Sering Ditanya</span></h2>
                <div class="section-line"></div>
            </div>

            <div class="faq-list reveal" id="faq-list">
                <div class="faq-item glass">
                    <button class="faq-question" type="button" aria-expanded="false">
                        <span>Layanan apa saja yang Anda tawarkan?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer"><p>Saya menawarkan web development, app development, analisis data, UI/UX design, audit keamanan siber, serta solusi financial tech &amp; trading (emas, saham, crypto, Web3).</p></div>
                </div>
                <div class="faq-item glass">
                    <button class="faq-question" type="button" aria-expanded="false">
                        <span>Berapa lama waktu pengerjaan proyek?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer"><p>Tergantung kompleksitas. Landing page sekitar 3–7 hari, aplikasi web/mobile 2–6 minggu, dan proyek analisis data 1–3 minggu.</p></div>
                </div>
                <div class="faq-item glass">
                    <button class="faq-question" type="button" aria-expanded="false">
                        <span>Apakah menerima proyek magang atau kolaborasi?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer"><p>Ya! Saya terbuka untuk proyek magang, kolaborasi riset, atau kontribusi ke open source. Silakan hubungi melalui form kontak.</p></div>
                </div>
                <div class="faq-item glass">
                    <button class="faq-question" type="button" aria-expanded="false">
                        <span>Teknologi apa yang biasa Anda gunakan?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer"><p>HTML/CSS/JS, Python, PHP, SQL, React Native, Laravel, Three.js, dan berbagai tools data seperti Pandas, Power BI, serta teknologi blockchain/Web3.</p></div>
                </div>
                <div class="faq-item glass">
                    <button class="faq-question" type="button" aria-expanded="false">
                        <span>Bagaimana cara memulai proyek dengan Anda?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer"><p>Klik "Hubungi Saya" dan isi form dengan detail kebutuhan Anda. Saya akan merespons maksimal 1x24 jam untuk diskusi awal secara gratis.</p></div>
                </div>
            </div>
        </div>
    </section>

'''
anchor = '<!-- ================= KONTAK ================= -->'
assert anchor in html
html = html.replace(anchor, faq_html + anchor)

# ---------- Simpan ----------
io.open(PATH, "w", encoding="utf-8", newline="").write(html)

checks = {
    "live-clock": 'id="live-clock"' in html,
    "cursor-dot": 'id="cursor-dot"' in html,
    "section-dots": 'id="section-dots"' in html,
    "scroll-percent": 'id="scroll-percent"' in html,
    "toast-container": 'id="toast-container"' in html,
    "layanan": 'id="layanan"' in html,
    "blog": 'id="blog"' in html,
    "testimoni": 'id="testimoni"' in html,
    "faq": 'id="faq"' in html,
    "services count": html.count('class="service-card'),
    "blog count": html.count('class="blog-card'),
    "testimonial count": html.count('class="testimonial-slide'),
    "faq count": html.count('class="faq-item'),
}
for k, v in checks.items():
    print(f"{k}: {v}")

