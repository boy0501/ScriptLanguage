from tkinter import *
import tkinter.ttk
import gfw




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


        

        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass