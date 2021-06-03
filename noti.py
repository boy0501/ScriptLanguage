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
import ggToilet

bot = telepot.Bot('1786093991:AAFmK0y7kfSnHEXVDJzxGcSaWcK8NLtjPSQ')

def getData(location):
    res_list = []
    ggToilet.getGGToiletDataFromISBN(location, 1)
    res_list = ggToilet.listToiletForTelegream
    # for line in range(len( ggToilet.listToiletForTelegream)):
    #     res_list.append(line+1, ggToilet.listToiletForTelegream[line]['PBCTLT_PLC_NM'])

    return res_list

def getToiletData(location, ToiletName):
    res_list = []
    ggToilet.getGGToiletDataFromISBN(location, 1)
    res_list = ggToilet.listToiletForTelegream
    for i in range(len(res_list)):
        if ToiletName == res_list[i]['PBCTLT_PLC_NM']:
            print(res_list[i]['PBCTLT_PLC_NM'])
            return res_list[i]

    # for line in range(len( ggToilet.listToiletForTelegream)):
    #     res_list.append(line+1, ggToilet.listToiletForTelegream[line]['PBCTLT_PLC_NM'])

    return None

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData( param, date_param )
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')
    run(current_month)