from tkinter import *
import gif
import gfw




class Logo:
    def __init__(self):
        self.frame = Frame(gfw.window)
        self.frame.place(x = 100, y = 0)
        self.logo = gfw.image.load('Asset/image/똥터.png')

        Label(self.frame,image=self.logo,background="skyblue2").pack()
        lbl = gif.ImageLabel(gfw.window)
        lbl.load('Asset/image/run2.gif')
        lbl.place(x=10,y=-50)
        self.byunimg = PhotoImage(file='Asset/image/메인변기.png')
        self.byunimg = self.byunimg.subsample(20,20)
        img = Label(gfw.window,image=self.byunimg,bg="skyblue2")
        img.place(x=230,y=0)


    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass