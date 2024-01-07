from tkinter import *
from tkinter import ttk 
import wave

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Audio Player").grid(column=0, row=0)

def play():
    print("sth")


ttk.Button(frm, text="Play", command=play()).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


