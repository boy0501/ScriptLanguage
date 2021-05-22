from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from urllib.parse import quote

conn = None

# 경기도 OpenAPI 접속정보 information
server = "openapi.gg.go.kr"

# URL만들기(여기서 인덱스 번호와 사이즈를 조절)
def userURIBuilder(uri, **user):
    str = uri + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

# HTTPSConnextion 서버 연결
def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)      #https프로토콜을 사용하기 위한 핸들러
    conn.set_debuglevel(1)
        
# 서버에 필요한 정보를 URL로 요청하고 XML문서로 응답받는 구조
def getGGToiletDataFromISBN(strSIGUN):
    global server, conn
    if conn == None :
        connectOpenAPIServer() 
    uri = userURIBuilder("/Publtolt", KEY = '083df84f1e7c4c37b50f457c75e7d3fa', pIndex="1", pSize="1000", SIGUN_NM = quote(strSIGUN))
    conn.request("GET", uri, None, {})      #이거에 대해서는 한번 알아보기
    
    req = conn.getresponse()
    print (req.status)
    if int(req.status) == 200 :
        print("Book data downloading complete!")
        s = req.read()
        s = s.decode("utf-8")
        return extractBookData(s)
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)   #xml의 정보를 읽어옴
    listSigun = {}
    global listToilet
    listToilet = []  # 화장실 리스트를 저장할 list 초기화
    itemElements = tree.iter(tag = "row")  # return list type
    for item in itemElements:
        toilet = {}     #각 화장실을 저장할 dict 초기화
        toilet['DATA_STD_DE'] = item.find("DATA_STD_DE").text
        toilet['SIGUN_NM'] = item.find("SIGUN_NM").text
        toilet['SIGUN_CD'] = item.find("SIGUN_CD").text
        toilet['PUBLFACLT_DIV_NM'] = item.find("PUBLFACLT_DIV_NM").text
        toilet['PBCTLT_PLC_NM'] = item.find("PBCTLT_PLC_NM").text
        toilet['MALE_FEMALE_TOILET_YN'] = item.find("MALE_FEMALE_TOILET_YN").text
        toilet['MALE_WTRCLS_CNT'] = item.find("MALE_WTRCLS_CNT").text
        toilet['MALE_UIL_CNT'] = item.find("MALE_UIL_CNT").text
        toilet['DATA_STD_DE'] = item.find("MALE_DSPSN_WTRCLS_CNT").text
        toilet['MALE_DSPSN_WTRCLS_CNT'] = item.find("MALE_DSPSN_UIL_CNT").text
        toilet['MALE_CHILDUSE_WTRCLS_CNT'] = item.find("MALE_CHILDUSE_WTRCLS_CNT").text
        toilet['MALE_CHILDUSE_UIL_CNT'] = item.find("MALE_CHILDUSE_UIL_CNT").text
        toilet['FEMALE_WTRCLS_CNT'] = item.find("FEMALE_WTRCLS_CNT").text
        toilet['FEMALE_DSPSN_WTRCLS_CNT'] = item.find("FEMALE_DSPSN_WTRCLS_CNT").text
        toilet['FEMALE_CHILDUSE_WTRCLS_CNT'] = item.find("FEMALE_CHILDUSE_WTRCLS_CNT").text
        toilet['MANAGE_INST_NM'] = item.find("MANAGE_INST_NM").text
        toilet['MANAGE_INST_TELNO'] = item.find("MANAGE_INST_TELNO").text
        toilet['OPEN_TM_INFO'] = item.find("OPEN_TM_INFO").text
        toilet['INSTL_YY'] = item.find("INSTL_YY").text
        toilet['REFINE_LOTNO_ADDR'] = item.find("REFINE_LOTNO_ADDR").text
        toilet['REFINE_ROADNM_ADDR'] = item.find("REFINE_ROADNM_ADDR").text
        toilet['REFINE_ZIP_CD'] = item.find("REFINE_ZIP_CD").text
        toilet['REFINE_WGS84_LOGT'] = item.find("REFINE_WGS84_LOGT").text
        toilet['REFINE_WGS84_LAT'] = item.find("REFINE_WGS84_LAT").text

        listToilet.append(toilet)

getGGToiletDataFromISBN('시흥시')
    