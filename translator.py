
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pyperclip
import os

# Create Translator Object
translator = Translator()

# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.config(bg="white")

# Function for Translation
def translate_text():
    text = input_text.get("1.0", END)

    src_lang = source_lang.get()
    dest_lang = target_lang.get()

    src_code = language_dict[src_lang]
    dest_code = language_dict[dest_lang]

    translated = translator.translate(text, src=src_code, dest=dest_code)

    output_text.delete("1.0", END)
    output_text.insert(END, translated.text)

# Function to Copy Text
def copy_text():
    translated = output_text.get("1.0", END)
    pyperclip.copy(translated)

# Function for Voice Output
def speak_text():
    translated = output_text.get("1.0", END)

    speech = gTTS(text=translated, lang='en')
    speech.save("voice.mp3")

    os.system("start voice.mp3")

# Language Dictionary
language_dict = {v.title(): k for k, v in LANGUAGES.items()}

# Heading
Label(root, text="AI Language Translator",
      font=("Arial", 20, "bold"),
      bg="white", fg="blue").pack(pady=10)

# Input Text
Label(root, text="Enter Text",
      font=("Arial", 12),
      bg="white").pack()

input_text = Text(root, height=8, width=70)
input_text.pack(pady=5)

# Language Selection Frame
frame = Frame(root, bg="white")
frame.pack(pady=10)

# Source Language
source_lang = ttk.Combobox(frame, values=list(language_dict.keys()), width=25)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=10)

# Target Language
target_lang = ttk.Combobox(frame, values=list(language_dict.keys()), width=25)
target_lang.set("Hindi")
target_lang.grid(row=0, column=1, padx=10)

# Translate Button
Button(root, text="Translate",
       font=("Arial", 12, "bold"),
       bg="green", fg="white",
       command=translate_text).pack(pady=10)

# Output Text
Label(root, text="Translated Text",
      font=("Arial", 12),
      bg="white").pack()

output_text = Text(root, height=8, width=70)
output_text.pack(pady=5)

# Buttons Frame
btn_frame = Frame(root, bg="white")
btn_frame.pack(pady=10)

Button(btn_frame, text="Copy Text",
       command=copy_text,
       bg="orange", fg="white").grid(row=0, column=0, padx=10)

Button(btn_frame, text="Speak",
       command=speak_text,
       bg="purple", fg="white").grid(row=0, column=1, padx=10)

# Run Application
root.mainloop()
