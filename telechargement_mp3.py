import re
import os
import yt_dlp
from urllib.parse import urlparse, parse_qs

def nettoie_nom(s):
    """Nettoie une chaîne pour en faire un nom de fichier valide."""
    return re.sub(r'[\\/:*?"<>|]', "_", s).strip()

def simplifie_url(u):
    """Extrait l'URL de base de YouTube pour éviter les doublons."""
    try:
        p = urlparse(u)
        q = parse_qs(p.query)
        if "v" in q:
            return f"https://www.youtube.com/watch?v={q['v'][0]}"
    except Exception:
        pass
    return u

dossier_script = os.path.dirname(os.path.abspath(__file__))
dossier_son = os.path.join(dossier_script, "son")
os.makedirs(dossier_son, exist_ok=True)

chemin_ffmpeg = os.path.join(dossier_script, "bin", "ffmpeg.exe")

if not os.path.exists(chemin_ffmpeg):
    print(f"ATTENTION : ffmpeg.exe non trouvé ici : {chemin_ffmpeg}")
    chemin_ffmpeg = None


while True:
    url = input("URL de la vidéo (ou 'q' pour quitter) : ").strip()
    if url.lower() == "q" or url == "":
        break
    
    url = simplifie_url(url)
    
    try:
        info_opts = {
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': False,
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(info_opts) as ydl_info:
            info = ydl_info.extract_info(url, download=False)
            titre = nettoie_nom(info.get('title', 'audio_téléchargé'))
        chemin_final_mp3 = os.path.join(dossier_son, f"{titre}.mp3")
        chemin_ffmpeg = os.path.join(dossier_script, 'bin', 'ffmpeg.exe')

        ydl_opts_download = {
            'ffmpeg_location': chemin_ffmpeg, 
            
            'format': 'bestaudio/best',
            'quiet': False,
            'no_warnings': True,
            'ignoreerrors': False,
            'noplaylist': True,
            'outtmpl': chemin_final_mp3,
            'keepvideo': False, 

            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                },
                {
                    'key': 'EmbedThumbnail',
                },
                {
                    'key': 'FFmpegMetadata',
                    'add_metadata': True,
                },
            ],

            'postprocessor_args': [
                '-ar', '48000'  
            ],

            'writethumbnail': True,
        }
         

        print(f"Téléchargement et conversion de '{titre}'...")
    
        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl_download:
            ydl_download.download([url])
        
        print(f"Terminé : {chemin_final_mp3}\n")

    except Exception as e:
        print("ERREUR :")
        print(repr(e))
