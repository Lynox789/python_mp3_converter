<div align="center">

[🇫🇷 Version Française](#version-française) | [🇬🇧 English Version](#english-version)

</div>

<div id="english-version"></div>

# English Version

# YouTube to MP3 Downloader

A Python script for downloading audio from YouTube videos and converting it to MP3 format. The script automates extraction, conversion, metadata tagging, and file management.

## Legal Disclaimer
This script is provided for educational and personal archiving purposes. 
Downloading copyrighted content without the explicit permission of the copyright holders is contrary to YouTube's terms of service. 
**The user** is **solely responsible** for the use of this script.



### Clone the project
Download this repository or clone it with git:
```bash
git clone https://github.com/Lynox789/python_mp3_converter
cd python_mp3_converter
```

## Features

* **Download**: Use of the `yt-dlp` library for reliable audio stream extraction.
* **Conversion**: Encoding to MP3 CBR (Constant Bitrate) at 192 kbps.
* **Metadata**: Automatic integration of the video thumbnail as album art (ID3 tag).
* **Cleaning**: Sanitisation of file names to remove characters not supported by the operating system.

## Technical Specifications

The script uses FFmpeg for post-processing the raw audio stream extracted from YouTube. The conversion parameters are strictly defined to ensure audio quality.

### Audio Processing and Sampling

The script forces specific arguments when calling FFmpeg via `postprocessor_args`.

* **Codec**: MP3 (MPEG-1 Audio Layer III).
* **Bitrate**: 192 kbps.
* **Sample Rate**: **48,000 Hz (48 kHz)**.

This parameter is defined in the code by the argument:
```python
“postprocessor_args”: [
    “-ar”, “48000”
]
```
Modify this parameter if necessary for a better sample rate.


<div id="version-française"></div>

# Version Française

# YouTube to MP3 Downloader

Un script Python permettant de télécharger l'audio des vidéos YouTube et de le convertir en format MP3. Le script automatise l'extraction, la conversion, le balisage des métadonnées et la gestion des fichiers.

## Avertissement Légal
Ce script est fourni à des fins éducatives et d'archivage personnel. 
Le téléchargement de contenus protégés par des droits d'auteur sans l'autorisation explicite des détenteurs de ces droits est contraire aux conditions d'utilisation de YouTube. 
**L'utilisateur** est le **seul responsable** de l'utilisation faite de ce script.



### Cloner le projet
Téléchargez ce dépôt ou clonez-le avec git :
```bash
git clone https://github.com/Lynox789/python_mp3_converter
cd python_mp3_converter
```

## Fonctionnalités

* **Téléchargement** : Utilisation de la bibliothèque `yt-dlp` pour une extraction fiable des flux audio.
* **Conversion** : Encodage en MP3 CBR (Constant Bitrate) à 192 kbps.
* **Métadonnées** : Intégration automatique de la miniature de la vidéo comme pochette d'album (ID3 tag).
* **Nettoyage** : Sanitization des noms de fichiers pour supprimer les caractères non supportés par le système d'exploitation.

## Spécifications Techniques

Le script utilise FFmpeg pour le post-traitement du flux audio brut extrait de YouTube. Les paramètres de conversion sont définis strictement pour garantir la qualité audio.

### Traitement Audio et Échantillonnage

Le script force des arguments spécifiques lors de l'appel à FFmpeg via `postprocessor_args`.

* **Codec** : MP3 (MPEG-1 Audio Layer III).
* **Débit (Bitrate)** : 192 kbps.
* **Fréquence d'échantillonnage (Sample Rate)** : **48 000 Hz (48 kHz)**.

Ce paramètre est défini dans le code par l'argument :
```python
'postprocessor_args': [
    '-ar', '48000'
]
```
Modifier ce paramètre ci nécessaire pour une meilleure fréquence d'échantillonage
