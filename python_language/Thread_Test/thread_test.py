# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:43:16 2019

@author: sundooedu

GIL 정책
______________________
동시에 X(아니고) 교대로
단, 어떤 함수가 대기할때 다른 함수가 CPU 분배받아 사용

함수A      함수A 
     함수B      함수B
______________________
함수A, 함수B 실행자(스레드) 생성
"""
import threading
sub_total_list=[]
import time

def work(id,start,end):
    sub_total=0 # start,end 수열 부분합
    for i in range(start, end):
        sub_total +=i
        print(id,'스레드',i,sub_total)
        time.sleep(0.5) # 1초 동안 실행중지 대기
    sub_total_list.append(sub_total)
# 1.기본 메인 스레드가 작업1과 작업2를 생성        
        
# 2.메인 스레드가 함수 실행
        
# 작업스레드 1과 2가 동시(교대) 실행(병렬 실행)         

#작업 스레드 1(=함수 실행자 = worker)가 함수 실행        
th1 = threading.Thread(target=work,args=('1',0,50))        
#작업 스레드 2(=함수 실행자 = worker)가 함수 실행 
th2 = threading.Thread(target=work,args=('2',50,101))   
  
th1.start()
th2.start()

# 3. join(): 메인스레드가 작업스레드가 종료될때까지 대기
th1.join()
th2.join()
# 4. 메인스레드가 전부합 계산

total_result=sub_total_list[0]+sub_total_list[1]
print(total_result)
#%%
# 복사 작업 및 복사 진행상황 슬라이드 동시 표시
import threading
import time
lock=threading.Lock() # lock을 써서 동시작업을 비동시(순차적으로)작업으로 제어 처리
                      # lock을 선점한 스레드가 lock을 획득하면 자물쇠가 잠긴 이후에 접근하는 
                      # 나머지 스레드들은 락이 헤제(열릴)될 때까지 대기하다가
                      # 락이 풀리면 접근 가능 
def copy_work():
    for i in range(1,101):
        lock.acquire()
        print(i,'개 복사')   # 동기(순서)화 블록 = 임계영역
                            # lock 코드 사이에 있는 코드가 임계영역이 되버린다.
        print('copy_work 스레드')                    
        lock.release()
        
        time.sleep(0.1)
        
def copy_slide_work():
    for i in range(1,101):
        lock.acquire()
        print(i,'% 복사진행') # 동기(순서)화 블록 = 임계영역
        print('copy_slide_work 스레드')
        lock.release()
        time.sleep(0.1)
        if i == 100:
            print('*복사완료*')
        
cpth1=threading.Thread(target=copy_work)
cpth1.start()
cpth2=threading.Thread(target=copy_slide_work)    
cpth2.start()    
        
        
        
        
        
        
        
        
        
        
        
        