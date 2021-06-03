from tkinter import *
import gif
import gfw
import datetime

class Logo:
    def __init__(self):
        global now
        now = datetime.datetime.now()
        self.frame = Frame(gfw.window)
        self.frame.place(x = 100, y = 0)
        self.logo = gfw.image.load('Asset/image/똥터3.png')
        Label(self.frame,background="skyblue3", image=self.logo).pack()

        lbl = gif.ImageLabel(gfw.window)
        lbl.load('Asset/image/run2.gif')
        lbl.place(x=280,y=-40)
        self.byunimg = PhotoImage(file='Asset/image/메인변기.png')
        self.byunimg = self.byunimg.subsample(20,20)

        global img
        img = Label(gfw.window,image=self.byunimg,bg="skyblue3")
        img.place(x=550,y=20)
        gfw.window.after(1000, self.update())
        

    def draw(self):
        pass

    def update(self):
        second = datetime.datetime.now() - now
        second = int(second.seconds/3600)
        img.place(x = 550 + second, y= 20)
        print("반복")


    def handle_event(self,e):
        pass
