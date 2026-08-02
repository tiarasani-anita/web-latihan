# TODO - Web Portofolio Anita Tiara Sani

> Daftar langkah sesi berjalan. Centang saat selesai.

## Sesi: Hilangkan Kotak Hitam + Teks Putih + Deploy Publik

### Perbaikan Kotak Hitam (css/style.css)
- [x] Ganti `.hero-name` dari gradien transparan → teks putih solid + glow text-shadow
- [x] Ganti `.hero-name.neon-edge` → teks putih solid + glow text-shadow
- [x] Ganti `.neon-edge` / `.neon-edge-sm` `filter: drop-shadow()` → `text-shadow`
- [x] Ganti `.gradient-text` dari gradien transparan → warna solid cerah (#7df9ff)
- [x] Sesuaikan override tema terang `[data-theme="light"]` (nama/gradient lebih gelap agar terbaca)

### Penyempurnaan Font & Tampilan Mobile
- [x] Media query ≤768px: ukuran font body/hero/judul, nav-links, spacing
- [x] Media query ≤480px: font kartu/hero/button, padding section, form, modal
- [x] Media query ≤360px: pastikan tidak ada teks terpotong

### Verifikasi Lokal
- [x] Buka di browser (desktop + mode mobile DevTools)
- [x] Jalankan check_entities.py & verify_full.py (semua True/lolos)

### Deploy Publik (Plan C)
- [ ] Deploy cepat ke Surge.sh (URL permanen gratis)
- [ ] Siapkan GitHub Pages (install git, repo, push) sesuai link anitatiara25.github.io/portfolio-anita
- [ ] Update meta og:url di index.html jika URL final berbeda

