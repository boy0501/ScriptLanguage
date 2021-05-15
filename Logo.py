from tkinter import *
import gfw




class Logo:
    def __init__(self):
        self.frame = Frame(gfw.window)
        self.frame.place(x = 0, y = 0)
        self.image = gfw.image.load('똥터.png')
        Label(self.frame,image=self.image).pack()
        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass