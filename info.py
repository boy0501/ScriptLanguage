
from tkinter import *
import tkinter.ttk
import gfw
import urllib.request              
import requests
from PIL import Image
from io import BytesIO
import PIL.ImageTk
import ggToilet

class InfoFunc:
    def __init__(self,Toilet):
        Button(gfw.window,text="뒤로가기",width=10,height=2).place(x=520,y=20)
        str = StringVar()
        self.textbox = Text(gfw.window,width=40,height=20,background="yellow")
        self.textbox.place(x=30,y=150)
        self.isbooked = False
        self.image = gfw.image.load('WhiteStar.png')
    
        self.bookmarkButton = Button(gfw.window,image=self.image,command=self.bookmarking)
        self.bookmarkButton.place(x=325,y=150)
        Button(gfw.window,image=gfw.image.load('Gmail.png')).place(x=325,y=250)
        Button(gfw.window,image=gfw.image.load('tellegram.png')).place(x=325,y=350)
        Button(gfw.window,text="저장하기",width=10,height=2,command=self.saveText).place(x=150,y=430)
        

    def bookmarking(self):
        self.isbooked = not self.isbooked
        if self.isbooked == True:
            self.image = gfw.image.load('YellowStar.png')
            self.bookmarkButton.configure(image=self.image)
        else:
            self.image = gfw.image.load('WhiteStar.png')
            self.bookmarkButton.configure(image=self.image)

    def saveText(self):
        imsi = self.textbox.get("1.0","end")
        f = open("임시.txt","w")
        f.write(imsi)
        f.close()
        #self.textbox.insert(INSERT,imsi) 값입력법





    def pushObj(self,obj):
        gfw.Objects[__name__].append(obj)

    

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass