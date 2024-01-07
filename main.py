from tkinter import *
from tkinter import ttk 
import os

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0, sticky=(N, W, E, S))

ttk.Label(frm, text="Audio Player").grid(row=0, column=0, columnspan=2)

def play():
    # Replace this with the actual implementation to play audio
    print("Playing audio...")

ttk.Button(frm, text="Play", command=play).grid(row=1, column=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=0, column=1)

def print_answers():
    print("sanie")

submit_button = Button(root, text='Submit', command=print_answers) 
submit_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
