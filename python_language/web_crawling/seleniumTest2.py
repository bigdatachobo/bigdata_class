# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:05:14 2019

@author: sundooedu
"""

#%% 
#google로그인
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# # 구글 웹브라우저 새창이 뜬다
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(1) # 웹브라우저 3초 대기시간
driver.get('https://accounts.google.com/ServiceLogin/signinchooser?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.co.kr%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.find_element_by_name('identifier').send_keys('') # 아이디
time.sleep(1)
#//*[@id="identifierNext"]
# '다음' 버튼 클릭            #//*[@id="identifierNext"](id 속성일때)
driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click() # 클래스 속성일때.
time.sleep(1)
driver.find_element_by_name('password').send_keys('') # 비밀번호
driver.find_element_by_xpath('//*[@id="passwordNext"]').send_keys(Keys.ENTER)
#%% 
from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(1) 
browser.get("http://python.org")
print(browser.current_url) # 창주소
print(browser.title) # 창제목
menus = browser.find_elements_by_css_selector('#top ul.menu li')
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
        print(m.text)
pypi.click() # 클릭
time.sleep(5) # 5초 대기
browser.quit() # 브라우저 종료
#%% 
# quiz
# 1. input 텍스트에 "list" 입력
# 2. 엔터 입력
# 3. 발견한 검색결과 페이지의 모든 h3 요소를 출력.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('chromedriver.exe')
# browser 창크기
browser.set_window_size(1200,1800)
browser.implicitly_wait(1) 
browser.get("http://python.org")
print(browser.current_url) # 창주소
print(browser.title) # 창제목
menus = browser.find_elements_by_css_selector('#top ul.menu li')
pypi = None

for m in menus:
    if m.text == "PyPI":
        pypi = m
        print(m.text)
        
pypi.click() # 클릭
time.sleep(2) # 5초 대기

search_box = browser.find_element_by_name("q")
search_box.send_keys("list")
search_box.send_keys(Keys.RETURN)

#driver.find_element_by_xpath('//*[@id="content"]').click()
#//*[@id="content"]/div[1]/div/form/button

response = browser.page_source  # == page = urlopen(url) (from || scrapingTest(teacher))


#bs = BeautifulSoup(response,'html.parser')
#search_list1 = bs.select('h3') # div class g를 의미함.
#search_list2 = bs.select('p')


search_list1 = browser.find_elements_by_tag_name('h3')
search_list2 = browser.find_elements_by_tag_name('p')


i=0
for info1,info2 in zip(search_list1, search_list2):
    print(i+1,'.',info1.text)
    print(info2.text)
    print('-'*40)
    i+=1

browser.quit()










