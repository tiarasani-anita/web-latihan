@echo off
REM ============================================================
REM  DEPLOY KE SURGE.SH - PORTOFOLIO ANITA
REM  ------------------------------------------------------------
REM  1. Double-click file ini.
REM  2. Ketik EMAIL (anitatiara25@gmail.com) lalu Enter.
REM  3. Ketik PASSWORD (untuk akun baru, password dibuat otomatis;
REM     bila sudah punya akun surge, gunakan password tersebut).
REM  4. Tunggu sampai muncul "Success!" + URL.
REM  Website live di: https://anita-portfolio.surge.sh
REM ============================================================
cd /d "%~dp0"
call npx --yes surge ./ anita-portfolio.surge.sh
pause

