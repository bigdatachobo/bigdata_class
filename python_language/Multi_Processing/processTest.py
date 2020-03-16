# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:35:27 2019

@author: sundooedu
"""

import threading
import time
sub_total_list=[]

def work(id,start,end):
    sub_total=0 # start,end 수열 부분합
    for i in range(start,end):
        sub_total+=i
        print(id,'스레드', sub_total)
        #time.sleep(0.1) # 0.1초 실행중지 대기 
    sub_total_list.append(sub_total)  
    
#1. 기본 메인스레드가  작업스레드1과 작업스레드2를 생성       
#2. 작업스레드1과 작업스레드2가 동시(교대로)실행(병렬실행)        
th1 = threading.Thread(target=work,args=('1',0,5000))        

th2 = threading.Thread(target=work,args=('2',5000,10000))
begin =time.time()
th1.start()
th2.start() 
#3. join():메인스레드가  작업스레드가 종료될때까지 대기
th1.join()
th2.join()
print("실행시간=",time.time() - begin)
#4. 메인스레드가 전부합 계산
total_result =sub_total_list[0]+sub_total_list[1]
print(total_result)