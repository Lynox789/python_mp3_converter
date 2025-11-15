# YouTube to MP3 Downloader

Un script Python permettant de télécharger l'audio des vidéos YouTube et de le convertir en format MP3. Le script automatise l'extraction, la conversion, le balisage des métadonnées et la gestion des fichiers.

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