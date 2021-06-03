# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import noti

def replyAptData(user, location):
    res_list = noti.getData( location )
    msg = ''
    # 받은 정보의 리스트를 정리하는 구간
    for i in range(len(res_list)):
        msg = ''
        msg += str("이름 : " + res_list[i]['PBCTLT_PLC_NM']+'\n')
        if res_list[i]['REFINE_ROADNM_ADDR'] == None:
            msg += ("도로명주소 : 정보가 없습니다\n")
        else:
            msg += str("도로명 주소 : " + res_list[i]['REFINE_ROADNM_ADDR']+'\n')
        if res_list[i]['OPEN_TM_INFO'] == None:
                msg += ("개방시간 : 미정\n")
        else:
            msg += str("개방시간 : " + res_list[i]['OPEN_TM_INFO']+'\n')
        if res_list[i]['MANAGE_INST_TELNO'] == None:
            msg += str("전화번호 : 없음\n")
        else:
            msg += str("전화번호 : " + res_list[i]['MANAGE_INST_TELNO'] + '\n')  
        msg += str("남녀공용 : " + res_list[i]['MALE_FEMALE_TOILET_YN'] + '\n')
        noti.sendMessage( user, msg )
        #msg += '\n'

    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '경기도의 시군구를 제대로 입력하세요' )

def replyToiletDate( user, location, toiletName ):
    res_list = noti.getToiletData( location, toiletName )

    if res_list != None:
        msg = ''
        # 받은 정보의 리스트를 정리하는 구간
        msg = ''
        msg += str("이름 : " + res_list['PBCTLT_PLC_NM']+'\n')
        if res_list['REFINE_ROADNM_ADDR'] == None:
            msg += ("도로명주소 : 정보가 없습니다\n")
        else:
            msg += str("도로명 주소 : " + res_list['REFINE_ROADNM_ADDR']+'\n')
        if res_list['OPEN_TM_INFO'] == None:
                msg += ("개방시간 : 미정\n")
        else:
            msg += str("개방시간 : " + res_list['OPEN_TM_INFO']+'\n')
        if res_list['MANAGE_INST_TELNO'] == None:
            msg += str("전화번호 : 없음\n")
        else:
            msg += str("전화번호 : " + res_list['MANAGE_INST_TELNO'] + '\n')  
        msg += str("남녀공용 : " + res_list['MALE_FEMALE_TOILET_YN'] + '\n')
        msg += str("메모\n")

        try:
            f = open('Asset/txt/' + res_list['SIGUN_NM']+'.txt',"r")
        except:
            msg += str("--메모없음--")

        for line in f:
            if line.startswith(res_list['PBCTLT_PLC_NM']):
                line = f.readline()
                line = line.replace('\+n','\n')
                msg += str(line + '\n')
        
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '화장실 [시군구] [화장실명]\nEx)화장실 시흥시 오이도역\n제대로 입력하세요' )

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지역') and len(args)>1:
        print('try to 지역', args[1])
        replyAptData( chat_id, args[1] )
    elif text.startswith('화장실')  and len(args)>1:
        tempArgs = ''
        for i in range(2, len(args)):
            tempArgs += args[i]

            if i != (len(args)-1):
                tempArgs +=' '
        print('try to 화장실', args[1], tempArgs)
        replyToiletDate( chat_id, args[1], tempArgs )
    else:
        bot.sendMessage(chat_id, '모르는 명령어입니다.\n지역 ex)\'지역 시흥시\'\n 화장실 ex)\'의정부시 상록근린공원\'\n 제대로 된 명령을 입력하세요.')

bot = telepot.Bot('1786093991:AAFmK0y7kfSnHEXVDJzxGcSaWcK8NLtjPSQ')
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

