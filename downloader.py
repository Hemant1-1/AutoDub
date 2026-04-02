import yt_dlp
import os

def download_video(url):
    """
    यह फंक्शन वीडियो को उसके सबसे उच्चतम रेजोल्यूशन (1080p/720p) में डाउनलोड करता है।
    """
    try:
        print("\n--- वीडियो हाई क्वालिटी में डाउनलोड हो रहा है... ---")
        
        ydl_opts = {
            # सबसे अच्छी वीडियो और ऑडियो क्वालिटी को मर्ज करके MP4 बनाना
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': 'downloaded_video.mp4',
            'merge_output_format': 'mp4',
            'quiet': False
        }
        
        # पुरानी फाइल को हटाना ताकि नई फ्रेश फाइल बने
        if os.path.exists("downloaded_video.mp4"):
            os.remove("downloaded_video.mp4")
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("सफलता! हाई क्वालिटी वीडियो डाउनलोड हो गया।")
        return True
    except Exception as e:
        print(f"Download Error: {e}")
        return False