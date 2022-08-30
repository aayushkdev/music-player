from pygame import mixer
import glob
import os
from tkinter import *
import pygame
#from tkinter import filedialog

root = Tk()

mixer.init()

song_name = StringVar()
song_name.set("-")

def chdir():
    try:
        folder_selected = filedialog.askdirectory()
        mylistbox.delete(0, END)
        os.chdir(folder_selected)
        for line in glob.glob("*.mp3"):
            mylistbox.insert(END, line)
    except:
        None

    
def stop():
    try:
        mixer.music.stop()
        song_name.set("-")
    except:
        return "No song is playing"
    
def start():
    filename = mylistbox.get(ACTIVE)
    try:
        mixer.music.load(filename)
        mixer.music.play()
        song_name.set(filename)
    except:
        return None
    
    
def optns():
    top = Toplevel(root)
    top.geometry("300x300")
    top.title("options")
    
    Button(top, text="change music directory", command=chdir).pack()  

    
    top.mainloop()

class Pause:
    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

PAUSE = Pause()

def pauseres():
    PAUSE.toggle()

root.geometry("700x500")
root.title("Music player")
root.resizable(False, False)


playlist = LabelFrame(root, text="Song playlist")
playlist.place(x=0, y=0, width=700,height=400)

controls = LabelFrame(root)
controls.place(x=0, y=400, width=700,height=100)

scrollbar = Scrollbar(playlist)
scrollbar.pack(side=RIGHT, fill=Y)

mylistbox = Listbox(playlist, yscrollcommand = scrollbar.set)

os.chdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'))
for line in glob.glob("*.mp3"):
    mylistbox.insert(END, line)

mylistbox.place(x=0, y=0, width=700, height=400)
scrollbar.config(command = mylistbox.yview)

song_playing = Label(controls, textvariable=song_name)
song_playing.place(x=350, y=2)


Button(controls, text="play/resume", command=pauseres).place(x=0, y=69)

Button(controls, text="stop", command=stop).place(x=85, y=69)

Button(controls, text="start", command=start).place(x=130, y=69)

Button(controls, text="options", command=optns).place(x=600, y=69)






root.mainloop()
