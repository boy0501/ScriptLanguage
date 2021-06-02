# coding=utf-8

import telepot

def Send( user, Toilet):
    bot = telepot.Bot('1786093991:AAFmK0y7kfSnHEXVDJzxGcSaWcK8NLtjPSQ')
    #bot.getME()    # 봇의 정보를 받고 싶으면 주석을 풀면 된다
    msg = '똥 터 에서 보내드립니다\n'

    msg += str("이름 : " + Toilet['PBCTLT_PLC_NM']+'\n')
    if Toilet['OPEN_TM_INFO'] == None:
            msg += ("개방시간 : 미정\n")
    else:
           msg += str("개방시간 : " + Toilet['OPEN_TM_INFO']+'\n')
    if Toilet['MANAGE_INST_TELNO'] == None:
        msg += str("전화번호 : 없음\n")
    else:
        msg += str("전화번호 : " + Toilet['MANAGE_INST_TELNO'] + '\n')  
    msg += str("남녀공용 : " + Toilet['MALE_FEMALE_TOILET_YN'] + '\n')

    # 위치를 추가해야돼 말아야돼??

    msg += str("메모\n")
    try:
        f = open('Asset/txt/' + Toilet['SIGUN_NM']+'.txt',"r")
    except:
        msg += str("--메모없음--")

    for line in f:
        if line.startswith(Toilet['PBCTLT_PLC_NM']):
            line = f.readline()
            line = line.replace('\+n','\n')
            msg += str(line + '\n')

    bot.sendMessage(user, msg)

