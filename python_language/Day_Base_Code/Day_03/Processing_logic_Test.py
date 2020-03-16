# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:10:51 2019

@author: sundooedu
"""

#%%
jumsu=[1,2,3]
hap=sum(jumsu)
print(hap)
#%%
#소스프로그램코드 -(파이썬 인터프리터(=쉘)=python.exe)> 윈도우즈 실행(이진) 코드 번역 후 대신 실행
#-윈도우 커널(실행자)->하드웨어 제어

#윈도우 인터프리터(=쉘) : explorer
#리눅스 인터프리터 : bash 쉘 

#컴파일러(번역자)

money = True
if money:
   print("택시를 타고 가라")
else:
   print("걸어 가라")
   
money=False
if money:
    print("택시를\n타고\n가라")

else:
    print("걸어\n가라")    
#%%
zzeon=2000
if (zzeon >= 3000):
    print("택시\n타라")
else:
    print("알바라도해서\n돈 좀 벌어라...")    
#%%
zzeon=2000
jigop_card=True
if (zzeon >= 3800 or jigop_card):
    print("택시ㄱㄱ")
else:
    print("카드도 없냐...")
#%%
pocket=['paper','card','money']  
if 'money' in pocket:
    print("택시ㄱㄱ")
else:
    print("걷기 운동이나 해라...")    
#%%
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: # "1차 상위조건이 거짓이고, 2차 조건이 참이면" 이렇게 해석!!!
     print("택시를 타고가라")
else:
     print("걸어가라")    
#%%
score=60     
msg='참' if (score >=60) else '거짓'
print(msg)    
#%%
#응용문제
# 짝/홀 판별 문제
import random
number=random.randint(0,1.0e10)

if (number%2==0):
    print(number," ",end="")
    print("짝이요~!!!")
else:
    print(number," ",end="")
    print("홀이요~!!!")    
#%%
num=int(input("어떤 숫자든 입력해봐라: ") )   

if (num%2==0):
    print(num)
    print("짝이다 이새끼야!")
else:
    print(num)
    print("홀이다 이새끼야!")
#%%
num=int(input("어떤 숫자든 입력해봐라: "))   

if (num%2==0):
    print(num,"짝이다 이새끼야!")
elif (num%2==1): 
    print(num,"홀이다 이새끼야!")
else:
    print("숫자를 입력하라고 임마!!!")
#%%    
Q01
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")    
#%%
Q02

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) 
        
 
