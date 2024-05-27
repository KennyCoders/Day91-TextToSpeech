import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

#---------------------Functions--------------------------------------------#
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def convert_text_to_speech(text, output_file, language, voice):
    tts = gTTS(text=text, lang=language, tld='com', slow=False, lang_check=False)
    tts.save(output_file)


def browse_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_path)


def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)


def convert_to_speech():
    pdf_path = pdf_entry.get()
    output_folder = output_entry.get()
    output_file = os.path.join(output_folder, "output.mp3")
    language = language_var.get()
    voice = voice_var.get()

    text = extract_text_from_pdf(pdf_path)
    convert_text_to_speech(text, output_file, language, voice)

    status_label.config(text="Text-to-speech conversion complete!")
    output_path_label.config(text=f"You can find the output audio file at: {output_file}")


#-------------------------- Create GUI-------------------------------#
root = tk.Tk()
root.title("PDF to Text-to-Speech Converter")

# Language selection
language_label = tk.Label(root, text="Select Language:")
language_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

language_var = tk.StringVar(root)
language_var.set("en")  # default language selection

language_menu = tk.OptionMenu(root, language_var, "en", "he")
language_menu.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Voice selection
voice_label = tk.Label(root, text="Select Voice:")
voice_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

voice_var = tk.StringVar(root)
voice_var.set("male")

voice_menu = tk.OptionMenu(root, voice_var, "male", "female")
voice_menu.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# PDF file selection
pdf_label = tk.Label(root, text="Select PDF File:")
pdf_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=2, column=1, padx=5, pady=5)

pdf_button = tk.Button(root, text="Browse", command=browse_pdf)
pdf_button.grid(row=2, column=2, padx=5, pady=5)

# Output folder selection
output_label = tk.Label(root, text="Select Output Folder:")
output_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=3, column=1, padx=5, pady=5)

output_button = tk.Button(root, text="Browse", command=browse_output_folder)
output_button.grid(row=3, column=2, padx=5, pady=5)


convert_button = tk.Button(root, text="Convert to Speech", command=convert_to_speech)
convert_button.grid(row=4, column=1, padx=5, pady=10)


status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=3)


output_path_label = tk.Label(root, text="")
output_path_label.grid(row=6, column=0, columnspan=3)

root.mainloop()
