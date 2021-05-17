
from tkinter import *
import tkinter.ttk
import gfw
import urllib.request              
import requests
from PIL import Image
from io import BytesIO
import PIL.ImageTk

class MainFunc:
    def __init__(self):
        #리스트박스를 위한 프레임/스크롤바
        self.ListFrame = Frame(gfw.window)
        self.ListFrame.place(x=30,y=150)
        self.scrollbar = Scrollbar(self.ListFrame)
        self.scrollbar.pack(side="right",fill="y")

        listbox = Listbox(self.ListFrame,yscrollcommand= self.scrollbar.set,width= 40,height=15)

        for line in range(1,1001):
            listbox.insert(line,str(line)+"/1000")
        
        listbox.pack(side="left")
        self.scrollbar["command"] = listbox.yview
        
        #실 사용할 버튼들
        Button(gfw.window,text="즐겨찾기",width=18,height=2).place(x=50,y=400)
        Button(gfw.window,text="정보",width=18,height=2).place(x=178,y=400)
        Button(gfw.window,text="검색",width=10,height=2).place(x=520,y=20)

        values=[str(i)+"번" for i in range(1, 101)] 

        
        combobox = tkinter.ttk.Combobox(gfw.window,values=values)
        combobox.place(x=330,y=40)
        combobox.config(state='readonly')
        #구글맵 띄우기
        largura = 300
        alturaplus = 300

        # 마지막 markers 만 표시됨
        #37.3394985,126.7336518,16.58z
        urlparams = urllib.parse.urlencode({'center': '31.3394985,126.7336518',
                                            'zoom': '15',
                                            'size': '%dx%d' % (largura, alturaplus),
                                            'maptype': 'roadmap',
                                            'markers': 'color:blue|label:S|40.702147,-74.015794',
                                            'markers': 'color:green|label:G|40.711614,-74.012318',
                                            'markers': 'color:red|label:C|40.718217,-73.998284',
                                            'key': 'AIzaSyBZRdlRcQY9vehUC0-A5m7TKYpi5iI48Yk'})
        # 세개의 marker 모두 표시됨.
        #urlparams = 'https://maps.googleapis.com/maps/api/staticmap?center=63.259591,-144.667969&zoom=6&size=640x640&markers=color:blue%7Clabel:S%7C62.107733,-145.541936&markers=color:green%7CDelta+Junction,AK&markers=color:0xFFFF00%7Clabel:C%7CTok,AK"&key=AIzaSyDdMEbLtZCpCmtJ2X-QZYRH1mOPGOUE76A'

        url = 'https://maps.googleapis.com/maps/api/staticmap?' + urlparams
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        self.image = PIL.ImageTk.PhotoImage(im)
        Label(gfw.window,image=self.image).place(x=330,y=150)
        
        

        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass