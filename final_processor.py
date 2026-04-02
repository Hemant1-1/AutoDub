import os
import time

def merge_audio_video_with_subs(video_path, audio_path, srt_path, output_path):
    """
    बिना क्वालिटी खोए वीडियो, डब आवाज़ और इंग्लिश सबटाइटल्स को जोड़ना।
    """
    try:
        # फाइल चेक करना
        if not os.path.exists(audio_path):
            print("आवाज़ वाली फाइल का इंतज़ार किया जा रहा है...")
            time.sleep(3)

        print("\n--- Step 6: Final Merging (Ultra Quality Mode) ---")
        
        # FFmpeg कमांड: 
        # -crf 18 (अति उत्तम क्वालिटी), -preset slow (बेहतर कंप्रेशन)
        command = (
            f'ffmpeg -y -i "{video_path}" -i "{audio_path}" '
            f'-vf "subtitles={srt_path}" '
            f'-c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k '
            f'-map 0:v:0 -map 1:a:0 -shortest "{output_path}"'
        )
        
        os.system(command)
        
        if os.path.exists(output_path):
            print(f"\nसफलता! आपका HD वीडियो तैयार है: {output_path}")
            return True
        return False
            
    except Exception as e:
        print(f"Merging Error: {e}")
        return False