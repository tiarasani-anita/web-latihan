# -*- coding: utf-8 -*-
"""Ekstrak blok CSS yang akan diedit untuk menghapus kotak hitam judul/subjudul."""
import io

css = io.open(r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css", encoding="utf-8").read()
out = io.open(r"C:/Users/COMPUTER/Desktop/portfolio-anita/blocks.txt", "w", encoding="utf-8")

targets = [
    ".hero-name {",
    ".hero-name.neon-edge {",
    ".gradient-text {",
    '[data-theme="light"] .gradient-text {',
    '[data-theme="light"] .hero-name.neon-edge {',
]

for t in targets:
    idx = css.find(t)
    if idx == -1:
        out.write("NOT FOUND: " + t + "\n\n")
        continue
    end = css.find("}", idx) + 1
    out.write("### " + t + "\n")
    out.write(css[idx:end] + "\n\n")

out.close()
print("OK")

