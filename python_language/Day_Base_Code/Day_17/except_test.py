# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:25:44 2019

@author: sundooedu
"""
try:
    4/0
except ZeroDivisionError as e: #예외발생시
    print(e)
else:#예외 미발생시
    print('else')
finally: # 예외 발생 여부에 상관없이 반드시 실행
    print("정상종료")

try:
    4/0
except:
    pass
print('정상종료')


try:
    a = [1,2]
    #print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
    print(type(e))
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

#%%
try:
    a = [1,2]
    #print(a[3])
    4/0
       #발생예외오류 모르지만 일단 예외처리
except Exception as e:
    print(e) # 해당 예외 메세지
    print(type(e)) #해당 예외타입 확인
#%%
def oddeven():
    su=-3
    if su < 0:
        raise Exception('음수 불가') # 강제 Exception
    if su%2 == 1:
        print('홀')
    else:
        print('짝')
    
oddeven()    
#%%
class Bird:
    def fly(self):
        """
        반드시 재정의
        """
        raise NotImplementedError
        
class Eagle(Bird):
    def fly(self):
        print("펄럭펄럭 난다")

eagle = Eagle()
eagle.fly()        
#%%

import random
counters = [0,0,0,0,0,0] #눈금수의 출현빈도수
counters_dict={}

try:
    f=open("나없는파일","r")
    pass
    
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

4/0

except Exception as e:
    print(e)

print("판다스2차분석")







