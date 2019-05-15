import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
import functools

root = Tk()
root.minsize(300, 300)

listofsongs = ["sounds/Bring Me The Horizon - mother tongue.mp3",
"sounds/Halfway Right - Linkin Park.mp3",
"sounds/State Champs Back And Forth.mp3"]
realnames = ["Mother Tongue by Bring Me The Horizon",
"Halfway Right by Linkin Park",
"Back and Forth by State Champs"]
albumcovers = []

v = StringVar()
songlabel = Label(root, textvariable = v, width = 35)
index = 0
repeat = 0
pygame.init()
pygame.mixer.init()

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(file)
        pygame.mixer.music.load(listofsongs[0])


def updatelabel():
     global index
     global songname
     v.set(realnames[index-1])


def nextsong():
    global index
    global repeat
    #if index+1 > len([listofsongs]):
     #   index = 0
    #else:
    index += 1
    try:
        pygame.mixer.music.load(listofsongs[index-1])
    except:
        index = 0
        print("something")
    pygame.mixer.music.play(repeat)
    updatelabel()

def prevsong():
    global index
    global repeat
    index -= 1
    try:
        pygame.mixer.music.load(listofsongs[index-1])
    except:
        index = 0
    pygame.mixer.music.play(repeat)
    updatelabel()

def repeatsong():
    global index
    global repeat
    repeat = -1
    pygame.mixer.music.play(-1)
    updatelabel()
    print(repeat)

def stopsong():
    pygame.mixer.music.stop()
    v.set("")

root.title("Melodic")
label = Label(root, text = 'Music Player')
label.pack()
listbox = Listbox(root)
listbox.pack()

for items in realnames:
    listbox.insert(0, items)

realnames.reverse()

nextbutton = Button(root, text = 'Next Song', command = functools.partial(nextsong))
nextbutton.pack()

previousbutton = Button(root, text = 'Previous Song', command = functools.partial(prevsong))
previousbutton.pack()

stopbutton = Button(root, text ='Stop Music', command = functools.partial(stopsong))
stopbutton.pack()

repeatbutton = Button(root, text ='Repeat', command = functools.partial(repeatsong))
repeatbutton.pack()



songlabel.pack()

root.mainloop()