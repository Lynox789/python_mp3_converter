@echo off
title Installation des dependances
echo      INSTALLATION POUR YOUTUBE MP3

:: 1. Vérification de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python depuis python.org (cochez "Add to PATH").
    pause
    exit
)

:: 2. Installation des librairies Python
echo.
echo [INFO] Installation de la librairie yt-dlp...
pip install -r requirements.txt

:: 3. Vérification de FFmpeg (Message informatif)

echo              IMPORTANT - FFMPEG
echo.
echo Ce script a besoin de FFmpeg pour convertir l'audio.
echo.
echo 1. Telechargez FFmpeg ici : https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
echo 2. Dezippez le dossier.
echo 3. Copiez "ffmpeg.exe" (qui est dans le dossier 'bin')
echo 4. Collez-le dans : C:\ffmpeg\ffmpeg.exe
echo    (Ou modifiez le script python pour pointer vers votre dossier)
echo.
pause
