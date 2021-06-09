from tkinter import *
import gif
import gfw
import datetime

class Logo:
    def __init__(self):
        now = datetime.datetime.now()
        self.frame = Frame(gfw.window)
        self.frame.place(x = 100, y = 0)
        self.logo = gfw.image.load('Asset/image/logo3.png')
        Label(self.frame,background="skyblue3", image=self.logo).pack()

        self.lbl = gif.ImageLabel(gfw.window)
        self.lbl.load('Asset/image/run3.gif')
        self.lbl.place(x=280,y=-40)
        self.byunimg = PhotoImage(file='Asset/image/logotoilet.png')
        self.byunimg = self.byunimg.subsample(20,20)
        self.imglabelx = 280

        global img
        img = Label(gfw.window,image=self.byunimg,bg="skyblue3")
        img.place(x=550,y=20)
        #gfw.window.after(1000, self.update())

        gfw.window.after(100,self.update)

        

    def draw(self):
        pass

    def update(self):
       # print("넘어옴")
        gfw.window.after(100,self.update)
        self.lbl.place(x=self.imglabelx)
        self.imglabelx += 2
        if self.imglabelx > 488:
            self.imglabelx = 280


    def handle_event(self,e):
        pass
