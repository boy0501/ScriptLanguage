from tkinter import *
import gfw




class MainFunc:
    def __init__(self):
        self.frame = Frame(gfw.window)
        self.frame.place(x = 0 , y = 100)
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side="right",fill="y")
        listbox = Listbox(self.frame,yscrollcommand= self.scrollbar.set)
        for line in range(1,1001):
            listbox.insert(line,str(line)+"/1000")
        listbox.pack(side="left")
        self.scrollbar["command"] = listbox.yview
        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass