import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results, check internet connection.")
        return None

def translate_text(text, target_language="fr"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated ({target_language}): {translation.text}")
    return translation.text

def text_to_speech(text, lang="fr"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("translated_speech.mp3")
    os.system("start translated_speech.mp3" if os.name == "nt" else "mpg321 translated_speech.mp3")

if __name__ == "__main__":
    source_language = "en"  # Change as needed
    target_language = "fr"  # Change to desired target language code

    input_text = speech_to_text()
    
    if input_text:
        translated_text = translate_text(input_text, target_language)
        text_to_speech(translated_text, target_language)
