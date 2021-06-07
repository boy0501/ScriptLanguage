
from tkinter import *
import tkinter.ttk
import gfw
import urllib.request              
import requests
from PIL import Image
from io import BytesIO
import PIL.ImageTk
import ggToilet
from info import InfoFunc
import pickle
import receiveTelegram

class MainFunc:
    def __init__(self):
        #리스트박스를 위한 프레임/스크롤바
        self.BookMarkTab = False        #북마크 화면이면 True 아니면 False
        self.Zoom = 13
        self.ListFrame = Frame(gfw.window)
        self.ListFrame.place(x=30,y=150)

        self.scrollbar = Scrollbar(self.ListFrame)
        self.scrollbar.pack(side="right",fill="y")


        self.listbox = Listbox(self.ListFrame,yscrollcommand= self.scrollbar.set,width= 40,height=15,bg="#EBE5D9")
        self.listbox.bind("<Button-1>",self.UpdateMap)
        #디폴트
        ggToilet.getGGToiletDataFromISBN('시흥시', 0)
        for line in range(len( ggToilet.listToilet)):
            self.listbox.insert(line+1, ggToilet.listToilet[line]['PBCTLT_PLC_NM'])
        # for line in range(1,1001):
        #     listbox.insert(line,str(line)+"/1000")
        
        self.listbox.selection_set(first=0)
        self.listbox.pack(side="left")
        self.scrollbar["command"] = self.listbox.yview
        
        uri = 'https://api-maps.cloud.toast.com/maps/v3.0/appkeys/vtJBJf5yCkI6EgPY/static-maps?lon=%s&lat=%s&width=300&height=300&mx=%s&my=%s' % (126.7379803,37.3706350,126.7379803,37.3706350)
        r = requests.get(uri)
        im = Image.open(BytesIO(r.content))
        self.image = PIL.ImageTk.PhotoImage(im)
        self.mapinfo = Label(gfw.window,image=self.image)
        self.mapinfo.place(x=330,y=150)

        #실 사용할 버튼들
        Button(gfw.window,text="즐겨찾기",width=18,height=2, bg = '#EBE5D9', activebackground = '#FACFAF',command=self.BookMark).place(x=40,y=400)
        Button(gfw.window,text="정보",width=18,height=2,  bg = '#EBE5D9', activebackground = '#FACFAF', command=self.ToInfo).place(x=183,y=400)
        Button(gfw.window,text="검색",width=10,height=2, bg = '#EBE5D9', activebackground = '#FACFAF',command=self.search).place(x=520,y=80)
        self.ZoominButton = Button(gfw.window,text="+",width=2,height=1, bg = '#EBE5D9', activebackground = '#FACFAF', command=self.ZoomIn)
        self.ZoominButton.place(x=600,y=370)
        self.ZoomOutButton = Button(gfw.window,text="-",width=2,height=1, bg = '#EBE5D9', activebackground = '#FACFAF', command=self.ZoomOut)
        self.ZoomOutButton.place(x=600,y=410)

        listSelectSigun = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', 
                           '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
                           '이천시', '의정부시', '파주시','평택시','포천시', '하남시','화성시']

        values=[listSelectSigun[i] for i in range(len(listSelectSigun))] 

        self.combobox = tkinter.ttk.Combobox(gfw.window,values=values)
        self.combobox.place(x=300,y=100)
        self.combobox.config(state='readonly')
        self.combobox.current(13)   #시흥시




    def ZoomIn(self):
        if self.Zoom + 1 < 19:
            self.Zoom += 1
        if self.BookMarkTab:
            y = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        else:
            y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        #y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
        #x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        url = 'https://api-maps.cloud.toast.com/maps/v3.0/appkeys/vtJBJf5yCkI6EgPY/static-maps?lon=%s&lat=%s&width=300&height=300&mx=%s&my=%s&zoom=%d' % (y,x,y,x,self.Zoom)
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        self.image = PIL.ImageTk.PhotoImage(im)
        self.mapinfo.configure(image=self.image)

    def ZoomOut(self):
        if self.Zoom - 1 > 0:
            self.Zoom -= 1
        if self.BookMarkTab:
            y = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        else:
            y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        #y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
        #x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        url = 'https://api-maps.cloud.toast.com/maps/v3.0/appkeys/vtJBJf5yCkI6EgPY/static-maps?lon=%s&lat=%s&width=300&height=300&mx=%s&my=%s&zoom=%d' % (y,x,y,x,self.Zoom)
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        self.image = PIL.ImageTk.PhotoImage(im)
        self.mapinfo.configure(image=self.image)

    def UpdateMap(self,event):
        if self.BookMarkTab:
            y = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = self.bookmarkList[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        else:
            y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
            x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        #y = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LOGT']
        #x = ggToilet.listToilet[self.listbox.curselection()[0]]['REFINE_WGS84_LAT']
        urlparams = urllib.parse.urlencode({'center': '%s,%s' % (x,y),
                                            'zoom': '15',
                                            'size': '%dx%d' % (300, 300),
                                            'maptype': 'roadmap',
                                            'markers': 'color:blue|label:S|40.702147,-74.015794',
                                            'markers': 'color:green|label:G|40.711614,-74.012318',
                                            'markers': 'color:red|label:C|%s,%s' % (x,y),
                                            'key': 'AIzaSyBZRdlRcQY9vehUC0-A5m7TKYpi5iI48Yk'})
        # 세개의 marker 모두 표시됨.
        #urlparams = 'https://maps.googleapis.com/maps/api/staticmap?center=63.259591,-144.667969&zoom=6&size=640x640&markers=color:blue%7Clabel:S%7C62.107733,-145.541936&markers=color:green%7CDelta+Junction,AK&markers=color:0xFFFF00%7Clabel:C%7CTok,AK"&key=AIzaSyDdMEbLtZCpCmtJ2X-QZYRH1mOPGOUE76A'
    #
        url = 'https://api-maps.cloud.toast.com/maps/v3.0/appkeys/vtJBJf5yCkI6EgPY/static-maps?lon=%s&lat=%s&width=300&height=300&mx=%s&my=%s&zoom=%d' % (y,x,y,x,self.Zoom)
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        self.image = PIL.ImageTk.PhotoImage(im)
        self.mapinfo.configure(image=self.image)

    def BookMark(self):
        self.BookMarkTab = True
        self.bookmarkList = []
        try:
            with open('Asset/binary/bookmark','rb') as f:
                self.bookmarkList = pickle.load(f)
        except:
            pass
        self.listbox.delete(0,END)
        for line in range(len(self.bookmarkList)):
            self.listbox.insert(line+1, self.bookmarkList[line]['PBCTLT_PLC_NM'])

    def pushObj(self,obj):
        gfw.Objects[__name__].append(obj)

    def search(self):
        self.BookMarkTab = False
        self.listbox.delete(0, len(ggToilet.listToilet)+1)
        ggToilet.getGGToiletDataFromISBN(self.combobox.get(), 0)
        for line in range(len( ggToilet.listToilet)):
            self.listbox.insert(line+1, ggToilet.listToilet[line]['PBCTLT_PLC_NM'])
    
    def ToInfo(self):
        if self.BookMarkTab:
            selectedToilet = self.bookmarkList[self.listbox.curselection()[0]]
        else:
            selectedToilet =  ggToilet.listToilet[self.listbox.curselection()[0]]
        
        mylist = gfw.window.place_slaves()
        gfw.Objects['imsi'] = mylist
        for i in mylist:
            if i._name == "!frame" or i._name == "!label" or i._name == "!imagelabel": #Logo는 무조건 첫번째니까 항상 frame 1임
                continue
            i.place_forget()

        info_func = InfoFunc(selectedToilet)
        gfw.world.add(gfw.layer.infofunc,info_func)
        
        

        

    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass