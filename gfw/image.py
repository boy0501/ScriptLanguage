from tkinter import *

images = {}

def load(fileName):
    global images
    if fileName in images:
        return images[fileName]

    image = PhotoImage(file = fileName)
    images[fileName] = image
    return image

def unload(file):
    global images
    if file in images:
        del images[file]