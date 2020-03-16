# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:48:16 2019

@author: sundooedu
"""

#%%
import requests
import urllib.request as req
import bs4
response = requests.get('https://finance.naver.com/marketindex/')
html = response.text
print(html)

# 파일 소스보기
import urllib.request as req
response = req.urlopen('https://finance.naver.com/marketindex/')
html = response.read()
print(html)

# 파일 다운로드 저장
req.urlretrieve('https://finance.naver.com/marketindex/',filename='marketindex.html')
# 그림 파일 저장
req.urlretrieve('http://www.sundooedu.co.kr/img_up/shop_pds/sundoo/site_content/logo1558576582.gif',filename='sd_logo.gif')
# 열어 주었으면 닫아줘야 한다.
response.close()
#%% 
# 자동으로 닫아주는 문법
with req.urlopen('https://finance.naver.com/marketindex/') as response:
    html = response.read()
    print(html)
 

with requests.get('https://finance.naver.com/marketindex/') as response:
     html = response.text
     print(html)
#%%
import bs4

with req.urlopen('https://finance.naver.com/marketindex/') as response:
    html = response.read()
    #print(html)
    bs = bs4.BeautifulSoup(html, 'html.parser')
    # .on(java script 클래스)가 사용자의 호버링 이벤트(마우스를 갖다 대는 행위)에 따라서 변화하므로 on클래스 생략
    usd_price = bs.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
    jpy_price = bs.select_one('a.head.jpy > div > span.value')
    eur_price = bs.select_one('a.head.eur > div > span.value')
    print(f'미국USD {usd_price.string}') # usd_price.string, usd_price.text 으로 해도 됨.
    print(f'일본JPY {jpy_price.getText()}')
    print(f'유럽EUR {eur_price.text}')

#%%
with req.urlopen('https://finance.naver.com') as response:
    html = response.read()
    #print(html)
    bs = bs4.BeautifulSoup(html, 'html.parser')
    # .on(java script 클래스)가 사용자의 호버링 이벤트(마우스를 갖다 대는 행위)에 따라서 변화하므로 on클래스 생략
    main_news = bs.select('div.news_area > div > ul span > a')
                                           # nth-child() 빼면서 좌우의 '>' 두개를 지워서 "ul"과 "span"은 자손관계로 변환
    for i,news in enumerate(main_news):
        print(f'{i+1}. {news.string}')
        print('-'*60)
    print('메인뉴스 갯수 =',len(main_news),'개') 
#%%
# quiz 01. 금융 뉴스 10개
#https://finance.naver.com/marketindex/    
#content > div.section_news > div > ul p > a    
with req.urlopen('https://finance.naver.com/marketindex/') as response:
    html = response.read()
    bs = bs4.BeautifulSoup(html, 'html.parser')
    main_news = bs.select('#content > div.section_news > div > ul p > a')
    
    for i,news in enumerate(main_news):
        print(f'{i+1}. {news.string}')
        print('-'*45)
    print('메인뉴스 갯수 =',len(main_news),'개')

#%%
# quiz 02. 영화 랭킹 11월 4일짜
#https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20191104
#old_content > table > tbody > tr:nth-child(n) > td.title > div > a
#old_content > table > tbody td:nth-child(3) > img 화살표 그림
#old_content > table > tbody > tr > td > img
    
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(3) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(3) > img
#old_content > table > tbody > tr:nth-child(5) > td:nth-child(3) > img    
#old_content > table > tbody > tr:nth-child(n) > td.range.ac  
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(7) > td:nth-child(1) > img
    
with req.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20191104') as response:
    html = response.read()
    bs = bs4.BeautifulSoup(html, 'html.parser')
    movie_ranking = bs.select('#old_content > table > tbody > tr:nth-child(n) > td.title > div > a')
    ranking_img = bs.select('#old_content > table > tbody > tr:nth-child(n) > td:nth-child(1) > img')
    
    for img, movie in zip(ranking_img,movie_ranking):
        print(f'{img.string} {movie.string}')
        print('-'*30)
    print('영화 랭킹 갯수 =',len(movie_ranking),'개')    
#%% 영화 평점순 크롤링
#https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20191104
#old_content > table > tbody > tr:nth-child(n) > td.title > div > a
#old_content > table > tbody > tr:nth-child(n) > td.point
import requests
import urllib.request as req
import bs4

with req.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20191104') as response:
    html = response.read()
    bs = bs4.BeautifulSoup(html, 'html.parser')
    movie_ranking = bs.select('#old_content > table > tbody > tr:nth-child(n) > td.title > div > a')                              
    ranking_point = bs.select('#old_content > table > tbody > tr:nth-child(n) > td.point')
    i=0
    for movie,point in zip(movie_ranking, ranking_point):
        print(f'{i+1}. {movie.string} {point.text}점')
        print('-'*30)
        i+=1
    print('영화 랭킹 갯수 =',len(movie_ranking),'개')
    
    for i,movie in enumerate(movie_ranking):
        #link = movie["href"]
        link = movie.get('href','#')
        print(f'{i+1}. {movie.string} {link}')
        print('-'*30)
            
    i=0    
    for movie,point in zip(movie_ranking, ranking_point):
        link = movie.get('href','#')
        print(f'{i+1}. {movie.string} {point.text}점 {"https://movie.naver.com"+link}')
        print('-'*107)
        i+=1
    print('영화 랭킹 갯수 =',len(movie_ranking),'개')
    
     movie_dict={} # 사전으로 저장
     for i in range(len(movie_ranking)):
         movie_dict[movie_ranking[i].string] = ranking_point[i].string
     len(movie_dict) 
     print(movie_dict)
     
import sys 
sys.setrecursionlimit(10000)  # 수치를 무한에서 1만으로 줄인것.
  
import pickle
f = open("movie_name_rate.dat", 'wb')
pickle.dump(movie_dict, f) # 사전을 파일에 저장
f.close()

f = open("movie_name_rate.dat", 'rb')
data = pickle.load(f)
print(data)
#%%
    
     