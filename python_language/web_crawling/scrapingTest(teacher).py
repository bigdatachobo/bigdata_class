# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:48:42 2019

@author: sundooedu
"""

#%%
import requests
import bs4

#파일소스보기
with requests.get('https://finance.naver.com/marketindex/')as response: 
    html = response.text

#파일소스보기
import urllib.request as req

with req.urlopen('https://finance.naver.com/marketindex/') as response: 
    html = response.read()
    print(html)
    bs= bs4.BeautifulSoup(html,'html.parser')
    # on클래스가 사용자의 호버링 이벤트에 따라서 변화하므로 on클래스 생략
    usd_price=bs.select_one('#exchangeList > li > a.head.usd > div > span.value')
    jpy_price=bs.select_one('#exchangeList > li > a.head.jpy > div > span.value')
    print(f'미국USD  {usd_price.string}') 
    print(f'일본JPY  {jpy_price.string}')                          
                            
    
#파일다운로드저장
req.urlretrieve('https://finance.naver.com/marketindex/',filename='marketindex.html')
#그림파일저장
req.urlretrieve('http://www.sundooedu.co.kr/img_up/shop_pds/sundoo/site_content/logo1558576582.gif','sd.gif')

#%%
with req.urlopen('https://finance.naver.com/marketindex/') as response: 
    html = response.read()
    bs= bs4.BeautifulSoup(html,'html.parser')
    # nth-child() 빼면서 좌우의 > 두개를 지워서 ul과 span자손관계로 변환 
    main_news=bs.select('#content > div.section_news > div > ul p > a')
    print('메인뉴스 개수 =',len(main_news))
    for i, news in enumerate(main_news) :                   
        print(f'{i+1}. {news.string}')
        print('-'*50)



#%%
import urllib.request as req
import bs4
with req.urlopen('https://finance.naver.com/marketindex/') as response: 
    html = response.read()
    bs= bs4.BeautifulSoup(html,'html.parser')
    # :nth-child() 
    main_news=bs.select('#content > div.section_news > div > ul > li:nth-child(n) > p > a')
    print('메인뉴스 개수 =',len(main_news))
    for i, news in enumerate(main_news) :                   
        print(f'{i+1}. {news.string}')
        print('-'*50)
#%%
import urllib.request as req
import bs4
with req.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20191104') as response: 
    html = response.read()
    bs= bs4.BeautifulSoup(html,'html.parser')
    # :nth-child() 
    main_news=bs.select('#old_content > table > tbody > tr:nth-child() > td.point')
    print('메인영화개수 =',len(main_news))
    for i, news in enumerate(main_news) :                   
        print(f'{i+1}. {news.string}')
        print('-'*50)        
#%%
import urllib.request as req
import bs4
with req.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20191104') as response: 
    html = response.read()
    bs= bs4.BeautifulSoup(html,'html.parser')
    # :nth-child() 
    main_news=bs.select('#old_content > table > tbody  td.title > div > a')
    print('메인영화개수 =',len(main_news))
    for i, news in enumerate(main_news) :                   
        print(f'{i+1}. {news.string}')
        print('-'*50)         
#%%
import urllib.request as req
import bs4
with req.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&tg=0&date=20191104') as response: 
    html = response.read()
    bs= bs4.BeautifulSoup(html,'html.parser')
    #영화명
    main_movie_name=bs.select('#old_content > table > tbody > tr > td.title > div > a')
    # 평점
    main_movie_point=bs.select('#old_content > table > tbody > tr > td.point')
    print('메인영화개수 =',len(main_movie_name))
    for i, elem in enumerate(main_movie_name) :                   
        print(f'{i+1}. {elem.string}')
        print('-'*50)
    #영화상세정보링크  
    main_movie_link=[]
    for i, elem in enumerate(main_movie_name) :
        #link=elem['href']           
        link=elem.get('href','#')
        main_movie_link.append('https://movie.naver.com'+link)
        print(f'{i+1}. {link}')
        print('-'*50) 
        
    for i, elem in enumerate(main_movie_point) :                   
        print(f'{i+1}. {elem.text}')
        print('-'*50)
    # (영화명,평점) 아이템 구성 사전
    movie_dict={}    
    for i in range(0,len(main_movie_name)):
       movie_dict[main_movie_name[i].text] = main_movie_point[i].text 
        
#%%
import pickle
f = open("movie.dat", 'wb') 
pickle.dump(movie_dict, f)
f.close()


f = open("movie.dat", 'rb')
data = pickle.load(f)
print(data)
f.close() 
#%%
movie_list= list(zip(main_movie_name,main_movie_link,main_movie_point))
import _pickle as pickle
f = open("movie2.dat", 'wb') 
pickle.dump(movie_list, f)
f.close()


f = open("movie2.dat", 'rb')
data = pickle.load(f)
print(data)
f.close() 

#%%
# 누적관객수
import requests #HTTP 요청 모듈

#http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do  목록수 3개  참고
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'

response = requests.get(url)

result = response.json()

num = len(result["boxOfficeResult"]["dailyBoxOfficeList"])
print(num)   
for i in range(0,num):
    print(result["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieCd"])
    print(result["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieNm"])
    
    print(result["boxOfficeResult"]["dailyBoxOfficeList"][i]["openDt"])  
    
    if result["boxOfficeResult"]["dailyBoxOfficeList"][i]["audiAcc"] != []:
        print(result["boxOfficeResult"]["dailyBoxOfficeList"][i]["audiAcc"])
    print('-'*30)       

#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys


url = "http://kopia.or.kr/info/statistics.php"
page = urlopen(url)

#column명을 받기 위해 작성
#인코딩 : 한국어 영어로 번역 
#디코딩(parse) : 영어를 한국어로 번역 
try:
    soup = BeautifulSoup(page, 'html.parser')
    a = soup.find_all('th')
    for i in a:

# 크롬에서는 tbody 보이지만 tbody 실제로 없음 빈리스트
#b = soup.select('#contents > div.contentArea > div.statistics_cont > table > tbody > tr > td') # 빈리스트
     b = soup.select('#contents > div.contentArea > div.statistics_cont > table  tr > td')
    #b = soup.find_all('td')
 
    for i in b:
        print(i)
except:
    print('failed')

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
     
     