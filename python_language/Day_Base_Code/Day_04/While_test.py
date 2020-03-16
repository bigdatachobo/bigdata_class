# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:15:49 2019

@author: sundooedu
"""

Love_hit=0
while Love_hit<10:
    Love_hit=Love_hit+1
    print("나무를 {}번 찍었습니다.".format(Love_hit))
    if Love_hit==10:
        print("넘어~~간다!!!")
# =============================================================================
# # 디버그(Debug) 모드
# # 특정줄에 중단점을 설정
# # 해당줄에서 실행을 중지후
# # 한줄(스텝)씩 실행 가능   
#  
# # 버그추적 ---> 버그 처리해결 (버그픽스:bugfix)     
#     
# # <실행흐름 (workflow = 순서)>  
#         
# # 브레이크 포인트 줄 F12 설정
# # 1. Ctrl + F5 디버그 모드 시작
# # 2. Ctrl + F12 브레이크 포인트 이동 (반복문 1회 실행!)
# 
# # Ctrl + F10 한줄 실행
# # Ctrl + F11 함수 내부 진입 한줄 실행        
# 
# # Ctrl + Shift + F12 디버그 모드 멈추기        
# =============================================================================
# =============================================================================
# #%%
# # 반복변수 = 시작값
# # while (반복변수) <= (마지막 값):
# #      <수행할 문장1>        
# #      <수행할 문장2>     
# #      <수행할 문장3> 
# #      반복변수 = 반복변수 + 1       
# =============================================================================
#%%
Love_hit=1
while Love_hit<=10:
    print("나무를 {}번 찍었습니다.".format(Love_hit))
    Love_hit=Love_hit+1        
#%%
prompt="""
1. Add
2. Del
3. List
4. Quit

Enter number : """ 
   
number = 0
while number != 4:
    print(prompt)
    number = int(input())
#%%
input_number1=int(input("반복 수행 횟수를 입력하세요 : "))
input_number2=int(input("첫 숫자를 선택하세요 : "))    
input_vari=input_number2

while input_vari <= input_number1:
    print("상대방에게 {}번 고백하셨습니다.".format(input_vari))
    input_vari=input_vari+1
#%%
#변수 선언시 가급적 기본값으로 입력    
input_number1=10
input_vari=1
loopCount=1  
n=0

# 메인메뉴 
menu=""" 
1.시작값 선택
2.마지막값 선택 
3.실행결과 보기 (기본 10번 고백하기)

Enter number : """

# 서브메뉴
sub_menu_first="시작 정수 입력 : "
sub_menu_second="마지막 정수 입력 : "

while n != 3:
    n=int(input(menu))
    if(n==1):
         input_vari=int(input(sub_menu_first))
    elif (n==2):
         input_number1=int(input(sub_menu_second))
         input
    else:
         pass  
    
while input_vari <= input_number1:
    print("상대방에게 {0}번 고백하셨습니다.".format(input_vari))
    if(input_vari==20):
        print("나무가 넘어갔습니다.")
        break
    input_vari=input_vari+1
    if (input_vari==input_number1+1):
        print("프로그램 정상종료")
#%% 1~10까지 더하기
# 반코딩 --> 스케치
while n <= 10:
    pass
print()
#%%
n=1
ssum=0
while n <= 10:
    #pass
    #ssum=ssum+n
    ssum += n # 간소화시킨 형태
    n += 1
print(ssum)
#%%
# =============================================================================
# 반복불규칙성:
# 반복변수=0
# while 반복병수 != 반복종료값:
#     <수행할 문장1>       
#     <수행할 문장2>  
#     <수행할 문장3>  
# =============================================================================
#%%
n=0
ssum=0
while n >= 0:
    n=int(input("0혹은 양의정수 입력 : "))
    if (n < 0):
        break
    ssum += n 
print(ssum)
#%%
n=0
hap = 0
isLoop=True
while isLoop:
    n=int(input("정수입력 : "))
    if (n<0):
        break
    hap+=n
print(hap)
#%%
# <연산성능 개선> 합공식 이용
input_num=int(input("1부터 더할 수를 입력하세요 : "))
print("1부터 {0}까지의 합".format(input_num))
print(int((input_num)*(input_num+1)/2))
#%%
input_num=int(input("n수를 입력하세요 : "))
print("n이 1부터 {0}까지의 합".format(input_num))
a1=1
r=2
print(((r**(input_num))-1)/(r-1))
#%%
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
# =============================================================================
#         a=(money-300)//500   내가 생각했던 코드
#         b=(money-300-500*a)//100
#         c=(money-300-500*a-100*b)//10
# =============================================================================
        change=money-300
        coin_500=change // 500  #강사님이 생각하신 코드
        change=change % 500      #전체자리 % 상위단위(10) = 하위단위(1) 나머지
        coin_100=change // 100
        change=change % 100
        coin_10=change // 10
        print(""" 500원 동전의 개수 : {0},
 100원 동전의 개수 : {1},
 10원 동전의 개수 : {2}""".format(coin_500,coin_100,coin_10))
        coffee = coffee -1
        
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
#%%
n=1234    # 1.대충 틀을 잡는다.

while ():
    pass
print()
#%%
n=1234
hap=0    # 2.합을 초기화함.
while ():
    pass
print()
#%%
n=1234
hap=0   
while (n !=0 ):
    #pass
    hap += n % 10
    n=n // 10
    if(n==0):
        print(hap)        
#%%
year=0
money=1000

while money <= 2000:
    year+=1   #year=year + 1
    interest = money*0.07
    money += interest  #money=money + interest
print(year)    
#%%
year=0
money=int(input("원금(만원)입력 하세요 : "))

while money <= 2000:
    year+=1   #year=year + 1
    interest = money*0.07
    money += interest  #money=money + interest
print(year)   
#%%
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: 
        continue
    print(a)
#%%
su=1
while su <= 10:
    if (su%2==0):
        su+=1      # 1증가.
        continue   # 조건문 되돌아가기전에 증가시켜라.
    print(su)
    su+=1          # 1증가가 하나 더 필요함.
    
    











  