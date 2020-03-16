# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:42:50 2019

@author: sundooedu
"""
import multiprocessing as mp
import random

num_45_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(f'리스트 길이 : {len(num_45_counter)}')
counter_dict={}
i=0
for i in range(8145060):
    value=random.sample(range(0,45),6)
    for j in range(0,6):
        num_45_counter[value[j]] += 1

for i in range(45):
    counter_dict[str(i+1)] = num_45_counter[i]
    print(f'로또 번호가 {i+1}인 경우는 {num_45_counter[i]}번')

order_list = sorted(counter_dict.items(),key=lambda x:x[1], reverse=True)
print("주사위의 빈도수 정렬사전",order_list)

max_frequency_num = []
for i in range(6):
    max_frequency_num.append(order_list[i][0])
    
ssum=sum(num_45_counter)
print(f'전체 나온 횟수 합 {ssum}')
    
print(max_frequency_num)

#%%
import multiprocessing as mp    
import random
from datetime import datetime
import lotto

with mp.Pool(processes=7) as pool:
    pool.map(lotto(), range(100))
    
start_time = datetime.datetime.now()        
print('실행시간 : ',datetime.datetime.now() - start_time)    
        



    











