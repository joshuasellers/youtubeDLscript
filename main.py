import yt_dlp


def download_video(url):
    """
    Downloads a video from the given URL using yt-dlp.
    """
    ydl_opts = {} # Empty dictionary for default options
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_audio_only(url, download_path='.'):
    """
    Downloads only the audio and converts it to MP3 format.
    """
    ydl_opts = {
        'verbose': True,
        'format': 'bestaudio/best',  # Download best quality audio
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Output file template
        'noplaylist': True,  # Only download single song, not entire playlist
        'progress_hooks': [my_progress_hook],  # Optional: Add a progress hook
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded audio from: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")


def my_progress_hook(d):
    """Optional function to log download progress."""
    if d['status'] == 'finished':
        print('\nDone downloading, starting post-processing...')


if __name__ == "__main__":
    url = 'https://soundcloud.com/xf8x/i-put-a-drill-beat-over-hello-by-adele'
    download_audio_only(url)
