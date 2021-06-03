import mimetypes
import mysmtplib
import fileinput
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def Send(recipientAddr, Toilet):
    #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소
    port = "587"
    htmlFileName = "message.html"

    senderAddr = "kimkiyoun33@gmail.com"     # 보내는사람 email 주소.
    #recipientAddr = "kevin67111@naver.com"   # 받는사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "똥 터 에서 보내드립니다"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msg.attach(MIMEText("이름 : " + Toilet['PBCTLT_PLC_NM']))
    if Toilet['OPEN_TM_INFO'] == None:
            msg.attach(MIMEText("개방시간 : 미정"))
    else:
           msg.attach(MIMEText("개방시간 : " + Toilet['OPEN_TM_INFO']))
    if Toilet['MANAGE_INST_TELNO'] == None:
        msg.attach(MIMEText("전화번호 : 없음"))
    else:
        msg.attach(MIMEText("전화번호 : " + Toilet['MANAGE_INST_TELNO']))  
    msg.attach(MIMEText("남녀공용 : " + Toilet['MALE_FEMALE_TOILET_YN']))

    msg.attach(MIMEText("메모"))
    try:
        f = open('Asset/txt/' + Toilet['SIGUN_NM']+'.txt',"r")
    except:
        pass

    for line in f:
        if line.startswith(Toilet['PBCTLT_PLC_NM']):
            line = f.readline()
            line = line.replace('\+n','\n')
            msg.attach(MIMEText(line))


    # 보낼 문서를 생성합니다
    # htmlFD = open(htmlFileName, 'rb')
    # HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    # htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    #msg.attach(HtmlPart)

    # 메일을 발송한다
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("kimkiyoun33@gmail.com","yurisoletminju-1")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()