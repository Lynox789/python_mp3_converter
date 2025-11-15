	# YouTube to MP3 Downloader

Un script Python simple et efficace pour télécharger l'audio des vidéos YouTube en format MP3 de haute qualité. Le script gère automatiquement le téléchargement, la conversion, et l'ajout des métadonnées (titre, couverture/thumbnail).

## Fonctionnalités

* **Téléchargement rapide** via `yt-dlp`.
* **Conversion MP3** automatique (qualité 192kbps).
* **Métadonnées incluses** : La miniature de la vidéo est intégrée comme couverture de l'album MP3.
* **Nettoyage** automatique des noms de fichiers.

## Prérequis

1.  **Python 3.x** installé sur votre machine.
2.  **FFmpeg** installé (nécessaire pour la conversion audio).

## Installation

### 1. Cloner le projet
Téléchargez ce dépôt ou clonez-le avec git :
```bash
git clone https://github.com/Lynox789/python_mp3_converter
cd python_mp3_converter
