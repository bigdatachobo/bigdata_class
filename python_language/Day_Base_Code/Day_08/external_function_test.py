# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:30:40 2019

@author: sundooedu
"""

a=list(range(10))

import random
i=random.randrange(1,101,2) # 마지막 수 비포함
j=random.randint(1,46) # 마지막 수 포함

k=random.random()
print(" %0.1f " % k)

k2=random.uniform(1.0,10.4)

k3=[1,2,3,4,5]
a=random.shuffle(k3)
b=random.choice(k3)

import random

#%%
lotto_list=list(range(1,46))
random.shuffle(lotto_list)
i=sorted(random.sample(lotto_list,6))

import math
print(math.e)
print(math.pi)    
i=math.ceil(3.4)    
j=math.trunc(-3.4) # 정수 방향이    ----> 0 trunc시에 -3 됨
k=math.floor(-3.4) # 정수 방향이    <--- 0 올림시 -4
o=round(4.6)
math.fabs(-3.5)
math.tau()
a=math.log(10) # 밑수가 자연상수 e
a2=math.log10(10) # 밑수가 10 인 log
b=math.log(2.718) 
c=math.log(10,100) # 두번째  인자가 밑수(100)로 log10)

a3=math.pow(2,10)
a4=math.sqrt(2) # 루트
a5=math.sin(a6)
a6=math.radians(180)
a7=math.degrees(a6)
a8=math.cos(math.pi)
#%%
a=4.1-1.2 #실수 2.8999...
print('%f'%a)
print('%0.1f'%a)

import decimal
a=decimal.Decimal('4.1')-decimal.Decimal('1.2')
print(a) #깔끔하게 2.9 로 떨어짐

if decimal.Decimal('4.1')-decimal.Decimal('1.2') == decimal.Decimal('2.9'):
    print('차이는 2.9입니다.')
    
import math    
if math.isclose(4.1-1.2,2.9):  
    print('차이는 2.9입니다.')  
#%%
import time
time.time() 

time.ctime()   

type(time.ctime())
type(time.ctime().split(' '))
time.ctime().split(' ')[-1]
time.ctime().split(' ')[0]

time.localtime()
time.strftime('%a %Y-%m-%d %H:%M:%S',time.localtime())
#%%
from datetime import datetime, timedelta
nowDate=datetime.now()
print(nowDate)
nowDate2=datetime.strftime(datetime.now(),'%a %Y-%m-%d %H:%M:%S')

oldDateTime=datetime(2018,10,14, 17,18,50,0)
oldDateTime.replace(year=2017)
oldDateStr=datetime.strftime(oldDateTime,'%a %Y-%m-%d %H:%M:%S')
#%%
import datetime
dt=timedelta(hours=-6)
dt2=timedelta(days=-3,hours=-6,minutes=30)
print(dt2)
# 6시간 이전의 datetime을 구해주고 있다.
six_before = datetime.now()+dt
diff=datetime.now()-oldDateTime
import time
time.time()
time.ctime()
type(time.ctime())
type(time.ctime().split(' '))
time.ctime().split(' ')[-1]
time.ctime().split(' ')[0]
time.localtime()

time.strftime('%a %Y-%m-%d %H:%M:%S',time.localtime()) # 암기
#%%
from datetime import datetime,timedelta
nowDate=datetime.now()
print(nowDate)
nowDateStr=datetime.strftime(datetime.now(),'%a %Y-%m-%d %H:%M:%S') #암기
#datetime 변경
oldDateTime=datetime(2019, 10, 16, 17, 9, 36, 0)
oldDateTime=oldDateTime.replace(year=2018)
oldDateStr=datetime.strftime(oldDateTime,'%a %Y-%m-%d %H:%M:%S')
#%%
dt=timedelta(hours=-6)
dt2=timedelta(days=-3 ,hours=-6,minutes=30)
print(dt2)
#6시간 이전의 datetime 
six_before = datetime.now()+ dt
# datetime간의 경과된 일시를 구함
diff = datetime.now() - oldDateTime
#%%
article_time=datetime(2019,10,16,8,3,0)
article_str=datetime.strftime(article_time,'%Y-%m-%d %p %H:%M:%S').replace('AM','오전')
#%%
dt=timedelta(hours=-6)
six_before = datetime.now()+ dt
print(diff.days,"일 이전")
print(diff.seconds//3600,"시 이전")
#%%
# Quiz 기사입력 2019.10.16. 오전 8:03
# 기사입력과 현재시간의 timedelta 구현후
# 만약 timedelta의 일수 있으면
# 일수 이전입력 콘솔 출력
# 아니면 
# 시수 이전입력 출력
#%% 내풀이
article_time=datetime(2019,10,16,8,3,0)
article_str=datetime.strftime(article_time,'%Y-%m-%d %p %H:%M:%S').replace('AM','오전')
dt=datetime.now()-article_time
dt2=timedelta(hours=-2)
dt3=timedelta(minutes=-20)
td = datetime.now() + dt2 + dt3
print(dt)
#%% 정답
from sd import date_util_test
compDateTime=datetime(2019,7,15,16,9,36)
date_util_test.print_Reg_Date(compDateTime)

#%%
from dateutil.relativedelta import relativedelta

diff=relativedelta(datetime.now(),oldDateTime).months # 달수       
diff=relativedelta(datetime.now(),oldDateTime).days   # 일수
diff=relativedelta(datetime.now(),oldDateTime).hours  # 시수
#%%









