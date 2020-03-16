# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:48:50 2019

@author: sundooedu
"""

list1=list(range(0,10))
list2=list(filter(lambda x:x%2==0,list1))
list2
list3=list(filter(lambda x:x%2==0 and x%3==0,list1))

def factorial(s):
    factor=1
    for i in list(range(1,s+1)):
        factor *= i
        return factor
    
 factorial(5)   
 list4=list(filter(lambda x: x*3 if x%3==0, list1))
 
from functools import reduce    
factorial=reduce(lambda x,y:x*y,lst5)
lst5=list(range(9,0,-1))

def factorial(x,y):
    return x*y

reduce(factorial,lst5)
#%%
bool(0) # '0'만 False 나머지 숫자들은 전부 True (음수도 True)
#%%
bool([]) # list가 비어있으면 False
#%%
bool('') # 문자가 비어있으면 False
#%%
# Q.01
def is_odd(number):
    if number%2==0:
        answer="짝수"
    else:
        answer="홀수"
    print(answer)

def is_odds(number):
    answer=(lambda x : "짝수" if (x%2==0)  else "홀수")(number)
    print(answer)
        
    
is_odds(5)       
#%%
# Q.02


def input_avg(*number):
    a=(lambda x: x+=i for i in number)
    

input_avg(input('숫자를 입력하세요 : '))

#%%
# Q.03
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
#%%
# Q.04
#print("you" "need" "python")
#print("you"+"need"+"python")
print("you", "need", "python")
#print("".join(["you", "need", "python"]))
#%%
# Q.05
with open("test.txt", 'w') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r') as f2:
    line= f2.read()
    print(line)
#%%
# Q.06    
from datetime import datetime    
def writeDiary():
    fstr='%Y%m%d'
    today_str=datetime.strftime(datetime.now(),fstr)
    file_name= today_str +'.diary'
    
    lst=[] 
    #total_line='' #입력된 모든줄
    while True:
        line = input('내용을 입력하세요:')
        if(line == '!quit'):break
        #total_line += line + "\n"
        lst.append(line+'\n')
        
    with open(file_name,'w',encoding='utf-8') as f:
    #f.write(total_line)
        f.writelines(lst)
    #f.close()
    print('오늘자 파일'+'('+ file_name +')'+'생성완료')      

def readDiary():
    filename = input('일기파일명 : ')
    with open(filename,'r',encoding='utf-8') as fp:
    #data=fp.read()
        data=fp.readlines()
    print("파일내용 : ",data)
    #fp.close()

def errorDiary():
    print('미존재 메뉴번호')    

menu='읽기 1 쓰기 2 : '
menu_bunho=input(menu)

if menu_bunho == '1' :
    readDiary()
elif menu_bunho == '2' :
    writeDiary()   
else:
    errorDiary()










