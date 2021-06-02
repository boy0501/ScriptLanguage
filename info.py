
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
import pickle
import gmail
import telegramButton

class InfoFunc:
    def __init__(self,Toilet):
        Button(gfw.window,text="뒤로가기",width=10,height=2,command=self.RetMain).place(x=520,y=20)
        self.textbox = Text(gfw.window,width=30,height=20,background="skyblue1")
        self.textbox.place(x=30,y=150)
        self.isbooked = False
        self.image = gfw.image.load('Asset/image/WhiteStar.png')
        self.Toilet = Toilet
        self.bookmarkButton = Button(gfw.window,image=self.image,command=self.bookmarking)
        self.bookmarkButton.place(x=260,y=150)
        self.bookmarkList = []
        Button(gfw.window,image=gfw.image.load('Asset/image/Gmail.png'), command = self.sendGmail).place(x=260,y=250)
        Button(gfw.window,image=gfw.image.load('Asset/image/tellegram.png'), command = self.sendTelegram).place(x=260,y=350)
        Button(gfw.window,text="저장하기",width=10,height=2,command=self.saveText).place(x=150,y=430)
        Button(gfw.window,text="여자화장실",width=10,height=1,command=self.LoadWomanChart).place(x=500,y=450)
        Button(gfw.window,text="남자화장실",width=10,height=1,command=self.LoadManChart).place(x=400,y=450)
        
        c_width = 300
        c_height = 280
        self.c = Canvas(gfw.window, width=c_width, height=c_height, bg= 'white')
        self.c.place(x=330,y=150)
        self.LoadText()
        self.LoadBookMark()
        self.LoadManChart()
        opentime = ""
        telno = ""
        if self.Toilet['OPEN_TM_INFO'] == None:
            opentime = "미정"
        else:
            opentime = self.Toilet['OPEN_TM_INFO']
        if self.Toilet['MANAGE_INST_TELNO'] == None:
            telno = "없음"
        else:
            telno = self.Toilet['MANAGE_INST_TELNO']            
        self.c.create_text(150,20,text="개방시간 : " + opentime)
        self.c.create_text(150,40,text="전화번호 : " + telno)
        self.c.create_text(150,60,text="남여공용? : " + self.Toilet['MALE_FEMALE_TOILET_YN'])

    def LoadManChart(self):
        #바 차트
        self.c.delete("delable")

        data = [int(self.Toilet['MALE_WTRCLS_CNT']),
        int(self.Toilet['MALE_UIL_CNT']),
        int(self.Toilet['MALE_DSPSN_WTRCLS_CNT']),
        int(self.Toilet['MALE_DSPSN_UIL_CNT']),
        int(self.Toilet['MALE_CHILDUSE_WTRCLS_CNT']),
        int(self.Toilet['MALE_CHILDUSE_UIL_CNT'])]


        #experiment with the variables below size to fit your needs

        c_width = 300
        c_height = 280

        y_stretch = 10
        y_gap = 20
        x_stretch = 20  #그래프간 간격
        x_width = 20    #그래프 한칸의 너비
        x_gap = 40      #그래프 시작만큼의 너비 
        for x, y in enumerate(data):
            # calculate reactangle coordinates
            x0 = x * x_stretch + x * x_width + x_gap
            y0 = c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = c_height - y_gap
            # Here we draw the bar
            self.c.create_rectangle(x0, y0, x1, y1, fill="red",tags="delable")
            self.c.create_text(x0+2, y0, anchor=SW, text=str(y),tags="delable")
        #self.c.create_text(50,270,text='\U0001f6bd')
        self.c.create_image(50,270,image=gfw.image.load("Asset/image/변기.png"),tags="delable")
        self.c.create_image(90,270,image=gfw.image.load("Asset/image/소변기.png"),tags="delable")
        self.c.create_image(130,270,image=gfw.image.load("Asset/image/장애.png"),tags="delable")
        self.c.create_image(170,270,image=gfw.image.load("Asset/image/장애.png"),tags="delable")
        self.c.create_image(210,270,image=gfw.image.load("Asset/image/어린이.png"),tags="delable")
        self.c.create_image(250,270,image=gfw.image.load("Asset/image/어린이.png"),tags="delable")

    
    def LoadWomanChart(self):
        self.c.delete("delable")
        data = [int(self.Toilet['FEMALE_WTRCLS_CNT']),
        int(self.Toilet['FEMALE_DSPSN_WTRCLS_CNT']),
        int(self.Toilet['FEMALE_CHILDUSE_WTRCLS_CNT'])]

        c_width = 300
        c_height = 280

        #experiment with the variables below size to fit your needs

        y_stretch = 5
        y_gap = 20
        x_stretch = 90  #그래프간 간격
        x_width = 20    #그래프 한칸의 너비 
        x_gap = 40      #그래프 시작만큼의 너비  
        for x, y in enumerate(data):
            # calculate reactangle coordinates
            x0 = x * x_stretch + x * x_width + x_gap
            y0 = c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = c_height - y_gap
            # Here we draw the bar
            self.c.create_rectangle(x0, y0, x1, y1, fill="red",tags="delable")
            self.c.create_text(x0+2, y0, anchor=SW, text=str(y),tags="delable")
        self.c.create_image(50,270,image=gfw.image.load("Asset/image/변기.png"),tags="delable")
        self.c.create_image(160,270,image=gfw.image.load("Asset/image/장애.png"),tags="delable")
        self.c.create_image(270,270,image=gfw.image.load("Asset/image/어린이.png"),tags="delable")
        

    def RetMain(self):
        mylist = gfw.window.place_slaves()
        for i in mylist:
            if i._name == "!frame" or i._name == "!label" or i._name == "!imagelabel": #Logo는 무조건 첫번째니까 항상 frame 1임
                continue
            i.place_forget()
        gfw.Objects['imsi'][7].place(x=30,y=150)    #명단리스트
        gfw.Objects['imsi'][6].place(x=50,y=400)    #정보
        gfw.Objects['imsi'][5].place(x=178,y=400)   #검색
        gfw.Objects['imsi'][4].place(x=520,y=20)    #즐찾
        gfw.Objects['imsi'][3].place(x=300,y=20)    #줌인
        gfw.Objects['imsi'][2].place(x=300,y=70)    #줌아웃
        gfw.Objects['imsi'][1].place(x=330,y=40)    #콤보박스
        gfw.Objects['imsi'][0].place(x=330,y=150)    #지도리스트

    def LoadBookMark(self):
        try:
            with open('Asset/binary/bookmark','rb') as f:
                self.bookmarkList = pickle.load(f)
        except:
            pass
        if self.Toilet in self.bookmarkList:
            self.isbooked = True
            self.bookmarkButton.configure(image=gfw.image.load('Asset/image/YellowStar.png'))
    def LoadText(self):
        try:
            f = open('Asset/txt/' + self.Toilet['SIGUN_NM']+'.txt',"r")
        except:
            open('Asset/txt/' + self.Toilet['SIGUN_NM']+'.txt',"w")
            return
        for line in f:
            if line.startswith(self.Toilet['PBCTLT_PLC_NM']):
                line = f.readline()
                line = line.replace('\+n','\n')
                self.textbox.insert(CURRENT,line)

        

    def bookmarking(self):
        self.isbooked = not self.isbooked   
        if self.isbooked == True:
            self.image = gfw.image.load('Asset/image/YellowStar.png')
            self.bookmarkButton.configure(image=self.image)
            self.bookmarkList.append(self.Toilet)
            with open('Asset/binary/bookmark','wb') as f:
                pickle.dump(self.bookmarkList,f)

        else:
            self.image = gfw.image.load('Asset/image/WhiteStar.png')
            self.bookmarkButton.configure(image=self.image)
            del self.bookmarkList[self.bookmarkList.index(self.Toilet)]
            with open('Asset/binary/bookmark','wb') as f:
                pickle.dump(self.bookmarkList,f)            

    def saveText(self):
        imsi = self.textbox.get("1.0","end")
        imsi = imsi.replace('\n',"\+n")
        ToChange = False
        FindNothing = True
        for line in fileinput.input('Asset/txt/' + self.Toilet['SIGUN_NM']+'.txt',inplace= True):
            if ToChange == True:
                line = line.replace(line,imsi+'\n')
                ToChange = False

            if line.startswith(self.Toilet['PBCTLT_PLC_NM']):
                ToChange = True
                FindNothing = False
            sys.stdout.write(line)
        if FindNothing == True:
            f = open('Asset/txt/' + self.Toilet['SIGUN_NM']+'.txt','a')
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

    
    def sendGmail(self):
        self.receiveMail = Tk()
        self.receiveMail.title("Write Receive Email")
        self.receiveMail.geometry("200x100")
        self.entryMail = Entry(self.receiveMail)
        self.sendbuttonMail = Button(self.receiveMail, text = "send", command = self.realSendGmail, width = 3, height = 1)
        self.entryMail.grid()
        self.sendbuttonMail.grid()
        self.receiveMail.mainloop()

    def realSendGmail(self):
        gmail.Send(str(self.entryMail.get()), self.Toilet)
        self.receiveMail.destroy()

    def sendTelegram(self):        #  보낼 텔레그램ID를 받는 창을 띄운다
        self.receiveTelegram = Tk()
        self.receiveTelegram.title("Write Receive TelegramID")
        self.receiveTelegram.geometry("200x100")
        self.entryTelegram = Entry(self.receiveTelegram)
        self.sendbuttonTelegram = Button(self.receiveTelegram, text = "send", command = self.realSendTelegram, width = 3, height = 1)
        self.entryTelegram.grid()
        self.sendbuttonTelegram.grid()
        self.receiveTelegram.mainloop()

    def realSendTelegram(self):       # 실제로 텔레그램 메세지을 보내는 함수
        telegramButton.Send(str(self.entryTelegram.get()), self.Toilet)
        self.receiveTelegram.destroy()


    def draw(self):
        pass

    def update(self):
        pass


    def handle_event(self,e):
        pass