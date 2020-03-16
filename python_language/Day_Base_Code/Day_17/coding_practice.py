# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:18:42 2019

@author: sundooedu
"""


# =============================================================================
# 1.김씨와 이씨는 각각 몇 명 인가요?
# 2."이재영"이란 이름이 몇 번 반복되나요?
# 3.중복을 제거한 이름을 출력하세요.
# 4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
# =============================================================================

#%%
# 01.김씨와 이씨는 각각 몇 명 인가요?
names="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
b=names.split(',')
count=[0,0]

for i in b:
    if '김' in i:
        count[0]+=1
    elif '이' in i:
        count[1]+=1
print(f'김씨 : {count[0]}번, 이씨 : {count[1]}번')
#%%
a=[ i[0] for i in b ] # 성씨만 따로 분리하여 리스트를 작성 후 김,이 count!!!
print("김씨 : %d\n이씨 : %d\n"%(a.count("김"), a.count("이")))  
#%%마지막 프린트만 변형
print(f'김씨 : {a.count("김")}\n이씨 : {a.count("이")}')
      
#%%
# 2."이재영"이란 이름이 몇 번 반복되나요?
local_list1=[0]
for i in b:
    if '이재영' in i:
        local_list1[0] += 1         
print(f'이재영 {local_list1[0]}번 반복')
#%% 2번 고수 풀이.
print(b.count("이재영"))
#%%
# 3.중복을 제거한 이름을 출력하세요.
c=list(set(b))
print(c)

#%%
# 4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
ordered_list=sorted(c)
print(ordered_list)
#%% 서버 
import socket        
def run_server(port=3000):
    host='192.168.0.137'
    with socket.socket() as s:
        s.bind((host,port))
        s.listen(1)
        print('서버시작')
        conn,addr=s.accept()
        msg=conn.recv(1024)
        print('수신 메세지: ',msg.decode())
        print('수신 메세지 바이트수 : ',len(msg))
        rMsg=reverse(msg.decode())
        print('송신 메세지',rMsg)
        print('송신 메세지 바이트수 : ',len(rMsg))
        conn.send(rMsg.encode())
        conn.close()

def reverse(str):
    return ''.join(reversed(str)) 
       
if __name__ == '__main__':
    run_server()
#%%
import socket

def run_client(host,port,strList):
    with socket.socket() as s:
        s.connect((host,port))
        msg=" ".join(strList)
        s.sendall(msg.encode())
        resp=s.recv(1024)

if __name__ == '__main__':
    run_client(host='192.168.0.137', port = 3000, strList=['a','b','c'] )        
#%%
import socket

def run_client(host,port,strList):
    with socket.socket() as s:
        s.connect((host,port))
        msg=" ".join(strList)
        s.sendall(msg.encode())
        resp=s.recv(1024)
        
run_client(host='192.168.0.137',port=3000,strList=['a','b','c'])
#%%
a=[-1,1,3,-2,2]

answer=sorted(list(filter(lambda x:x<0,a)),key=lambda x:abs(x)) + sorted(list(filter(lambda x:x>0,a)))

def sort(origin_list):
    return sorted(list(filter(lambda x:x<0,origin_list)),key=lambda x:abs(x)) + sorted(list(filter(lambda x:x>0,origin_list)))
#%%

hour_in_3=list(filter(lambda x: x in '3',list(str(range(24)))))    
#%%
input_count=int(input("입력할 정수 개수를 입력시오 : "))
ssum=0
for i in range(input_count):
    ssum += int(input('숫자를 입력하시오 : '))
print(f'''합 : {ssum} 
평균값 : {ssum/input_count}''')    

del input_count,ssum,i
#%%
num_list=[0,0,0,0,0,0,0,0,0,0]  
true_list=[]

while True:
    input_num=int(input('0~9까지 숫자를 빼놓지않고 무작위로 입력하시오 : '))
    if input_num >= 10:
        break
    elif input_num == ' ':
        break
    num_list[input_num] += 1
    
for i in range(10):
    if num_list[i] == 1:
        true_list.append(True)
    elif num_list[i] < 1 or  num_list[i] >1  :
        true_list.append(False)

if False in true_list:        
    print(False)
else:
    print(True)    
#%%
a = input("0~9 사이의 숫자로 이루어진 문자열 입력 : ")
print('true' if len(a) == len(set(a)) == 10  else 'false') 
#%%
value=10
spec=150
cost=3
add_on=[30,70,15,40,65]

add_on.sort(reverse=True)

for i in add_on:
    if (spec/value) > (spec + i)/(value + cost):
        break
    else:
        spec+=i
        value+=cost
print(int(spec/value))        
#%%
value=10
spec=150
cost=3
add_on=[30,70,15,40,65]

add_on.sort(reverse=True)

for i in add_on:
    pre_cost=spec/value
    new_cost=((spec + i)/(value + cost))
    if (spec/value) > ((spec + i)/(value + cost)):
        break
    else:
        spec+=i
        value+=cost
print(int(spec/value))    
#%%
for i in range(1,7):
    print('O'*(6-i)+'X'*(i))        
#%%
from itertools import zip_longest

def compare(left, right):
    left_vars = map(int, left.split('.'))
    right_vars = map(int, right.split('.'))
    for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
        if a > b:
            return '>'
        elif a < b:
            return '<'
    return '='

CASES = [
         ['1.2.3','1.2.3'],
         ['0.0.2', '0.0.1'],
         ['1.0.10', '1.0.3'],
         ['1.2.0', '1.1.99'],
         ['1.1', '1.0.1']
        ]

if __name__ == '__main__':
    for case in CASES:
        print('{0[0]} {1} {0[1]}'.format(case, compare(*case)))
#%% 내 풀이
import collections
def split(x):
    for i in range(len(x)):
        x[i]
    return x[i]    

num_1000=list(map(str,list(range(1,1001))))
num_frequency=sorted(list(map(lambda x: split(x) ,num_1000)))
char_dict = collections.Counter(num_frequency)
print(char_dict)
#%% 고수 풀이
from collections import defaultdict

d = defaultdict(int)
for n in range(1, 1001):
    for x in str(n):
        d[x] += 1
        print(d)

print(d)
#%%
string=str(input('정수를 입력하세요. : '))        

attatch=string[0]

for i in string:
    if int(attatch[-1])%2==0 and int(i)%2==0:
        attatch += '*'+ i
    elif int(attatch[-1])%2==1 and int(i)%2==1:
        attatch += '-'+ i
    else:
        attatch += i
        
print(attatch[2:])
#%%
#약수 찾기
n=int(input("정수를 입력하세요 : "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
#%% 완전수 찾기
input_num=int(input("정수를 입력하세요 : "))        
ssum=0
for i in range(1,input_num+1):
    ssum=0
    for j in range(1,i):
        if i%j == 0:
            ssum+=j
    if ssum == i:
        print(i,end=' ')        
#%% 고수풀이
num= int(input("숫자를 입력하시오 : "))
print([x for x in range(1, num+1) if x==sum(y for y in range(1, x) if x%y==0)])
#%%
for a in range(1,1000):
    for b in range(1,1000-a):
        c=1000-(a+b)
        if (a*a+b*b==c*c) & (a<b<c):
            print(a,b,c)
            print(a*b*c)
#%%
def fibo(n):
    fibo_list=[]
    a=1
    b=2
    fibo_list.append(a)
    for i in range(n):
        fibo_list.append(b)
        a,b=b,a+b                
    return fibo_list[n]       

fibo_sum=sum(list(filter(lambda x: x%2==0 and x<=4000000 ,map(lambda x:fibo(x),range(32)))))
#%%
def double_diff(n):
    double1=sum(list(map(lambda x:x**2,range(1,n+1))))
    double2=(sum(list(range(1,n+1))))**2
    return double2-double1
double_diff(100)
#%%
import string
crypto_ref = list(string.ascii_uppercase)

def secret(string,n):
    a=list(string)
    while True:
        if ' ' in a:
            a.remove(' ')
        else:
            break
    crypted=[]
    for i in a:
        b=crypto_ref.index(i)
        crypted.append(crypto_ref[int((b+n)%26)])
    return ''.join(crypted)    
    

secret(' NIKE ADDIDAS PUMA ',5)

#%%
# 2진법 변환 코딩
def binary(num):
  binar=[]
  while True:
    if int(num)%2==0:
      binar.append('0')
    elif int(num)%2==1:
      binar.append('1')
    num = int(num)//2
    if int(num)==0:
      break
  return ''.join(binar.__reversed__())

print(binary(73))  #1001001
print(binary(8))   #1000
#%%
import math
def root_formula(a,b,c):
    d = (-b + math.sqrt((b**2)-4*a*c))/2*a 
    e = (-b - math.sqrt((b**2)-4*a*c))/2*a
    return (f'{round(d,3)},{round(e,3)}')

root_formula(-1,3,2)
#%%
import math
import numpy as np
from functools import reduce

prime=[]
for i in range(1,21):
    temp=[]
    for j in range(1,i+1):
        if i%j==0:
            temp.append(j)
    if len(temp)==2:
        prime.append(i)        
        
multi= reduce(lambda x,y: x*y,prime)

not_zero=[]
for k in range(1,21):
    if multi%k != 0 :
        not_zero.append(k)
        
print(not_zero)        
        
print(prime)
multi= reduce(lambda x,y: x*y,prime)
print(multi)

#%%
from itertools import permutations
from itertools import combinations
a=[2, 6, 4, 7]

b=list(permutations(a,3))
c=list(combinations(a,3))

combi_multi=[]
for i in c:
    ggob=1
    for j in i:
        ggob *= j
    combi_multi.append(ggob)
print(combi_multi)    
from itertools import combinations
a=[2, 6, 4, 7]
c=list(combinations(a,3))
d=list(map(lambda x:np.cumprod(x)[-1],c))

list(map(lambda x:np.cumprod(x)[-1],list(combinations([2,6,4,7],3))))
#%%
string_input=str(input("아스키코드를 알고싶은 문자를 입력하세요 : "))
for t in string_input:
    print(f'{t}는 아스키코드로 {ord(t)}입니다.')
#%%
import re    
normal_input=input('입력하세요 : ')
regex=re.compile('\d+')
a=list(map(lambda x:regex.findall(x),normal_input))
b=list(map(lambda x:regex.findall(x),''.join(a)))
print(''.join(b))
#%%
print(''.join(i for i in input('숫자를 입력하세요.') if i.isdigit()))
#%%
a=str(input("숫자 : "))
print(f'입력:{a}, 출력:{a[:1]+(len(a)-1)*"0"}자릿수')
#%%
def mean(n):
    return(sum(n)/len(n))
    
print(mean([11, 17, 20, 24]))
#%%
def median(n):
    m=sorted(n)
    if len(m)%2==1:
        answer=m[int(len(m)/2)]
    elif len(m)%2==0:
        answer=(m[int(len(m)/2)-1]+m[int(len(m)/2)])/2
    return answer
        
print(median([7, 9, 14])) #9
print(median([24, 31, 35, 49])) #33
print(median([17, 37, 37, 47, 57])) #37    
#%%
def odd_even_count(n):
    odd=0
    even=0
    for i in n:
        if i%2==0:
            even+=1
        elif i%2==1:
            odd+=1
    return (f'홀수:{odd}, 짝수:{even}')

odd_even_count([3, 4, 5, 6, 7]) # '홀수:3, 짝수:2'
odd_even_count([12, 16, 22, 24, 29]) # '홀수:1, 짝수:4'
odd_even_count([41, 43, 45, 47, 49]) # '홀수:5, 짝수:0'
#%%
def count_odd_n_even(lst):
    odd = len([x for x in lst if x % 2 == 1])
    return (f'홀수:{odd}, 짝수:{len(lst) - odd}')

count_odd_n_even([3, 4, 5, 6, 7])
#%%
def is_tri(n):
    if len(n)==3 and sum(n)==180 and min(n) != 0:
        if max(n) == 90:
            return "직각삼각형"
        elif max(n) > 90:
            return "둔각삼각형"
        else:
            return "예각삼각형"
    elif len(n) !=3 or sum(n) != 180 or min(n) == 0:
        return "삼각형이 아닙니다."

if __name__ == "__main__":
    angle_list=[[60, 60, 60],[30, 60, 90],[0, 90, 90],
                [20, 40, 120],[60, 70, 80],[40, 40, 50, 50]]
    for i,angles in enumerate(angle_list):
        print(f'{i+1}. {is_tri(angles)}')
#%%
a='5923'
hap=0
for num in a:
    hap+=int(num)
print(hap)
sum(list(map(lambda x:int(x),input("숫자를 입력하세요 : "))))
#%%
import time
time.time()

time.strftime('%H:%M:%S',time.localtime(time.time()))
