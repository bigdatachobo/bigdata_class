# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:09:09 2019

@author: sundooedu
"""
# 변경 내역
# 1. with as 적용
# 2. 지역변수 : 함수지역에 선언
data = None
try:
    f = open('test.txt','r',encoding='utf-8') # 첫번째 시도
except FileNotFoundError:
    open('test.txt','w',encoding='utf-8') # 재시도 Retry 기법 : 파일 생성 후
    f = open('test.txt','r',encoding='utf-8')  # 다시 읽어 드림 
f.close()
# =============================================================================
# 암기하기!!!
try:
    #data = []    
    data=f.readlines()
except ValueError as e:
    print(e)
    data.clear() # 데이터 지우기(리셋)
    with open('test.txt','r',encoding='utf-8') as f:
        data = f.readlines()

print(data)
# =============================================================================        
finally:   

print(data)

data = 2 # 전역 변수 함수 끝난 후에도 살아있음
def func():
    data=1 # 지역 변수 함수 끝나면 사라짐
           # 함수 지역에 선언된 변수만 지역 변수
    print(data) 
    
data = 2
func()
print(data)
#%%
import sys

for i in range(3):
    try:
        a = int(input("정수입력 : "))
        print(a)
    except ValueError as e:
        print(e)
        print('정수가 아닙니다.')
        if i>=2: # 세번 잘못 입력시
            #raise Exception("너 로못이지..! 프로그램 종료")
            sys.exit()
    else:
        break
print('GG')    
#%% up-version.
import sys
import random

# 4자리 난수 보안문자
def getSecChar():
    SecChar = ''
    for i in range(4):
        #random.randint(0,9) # 시작 번호를 적어줘야함
        SecChar += str(random.randrange(10)) # 시작번호 없어도됨
    return SecChar

isHuman = True # 사람여부
sc=''
for i in range(4):
    try:
        # 사람여부에 따른 동적 입력화면
        if isHuman:
            a = int(input("정수입력 : "))
            print(a)
        else:
            a = int(input("정수입력 : "))
            b = input("보안난수문자 입력 : ")
            if (b != sc):
                print('너 로봇')
                sys.exit()
            
    except ValueError as e:
        print(e)
        print('정수가 아닙니다.')
        if i==2: # 두번 잘못 입력시
            #raise Exception("너 로못이지..! 프로그램 종료")
            #sys.exit()
            isHuman = False
            sc=getSecChar()
            print('보안문자입력 :',sc)
        if(i==3): # 마지막 네번 잘못 입력시
            sys.exit()
    else:
        break
print('GG')


        