# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:09:35 2019

@author: sundooedu
"""
#%%
# 함수 선언
def add(a,b):
    r=a+b-1
    return r
# 함수 사용시 유지보수 작업량 감소
# 재사용성 향상    
#%%
a=1
b=2
r=add(a,b)    #함수 호출(call)
r
#%%
# 1. 매개변수는 기본값을 가질 수 있다.
def add(la=2,lb=1):
    lr=la+lb
    return lr

r=add(3) #la인자가 3으로 해서 생략된 lb는 기본값인 1사용
print(r)

r=add(lb=3) # 매개변수를 직접 지정해준다.
print(r)
#%%
def add_many(*args): # "*"을 앞에 붙여주면 튜플로 만들어준다.
    result = 0       # "*" 0개 이상의 모든 수를 뜻함
    for i in args: 
        result = result + i 
    return result 

add_many( )
#%%
def add_mul(choice, *args): 
    if choice == "add": 
         result = 0  # 0값으로 초기화
         for i in args: 
             result = result + i 
    elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
    return result 

add_mul("mul", 1,2,4)
add_mul('mul', 1,2,3,4,5)
#%%
def add_mul(choice, *args): 
    if choice == "add": 
         result = 0  # 0값으로 초기화
         if(len(args) > 0):
             for i in args: 
                 result = result + i 
    elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
    return result 
#%%
def add_mul(choice, *args): 
    if choice == "add": 
         result = 0  # 0값으로 초기화
         if(bool(args)==True):  #args에 bool()을 붙여야 한다.
             for i in args: 
                 result = result + i 
    elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
    return result     


add_mul('add', 1,2,3,4,5)
#%%
def add_and_mul(a,b):
    return a+b, a*b    #튜플로 패킹(packing)이 되는 것.
print(add_and_mul(1,2))
r1,r2=add_and_mul(1,2) # unpacking 언패킹 
print(r1,r2)           # 요소들을 저장소에서 빼내는 것.
#%%
country = input("국가를 입력하시오: ")
state = input("도를 입력하시오: ")

shipping_cost = 0
if country == "한국":
	if state == "제주도":
		shipping_cost = 10000
	else :
		shipping_cost = 5000
else :
		shipping_cost = 20000
print("배송료는", shipping_cost, "입니다.")
#%%
country = input("국가를 입력하시오: ")
state = input("도를 입력하시오: ")
def destination(country,state):
    shipping_cost=0
    if country=="한국":
        if state=="제주도":
            return shipping_cost=10000
        else:
            return shipping_cost=5000
    
    else:
        return shipping_cost=20000
#%%    

def get_shipping_cost(country="한국",state="서울"):
    shipping_cost=0
    if country == "한국":
    	if state == "제주도":
    		shipping_cost = 10000
    	else :
    		shipping_cost = 5000
    else :
    		shipping_cost = 20000    
    return shipping_cost    
    
country = input("국가를 입력하시오: ")
if(country==""):
    country="한국"
state = input("도를 입력하시오: ")
if(country==""):
    state="서울"

shipping_cost = get_shipping_cost(country,state) # 디폴트값 설정 

print("배송료는", shipping_cost, "입니다.")
#%%
def input_calc():
    print("-"*35)
    menu="""
    1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 
    0.종료
    """
    print(menu)
    print("-"*35)
    menu_Bunho=int(input("메뉴번호 입력 : "))
    print(menu_Bunho,"번 선택")
    num1=1
    num2=1
    if (menu_Bunho >=1 and menu_Bunho<= 4):
        num1=int(input("첫 번째 정수 입력 :"))
        num2=int(input("두 번째 정수 입력 :"))
    return menu_Bunho,num1,num2 #튜플(menu_Bunho,num1,num2)로 묶여져서 return이 된다.

#def process_calc():
    #pass
    
    
def add_calc(num1,num2):
    return num1 + num2

def minus_calc(num1,num2):
    return num1 - num2

def multi_calc(num1,num2):
    return num1*num2

def div_calc(num1,num2):
    return num1/num2



def control_calc():
        while True:
             menu_Bunho,num1,num2=input_calc()  #메뉴번호 작업을 처리하는 처리기능 선택 연결호출
          
             if(menu_Bunho==1):
                result=add_calc(num1,num2)
       
             elif(menu_Bunho==2):  
                result=minus_calc(num1,num2)
     
             elif(menu_Bunho==3):    
                result=multi_calc(num1,num2)
       
             elif(menu_Bunho==4):
                result=div_calc(num1,num2)
         
             elif(menu_Bunho==0):
                print("프로그램 정상종료")
                break #즉시 반복을 정지하고 빠져나감
             #결과화면:결과제공기능 연결호출 
             
             #1~4가 아닌경우
             elif(menu_Bunho < 0 or menu_Bunho > 4 ):
                 print("잘못된 메뉴번호입니다.\n다시입력")
                 continue # (while,for) 문으로 되돌아가는 반복제어문
             elif(menu_Bunho.isdigit == False ):
                 print("잘못된 메뉴번호입니다.\n다시입력")
                 continue    
             
             view_calc(result)
         
            
def view_calc(result):
      print("계산결과 = ",result)
    

#%%
  
control_calc()

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
#%%
s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87,
     87, 36, 82, 98, 84, 76, 63, 69, 53, 22] 

su=[]
wu=[]
mi=[]
yang=[]
ga=[]

for i in range(len(s)):
    
    if (s[i]//90==1):
        su.append(s[i])
        
    elif (s[i]//80==1):
        wu.append(s[i])
        
    elif(s[i]//70==1):
        mi.append(s[i])
        
    elif(s[i]//60==1):
        yang.append(s[i])
        
    else:
        ga.append(s[i])
    i=i+1
    
grade=['수','우','미','양','가']    
eng=[su,wu,mi,yang,ga]


for i in range(0,5):
    print("{0} : {1}".format(grade[i],len(eng[i])))
    i=i+1    

#%%
#refactoring 코드를 다듬는 과정.
# 코드를 간소화 시키는 과정.
# 중복코드 및 불필요한 코드 제거.

#%%
def gradecount(s):
    count_su=0
    count_wu=0
    count_mi=0
    count_yang=0
    count_ga=0
    grade1=['수','우','미','양','가']
    count_list=[count_su,count_wu,count_mi,count_yang,count_ga]
    
    for i in s:
        if (i//90==1):
            count_list[0]+=1
        elif (i//80==1):
            count_list[1]+=1
        elif (i//70==1):
            count_list[2]+=1
        elif (i//60==1):
            count_list[3]+=1
        else:
            count_list[4]+=1
         
            # 변한값을 새로이 업데이트 시켜줘야해서 count_list[i]로해서 
            # 각 단계별로 업데이트를 시켜줘야 한다.
    for j in range(len(count_list)):
        print("{0} : {1}명".format(grade1[j],count_list[j]))
        
    

s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87,
     87, 36, 82, 98, 84, 76, 63, 69, 53, 22]         
gradecount(s)       
        
#%%
add = lambda a, b: a+b
result = add(3, 4)

print(result) 

result=(lambda a,b:a+b)(3,4)
result

result=(lambda : 1)()
result

result = (lambda x: '짝' if x%2==0 else '홀')(3)  # 한줄로 if else  표현가능
result
#변수명이 곧 함수명
#한줄 리턴문이 없는 무명(익명) 함수

# 리스트 내포 표현식이 가장 많이 씀.
a=[2,3,4,5]

b=[i*2 for i in a if i%2==0] # 리스트 내포
b
result=
a=[2,3,4,5]    
b=[i*2 if i%2==0 else i*3 for i in a ]    
b       
#%%
lst=[2,3,4,5]
r_list=(lambda a:[i*2 if i%2==0 else i*3 for i in a ])(lst)        
        
        
        
        
        
        
        
