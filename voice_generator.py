from gtts import gTTS
import os

def generate_voice(input_file, output_file, lang_code):
    """
    यह फंक्शन स्क्रिप्ट को आवाज़ में बदलता है।
    input_file: अनुवादित टेक्स्ट फाइल (translated_script.txt)
    output_file: बनने वाली ऑडियो फाइल (final_voice.mp3)
    lang_code: डबिंग की भाषा (hi, es, fr, आदि)
    """
    try:
        # 1. अनुवादित टेक्स्ट फाइल को पढ़ना
        if not os.path.exists(input_file):
            print(f"Error: '{input_file}' फाइल नहीं मिली!")
            return False

        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        if not text.strip():
            print("Error: स्क्रिप्ट फाइल खाली है।")
            return False

        print(f"--- Step 5: Generating AI Voice ({lang_code}) ---")
        
        # 2. Google TTS का उपयोग करके आवाज़ बनाना
        # हमने यहाँ से 'pydub' हटा दिया है ताकि Python 3.13 में एरर न आए
        tts = gTTS(text=text, lang=lang_code)
        
        # 3. ऑडियो फाइल को सेव करना
        tts.save(output_file)
        
        print(f"Success! आवाज़ तैयार है: {output_file}")
        
        # 4. main.py को सफलता का सिग्नल भेजना
        return True 

    except Exception as e:
        print(f"Voice Generation Error: {e}")
        return False