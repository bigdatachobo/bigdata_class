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
print("실행시간=",round(time.time() - begin,3))
#4. 메인스레드가 전부합 계산
total_result =sub_total_list[0]+sub_total_list[1]
print(total_result)

#%% up-version
# 멀티 프로세싱
import threading
import multiprocessing as mp
import time
from mpwork import *
# 작업 프로세스간 비공유
#sub_total_list=[]
# 0.Manager 생성

manager = mp.Manager()
sub_total_dict = manager.dict() # 작업 프로세서간 공유할 사전
    
#1. 기본 메인스레드가  작업스레드1과 작업스레드2를 생성       
#2. 작업스레드1과 작업스레드2가 동시(교대로)실행(병렬실행)        
th1 = mp.Process(target=work,args=('0',0,5000,sub_total_dict))        

th2 = mp.Process(target=work,args=('1',5000,10000,sub_total_dict))

begin =time.time()
th1.start()
th2.start() 
#3. join():메인스레드가  작업스레드가 종료될때까지 대기
th1.join()
th2.join()
print("실행시간=",round(time.time() - begin,4))
#4. 메인스레드가 전부합 계산
total_result =sub_total_dict['0']+sub_total_dict['1'] # dict 형식이므로 key 값으로 str(0)='0' 형식으로 넣는다.                          
import os
print('프로세스 id = ',os.getpid())
print(total_result)

