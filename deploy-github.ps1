# ============================================================
# DEPLOY KE GITHUB PAGES - PORTOFOLIO ANITA
# ------------------------------------------------------------
# 1. Pastikan sudah membuat repo PUBLIK di GitHub bernama:
#       portfolio-anita
#    (di akun: tiarasani-anita)
#    Tanpa repo ini push akan gagal.
# 2. Jalankan script ini (klik kanan -> Run with PowerShell).
#    Git Credential Manager akan muncul popup login browser.
# 3. Setelah push sukses:
#       Settings -> Pages -> Source: Deploy from a branch
#       Branch: main / (root)
#    Website live di:
#       https://tiarasani-anita.github.io/portfolio-anita/
# ============================================================
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

$remote = 'https://github.com/tiarasani-anita/portfolio-anita.git'

# Set remote (jika sudah ada, perbarui)
git remote remove origin 2>$null
git remote add origin $remote

# Pastikan branch main
$branch = git rev-parse --abbrev-ref HEAD
if ($branch -ne 'main') {
    git branch -M main
}

# Push ke GitHub (popup login GCM akan muncul)
git push -u origin main

Write-Host ''
Write-Host '====================================================' -ForegroundColor Cyan
Write-Host ' PUSH BERHASIL!' -ForegroundColor Green
Write-Host ' Langkah terakhir di GitHub:' -ForegroundColor Yellow
Write-Host '   Settings -> Pages -> Source: Deploy from a branch' -ForegroundColor Yellow
Write-Host '   Branch: main / (root) -> Save' -ForegroundColor Yellow
Write-Host ' Website live: https://tiarasani-anita.github.io/portfolio-anita/' -ForegroundColor Green
Write-Host '====================================================' -ForegroundColor Cyan

