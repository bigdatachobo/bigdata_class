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
driver.implicitly_wait(3) # 웹브라우저 3초 대기시간
driver.get('https://accounts.google.com/ServiceLogin/signinchooser?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.co.kr%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.find_element_by_name('identifier').send_keys('')
time.sleep(1)
#'다음' 버튼 클릭
driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
time.sleep(1)
driver.find_element_by_name('password').send_keys('')
driver.find_element_by_xpath('//*[@id="passwordNext"]').send_keys(Keys.ENTER)

#%%
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(3) # 웹브라우저 3초 대기시간
browser.get("http://python.org")
print(browser.current_url)#창주소
print(browser.title)#창제목
menus = browser.find_elements_by_css_selector('#top ul.menu li')
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
        print(m.text)
pypi.click() # 클릭
time.sleep(1) # 5초 대기
#browser.quit() # 브라우저 종료
# <input id="id-search-field" name="q" 검색창 name으로 검색하기
# 태그 name으로 특정한 태그를 찾을 수 있음
elem = browser.find_element_by_name("q")

# input 텍스트 초기화 
#elem.clear()

# 태그가 input 태그이므로 입력창에 키이벤트가 전달되면, 입력값이 자동으로 작성됨
elem.send_keys("list")

# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
elem.send_keys(Keys.RETURN)

# 모든 태그 검색
h3s = browser.find_elements_by_tag_name('h3')
print (h3s[0].text)#List 1.3.0

for h3 in h3s:
    print (h3.text)
#%%

