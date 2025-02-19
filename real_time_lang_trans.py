import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk, messagebox

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening... Speak now!")
        root.update_idletasks()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        input_text.set(text)
        status_label.config(text="Speech recognized successfully!")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio.")
    except sr.RequestError:
        messagebox.showerror("Error", "Network error. Please check your internet connection.")

def translate_text():
    text = input_text.get()
    target_lang = language_dict[language_var.get()]
    translator = Translator()
    
    try:
        translated = translator.translate(text, dest=target_lang)
        translated_text.set(translated.text)
        status_label.config(text=f"Translated to {language_var.get()}")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def text_to_speech():
    text = translated_text.get()
    target_lang = language_dict[language_var.get()]
    
    try:
        tts = gTTS(text=text, lang=target_lang, slow=False)
        tts.save("translated_speech.mp3")
        os.system("start translated_speech.mp3" if os.name == "nt" else "mpg321 translated_speech.mp3")
        status_label.config(text="Playing translated speech...")
    except Exception as e:
        messagebox.showerror("TTS Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Real-Time Language Translator")
root.geometry("500x400")
root.resizable(False, False)

# Language Selection
language_dict = {name.capitalize(): code for code, name in LANGUAGES.items()}
language_var = tk.StringVar()
language_var.set("Spanish")  # Default language

# Input and Output Variables
input_text = tk.StringVar()
translated_text = tk.StringVar()

# UI Components
tk.Label(root, text="Real-Time Language Translator", font=("Arial", 14, "bold")).pack(pady=10)
ttk.Button(root, text="Speak", command=speech_to_text).pack(pady=5)
tk.Entry(root, textvariable=input_text, width=50).pack(pady=5)

tk.Label(root, text="Select Language:").pack(pady=5)
ttk.Combobox(root, textvariable=language_var, values=list(language_dict.keys()), state="readonly").pack(pady=5)

ttk.Button(root, text="Translate", command=translate_text).pack(pady=5)
tk.Entry(root, textvariable=translated_text, width=50, state="readonly").pack(pady=5)

ttk.Button(root, text="Play Audio", command=text_to_speech).pack(pady=10)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)

root.mainloop()
