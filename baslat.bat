@echo off
chcp 65001 > nul
title GUMUS RAKET TENIS KULUBU - YEREL SUNUCU (BADEMLI)
color 0A

echo ======================================================================
echo    GÜMÜŞ RAKET TENİS KULÜBÜ & DEUCE CAFE — YEREL SUNUCU (ANA PC)
echo    Bademli / Bursa
echo ======================================================================
echo.
echo Sunucu başlatılıyor... Lütfen bu siyah pencereyi açık bırakınız.
echo Tarayıcınız otomatik olarak açılacaktır.
echo.

python --version >nul 2>&1
if %errorlevel% equ 0 (
    python server.py
) else (
    py --version >nul 2>&1
    if %errorlevel% equ 0 (
        py server.py
    ) else (
        echo [BİLGİ] Python komutu bulunamadı, doğrudan tarayıcı ile açılıyor...
        start gumus_raket_v3.html
    )
)

pause
