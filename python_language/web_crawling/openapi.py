# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:18:14 2019

@author: sundooedu
"""

#%%
#http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do  

import requests #HTTP 요청 모듈
#import json

#목록수 10개  참고
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e&itemPerPage=10'
response = requests.get(url)
#json 문자열을 Python Dictionary로 변경
#result = json.loads(response) # 첫번째 방식 2줄
result = response.json()      # 두번째 방식 1줄

num = len(result["movieListResult"]["movieList"])
print(num)   
for i in range(0,num):
    print(result["movieListResult"]["movieList"][i]["movieCd"])
    print(result["movieListResult"]["movieList"][i]["movieNm"])    
    print(result["movieListResult"]["movieList"][i]["openDt"])
    #print(result["movieListResult"]["movieList"][i]["directors"])
    #print(result["movieListResult"]["movieList"][i].get("salesAcc",'None'))
    print(result["movieListResult"]["movieList"][i].get("genreAlt",'None'))
    # dict 키값, 리스트 인덱스 조합 추출
    if result["movieListResult"]["movieList"][i]["directors"] != []:
        print(result["movieListResult"]["movieList"][i]["directors"][0]["peopleNm"])
    print('-'*30)
#%%
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'
response = requests.get(url)
result1 = response.json()
extract_from = result1["boxOfficeResult"]["dailyBoxOfficeList"]
num = len(result1["boxOfficeResult"]["dailyBoxOfficeList"])
print(num)

def asia_unit(num): # 천만단위까지 표시
    a = (int(num)//10000)
    b = (int(num)%10000)
    return str(a)+'만'+str(b)

for i in range(0,num):
    print(f'영화 코드 : {extract_from[i]["movieCd"]}')
    print(f'영화 제목 : {extract_from[i]["movieNm"]}')    
    print(f'개봉일 : {extract_from[i]["openDt"]}')
    #audiACC = format(int(extract_from[i]["audiAcc"]),',')  # 천단위 표시
    audiACc = asia_unit(extract_from[i]["audiAcc"])
    print(f'''누적 관객수 : {audiACc}''')
    print('-'*30)
    
#%%
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20170561'
response = requests.get(url)
d = response.json()
movieInfo = d['movieInfoResult']['movieInfo']

print(f'''영화 코드 : {movieInfo['movieCd']}
영화명 : {movieInfo['movieNm']}({movieInfo['movieNmEn']})
개봉일 : {movieInfo['openDt']}
런닝타임 : {movieInfo['showTm']}''')
for i in range(len(movieInfo['actors'])):
    print(f'{movieInfo["actors"][i]["peopleNm"]}',end='')
    
for i in range(len(movieInfo['showTypes'])):
    print(f'{movieInfo["showTypes"][i]["showTypeGroupNm"]}',end='')
#%%
import requests
import urllib.request as req
import bs4
import pandas as pd
# =============================================================================
# import sys 
# sys.setrecursionlimit(10000)
# =============================================================================


with req.urlopen('http://kopia.or.kr/info/statistics.php') as response:
    html = response.read()
    bs = bs4.BeautifulSoup(html, 'html.parser')
    category = bs.find_all('th')
    contract_data = bs.find_all('td')                             
    print(category)
    print(contract_data)
    header = list(map(lambda x: x.getText() ,category))
    export =  list(map(lambda x: x.getText() ,contract_data))

country=[]
company=[]
equipment=[]
projectname=[]
callfrom=[]
callmoney=[]
calldate=[]

for i in range(0,len(export)):
    if i%7==0:
        country.append(export[i])
    elif i%7 == 1:
        company.append(export[i])
    elif i%7 == 2:
        equipment.append(export[i])
    elif i%7 == 3:
        projectname.append(export[i])
    elif i%7 == 4:
        callfrom.append(export[i])
    elif i%7 == 5:
        callmoney.append(export[i])
    elif i%7 == 6:
        calldate.append(export[i])
    else:
        print("something wrong")

# pandas로 데이터를 dict 형식으로 만들고 key 값을 header[i]로 주고 value 값을 위 식으로 분류한 값으로 준다. 
data={}
data_list=[country,company,equipment,projectname,callfrom,callmoney,calldate]

for i,j in zip(header,data_list):
    data[i]=j
        
# =============================================================================
# data={header[0]:country,
#       header[1]:company,
#       header[2]:equipment,
#       header[3]:projectname,
#       header[4]:callfrom,
#       header[5]:callmoney,
#       header[6]:calldate}
# =============================================================================
df = pd.DataFrame(data)
df
# =============================================================================
# export_list=[]
# for i, j, k, x, y, z, p in zip(country,company,equipment,projectname,callfrom,callmoney,calldate ):
#     export_list.append(i,j,k,x,y,z,p)
# =============================================================================

    
                         
      
# =============================================================================
# for i in range(len(category)):
#     print(f'{category[i].getText()}',end='      ')
# print('-'*100)
# for i in range(10):
#     print(f'{export[7*i]} {export[7*i+1]} {export[7*i+2]} {export[7*i+3]} {export[7*i+4]} {export[7*i+5]} {export[7*i+6]}\n') 
# 
# 
# =============================================================================
    
#%% 선생님 풀이
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import gc # garbage collector
gc.collect

url = "http://kopia.or.kr/info/statistics.php"
page = urlopen(url)

#column명을 받기 위해 작성
#인코딩 : 한국어 영어로 번역 
#디코딩(parse) : 영어를 한국어로 번역 
try:
    page = urlopen(url) # 네트워크 예외 상황
    # 디코딩(parse) 연산 예외 상황
    soup = BeautifulSoup(page, 'html.parser')
    # find_all : 태그명, 속성명으로 검색
    a = soup.find_all('th')
    for i in a:

# 크롬에서는 tbody 보이지만 tbody 실제로 없음 빈리스트
#b = soup.select('#contents > div.contentArea > div.statistics_cont > table > tbody > tr > td') # 빈리스트
     # select : 태그명, 속성명, 태그간의 관계 css 선택자로 검색   
     b = soup.select('#contents > div.contentArea > div.statistics_cont > table  tr > td')
    #b = soup.find_all('td')
        
     for i in b:
        print(i)
except Exception as e:
    print('failed')
    print('caused by',e)

#가져온 데이터 a를 m_col에 넣는 과정
m_col = []
for tag in a:
    m_col.append(tag.text)
    #print(tag.text)
print(m_col)
#가져온 데이터 b를 각 list에 넣는 과정

m_country = [] #발주지역 및 발주국가
m_inher = [] # 수주기업
m_equip = [] # 설비구분
m_pro = [] #프로젝트 명
m_odoz = [] # 발주처
m_pay = [] #수주 금액
m_time = [] #수주 시기

# 각 리스트의 해당 td의 text만 추출하여 추가.
for i in range(0,len(b)):
    if i%7==0:
        m_country.append(b[i].text)
    elif i%7 == 1:
        m_inher.append(b[i].text)
    elif i%7 == 2:
        m_equip.append(b[i].text)
    elif i%7 == 3:
        m_pro.append(b[i].text)
    elif i%7 == 4:
        m_odoz.append(b[i].text)
    elif i%7 == 5:
        m_pay.append(b[i].text)
    elif i%7 == 6:
        m_time.append(b[i].text)
    else:
        print("something wrong")

for i in range(0,10):
     print(m_country[i],m_inher[i])
     
export_list={}
for i in zip()     