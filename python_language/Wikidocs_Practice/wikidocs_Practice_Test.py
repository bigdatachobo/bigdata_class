# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:20:47 2019

@author: sundooedu
"""
#%%
# Q 001
print("Hello World")
#%%
# Q 002
print("Mary's cosmetics")
#%%
# Q 003
print('신씨가 소리질렀다."도둑이야".')
#%%
# Q 004
print("C:\\\\Windows")
#%%
# Q 005
print("안녕하세요.\n만나서\t\t반갑습니다.")
#%%
# Q 006
print("오늘은","일요일")
#%%
# Q 007
print("naver;kakao;sk;samsung")
#%%
# Q 008
print("naver/kakao/sk/samsung")
print("naver","kakao","sk","samsung",sep="/")
#%%
# Q 009
print("first",end=" ");print("second",end=" ")
#%%
# Q 010
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))
#%%
# Q 011
a = "3"
b = "4"
print(a + b)
#%%
# Q 012
s = "hello"
t = "python"

print(s+"!"+" "+t)
#%%
# Q 013
print("Hi" * 3)
#%%
# Q 014
print("-"*80)
#%%
# Q 015
t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*4)
#%%
# Q 016
print(2.0e4*10)
#%%
# Q 017
print(2 + 2 * 3 )
#%%
# Q 018
a = "132"
type(a)
#%%
# Q 019
num_str = "720"
a=int(num_str)
type(a)
#%%
# Q 020
num = 100
a=str(num)
type(a)
#%%
# Q 021
lang='python'
a=lang.split()
print(lang[:1],'',lang[2:3])

#%%
# Q 022
license_plate = "24가 2210"
print(license_plate[-4:])

#%%
# Q 023
string = "홀짝홀짝홀짝"
a=string.find("짝")
print(string[0],string[2],string[4])

#%%
# Q 024
string = "PYTHON"
print(string[::-1])

#%%
# Q 025
phone_number = "010-1111-2222"
a=phone_number.split('-')
print(a[0],a[1],a[2])
#%%
# Q 026
phone_number = "010-1111-2222"
a=phone_number.split('-')
print(a[0],a[1],a[2],sep='')

b=phone_number.replace('-',' ')
#%%
# Q 027
 url = "http://sharebook.kr"
 a=url.split('.')
 print(a[1])
 
 print(url[-2:])
 
#%%
# Q 028
lang = 'python'
lang[0] = 'p'
print(lang)
#%%
# Q 029
string = 'abcdfe2a354a32a'
a=string.replace('a','A')
print(a)

#%%
# Q 030
string = 'abcd'
a=string.replace('b', 'B')
print(a)

#%%
# Q 041
movie_rank=['닥터 스트레인지','스플릿','럭키']
#%%
# Q 042
a=movie_rank.append('배트맨')
print(movie_rank)
#%%
# Q 043
a=movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
#%%
# Q 044
a=movie_rank.remove('럭키')
#%%
# Q 045
del movie_rank[2:]
#%%
# Q 046
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2         
#%%
# Q 047
nums = [1, 2, 3, 4, 5, 6, 7]
a=max(nums)
b=min(nums)

print("max : {}".format(a))
print("min : {}".format(b))
#%%
# Q 048
nums = [1, 2, 3, 4, 5]
a=sum(nums)
#%%
# Q 049
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", 
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
c=len(cook)
#%%
# Q 050
nums = [1, 2, 3, 4, 5]
avg=sum(nums)/len(nums)
#%%
# Q 051
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
#%%
# Q 052
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd=[i for i in nums if i%2==1 ]
#%%
# Q 053
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=[i for i in nums if i%2==0 ]
#%%
# Q 054
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
#%%
# Q 055
interest = ['삼성전자', 'LG전자', 'Naver']
print("{0} {1}".format(interest[0],interest[2]))

#%%
# Q 056
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

for i in range(len(interest)):
    print(interest[i],end=" ")

print(' '.join(interest))
#%%
# Q 057
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']    

for i in range(len(interest)):
    print(interest[i],end="")

print('/'.join(interest))
#%%
# Q 058
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

#%%
# Q 059
string = "삼성전자/LG전자/Naver"
a=string.split('/')
#%%
# Q 060
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
b=string.split('/')
#%%
# Q 061
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)
#%%
# Q 062
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)
#%%
# Q 063
my_variable=()
type(my_variable)
#%%
# Q 064
t = (1, 2, 3)
a=t[0]

#%%
# Q 065
tuple_test=(1)
#%%
# Q 066
t = ('a', 'b', 'c')
t = (t[0].upper(), t[1], t[2])
#%%
# Q 067
interest = ('삼성전자', 'LG전자', 'SK Hynix')
list_interest=list(interest)
#%%
# Q 068
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tuple_interest=tuple(interest)
#%%
# Q 069

#%%
# Q 070
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)
#%%
# Q 071
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
len(scores)
a,b,c,d,e,f,g,h,*i=scores
print(a,b,c,d,e,f,g,h)
*valid_score, a, b = scores
#%%
# Q 072
a,b,*c=scores
_, _, *valid_score = scores
#%%
# Q 073
_, *valid_score, _ = scores
#%%
# Q 074
temp={}
#%%
# Q 075
icecream_price={'메로나':'1000','폴라포':'1200','빵빠레':'1800'}
#%%
# Q 076
icecream_price['죠스바'] = 1200
icecream_price['월드콘'] = 1500
#%%
# Q 077
print("메로나가격 : {}".format(icecream_price['메로나']))
#%%
# Q 078
icecream_price['메로나'] = 1300
#%%
# Q 079
del icecream_price['메로나']
#%%
# Q 080
# dictionary에 누가바가 존재하지 않음
#%%
# Q 081
inventory={'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
#%%
# Q 082
print(inventory['메로나'][0],'원')
#%%
# Q 083
print(inventory['메로나'][1],'개')
#%%
# Q 084
a=inventory['월드콘']=[500,7]
#%%
# Q 085
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
a=list(icecream.keys())
#%%
# Q 086
b=list(icecream.values())
#%%
# Q 087
c=sum(b)
#%%
# Q 088
new_product = {'팥빙수':2700, '아맛나':1000}
d=icecream['팥빙수']=2700
e=icecream['아맛나']=1000
#%%
# Q 089
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
f={keys[0]:vals[0],keys[1]:vals[1],keys[2]:vals[2]}

result = dict(zip(keys, vals))

#%%
# Q 090
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

result2=dict(zip(date,close_price))
#%%
# Q 091
bool(0)
bool(1)
bool()
#%%
# Q 092
print(3 == 5)
#%%
# Q 093
print(3 < 5)
#%%
# Q 094
x = 4
print(1 < x < 5)
#%%
# Q 095
print ((3 == 3) and (4 != 3))
#%%
# Q 096
print(3 >= 4)
#%%
# Q 097
if 4 < 3:
    print("Hello World")
#%%
# Q 098
    if 4 < 3:
        print("Hello World.")
    else:
        print("Hi, there.")
#%%
# Q 099
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")        
#%%
# Q 100
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
#%%
# Q 101
hi=input("'안녕하세요'를 입력하세요 : ")
print(hi*2)
#%%
# Q 102
input_num= int(input('숫자를 입력하세요. : '))
print(input_num+10)
#%%
# Q 103
input_num= int(input('숫자를 입력하세요. : '))
determine_lambda_function=(lambda x : '짝' if x%2==0 else '홀')(input_num)
print(determine_lambda_function)
#%%
# Q 104
num=int(input("숫자를 입력하세요. : "))
if num <=235:
    print(num+20)
elif num > 235:
    print(255)    
#%%
# Q 105
while True:    
    num=int(input("숫자를 입력하세요. : "))
    if num==444:
        break
    elif num < 20:
        print(0)     
    elif num >=20:
        print(num-20)
#%%
# Q 106
from datetime import datetime
oclock=datetime.now()
st=oclock.strftime('%H:%M')

if (st[3:] == '00') :
    print("정각입니다.")
else:
    print("정각이 아닙니다.")    
#%%
# Q 107
fruit = ["사과", "포도", "홍시"]
while True:
    fruit_name=str(input("좋아하는 과일은? : "))
    if fruit_name == '없음':
        print("응~꺼져~")
        break
    elif fruit_name in fruit:
        print("정답입니다.")    
    else:
        print("틀렸습니다.")    
    
#%%
# Q 108
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

while True:
    input_investment_list=str(input("투자종목을 입력하세요 : "))
    if input_investment_list == '돈없어':
        print('응 꺼져~')
        break
    elif input_investment_list in warn_investment_list :
        print('투자 경고 종목입니다')
    else:
        print("투자 경고 종목이 아닙니다.")
        
#%%
# Q 109
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
while True:
    like_fruit=str(input("좋아하는 계절은? : "))
    
    if like_fruit == '없어':
        print("응~ 꺼져~")
        break
    elif like_fruit in fruit.keys():
        print("정답입니다.")
    else:       
        print("오답입니다.")
        
#%%
# Q 110
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
while True:
    like_fruit=str(input("좋아하는 과일은? : "))
    
    if like_fruit == '없어':
        print("응~ 꺼져~")
        break
    elif like_fruit in fruit.values():
        print("정답입니다.")
    else:       
        print("오답입니다.") 
        
#%%
# Q 111  
while True:        
    instr=str(input("알파벳을 입력하세요 : "))
    if instr == '몰라':
        print("영알못~")
        break
    elif instr.islower() == True: 
        print(instr.upper())
    else:
        print(instr.lower())    
#%%
# Q 112 
level=['A','B','C','D','E']        
while True:        
    score=int(input("점수를 입력하세요 : "))
    if score >= 81:
        print(level[0])
    elif score >= 61:
        print(level[1])
    elif score >=41:
        print(level[2])
    elif score >=21:
        print(level[3])
    elif score >= 0:
        print(level[4])
        
#%%
# Q 113  
change_rate={'$':'1200','Y':'10.96','EU':'1268','YUI':'171'}

while True:
    select_country=str(input("환전 화폐 국가를 선택하세요 : "))
    change_money=int(input("환전할 금액은? :"))
    if select_country == "돈없어":
        print("응 꺼져~")
        break
    elif select_country in change_rate.keys():
        print(float(change_rate[select_country])*float(change_money),"원")
        
     
#%%
# Q 114  
num_list=[]
for i in range(0,3):
    num=int(input("숫자 세개를 입력하시오 : "))
    if len(num_list) < 3:
        num_list.append(num)
    elif len(num_list) == 3:    
        print(max(num_list))
#%%
# Q 115  
tel={'011':'SKT','016':'KT','019':'LGU','010':'Null'}

while True:    
    intel=input("휴대폰 번호 입력 : ")
    if intel[:3] == '011':
        print('당신은 SKT 사용자입니다.')
    elif intel[:3] == '016':
        print('당신은 KT 사용자입니다.')
    elif intel[:3] == '019':
        print('당신은 LGU 사용자입니다.')
    elif intel[:3] == '010':
        print('당신은 Null 사용자입니다.')
    else:
        print('당신은 X-man 입니다.')
       
#%%
# Q 116 
pzip=input("우편번호를 입력하세요 : ")

if pzip[2] in '012' :
    print("강북구")
elif pzip[2] in '345':
    print("도봉구")
elif pzip[2] in '6789':
    print("노원구")
    
        
#%%
# Q 117  
while True:    
    id_num=input('주민등록번호 : ')
    if id_num[7] in ['1','3'] :
        print("남자")
    else:
        print("여자")   

id_num1=input('주민번호 : ')
det=list(map(lambda x : '남자' if x[7] in ['1','3'] else '여자',id_num1))  
print(det)              
#%%
# Q 118
s=['00','01','02','03','04','05','06','07','08']
p=['09','10','11','12'] 
while True:
    id_num=input("주민등록번호 : ")
    if id_num[8:10] in s:
        print("서울 입니다.")
    elif id_num[8:10] in p:
        print("부산 입니다.")
    else:
        print("서울이 아닙니다.")
        
#%%
# Q 119
rt='234567892345'
id_num=input("주민번호를 입력하세요 :")
#id_list=id_num.split('-')
#id_new_join=''.join(id_list)
id_new=id_num.replace('-','')

ssum=0
for i in range(0,12):
    ssum += int(rt[i])*int(id_new[i])
    
if id_new[-1] == (11 - (ssum%11)):
    print('유효한 주민등록번호입니다.')
else:
    print("유효하지 않은 주민등록번호입니다.")
#%%
# Q 120 모르겠음.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']        
    
volatility = int(btc['max_price']) - int(btc['min_price'])
if int(btc['opening_price']) + volatility > int(btc['max_price']) :
    print("상승장")
else :
    print("하락장")    
#%%
# Q 121
for i in ["가", "나", "다", "라"]:
    print(i,end='')    
#%%
# Q 122
for i in ["사과", "귤", "수박"]:
    print(i)   
#%%
# Q 123
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
    print("--")    
#%%
# Q 124 
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
print("--")    
#%%
# Q 125
menu = ["김밥", "라면", "튀김"]
for i in menu:
    print(f'오늘의 메뉴:{i}')
#%%
# Q 126
portfolio = ["SK하이닉스", "삼성전자", "LG전자"]
for i in portfolio:
    print(f'{i} 보유중')    
#%%
# Q 127
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']

for i in pets:
    print(f'{i} {len(i)}')    
#%%
# Q 128
prices = [100, 200, 300]
for i in prices:
    print(f'{i+10}')    
#%%
# Q 129
prices = ["129,300", "1,000", "2,300"]
for i in prices:
    a=i.replace(',','')
    print(f'{a}')    
#%%
# Q 130      
menu = ["면라", "밥김", "김튀"]
for i in menu:
    print(f'{i[::-1]}')
#%%
# Q 131
my_list = ["가", "나", "다", "라"]
for i in list(range(1,4)):
    print(my_list[i])
   
#%%
# Q 132
my_list = [1, 2, 3, 4, 5, 6]
for i in list(range(0,6,2)):
    print(my_list[i])    
#%%
# Q 133
my_list = [1, 2, 3, 4, 5, 6]
for i in list(range(1,6,2)):
    print(my_list[i])
#%%
# Q 134
my_list = ["가", "나", "다", "라"]
my_list.reverse()
for i in my_list:
    print(i)
#%%
# Q 135
my_list = [3, -20, -3, 44]
minus=list(filter(lambda x:x<0,my_list))
print(minus)
#%%
# Q 136
my_list = [3, 100, 23, 44]
triple=list(filter(lambda x:x%3==0,my_list))
print(triple)
#%%
# Q 137
my_list = ["I", "study", "python", "language", "!"]
length=list(filter(lambda x: len(x)>3,my_list))
print(length)

#%%
# Q 138
my_list = [3, 1, 7, 10, 5, 6]
big_small=list(filter(lambda x: 5< x <10,my_list))
print(big_small)
#%%
# Q 139
my_list = [13, 21, 12, 14, 30, 18]
union=list(filter(lambda x: x%3==0 and 10<x<20,my_list))
print(union)
#%%
# Q 140    
my_list = [3, 1, 7, 12, 5, 16]
oror=list(filter(lambda x: x%3==0 or x%4==0,my_list))
print(oror)








    