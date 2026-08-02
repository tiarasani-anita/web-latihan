# -*- coding: utf-8 -*-
"""Hilangkan total kotak hitam: ganti SEMUA text-shadow pada selector
.neon-edge / .neon-edge-sm / hero-name / gradient-text menjadi
filter: drop-shadow() yang mengikuti bentuk huruf.

Penyebab kotak hitam yang tersisa: text-shadow pada selector umum
.neon-edge (baris ~473) & .neon-edge-sm (baris ~483) & override
[data-theme="light"] masih menggambar kotak buram di belakang teks
yang menggunakan background-clip:text + -webkit-text-fill-color:transparent.
"""
import io
import re

PATH = r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css"
css = io.open(PATH, encoding="utf-8").read()

def replace_block(css, selector_pattern, old_prop, new_prop):
    """Ganti properti lama dengan baru di dalam blok selector tertentu."""
    count = 0
    for m in re.finditer(selector_pattern, css):
        block_start = css.find('{', m.end())
        block_end = css.find('}', block_start)
        block = css[block_start+1:block_end]
        if old_prop in block:
            # Ganti seluruh properti text-shadow di blok ini dengan new_prop
            new_block = re.sub(r'text-shadow\s*:\s*[^;]+;', new_prop, block)
            css = css[:block_start+1] + new_block + css[block_end:]
            count += 1
    return css, count

# 1) .neon-edge umum
css, c1 = replace_block(css, r'\.neon-edge\s*\{', 'text-shadow',
    'filter: drop-shadow(0 0 2px rgba(255,255,255,0.55)) drop-shadow(0 0 8px rgba(0,240,255,0.55)) drop-shadow(0 0 22px rgba(255,46,196,0.35)) drop-shadow(0 0 44px rgba(139,92,246,0.2));')

# 2) .neon-edge-sm umum
css, c2 = replace_block(css, r'\.neon-edge-sm\s*\{', 'text-shadow',
    'filter: drop-shadow(0 0 2px rgba(255,255,255,0.5)) drop-shadow(0 0 7px rgba(0,240,255,0.5)) drop-shadow(0 0 16px rgba(255,46,196,0.3));')

# 3) override light .neon-edge
css, c3 = replace_block(css, r'\[data-theme="light"\] \.neon-edge\s*\{', 'text-shadow',
    'filter: drop-shadow(0 0 3px rgba(255,255,255,0.9)) drop-shadow(0 0 8px rgba(0,240,255,0.55)) drop-shadow(0 0 16px rgba(255,46,196,0.35));')

# 4) override light .neon-edge-sm
css, c4 = replace_block(css, r'\[data-theme="light"\] \.neon-edge-sm\s*\{', 'text-shadow',
    'filter: drop-shadow(0 0 3px rgba(255,255,255,0.9)) drop-shadow(0 0 8px rgba(0,240,255,0.5)) drop-shadow(0 0 14px rgba(255,46,196,0.3));')

io.open(PATH, "w", encoding="utf-8", newline="").write(css)
print("neon-edge umum   :", c1)
print("neon-edge-sm umum:", c2)
print("light neon-edge  :", c3)
print("light neon-edge-sm:", c4)
print("Selesai.")

