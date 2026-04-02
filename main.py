import os
from downloader import download_video
from processor import extract_audio
from transcriber import convert_speech_to_text
from translator import translate_to_language
from voice_generator import generate_voice
from final_processor import merge_audio_video_with_subs
from moviepy.editor import VideoFileClip

def start_dubbing():
    try:
        # स्टेप 0: इनपुट
        video_url = input("YouTube वीडियो लिंक डालें: ")
        print("\nभाषा कोड: hi (Hindi), es (Spanish), fr (French)")
        target_lang = input("डबिंग भाषा कोड चुनें (उदा. hi): ").lower().strip()

        # भाषा कोड सुधार
        if target_lang == "hindi": target_lang = "hi"

        # स्टेप 1: HD डाउनलोड
        if not download_video(video_url): return
        
        # स्टेप 2: ऑडियो निकालना
        extract_audio("downloaded_video.mp4", "output_audio.wav")
        
        # स्टेप 3: इंग्लिश सबटाइटल
        convert_speech_to_text("output_audio.wav")
        
        # स्टेप 4: अनुवाद
        translate_to_language("script.txt", "translated_script.txt", target_lang)
        
        # स्टेप 5: डब आवाज़ बनाना
        generate_voice("translated_script.txt", "final_voice.mp3", target_lang)
        
        # स्टेप 6: HD मर्जिंग
        final_file = "HD_Coding_Dubbed_Video.mp4"
        merge_audio_video_with_subs(
            "downloaded_video.mp4", 
            "final_voice.mp3", 
            "output_audio.srt", 
            final_file
        )
        
        print(f"\nबधाई हो! प्रोजेक्ट पूरा हुआ। फाइल देखें: {final_file}")

    except Exception as e:
        print(f"Main Error: {e}")

if __name__ == "__main__":
    start_dubbing()