from tkinter import font
import gfw

fonts = {}

def load(file, size):
    key = file + '_' + str(size)
    global fonts
    if key in fonts:
        return fonts[key]
    font = font.Font(gfw.window,family = file, size= size)
    fonts[key] = font
    return font

def unload(file, size):
    key = file + '_' + str(size)
    global fonts
    if key in fonts:
        del fonts[key]