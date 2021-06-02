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

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()

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
        print('try to 화장실', args[1])
        save( chat_id, args[1] )
    else:
        bot.sendMessage(chat_id, '모르는 명령어입니다.\n지역 ex)\'지역 시흥시\'\n 화장실 ex)\'의정부시 상록근린공원\'\n 제대로 된 명령을 입력하세요.')

bot = telepot.Bot('1786093991:AAFmK0y7kfSnHEXVDJzxGcSaWcK8NLtjPSQ')
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

