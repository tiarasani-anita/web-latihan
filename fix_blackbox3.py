# -*- coding: utf-8 -*-
"""SOLUSI FINAL KOTAK HITAM:
filter: drop-shadow() pada elemen dengan background-clip:text
+ -webkit-text-fill-color:transparent -> BUG kotak hitam di Chrome.

Ganti SEMUA filter: drop-shadow() pada elemen teks gradient menjadi
text-shadow (aman, mengikuti bentuk glyph, bukan kotak).
"""
import io

PATH = r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css"
css = io.open(PATH, encoding="utf-8").read()

reps = []

# 1) .hero-name utama
reps.append((
    """    animation: floatName 7s ease-in-out infinite, gradientMove 8s linear infinite;
    filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.28)) drop-shadow(0 0 30px rgba(255, 46, 196, 0.16));
    will-change: transform, filter;""",
    """    animation: floatName 7s ease-in-out infinite, gradientMove 8s linear infinite;
    text-shadow: 0 0 12px rgba(0, 240, 255, 0.28), 0 0 30px rgba(255, 46, 196, 0.16);
    will-change: transform;"""
))

# 2) .neon-edge umum
reps.append((
    """.neon-edge {
    filter: drop-shadow(0 0 2px rgba(255,255,255,0.55)) drop-shadow(0 0 8px rgba(0,240,255,0.55)) drop-shadow(0 0 22px rgba(255,46,196,0.35)) drop-shadow(0 0 44px rgba(139,92,246,0.2));
}""",
    """.neon-edge {
    text-shadow: 0 0 2px rgba(255,255,255,0.55), 0 0 8px rgba(0,240,255,0.55), 0 0 22px rgba(255,46,196,0.35), 0 0 44px rgba(139,92,246,0.2);
}"""
))

# 3) .neon-edge-sm umum
reps.append((
    """.neon-edge-sm {
    filter: drop-shadow(0 0 2px rgba(255,255,255,0.5)) drop-shadow(0 0 7px rgba(0,240,255,0.5)) drop-shadow(0 0 16px rgba(255,46,196,0.3));
}""",
    """.neon-edge-sm {
    text-shadow: 0 0 2px rgba(255,255,255,0.5), 0 0 7px rgba(0,240,255,0.5), 0 0 16px rgba(255,46,196,0.3);
}"""
))

# 4) .hero-name.neon-edge
reps.append((
    """    animation: gradientMove 8s linear infinite, floatName 7s ease-in-out infinite;
    filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.45)) drop-shadow(0 0 8px rgba(0, 240, 255, 0.5)) drop-shadow(0 0 18px rgba(255, 46, 196, 0.35)) drop-shadow(0 0 36px rgba(139, 92, 246, 0.25));""",
    """    animation: gradientMove 8s linear infinite, floatName 7s ease-in-out infinite;
    text-shadow: 0 0 3px rgba(255, 255, 255, 0.45), 0 0 8px rgba(0, 240, 255, 0.5), 0 0 18px rgba(255, 46, 196, 0.35), 0 0 36px rgba(139, 92, 246, 0.25);"""
))

# 5) [data-theme="light"] .neon-edge
reps.append((
    """[data-theme="light"] .neon-edge {
    filter: drop-shadow(0 0 3px rgba(255,255,255,0.9)) drop-shadow(0 0 8px rgba(0,240,255,0.55)) drop-shadow(0 0 16px rgba(255,46,196,0.35));
}""",
    """[data-theme="light"] .neon-edge {
    text-shadow: 0 0 3px rgba(255,255,255,0.9), 0 0 8px rgba(0,240,255,0.55), 0 0 16px rgba(255,46,196,0.35);
}"""
))

# 6) [data-theme="light"] .neon-edge-sm
reps.append((
    """[data-theme="light"] .neon-edge-sm {
    filter: drop-shadow(0 0 3px rgba(255,255,255,0.9)) drop-shadow(0 0 8px rgba(0,240,255,0.5)) drop-shadow(0 0 14px rgba(255,46,196,0.3));
}""",
    """[data-theme="light"] .neon-edge-sm {
    text-shadow: 0 0 3px rgba(255,255,255,0.9), 0 0 8px rgba(0,240,255,0.5), 0 0 14px rgba(255,46,196,0.3);
}"""
))

# 7) [data-theme="light"] .hero-name.neon-edge
reps.append((
    """[data-theme="light"] .hero-name.neon-edge {
    /* Glow lembut via filter (mengikuti bentuk huruf, bukan kotak) */
    filter: drop-shadow(0 0 4px rgba(0, 240, 255, 0.4)) drop-shadow(0 0 10px rgba(255, 46, 196, 0.3));
}""",
    """[data-theme="light"] .hero-name.neon-edge {
    /* Glow lembut via text-shadow (mengikuti bentuk huruf, bukan kotak) */
    text-shadow: 0 0 4px rgba(0, 240, 255, 0.4), 0 0 10px rgba(255, 46, 196, 0.3);
}"""
))

# 8) .gradient-text lengkap
reps.append((
    """.gradient-text {
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
    -webkit-background-clip: text;
    background-clip: text;
    color: var(--neon-cyan);
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 6px rgba(0, 240, 255, 0.25));
}""",
    """.gradient-text {
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
    -webkit-background-clip: text;
    background-clip: text;
    color: var(--neon-cyan);
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 6px rgba(0, 240, 255, 0.25);
}"""
))

# 9) [data-theme="light"] .gradient-text
reps.append((
    """[data-theme="light"] .gradient-text {
    filter: drop-shadow(0 0 6px rgba(0, 240, 255, 0.25));
}""",
    """[data-theme="light"] .gradient-text {
    text-shadow: 0 0 6px rgba(0, 240, 255, 0.25);
}"""
))

for old, new in reps:
    cnt = css.count(old)
    if cnt != 1:
        print("PERINGATAN - kemunculan", cnt, "untuk:", old[:60])
    css = css.replace(old, new)

io.open(PATH, "w", encoding="utf-8", newline="").write(css)
print("OK. Semua filter drop-shadow pada teks gradient diganti text-shadow.")

