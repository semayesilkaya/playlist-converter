import yt_dlp
import os


def download_playlist_as_mp3(playlist_url, download_folder='Sarkilar'):
    # İndirme klasörünü oluştur
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': 'bestaudio/best',  # En iyi ses kalitesini çek
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Ses kalitesi (128, 192, 256, 320 olabilir)
        }],
        # Dosya adı formatı: "Klasör/Şarkı Adı.mp3"
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',

        # 255 şarkı içinde silinmiş/gizliye alınmış video varsa scriptin çökmesini engeller, sonrakine geçer
        'ignoreerrors': True,

        # Konsol çıktısını biraz daha temiz tutar
        'quiet': False,
        'no_warnings': True,
        'extract_flat': False  # Listeyi sadece okumayıp dosyaları indirmesini sağlar
    }

    try:
        print(f"🎵 Çalma listesi indirilmeye başlanıyor... (Hedef Klasör: {download_folder})")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("\n✅ Tüm indirme işlemi tamamlandı!")
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")


if __name__ == "__main__":
    # İndirilecek YouTube Music Playlist URL'si
    playlist_link = "https://music.youtube.com/playlist?list=PLvprsZ8A5-j_uv0LH9DlFBRryil75P3ru"

    download_playlist_as_mp3(playlist_link)