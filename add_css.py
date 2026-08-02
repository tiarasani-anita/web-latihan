# -*- coding: utf-8 -*-
"""Tambahkan CSS untuk fitur-fitur baru."""
import io

PATH = "css/style.css"
css = io.open(PATH, encoding="utf-8").read()

new_css = '''
/* ============================================================
   FITUR BARU - MODERN & INTERAKTIF
   ============================================================ */

/* ---------- LIVE CLOCK ---------- */
.live-clock {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 40px;
    padding: 5px 12px;
    backdrop-filter: blur(8px);
    cursor: default;
    transition: var(--transition);
    animation: navFloat 3.6s ease-in-out 0.6s infinite;
}

.live-clock:hover {
    box-shadow: var(--shadow-neon);
    transform: translateY(-2px);
}

.clock-icon {
    font-size: 0.95rem;
}

.clock-time {
    font-family: 'Sora', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--neon-cyan);
    letter-spacing: 0.5px;
    font-variant-numeric: tabular-nums;
}

/* ---------- CUSTOM CURSOR ---------- */
.cursor-dot,
.cursor-ring {
    position: fixed;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 10000;
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

.cursor-dot {
    width: 8px;
    height: 8px;
    background: var(--neon-cyan);
    box-shadow: 0 0 10px var(--neon-cyan);
    transition: opacity 0.2s ease;
}

.cursor-ring {
    width: 36px;
    height: 36px;
    border: 1.5px solid var(--neon-magenta);
    box-shadow: 0 0 12px rgba(255, 46, 196, 0.3);
    transition: width 0.25s ease, height 0.25s ease, border-color 0.25s ease, opacity 0.2s ease;
}

.cursor-ring.hovering {
    width: 56px;
    height: 56px;
    border-color: var(--neon-cyan);
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
}

@media (max-width: 768px), (prefers-reduced-motion: reduce) {
    .cursor-dot, .cursor-ring { display: none; }
}

/* ---------- SECTION DOTS ---------- */
.section-dots {
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 999;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.section-dots .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: 1.5px solid var(--neon-cyan);
    background: transparent;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
}

.section-dots .dot:hover {
    background: var(--neon-cyan);
    box-shadow: 0 0 10px var(--neon-cyan);
}

.section-dots .dot.active {
    background: var(--neon-magenta);
    border-color: var(--neon-magenta);
    box-shadow: 0 0 12px var(--neon-magenta);
    transform: scale(1.3);
}

.section-dots .dot::after {
    content: attr(data-label);
    position: absolute;
    right: 22px;
    top: 50%;
    transform: translateY(-50%) translateX(8px);
    white-space: nowrap;
    font-size: 0.68rem;
    font-family: 'Sora', sans-serif;
    color: var(--text-primary);
    background: var(--nav-bg);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 4px 10px;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    backdrop-filter: blur(8px);
}

.section-dots .dot:hover::after {
    opacity: 1;
    visibility: visible;
    transform: translateY(-50%) translateX(0);
}

@media (max-width: 768px) {
    .section-dots { display: none; }
}

/* ---------- SCROLL PERCENTAGE ---------- */
.scroll-percent {
    position: fixed;
    bottom: 28px;
    left: 28px;
    z-index: 998;
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-family: 'Sora', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--neon-cyan);
    background: var(--nav-bg);
    border: 1px solid var(--border-color);
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-neon);
    opacity: 0;
    visibility: hidden;
    transform: translateY(18px);
    transition: var(--transition);
}

.scroll-percent.show {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.scroll-percent::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 50%;
    padding: 2px;
    background: conic-gradient(var(--neon-cyan) var(--percent, 0%), transparent var(--percent, 0%));
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
    mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    mask-composite: exclude;
    pointer-events: none;
}

@media (max-width: 768px) {
    .scroll-percent { display: none; }
}

/* ---------- TOAST NOTIFICATION ---------- */
.toast-container {
    position: fixed;
    top: 90px;
    right: 20px;
    z-index: 10001;
    display: flex;
    flex-direction: column;
    gap: 10px;
    pointer-events: none;
}

.toast {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 260px;
    max-width: 340px;
    padding: 13px 18px;
    border-radius: 14px;
    background: var(--nav-bg);
    border: 1px solid var(--border-color);
    backdrop-filter: blur(14px);
    box-shadow: var(--shadow-neon);
    color: var(--text-primary);
    font-size: 0.88rem;
    font-family: 'Inter', sans-serif;
    transform: translateX(120%);
    opacity: 0;
    transition: transform 0.4s cubic-bezier(0.22, 0.61, 0.36, 1), opacity 0.4s ease;
    pointer-events: auto;
}

.toast.show {
    transform: translateX(0);
    opacity: 1;
}

.toast.hide {
    transform: translateX(120%);
    opacity: 0;
}

.toast-icon {
    font-size: 1.2rem;
    flex-shrink: 0;
}

.toast.success { border-color: rgba(0, 255, 163, 0.5); }
.toast.error { border-color: rgba(255, 46, 196, 0.5); }
.toast.info { border-color: rgba(0, 240, 255, 0.5); }

/* ---------- SECTION SUBTITLE ---------- */
.section-sub {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-top: 10px;
}

/* ---------- LAYANAN (BENTO GRID) ---------- */
.services-bento {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.service-card {
    padding: 30px 26px;
    border-radius: 18px;
    position: relative;
    overflow: hidden;
    min-height: 220px;
    display: flex;
    flex-direction: column;
}

.service-card::before {
    content: '';
    position: absolute;
    top: -30px;
    right: -30px;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: radial-gradient(circle, var(--glow-soft), transparent 70%);
    opacity: 0.5;
}

.bento-wide {
    grid-column: span 1;
}

.service-icon {
    font-size: 2.4rem;
    margin-bottom: 14px;
    filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.4));
    transition: transform 0.4s ease;
}

.service-card:hover .service-icon {
    transform: scale(1.15) rotate(-8deg);
}

.service-card h3 {
    font-family: 'Sora', sans-serif;
    font-size: 1.15rem;
    margin-bottom: 10px;
}

.service-card p {
    color: var(--text-secondary);
    font-size: 0.88rem;
    flex: 1;
    margin-bottom: 16px;
}

.service-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.service-tags span {
    font-size: 0.7rem;
    padding: 4px 10px;
    border-radius: 20px;
    border: 1px solid var(--border-color);
    color: var(--neon-cyan);
    background: var(--glow-soft);
}

/* ---------- BLOG / ARTIKEL ---------- */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 28px;
}

.blog-card {
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.blog-thumb {
    height: 160px;
    display: grid;
    place-items: center;
    position: relative;
    overflow: hidden;
}

.blog-thumb::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0, 240, 255, 0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.12) 1px, transparent 1px);
    background-size: 36px 36px;
    animation: thumbGrid 8s linear infinite;
}

.blog-thumb-1 { background: linear-gradient(135deg, #00f0ff22, #8b5cf622); }
.blog-thumb-2 { background: linear-gradient(135deg, #ff2ec422, #00ffa322); }
.blog-thumb-3 { background: linear-gradient(135deg, #8b5cf622, #00f0ff22); }

.blog-emoji {
    position: relative;
    z-index: 2;
    font-size: 3.2rem;
    filter: drop-shadow(0 0 16px rgba(0, 240, 255, 0.5));
    transition: transform 0.5s ease;
}

.blog-card:hover .blog-emoji {
    transform: scale(1.2) rotate(8deg);
}

.blog-body {
    padding: 24px;
    display: flex;
    flex-direction: column;
    flex: 1;
}

.blog-cat {
    align-self: flex-start;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    color: var(--neon-magenta);
    background: rgba(255, 46, 196, 0.08);
    border: 1px solid rgba(255, 46, 196, 0.35);
    margin-bottom: 12px;
}

.blog-body h3 {
    font-family: 'Sora', sans-serif;
    font-size: 1.05rem;
    margin-bottom: 10px;
    line-height: 1.4;
}

.blog-body p {
    color: var(--text-secondary);
    font-size: 0.86rem;
    flex: 1;
    margin-bottom: 16px;
}

.blog-meta {
    display: flex;
    gap: 16px;
    font-size: 0.75rem;
    color: var(--text-secondary);
}

/* ---------- TESTIMONI CAROUSEL ---------- */
.testimonial-carousel {
    max-width: 720px;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
}

.testimonial-track {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1);
}

.testimonial-slide {
    min-width: 100%;
    padding: 8px;
}

.testimonial-card {
    padding: 40px 36px;
    text-align: center;
    border-radius: 20px;
    position: relative;
}

.testimonial-quote {
    font-size: 3.5rem;
    font-family: Georgia, serif;
    color: var(--neon-cyan);
    text-shadow: 0 0 16px rgba(0, 240, 255, 0.5);
    line-height: 1;
    margin-bottom: 8px;
}

.testimonial-text {
    color: var(--text-primary);
    font-size: 1.02rem;
    font-style: italic;
    margin-bottom: 24px;
    line-height: 1.7;
}

.testimonial-author {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
}

.testimonial-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-family: 'Sora', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    color: #060913;
    background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
    box-shadow: 0 0 14px var(--glow-soft);
}

.testimonial-author h4 {
    font-family: 'Sora', sans-serif;
    font-size: 0.95rem;
    text-align: left;
}

.testimonial-author span {
    display: block;
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-align: left;
}

.testimonial-nav {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-top: 24px;
}

.testimonial-arrow {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--neon-cyan);
    font-size: 1rem;
    cursor: pointer;
    transition: var(--transition);
    display: grid;
    place-items: center;
}

.testimonial-arrow:hover {
    background: var(--neon-cyan);
    color: #060913;
    box-shadow: 0 0 18px var(--glow-soft);
    transform: scale(1.1);
}

.testimonial-dots {
    display: flex;
    gap: 8px;
}

.testimonial-dots .t-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    border: 1px solid var(--neon-cyan);
    background: transparent;
    cursor: pointer;
    transition: all 0.3s ease;
}

.testimonial-dots .t-dot.active {
    background: var(--neon-magenta);
    border-color: var(--neon-magenta);
    box-shadow: 0 0 10px var(--neon-magenta);
    transform: scale(1.3);
}

/* ---------- FAQ ACCORDION ---------- */
.faq-list {
    max-width: 720px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.faq-item {
    border-radius: 14px;
    overflow: hidden;
    transition: var(--transition);
}

.faq-item:hover {
    border-color: var(--neon-cyan);
    box-shadow: var(--shadow-neon);
}

.faq-question {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 18px 22px;
    background: transparent;
    border: none;
    color: var(--text-primary);
    font-family: 'Sora', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    text-align: left;
    cursor: pointer;
    transition: var(--transition);
}

.faq-question:hover {
    color: var(--neon-cyan);
}

.faq-icon {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    border: 1px solid var(--border-color);
    color: var(--neon-cyan);
    font-size: 1.1rem;
    flex-shrink: 0;
    transition: transform 0.4s ease, background 0.3s ease, color 0.3s ease;
}

.faq-item.open .faq-icon {
    transform: rotate(45deg);
    background: var(--neon-cyan);
    color: #060913;
    border-color: var(--neon-cyan);
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.45s cubic-bezier(0.22, 0.61, 0.36, 1);
}

.faq-answer p {
    padding: 0 22px 20px;
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.7;
}

/* ---------- RESPONSIVE FITUR BARU ---------- */
@media (max-width: 900px) {
    .services-bento {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .services-bento {
        grid-template-columns: 1fr;
    }

    .live-clock {
        display: none;
    }

    .testimonial-card {
        padding: 30px 22px;
    }
}

/* ---------- NAVBAR: Sembunyikan clock di layar sangat kecil ---------- */
@media (max-width: 480px) {
    .weather-widget {
        display: none;
    }
}
'''

css += new_css
io.open(PATH, "w", encoding="utf-8", newline="").write(css)

checks = {
    "live-clock": ".live-clock" in css,
    "cursor-dot": ".cursor-dot" in css,
    "section-dots": ".section-dots" in css,
    "scroll-percent": ".scroll-percent" in css,
    "toast": ".toast" in css,
    "services-bento": ".services-bento" in css,
    "blog-grid": ".blog-grid" in css,
    "testimonial-carousel": ".testimonial-carousel" in css,
    "faq-list": ".faq-list" in css,
}
for k, v in checks.items():
    print(f"{k}: {v}")

