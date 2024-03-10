from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.title("Memory Palace Words")

stringvars = []

file = open("words.txt", "r+")

li = file.readlines()

def new_stringvar():
    stringvar = StringVar(value=li[random.randint(0,len(li))-1])
    stringvars.append(stringvar)
    label = ttk.Label(root, textvariable=stringvar)
    label.pack(side=TOP)

new_stringvar_button = ttk.Button(root, text="New Text", command=new_stringvar)
new_stringvar_button.pack()

root.mainloop()