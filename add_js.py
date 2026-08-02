# -*- coding: utf-8 -*-
"""Tambahkan fungsi JavaScript baru ke main.js untuk fitur modern."""
import io

PATH = "js/main.js"
js = io.open(PATH, encoding="utf-8").read()

# 1) Registrasi fungsi baru di DOMContentLoaded
old_init = """    initTiltSpotlight();
    initMagnetic();
});"""

new_init = """    initTiltSpotlight();
    initMagnetic();
    initLiveClock();
    initCustomCursor();
    initSectionDots();
    initScrollPercent();
    initToast();
    initFaqAccordion();
    initTestimonialCarousel();
    initClickBurst();
});"""

assert old_init in js, "init block not found!"
js = js.replace(old_init, new_init)

# 2) Tambahkan fungsi-fungsi baru di akhir file
new_funcs = '''
/* ============================================================
   17. LIVE CLOCK REAL-TIME
   ============================================================ */
function initLiveClock() {
    const timeEl = document.getElementById('clock-time');
    if (!timeEl) return;

    function update() {
        const now = new Date();
        const hh = String(now.getHours()).padStart(2, '0');
        const mm = String(now.getMinutes()).padStart(2, '0');
        const ss = String(now.getSeconds()).padStart(2, '0');
        timeEl.textContent = `${hh}:${mm}:${ss}`;
    }
    update();
    setInterval(update, 1000);
}

/* ============================================================
   18. CUSTOM CURSOR (DOT + RING)
   ============================================================ */
function initCustomCursor() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (window.matchMedia('(max-width: 768px)').matches) return;

    const dot = document.getElementById('cursor-dot');
    const ring = document.getElementById('cursor-ring');
    if (!dot || !ring) return;

    let mouseX = -100;
    let mouseY = -100;
    let ringX = mouseX;
    let ringY = mouseY;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        dot.style.left = `${mouseX}px`;
        dot.style.top = `${mouseY}px`;
    });

    // Perbesar ring saat hover elemen interaktif
    document.querySelectorAll('a, button, .nav-link, .btn, [data-tilt], .faq-question').forEach((el) => {
        el.addEventListener('mouseenter', () => ring.classList.add('hovering'));
        el.addEventListener('mouseleave', () => ring.classList.remove('hovering'));
    });

    function move() {
        ringX += (mouseX - ringX) * 0.16;
        ringY += (mouseY - ringY) * 0.16;
        ring.style.left = `${ringX}px`;
        ring.style.top = `${ringY}px`;
        requestAnimationFrame(move);
    }
    move();
}

/* ============================================================
   19. SECTION NAVIGATION DOTS
   ============================================================ */
function initSectionDots() {
    const container = document.getElementById('section-dots');
    if (!container) return;

    const sections = document.querySelectorAll('section[id]');
    const labels = {
        home: 'Beranda',
        tentang: 'Tentang',
        layanan: 'Layanan',
        keahlian: 'Keahlian',
        sertifikasi: 'Sertifikasi',
        blog: 'Blog',
        proyek: 'Proyek',
        testimoni: 'Testimoni',
        pendidikan: 'Pendidikan',
        faq: 'FAQ',
        kontak: 'Kontak'
    };

    sections.forEach((section) => {
        const dot = document.createElement('button');
        dot.className = 'dot';
        dot.dataset.label = labels[section.id] || section.id;
        dot.setAttribute('aria-label', `Ke ${labels[section.id] || section.id}`);
        dot.addEventListener('click', () => {
            section.scrollIntoView({ behavior: 'smooth' });
        });
        container.appendChild(dot);
    });

    const dots = container.querySelectorAll('.dot');
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    dots.forEach((d) => d.classList.remove('active'));
                    const idx = Array.from(sections).indexOf(entry.target);
                    if (dots[idx]) dots[idx].classList.add('active');
                }
            });
        },
        { threshold: 0.4 }
    );
    sections.forEach((s) => observer.observe(s));
}

/* ============================================================
   20. SCROLL PERCENTAGE
   ============================================================ */
function initScrollPercent() {
    const el = document.getElementById('scroll-percent');
    if (!el) return;

    const update = () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const percent = docHeight > 0 ? Math.round((scrollTop / docHeight) * 100) : 0;
        el.textContent = `${percent}%`;
        el.style.setProperty('--percent', `${percent}%`);
        el.classList.toggle('show', window.scrollY > 300);
    };

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
}

/* ============================================================
   21. TOAST NOTIFICATION
   ============================================================ */
function initToast() {
    window.showToast = (message, type = 'info') => {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const icons = { success: '✅', error: '⚠️', info: 'ℹ️' };
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `<span class="toast-icon">${icons[type] || 'ℹ️'}</span><span>${message}</span>`;
        container.appendChild(toast);

        requestAnimationFrame(() => toast.classList.add('show'));

        setTimeout(() => {
            toast.classList.add('hide');
            setTimeout(() => toast.remove(), 400);
        }, 3200);
    };
}

/* ============================================================
   22. FAQ ACCORDION
   ============================================================ */
function initFaqAccordion() {
    const items = document.querySelectorAll('.faq-item');
    if (!items.length) return;

    items.forEach((item) => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        question.addEventListener('click', () => {
            const isOpen = item.classList.contains('open');

            // Tutup semua
            items.forEach((it) => {
                it.classList.remove('open');
                it.querySelector('.faq-answer').style.maxHeight = '0px';
                it.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            });

            // Buka yang diklik bila sebelumnya tertutup
            if (!isOpen) {
                item.classList.add('open');
                answer.style.maxHeight = `${answer.scrollHeight}px`;
                question.setAttribute('aria-expanded', 'true');
            }
        });
    });
}

/* ============================================================
   23. TESTIMONIAL CAROUSEL
   ============================================================ */
function initTestimonialCarousel() {
    const track = document.getElementById('testimonial-track');
    const dotsWrap = document.getElementById('testimonial-dots');
    const prevBtn = document.getElementById('testimonial-prev');
    const nextBtn = document.getElementById('testimonial-next');
    if (!track) return;

    const slides = track.querySelectorAll('.testimonial-slide');
    const total = slides.length;
    let current = 0;
    let autoTimer;

    // Buat dots
    slides.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.className = 't-dot';
        dot.setAttribute('aria-label', `Testimoni ${i + 1}`);
        dot.addEventListener('click', () => goTo(i));
        dotsWrap.appendChild(dot);
    });
    const dots = dotsWrap.querySelectorAll('.t-dot');

    function goTo(index) {
        current = (index + total) % total;
        track.style.transform = `translateX(-${current * 100}%)`;
        dots.forEach((d, i) => d.classList.toggle('active', i === current));
    }

    function next() { goTo(current + 1); }
    function prev() { goTo(current - 1); }

    nextBtn.addEventListener('click', () => { next(); resetAuto(); });
    prevBtn.addEventListener('click', () => { prev(); resetAuto(); });

    function resetAuto() {
        clearInterval(autoTimer);
        autoTimer = setInterval(next, 5000);
    }

    // Hentikan auto saat hover
    const carousel = document.getElementById('testimonial-carousel');
    carousel.addEventListener('mouseenter', () => clearInterval(autoTimer));
    carousel.addEventListener('mouseleave', resetAuto);

    // Inisialisasi
    goTo(0);
    resetAuto();
}

/* ============================================================
   24. PARTICLE BURST SAAT KLIK
   ============================================================ */
function initClickBurst() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const colors = ['#00f0ff', '#ff2ec4', '#8b5cf6', '#00ffa3', '#7df9ff'];

    document.addEventListener('click', (e) => {
        // Jangan aktif saat mengklik tombol/aksi penting
        if (e.target.closest('button, a, .faq-question, .project-detail-btn, .theme-toggle, .hamburger')) return;

        const count = 12;
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('span');
            particle.className = 'burst-particle';
            particle.style.left = `${e.clientX + window.scrollX}px`;
            particle.style.top = `${e.clientY + window.scrollY}px`;
            particle.style.background = colors[Math.floor(Math.random() * colors.length)];

            const angle = (Math.PI * 2 * i) / count;
            const dist = 40 + Math.random() * 50;
            const dx = Math.cos(angle) * dist;
            const dy = Math.sin(angle) * dist;
            particle.style.setProperty('--dx', `${dx}px`);
            particle.style.setProperty('--dy', `${dy}px`);
            particle.style.setProperty('--size', `${3 + Math.random() * 5}px`);

            document.body.appendChild(particle);
            setTimeout(() => particle.remove(), 700);
        }
    });
}

'''

js += new_funcs

# Tambahkan CSS untuk burst-particle di akhir (dikombinasikan dengan add_css nanti,
# tapi kita tambahkan langsung di sini supaya JS-nya lengkap)
io.open(PATH, "w", encoding="utf-8", newline="").write(js)

# Verifikasi
checks = {
    "initLiveClock": "function initLiveClock" in js,
    "initCustomCursor": "function initCustomCursor" in js,
    "initSectionDots": "function initSectionDots" in js,
    "initScrollPercent": "function initScrollPercent" in js,
    "initToast": "function initToast" in js,
    "initFaqAccordion": "function initFaqAccordion" in js,
    "initTestimonialCarousel": "function initTestimonialCarousel" in js,
    "initClickBurst": "function initClickBurst" in js,
    "registered": "initLiveClock();" in js and "initClickBurst();" in js,
}
for k, v in checks.items():
    print(f"{k}: {v}")

