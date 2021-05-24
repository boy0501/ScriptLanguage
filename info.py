
from tkinter import *
import tkinter.ttk
import gfw
import urllib.request              
import requests
from PIL import Image
from io import BytesIO
import PIL.ImageTk
import ggToilet
import fileinput
import sys

class InfoFunc:
    def __init__(self,Toilet):
        Button(gfw.window,text="뒤로가기",width=10,height=2).place(x=520,y=20)
        str = StringVar()
        self.textbox = Text(gfw.window,width=40,height=20,background="yellow")
        self.textbox.place(x=30,y=150)
        self.isbooked = False
        self.image = gfw.image.load('WhiteStar.png')
        self.Toilet = Toilet
        self.bookmarkButton = Button(gfw.window,image=self.image,command=self.bookmarking)
        self.bookmarkButton.place(x=325,y=150)
        Button(gfw.window,image=gfw.image.load('Gmail.png')).place(x=325,y=250)
        Button(gfw.window,image=gfw.image.load('tellegram.png')).place(x=325,y=350)
        Button(gfw.window,text="저장하기",width=10,height=2,command=self.saveText).place(x=150,y=430)
        self.LoadText()

    def LoadText(self):
        try:
            f = open(self.Toilet['SIGUN_NM']+'.txt',"r")
        except:
            open(self.Toilet['SIGUN_NM']+'.txt',"w")
            return
        for line in f:
            if line.startswith(self.Toilet['PBCTLT_PLC_NM']):
                line = f.readline()
                line = line.replace('\+n','\n')
                self.textbox.insert(CURRENT,line)

        

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
        imsi = imsi.replace('\n',"\+n")
        ToChange = False
        FindNothing = True
        for line in fileinput.input(self.Toilet['SIGUN_NM']+'.txt',inplace= True):
            if ToChange == True:
                line = line.replace(line,imsi+'\n')
                ToChange = False

            if line.startswith(self.Toilet['PBCTLT_PLC_NM']):
                ToChange = True
                FindNothing = False
            sys.stdout.write(line)
        if FindNothing == True:
            f = open(self.Toilet['SIGUN_NM']+'.txt','a')
            f.write(self.Toilet['PBCTLT_PLC_NM']+'\n')
            f.write(imsi+'\n')
            f.close()
        #f = open("임시.txt","a")
        #for line in f:
        #    if line.startswith(self.Toilet['PBCTLT_PLC_NM']):
        #        line = f.readline()
        #        
        #f.write(self.Toilet['PBCTLT_PLC_NM']+'\n')
        #f.write(imsi+'\n')
        #for line in f:
        #    if line.startswith('name'):

        
        #self.textbox.insert(INSERT,imsi) 값입력법





    def pushObj(self,obj):
        gfw.Objects[__name__].append(obj)

    

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass