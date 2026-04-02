import whisper
from whisper.utils import get_writer
import os

def convert_speech_to_text(audio_file):
    try:
        print("Whisper AI मॉडल लोड हो रहा है...")
        model = whisper.load_model("base")
        
        # 'task=transcribe' यह सुनिश्चित करेगा कि सबटाइटल्स इंग्लिश में रहें
        print("सबटाइटल बनाए जा रहे हैं (English)...")
        result = model.transcribe(audio_file, task="transcribe")
        
        # SRT फाइल बनाना
        writer = get_writer("srt", ".")
        writer(result, audio_file)
        
        # टेक्स्ट को script.txt में सेव करना
        with open("script.txt", "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        print("सफलता! 'script.txt' और 'output_audio.srt' तैयार हैं।")
        return result["segments"]
    except Exception as e:
        print(f"Transcription Error: {e}")
        return None