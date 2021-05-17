# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# from urllib.parse import quote_plus
 
# baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# plusUrl = input('검색어 입력: ') 
# crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
 
# url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
# html = urlopen(url)
# soup = bs(html, "html.parser")
# img = soup.find_all(class_='thumb')
 
# n = 1
# for i in img:
#     print(n)
#     imgUrl = i.find("img")["src"]
#     with urlopen(imgUrl) as f:
#         with open('./images/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
#             img = f.read()
#             h.write(img)
#     n += 1
#     if n > crawl_num:
#         break
    
    
# print('Image Crawling is done.')


# 코알라유니브 스터디: 공공공공공경경 - 고주형
# 네이버 신지도 데이터 수집하기

# from bs4 import BeautifulSoup as soup
# from tkinter import *
# import urllib.parse
# import urllib.request
# from PIL import Image,ImageTk
# import io
# import tkinterweb
# from tkinter import *
# import base64
# root= Tk()
# imgs = []
# for i in range(9):
#     image_byt = urllib.request.urlopen("https://map0.daumcdn.net/map_2d/2103dor/L3/1912/804.png").read()
#     image_b64 = base64.encodestring(image_byt)
#     photo = PhotoImage(data=image_b64)
#     imgs.append(photo)

# label1 = Label(root, image=photo)
# label1.pack()
# root.mainloop()

# import folium
# from folium.plugins import MarkerCluster

# map = folium.Map(location = [35.8797296,128.4964884], zoom_start =7)


# map
# map.save('good.html')


# Import Module
# from tkinter import *
# from tkhtmlview import HTMLLabel
  
# # Create Object
# root = Tk()
  
# # Set Geomerty
# root.geometry("400x400")
# f = open("good.html")
# b = f.read()
# # Add label
# my_label = HTMLLabel(root, html=str(b)
# )
  
# # Adjust label
# my_label.pack(pady=40, padx=40)
  
# # Execute Tkinter
# root.mainloop()
# Import Module
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# import requests
 
 
# def getLatLng(address):
#     result = ""
 
#     url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
#     rest_api_key = 'f3efd197e63611e719ced7d8c406b4b3'
#     header = {'Authorization': 'KakaoAK ' + rest_api_key}
 
#     r = requests.get(url, headers=header)
 
#     if r.status_code == 200:
#         result_address = r.json()["documents"][0]["address"]
        
#         result = result_address["y"], result_address["x"]
#     else:
#         result = "ERROR[" + str(r.status_code) + "]"
    
#     return result
 
 
# def getKakaoMapHtml(address_latlng):
#     javascript_key = "c57f7ba1f7d11b63fb8c13d2cf924fe1"
 
#     result = ""
#     result = result + "<div id='map' style='width:300px;height:200px;display:inline-block;'></div>" + "\n"
#     result = result + "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + javascript_key + "'></script>" + "\n"
#     result = result + "<script>" + "\n"
#     result = result + "    var container = document.getElementById('map'); " + "\n"
#     result = result + "    var options = {" + "\n"
#     result = result + "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
#     result = result + "           level: 3" + "\n"
#     result = result + "    }; " + "\n"
#     result = result + "    var map = new kakao.maps.Map(container, options); " + "\n"
    
#     # 검색한 좌표의 마커 생성을 위해 추가
#     result = result + "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
#     result = result + "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
#     result = result + "    marker.setMap(map); " + "\n"
 
#     result = result + "</script>" + "\n"
    
#     return result
 
# # main()
# if __name__ == "__main__":
#     address = "서울 강남구 선릉로 669"
    
#     # 카카오 REST API로 좌표 구하기
#     address_latlng = getLatLng(address)
 
#     # 좌표로 지도 첨부 HTML 생성
#     if str(address_latlng).find("ERROR") < 0:
#         map_html = getKakaoMapHtml(address_latlng)
        
#         print(map_html)
#     else:
#         print("[ERROR]getLatLng")


# from tkinter import *
# from tkhtmlview import HTMLLabel
  
# # Create Object
# root = Tk()
  
# # Set Geomerty
# root.geometry("400x400")
  
# # Add label
# my_label = HTMLLabel(root, html="""
# <div id='map' style='width:300px;height:200px;display:inline-block;'></div>
# <script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=c57f7ba1f7d11b63fb8c13d2cf924fe1'></script>
# <script>
#     var container = document.getElementById('map');
#     var options = {
#            center: new kakao.maps.LatLng(37.5166119773031, 127.041258693516),
#            level: 3
#     };
#     var map = new kakao.maps.Map(container, options);
#     var markerPosition  = new kakao.maps.LatLng(37.5166119773031, 127.041258693516);
#     var marker = new kakao.maps.Marker({position: markerPosition});
#     marker.setMap(map);
# </script>


# """)
  
# # Adjust label
# my_label.pack(pady=20, padx=20)
  
# # Execute Tkinter
# root.mainloop()
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# from tkinter import *
# import base64
# import urllib.request

# window = Tk()

# u = urllib.request.urlopen("https://www.google.co.kr/maps/place/%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%8B%9C%ED%9D%A5%EC%8B%9C+%EC%A0%95%EC%99%951%EB%8F%99+%EC%82%B0%EA%B8%B0%EB%8C%80%ED%95%99%EB%A1%9C+237/@37.3403904,126.7313098,17z/data=!3m1!4b1!4m5!3m4!1s0x357b71060072975f:0xa150df14513cae41!8m2!3d37.3403904!4d126.7334985?hl=ko")
# raw_data = u.read()
# u.close()

# pimg = PhotoImage(data=base64.encodestring(raw_data))
# Label(window,image=pimg).pack()

# window.mainloop()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# import googlemaps
# from datetime import datetime

# gmaps = googlemaps.Client(key='AIzaSyBZRdlRcQY9vehUC0-A5m7TKYpi5iI48Yk')

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)

import urllib.request              
import requests
from PIL import Image
from io import BytesIO
import tkinter

largura = 100
alturaplus = 100
final = Image.new("RGB", (largura, alturaplus))

# 마지막 markers 만 표시됨
urlparams = urllib.parse.urlencode({'center': 'Brooklyn+Bridge,New+York,NY',
                                    'zoom': '15',
                                    'size': '%dx%d' % (largura, alturaplus),
                                    'maptype': 'hybrid',
                                    'markers': 'color:blue|label:S|40.702147,-74.015794',
                                    'markers': 'color:green|label:G|40.711614,-74.012318',
                                    'markers': 'color:red|label:C|40.718217,-73.998284',
                                    'key': 'AIzaSyBZRdlRcQY9vehUC0-A5m7TKYpi5iI48Yk'})
# 세개의 marker 모두 표시됨.
#urlparams = 'https://maps.googleapis.com/maps/api/staticmap?center=63.259591,-144.667969&zoom=6&size=640x640&markers=color:blue%7Clabel:S%7C62.107733,-145.541936&markers=color:green%7CDelta+Junction,AK&markers=color:0xFFFF00%7Clabel:C%7CTok,AK"&key=AIzaSyDdMEbLtZCpCmtJ2X-QZYRH1mOPGOUE76A'

url = 'https://maps.googleapis.com/maps/api/staticmap?' + urlparams

r = requests.get(url)
im = Image.open(BytesIO(r.content))
#final.paste(im)
#final.show()

import PIL.ImageTk
root = tkinter.Tk()
#canvas = tkinter.Canvas(root,width=999,height=999)
#canvas.pack()
image = PIL.ImageTk.PhotoImage(im)
#imagesprite = canvas.create_image(400,400,image=image)
tkinter.Label(root,image=image).pack()

root.mainloop()