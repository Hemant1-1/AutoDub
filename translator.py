from deep_translator import GoogleTranslator

def translate_to_language(input_file, output_file, lang_code):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        print(f"अनुवाद किया जा रहा है ({lang_code})...")
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(translated)
        return True
    except Exception as e:
        print(f"Translation Error: {e}")
        return False