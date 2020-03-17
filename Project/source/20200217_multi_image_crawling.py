# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:23:23 2020

@author: sundooedu
"""
#%%
from bs4 import BeautifulSoup
import urllib.request as urq
import multiprocessing
import time
import os

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')

# 총 크롤링 갯수를 프로세스에 맞춰 할당량 계산
def get_count(num, p=4):
    lst = [] # 프로세스당 크롤링할 이미지 개수 할당량 리스트
    allocate = int(num/p) # 프로세스 1개당 크롤링할 이미지 개수
    
    for n in range(p):
        lst.append(allocate)
        
    lst[p-1] = lst[p-1] + num%p # 마지막 프로세스는 할당량 분배 후 남는 작업도 포함
    print("프로세스당 할당량:", lst)
    return lst

def duplicate(img):
    return os.path.exists('../image/'+img)
           # 경로 입력시 해당 파일 존재 유/무 리턴
           # 존재할 경우 True/ 존재하지 않으면 False

def get(max_count=1):
    base_url = 'http://10000img.com/' # 이미지 src와 조합하여 다운받을 주소
    renew_url = 'http://10000img.com/ran.php' # 새이미지 접속할 URL
    
    count = 1
    while count <= max_count:
        print('+--------------[%d번 째 이미지]----------------+'% count)
        
        html = urq.urlopen(renew_url)
        source = html.read()
        
        soup = BeautifulSoup(source, 'html.parser')
        
        img = soup.find('img') # 이미지 태그
        img_src = img.get('src') # 이미지 경로
        img_url = base_url + img_src # 다운로드를 위해 base_url과 합침
        img_name = img_src.replace("/",'') # 이미지 src에서 '/' 없애기
        
        if not duplicate(img_name):
            urq.urlretrieve(img_url, '../image/'+img_name)
        else:
            print('중복된 이미지!')
            
        print('이미지 src:', img_src)
        print('이미지 url:', img_url)
        print('이미지 명:', img_name)
        print('\n')
        count += 1 # 갯수 1 증가

if __name__ == '__main__':
    
    num = int(input("이미지 수: "))
    start = time.time() # 크롤링 시작 시간
    
    process = []
    for count in get_count(num, 4):
        p = multiprocessing.Process(target=get, args=(count,))
        process.append(p)
        p.run()
        p.start()
       
    for p in process:
        p.join()
        
    print("크롤링 종료")
    print("크롤링 소요 시간:", round(time.time() - start, 6)) # 소수점 아래 6자리까지