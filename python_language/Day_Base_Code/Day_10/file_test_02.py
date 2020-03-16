# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:04:32 2019

@author: sundooedu
"""

from datetime import datetime
import pickle
with open('test_data.txt','wb') as fp:
    data1='30대 기혼 직장인 화장품 쿠폰반응 YES 유의\n'
    data2='30대 기혼 여성 직장인 구매 확률 90% 유의\n'    
    pickle.dump({'dt': data1,'nb':data2},fp) # 사전(dict):
    


fp=open('test_data.txt','rb')
data=pickle.load(fp)
#print(data['nb'])
data['svm']='서포트벡터머신'    # 새아이템 추가
data['svm']='Support_Vector_Machine'  # 아이템 수정
del data['svm'] # 내장함수 del 을 이용하여 삭제 가능
print(data.get('svm','未存在開金'))
#키값들 반복 추출
for k in data.keys():
    print(k,end=' ')
#벨류값들 반복 출력
for k in data.keys():
    print(data[k])
 
for v in data.values():
    print(v)

for i in data.items():
    print(i)
        
fp.close() 

 
#%%
import pickle
f = open("test.txt", 'wb')
data = {1: '파이썬', 2: 'you need'}
pickle.dump(data, f)
f.close()


f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)


