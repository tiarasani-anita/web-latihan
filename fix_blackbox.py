# -*- coding: utf-8 -*-
"""Hilangkan KOTAK HITAM pada teks gradient/neon.

Penyebab: text-shadow pada elemen dengan -webkit-text-fill-color:transparent
          + background-clip:text dirender sebagai kotak gelap di belakang
          teks oleh Chrome.
Solusi : ganti text-shadow -> filter: drop-shadow() yang mengikuti bentuk
          huruf (alpha channel), sehingga glow tetap ada tanpa kotak.
"""
import io

PATH = r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css"
css = io.open(PATH, encoding="utf-8").read()

reps = []

# 1) .hero-name (utama): text-shadow -> filter drop-shadow
reps.append((
    """    animation: floatName 7s ease-in-out infinite, gradientMove 8s linear infinite;
    text-shadow: 0 0 12px rgba(0, 240, 255, 0.28), 0 0 30px rgba(255, 46, 196, 0.16);
    will-change: transform;
}""",
    """    animation: floatName 7s ease-in-out infinite, gradientMove 8s linear infinite;
    filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.28)) drop-shadow(0 0 30px rgba(255, 46, 196, 0.16));
    will-change: transform, filter;
}"""
))

# 2) .hero-name.neon-edge (blok duplikat awal)
reps.append((
    """.hero-name.neon-edge {
    /* Gradasi tetap hidup, tapi glow lebih lembut (tanpa filter agar tidak kotak hitam) */
    text-shadow: 0 0 4px rgba(0, 240, 255, 0.4), 0 0 10px rgba(255, 46, 196, 0.3);
}""",
    """.hero-name.neon-edge {
    /* Glow lembut via filter (mengikuti bentuk huruf, bukan kotak) */
    filter: drop-shadow(0 0 4px rgba(0, 240, 255, 0.4)) drop-shadow(0 0 10px rgba(255, 46, 196, 0.3));
}"""
))

# 3) .hero-name.neon-edge (blok lengkap)
reps.append((
    """    animation: gradientMove 8s linear infinite, floatName 7s ease-in-out infinite;
    text-shadow: 0 0 3px rgba(255, 255, 255, 0.45), 0 0 8px rgba(0, 240, 255, 0.5), 0 0 18px rgba(255, 46, 196, 0.35), 0 0 36px rgba(139, 92, 246, 0.25);
}""",
    """    animation: gradientMove 8s linear infinite, floatName 7s ease-in-out infinite;
    filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.45)) drop-shadow(0 0 8px rgba(0, 240, 255, 0.5)) drop-shadow(0 0 18px rgba(255, 46, 196, 0.35)) drop-shadow(0 0 36px rgba(139, 92, 246, 0.25));
}"""
))

# 4) .gradient-text (blok duplikat awal)
reps.append((
    """.gradient-text {
    text-shadow: 0 0 6px rgba(0, 240, 255, 0.25);
}""",
    """.gradient-text {
    filter: drop-shadow(0 0 6px rgba(0, 240, 255, 0.25));
}"""
))

# 5) .gradient-text (blok lengkap)
reps.append((
    """.gradient-text {
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
    -webkit-background-clip: text;
    background-clip: text;
    color: var(--neon-cyan);
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 6px rgba(0, 240, 255, 0.25);
}""",
    """.gradient-text {
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
    -webkit-background-clip: text;
    background-clip: text;
    color: var(--neon-cyan);
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 6px rgba(0, 240, 255, 0.25));
}"""
))

# 6) Keyframes floatName: buang text-shadow (sumber kotak hitam saat animasi)
reps.append((
    """@keyframes floatName {
    0%, 100% {
        transform: perspective(700px) rotateX(0deg) rotateY(0deg) translateY(0);
        text-shadow: 0 12px 30px rgba(0, 240, 255, 0.25);
    }
    25% {
        transform: perspective(700px) rotateX(5deg) rotateY(-8deg) translateY(-14px);
        text-shadow: 0 22px 44px rgba(255, 46, 196, 0.35);
    }
    50% {
        transform: perspective(700px) rotateX(-3deg) rotateY(6deg) translateY(0);
        text-shadow: 0 8px 26px rgba(139, 92, 246, 0.3);
    }
    75% {
        transform: perspective(700px) rotateX(4deg) rotateY(-5deg) translateY(-10px);
        text-shadow: 0 18px 40px rgba(0, 240, 255, 0.35);
    }
}""",
    """@keyframes floatName {
    0%, 100% {
        transform: perspective(700px) rotateX(0deg) rotateY(0deg) translateY(0);
    }
    25% {
        transform: perspective(700px) rotateX(5deg) rotateY(-8deg) translateY(-14px);
    }
    50% {
        transform: perspective(700px) rotateX(-3deg) rotateY(6deg) translateY(0);
    }
    75% {
        transform: perspective(700px) rotateX(4deg) rotateY(-5deg) translateY(-10px);
    }
}"""
))

for old, new in reps:
    assert css.count(old) == 1, "Tidak unik: " + old[:70]
    css = css.replace(old, new)

io.open(PATH, "w", encoding="utf-8", newline="").write(css)
print("OK. text-shadow pada elemen gradient diganti filter: drop-shadow().")

