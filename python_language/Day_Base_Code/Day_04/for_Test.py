# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:32:45 2019

@author: sundooedu
"""

test_list = ['one', 'two', 'three'] 
list_str=" ".join(test_list) # 문자열도 일일이 나눠져서 출력됨.
list_tuple= tuple(test_list)
for i in list_tuple:
    print(i)
    
 a = [(1,2), (3,4), (5,6)]   # 리스트 안에 또 튜플이 들어있는 구조.
for (first, last) in a:
    print(first + last)    
    
#%%
# 수열 함수 Range() 함수
a=list(range(1,11,2))    
a=list(range(101)) # 시작숫자가 생략되면 default는 <0> 이다.
a    
#%%   # 매우 중요!!! 통으로 외우기!!!
ssum=0
for a in range(1,11): # range를 list로 변환시키지 않아도 된다.
    ssum=ssum+a
    
print(ssum)
#%%
i=1
ssum=0
while i<11:
    ssum=ssum+i
    i=i+1
print(ssum)    
#%%
# Q4.
for i in range(1,101):
   print(i)    
#%%
# Q5.
scores=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
ssum=0
for i in scores:
    ssum=ssum+i

print(ssum/len(scores))
#%%
# Q6.
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if (n%2==1)]
result
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
        
        
#%%
# Q04 10.04 메모장에 있던 퀴즈 
x=87
y=36
answer=0

while (x+y) != answer:
    answer=int(input(str(x)+"+"+str(y)+"의 값은?"))
    
    if x+y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
#%%
# Q05 10.04 메모장에 있던 퀴즈        
        
country=input("국가를 입력하시오 : ")      
state=input("도를 입력하시오 : ")  

shipping_cost=0

if country=="한국":
    if state=="제주도":
        shipping_cost="10K"
    else:
        shipping_cost="5K"
else:
    shipping_cost="20K"        
print("배송료는 {0}입니다.".format(shipping_cost))
#%%
# Q06 10.04 메모장에 있던 퀴즈 

for b in range(2,101):    # 짝수만
   if b%2==0:
       print(b,end=' ')
       
for b in range(2,101):    # 홀수만
   if b%2==0:
       pass
   else:
       print(b,end=' ')       
#%%
for i in range(1,101,2): # i에 어떤 값이 있는 동안~
    print(i, end=" ")   # 공차 2를 줘서 코드를 줄인다.
    
       
#%%
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break       
#%%
        
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))        
#%%
for i in range(2,10):
    for j in range(1,10):
        print("{0}x{1}={2}".format(i,j,i*j),end=" ")
    print(' ')        
#%%
a=[1,2,3,4]
result=[i*3 for i in a if i%2==0]
result
for i in a:
    if i%2==0:
       result.append(i*3)
       print(result)
#%%
a=[1,2,3,4,'A','B']
result=[i*3 for i in a if (type(i)==int) and (i%2==0)]  # 형식이 정수이면서 짝수인
result
#%%
a=[1,2,3,4,'A','B']
result=[i*3 for i in a]
result
#%%
a={1,2,3,4,'A','B'} # set도 내포가 가능
result=[i*3 for i in a if (type(i)==int) and (i%2==0)]  # 형식이 정수이면서 짝수인
result
#%%
a={1:'A',2:'B'}
result={key:val*3 for key,val in a.items()} # 반복변수(iterator)가 두개가 와야된다. i=key, j=val
result
#%%
a = [1, 2, 3]
ia = iter(a)  #첫번째 요소 이전을 가리킴
type(ia)

next(ia)
1
next(ia)
2
next(ia)
3
next(ia)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
#%%
a = {1, 2, 3, 5, 7, 9, 10}
ia = iter(a)  #첫번째 요소 이전을 가리킴
type(ia)
a

next(ia)
#%%
a=[1,2,3,1,2,3,1,2,3,1,2,3]
import sys
asize=sys.getsizeof(a)
ia=iter(a)
iasize=sys.getsizeof(ia)
# 이터레이터를 써야하는 이유
# 일관성
# 다양한 자료구조와 상관없는 일관성(단일화된)있는  # 일관=추상화
# 이터레이터 자료구조.
# 이터레이터는 메모리 절약 가능
#%%
# Q2
i=0
ssum=0
while i<1000:
      if i%3==0:
          ssum=ssum+i  
      i=i+1
print(ssum)
#%%
# Q3
i=1
while i<=5:
     print("*"*i)
     i=i+1    
     
i=5
while i>0:
     print("*"*i)
     i=i-1      
     
#%%
# Q5      
a=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
ssum=0
for i in a:
    ssum=ssum+i
print("A학급 평균 점수 : {0}".format(ssum/len(a)))     
#%%
# Q6 
numbers=['1','2','3','사','오'] # 문자형식의 숫자
result=[int(n) for n in numbers if n.isdigit()==True ]
print(result[0])
i=iter(result)
next(i)

# 제너레이터 내포
result=(int(n) for n in numbers if n.isdigit()==True ) # 소괄호로 바꾼것만으로 iterate가 된다.
next(result)
print(next(result))



















    