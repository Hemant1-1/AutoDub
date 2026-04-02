from moviepy.editor import VideoFileClip
import os

def extract_audio(video_file, output_audio):
    """
    यह फंक्शन वीडियो से ऑडियो निकालकर उसे .wav फॉर्मेट में सेव करता है।
    """
    try:
        print(f"ऑडियो निकाला जा रहा है: {video_file}...")
        video = VideoFileClip(video_file)
        video.audio.write_audiofile(output_audio)
        video.close()
        print(f"सफलता! ऑडियो सेव हो गया: {output_audio}")
        return True
    except Exception as e:
        print(f"Audio Extraction Error: {e}")
        return False