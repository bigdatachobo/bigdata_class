# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:28:53 2019

@author: sundooedu
"""

# =============================================================================
# 1. 주사위를 1000번 던져서 나오는 값들의 빈도를 계산하는 프로그램을 작성해보자. 
# 즉 1, 2, 3, 4, 5, 6의 값이 각각 몇 번이나 나오는지를 계산한다. 
# 난수 발생 함수와 리스트,사전을 사용해보자. 
# 
# * 결과화면
# 주사위가  1 인 경우는  154 번
# 주사위가  2 인 경우는  185 번
# 주사위가  3 인 경우는  149 번
# 주사위가  4 인 경우는  166 번
# 주사위가  5 인 경우는  165 번
# 주사위가  6 인 경우는  181 번
# 
# 주사의 빈도수 사전 : {'1': 154, '2': 185, '3': 149, '4': 166, '5': 165, '6': 181}
# =============================================================================
#%% 내 풀이
import random
import collections

i=0
dice_list=[]

while i < 1000:
    dice=random.randrange(1,7)
    dice_list.append(dice)
    i+=1

num_count = collections.Counter(dice_list)        
ordered_list = sorted(num_count.items(),key=lambda x:x[0])

for i in list(range(0,6)):
    print(f'주사위가 {ordered_list[i][0]}인 경우는 {ordered_list[i][1]}번')
    
ssum=0    
for i in list(range(0,6)):
    ssum+=ordered_list[i][1]    
print(f'주사위 던진 총 횟수 : {ssum}')    

print(f'주사위의 빈도수 사전 : {dict(ordered_list)}')    
#%% 선생님 풀이
import random
counters = [0,0,0,0,0,0] #눈금수의 출현빈도수
counters_dict={}

for i in range(1000):
    value = random.randint(0,5) # counters 리스트 인덱스 번호와 맞추기 위해 주사위 눈금을 0부터 시작
    counters[value] += 1

for i in range(6):
    counters_dict[str(i+1)] = counters[i]
    print(f'주사위가 {i+1}인 경우는 {counters[i]}번')    

print("주사위의 빈도수 사전",counters_dict)

#벨류(빈도수) 기준 아이템들 내림차(역)정렬 리스트, x는 아이템 x[1] 빈도수
order_list = sorted(counters_dict.items(),key=lambda x:x[1], reverse=True)
print("주사위의 빈도수 정렬사전",order_list)
#%%














