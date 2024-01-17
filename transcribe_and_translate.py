import os
import sys
from typing import List

import whisper
import translators as ts

def transcribe(model, lang, path):
    """Transcribes speech from a file."""
    
    model = whisper.load_model(model)
    result = model.transcribe(path, language=lang)
    
    return result["text"]

def translate(text: str, dest_langs: List[str]) -> dict:
    """Translates text into multiple languages."""

    translated_texts = {}

    for dest_lang in dest_langs:
        translation = ts.google(text, to_language=dest_lang)
        translated_texts[dest_lang] = translation

    return translated_texts

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python transcribe_and_translate.py <model> <input_file> <output_directory>")
        exit(1)
        
    model = sys.argv[1]
    input_file = sys.argv[2]
    output_dir = sys.argv[3]

    # Transcribe Spanish audio
    transcription = transcribe(model, "es", input_file)
    print(f"Transcription:\n{transcription}\n")

    # Translate transcription into target languages
    dest_langs = ["por", "eng", "hrv", "jpn"]
    translations = translate(transcription, dest_langs)

    # Save translations to files
    for lang, translation in translations.items():
        with open(os.path.join(output_dir, f"{lang}.txt"), "w") as outfile:
            outfile.write(translation)
            print(f"Translation ({lang}):\n{translation}\n")
