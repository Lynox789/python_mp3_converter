@echo off
title Installation et Lancement

echo      INSTALLATION ET LANCEMENT

:: 1. Vérification de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python (cochez "Add to PATH").
    pause
    exit
)

:: 2. Installation des librairies
echo.
echo [INFO] Installation des dependances...
pip install -r requirements.txt

:: 3. Vérification de FFmpeg (Dossier 'bin')
echo.
if exist "bin\ffmpeg.exe" (
    echo [INFO] FFmpeg detecte.
) else (
    echo [ATTENTION] FFmpeg introuvable dans le dossier 'bin'.
    echo Le script risque d'echouer.
)

:: 4. Lancement du script
echo.
echo      LANCEMENT DU PROGRAMME
echo.
python telechargement_mp3.py

pause
