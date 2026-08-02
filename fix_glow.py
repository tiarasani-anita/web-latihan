# -*- coding: utf-8 -*-
"""Modernisasi glow teks agar lebih premium & tidak kuno."""
import io

CSS = r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css"

with io.open(CSS, encoding="utf-8") as f:
    css = f.read()

# Daftar perubahan glow: string lama -> string baru
repls = [
    # .hero-role glow
    ('text-shadow: 0 0 12px var(--neon-cyan);\n}\n\n.type-cursor {',
     'text-shadow: 0 0 8px rgba(0, 240, 255, 0.5);\n}\n\n.type-cursor {'),
    # .stat-number glow
    ('text-shadow: 0 0 14px var(--neon-cyan);\n}\n\n.stat-plus {',
     'text-shadow: 0 0 8px rgba(0, 240, 255, 0.5);\n}\n\n.stat-plus {'),
    # .neon-dot glow
    ('text-shadow: 0 0 10px var(--neon-magenta);\n}\n\n/* Link navigasi */',
     'text-shadow: 0 0 8px rgba(255, 46, 196, 0.5);\n}\n\n/* Link navigasi */'),
    # .skill-percent glow
    ('text-shadow: 0 0 10px var(--neon-cyan);\n}\n\n.skill-bar {',
     'text-shadow: 0 0 8px rgba(0, 240, 255, 0.45);\n}\n\n.skill-bar {'),
    # .timeline-date glow
    ('text-shadow: 0 0 8px rgba(255, 46, 196, 0.4);',
     'text-shadow: 0 0 6px rgba(255, 46, 196, 0.35);'),
    # .weather-temp glow
    ('text-shadow: 0 0 8px var(--glow-soft);\n}\n\n.skill-bar {',
     'text-shadow: 0 0 6px rgba(0, 240, 255, 0.4);\n}\n\n.skill-bar {'),
    # .preloader-logo glow
    ('text-shadow: 0 0 24px var(--neon-cyan), 0 0 64px var(--neon-magenta);',
     'text-shadow: 0 0 18px rgba(0, 240, 255, 0.5), 0 0 40px rgba(255, 46, 196, 0.3);'),
    # .cert-badge glow
    ('filter: drop-shadow(0 0 14px var(--neon-cyan));',
     'filter: drop-shadow(0 0 8px rgba(0, 240, 255, 0.4));'),
    # .gradient-text glow
    ('filter: drop-shadow(0 0 10px rgba(0, 240, 255, 0.3));',
     'filter: drop-shadow(0 0 6px rgba(0, 240, 255, 0.25));'),
]

count = 0
for old, new in repls:
    if old in css:
        css = css.replace(old, new)
        count += 1
    else:
        print("TIDAK KETEMU:", old[:60])

with io.open(CSS, "w", encoding="utf-8", newline="") as f:
    f.write(css)

print(f"OK. {count} perubahan diterapkan.")
