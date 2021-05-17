
from tkinter import *
import tkinter.ttk
import gfw
import urllib.request
import base64





class MainFunc:
    def __init__(self):
        #리스트박스를 위한 프레임/스크롤바
        self.ListFrame = Frame(gfw.window)
        self.ListFrame.place(x=50,y=150)
        self.scrollbar = Scrollbar(self.ListFrame)
        self.scrollbar.pack(side="right",fill="y")

        listbox = Listbox(self.ListFrame,yscrollcommand= self.scrollbar.set,width= 40,height=15)

        for line in range(1,1001):
            listbox.insert(line,str(line)+"/1000")
        
        listbox.pack(side="left")
        self.scrollbar["command"] = listbox.yview
        
        #실 사용할 버튼들
        Button(gfw.window,text="즐겨찾기",width=18,height=2).place(x=50,y=400)
        Button(gfw.window,text="정보",width=18,height=2).place(x=198,y=400)
        Button(gfw.window,text="검색",width=10,height=2).place(x=540,y=20)

        values=[str(i)+"번" for i in range(1, 101)] 

        
        combobox = tkinter.ttk.Combobox(gfw.window,values=values)
        combobox.place(x=350,y=40)
        combobox.config(state='readonly')
        #u = urllib.request.urlopen("https://www.google.co.kr/maps/place/%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%8B%9C%ED%9D%A5%EC%8B%9C+%EC%A0%95%EC%99%951%EB%8F%99+%EC%82%B0%EA%B8%B0%EB%8C%80%ED%95%99%EB%A1%9C+237/@37.3403904,126.7313098,17z/data=!3m1!4b1!4m5!3m4!1s0x357b71060072975f:0xa150df14513cae41!8m2!3d37.3403904!4d126.7334985?hl=ko")
        #raw_data = u.read()
        #u.close()
        f = open("보기용.png","rb")
        img = f.read()
        pimg = PhotoImage(data=img)
        Label(gfw.window,image=pimg).pack()

        

        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass