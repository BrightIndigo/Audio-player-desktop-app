from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import pygame

pygame.mixer.init()

root = Tk()
root.title("Audio Player")
root.geometry("250x150")
frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0)

music_files = []
song = 0

def play():
    global song
    if music_files:
        music_file = music_files[song]
        print("Playing:", music_file)
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        current_song_label.config(text="Now Playing: " + os.path.basename(music_file))

def select_folder():
    folder_path = filedialog.askdirectory()
    print("Selected Folder:", folder_path)
    files = os.listdir(folder_path)
    global music_files
    music_files = [os.path.join(folder_path, file) for file in files if file.endswith(('.mp3', '.wav'))]

def next():
    global song
    song += 1
    if song >= len(music_files):
        song = 0
    play()

def previous():
    global song
    song -= 1
    if song >= len(music_files):
        song = 0
    play()

submit_button = Button(root, text='Browse', command=select_folder)
submit_button.grid(row=0, column=1)

play_button = ttk.Button(frm, text="Play", command=play)
play_button.grid(row=2, column=0)

next_button = ttk.Button(frm, text="Next", command=next)
next_button.grid(row=3, column=0)

previous_button = ttk.Button(frm, text="Previous", command=previous)
previous_button.grid(row=4, column=0)

ttk.Button(frm, text="Quit", command=root.destroy).grid(row=5, column=0)

current_song_label = ttk.Label(frm, text="")
current_song_label.grid(row=1, column=0, columnspan=1)

root.mainloop()
