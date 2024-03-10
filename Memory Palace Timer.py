import tkinter as tk
import random

data = []

def veletlen_valasztas(lista):
    return random.choice(lista)

def display_words():
    file_path = "words.txt"  # Fájl elérési útvonala
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            global data
            data = file.read().splitlines()
            if data:
                chosen_word = veletlen_valasztas(data)
                word_label.config(text=chosen_word)
            else:
                word_label.config(text="A fájl üres.")
    except FileNotFoundError:
        word_label.config(text="A fájl nem található.")
    root.after(1000, display_words)  # 1000 ms = 1 másodperc

root = tk.Tk()
root.title("Szavak kiírása")

start_button = tk.Button(root, text="Indítás", command=display_words)
start_button.pack(pady=10)

word_label = tk.Label(root, text="")
word_label.pack(pady=10)

root.mainloop()
