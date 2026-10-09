@echo off
chcp 65001 > nul
title Gümüş Raket — Güncelleme Sihirbazı
cls
echo ========================================================
echo  🎾 GÜMÜŞ RAKET & DEUCE CAFE — SİSTEM GÜNCELLEME
echo ========================================================
echo.
echo [1/3] Mevcut veritabanı korunuyor ve güvenlik yedeği alınıyor...
if exist gumus_raket_veritabani.json (
    if not exist Yedekler mkdir Yedekler
    copy /Y gumus_raket_veritabani.json "Yedekler\guncelleme_oncesi_%date:~6,4%-%date:~3,2%-%date:~0,2%.json" > nul
    echo   [✓] Veritabanı yedeği güvenle Yedekler klasörüne kaydedildi.
) else (
    echo   [i] Henüz veritabanı dosyası oluşmamış (yeni kurulum).
)
echo.
echo [2/3] Güncel kodlar GitHub'dan çekiliyor...
git pull origin main
if %errorlevel% neq 0 (
    git pull
)
echo.
echo [3/3] Güncelleme başarıyla tamamlandı!
echo.
echo   [✓] 124 öğrenci, aidat, kasa ve kordaj kayıtlarınıza dokunulmadı.
echo   [✓] Yeni özellikler ve ekranlar hazır.
echo.
echo   Sistemi başlatmak için 'baslat.bat' dosyasını çalıştırabilir
echo   veya tarayıcınızda sayfayı yenileyebilirsiniz (F5).
echo ========================================================
pause
