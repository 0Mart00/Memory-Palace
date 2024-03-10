from tkinter import *
import tkinter as ttk
import random


root = Tk()

length = 10
test = []

def new_number():
    test.clear()
    for x in range(length):
        test.append(str(random.randint(0, 9)))
    update_label()

def update_label():
    label.config(text=label.cget("text") + "\n" + "".join(test))

label = ttk.Label(root, text="", font=("Arial", 20))  
label.pack(side=TOP)

button = ttk.Button(root, text="Generate Numbers", command=new_number)
button.pack()

root.mainloop()
