# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:55:33 2020

@author: sundooedu
"""
#%%
import os
from selenium import webdriver

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project')
#%%
'''
페이지의 단일 element에 접근하는 api,

find_element_by_name('HTML_name')
find_element_by_id('HTML_id')
find_element_by_xpath('/html/body/some/xpath')

페이지의 여러 elements에 접근하는 api 등이 있다.

find_element_by_css_selector('#css > div.selector')
find_element_by_class_name('some_class_name')
find_element_by_tag_name('h1')

driver.page_source API를 이용
현재 렌더링 된 페이지의 Elements를 모두 가져올 수 있다
'''
#%%
# Chrome
driver_c = webdriver.Chrome('driver/chromedriver')
driver_c.implicitly_wait(1)

# url에 접근
driver_c.get('https://google.com')

#%%
# Phantomjs
driver_p = webdriver.PhantomJS('driver/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver_p.implicitly_wait(1)

# url에 접근
driver_p.get('https://google.com')
#%%
# 네이버에 로그인
driver = webdriver.Chrome('driver/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# 아이디 비번 입력
driver.find_element_by_name('id').send_keys('naver-id')
driver.find_element_by_name('pw').send_keys('anykeys')
# 로그인 버튼 누르기
driver.find_element_by_xpath('//*[@id="log.login"]').click()
#%%
# 하나씩 크롤링 
import requests
from bs4 import BeautifulSoup as bs
import time


def get_links(): # 블로그의 게시글 링크들을 가져옵니다.
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    data = []

    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io'+link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    # 가져온 데이터로 뭔가 할 수 있겠죠?
    # 하지만 일단 여기서는 시간만 확인해봅시다.
    print(soup.select('h1')[0].text) # 첫 h1 태그를 봅시다.

if __name__=='__main__':
    
    start_time = time.time()
    
    for link in get_links():
        get_content(link)
        
    print("--- %s seconds ---" % (time.time() - start_time))
#%%
import requests
from bs4 import BeautifulSoup as bs
import time

from multiprocessing import Pool # Pool import하기


def get_links(): # 블로그의 게시글 링크들을 가져옵니다.
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    data = []

    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io'+link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    # 가져온 데이터로 뭔가 할 수 있겠죠?
    # 하지만 일단 여기서는 시간만 확인해봅시다.
    print(soup.select('h1')[0].text) # 첫 h1 태그를 봅시다.

if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
    pool.map(get_content, get_links()) # get_content 함수를 넣어줍시다.
    print("--- %s seconds ---" % (time.time() - start_time))    
#%%
# 순차 작업
import time

start_time = time.time()

def fibo(n): # 회귀적 피보나치 함수
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num_list = [31, 32, 33, 34]
result_list = []
for num in num_list:
    result_list.append(fibo(num))

print(result_list)
print("--- %s seconds ---" % (time.time() - start_time))
#%%
# 병렬 작업
from multiprocessing import Pool
import time

start_time = time.time()

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def print_fibo(n): # 피보나치 결과를 확인합니다.
    print(fibo(n))

num_list = [31, 32, 33, 34]

pool = Pool(processes=7) # 4개의 프로세스를 사용합니다.
pool.map(print_fibo, num_list) # pool에 일을 던져줍니다.
print("--- %s seconds ---" % (time.time() - start_time))
#%%
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()