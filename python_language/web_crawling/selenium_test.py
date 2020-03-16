# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:06:18 2019

@author: sundooedu
"""
#%%
#구글검색
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 구글 웹브라우저 새창이 뜬다.
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3) # 묵시적인 기다림 관례상 3초 대기시간 줌.(넣어주는게 좋음.)
driver.get('https://www.google.com')
# 요소의 name명이 "q"인 요소 가져오기(html 코드 상에서 검색창 이름이 "q"임)
search_box = driver.find_element_by_name("q")
#위 개발자 도구를 확인해보면 우리가 사용할 input의 name이 q 인것을 확인할 수 있습니다. search_box가 커서를 어디다 둬야할 지 name으로 찾아준겁니다. 
time.sleep(1)# 1초 실행 중지
search_box.send_keys("파이썬") # 파이썬을 키보드 입력
time.sleep(1) # 1초 실행 중지
search_box.send_keys(Keys.RETURN) # submit() 대신 엔터(RETURN 이 엔터를 의미함.)
time.sleep(1)

# 현재 페이지 page_source 
# search_list 검색결과 리스트  가져오기
response = driver.page_source  # == page = urlopen(url) (from || scrapingTest(teacher))
from bs4 import BeautifulSoup

bs = BeautifulSoup(response,'html.parser')
search_list = bs.select('div.g') # div class g를 의미함.

for i,info in enumerate(search_list) :
    print(i+1,'.',info.text)
    print('-'*70)

# 검색결과 리스트에서  2번째 요소(파이썬 자습서 - Python 3.8.0 문서)선택 클릭 
res= driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div:nth-child(2) > div > div > div.r > a')
res.click()
driver.set_window_size(1400,1000)
driver.get_screenshot_as_file('google_screenshot.png')
time.sleep

driver.back() # 이전 페이지로 가기( 뒤로가기 )
time.sleep(2) 
driver.forward() # 이후 페이지로 다시 가기 ( 앞으로가기 )
time.sleep(2)


driver.quit() # 구글 웹브라우저창 닫기
#%%








