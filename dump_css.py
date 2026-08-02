# -*- coding: utf-8 -*-
"""Dump aturan CSS yang berkaitan dengan background-clip:text / filter / box hitam."""
import io
import re

css = io.open(r"C:/Users/COMPUTER/Desktop/portfolio-anita/css/style.css", encoding="utf-8").read()
out = io.open(r"C:/Users/COMPUTER/Desktop/portfolio-anita/css_dump.txt", "w", encoding="utf-8")

def dump_block(pattern, label):
    out.write("\n" + "="*70 + "\n")
    out.write(label + "\n")
    out.write("="*70 + "\n")
    for m in re.finditer(pattern, css):
        start = m.start()
        # cari awal rule: mundur ke '{' terdekat yang bukan di dalam string; ambil 300 chars sebelumnya
        sel_start = css.rfind("}", 0, start)
        sel_start = css.rfind("{", 0, start)
        # dapatkan selector penuh
        brace = css.rfind("{", 0, start)
        prev_brace = css.rfind("}", 0, start)
        block_start = max(prev_brace, brace)
        # cari blok berakhir
        end = css.find("}", start)
        block = css[block_start+1:end+1]
        out.write(block.strip() + "\n\n")

dump_block(r"background-clip:\s*text", "RULES DENGAN background-clip: text")
dump_block(r"filter:\s*drop-shadow", "RULES DENGAN filter: drop-shadow")
dump_block(r"-webkit-text-fill-color", "RULES DENGAN -webkit-text-fill-color")
dump_block(r"color:\s*transparent", "RULES DENGAN color: transparent")

out.close()
print("OK dumped")

