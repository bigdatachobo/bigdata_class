# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:15:15 2019

@author: sundooedu
"""
#%%
print(bool(''))
print(bool([]))
print(bool(None))
#변수 선언
v=None # v라는 변수를 선언만하겠다. 값은 없음.
#최초의 값을 대입하는 것을 변수 초기화라고 부른다.
v=1 # initialize(변수 초기화)
print(bool(v))
#%%
# bool은 "~이다, ~아니다, ~있다, ~없다"라는 의미이며
# 상태를 나타내는 논리형이다.
#%%
Q01
score_dict={"국어":80,"영어":75,"수학":55}
a=score_dict.values()
b=list(a)
print("평균:",(b[0]+b[1]+b[2])/3)
#%%
Q02
n=13
if (n%2==0):
    print("자연수 13은 짝수")
else:
    print("자연수 13은 홀수")
#%%
Q03    
hong='881120-1068234'
a=hong.split('-')
print("연월일부분:",a[0],",","민증 뒷부분:",a[1])
#%%
Q04
pin = "881120-1068234"

a=pin.find('-')
b=pin[a+1:a+2]

if b==2:
    print("성별:여자")
else:
    print("성별:남자")    
#%%
Q05
a="a:b:c:d"
b=a.replace(":","#")
print(b)            
#%%
Q06
a=[1,3,5,4,2]
a.sort()
a.reverse()
a
print(a)
#%%
Q07
a=['Life', 'is', 'too', 'short']
" ".join(a) 
#%%
Q08
t=(1,2,3)
a=list(t)
a.append(4)
a
t1=tuple(a)
t1
#%%
Q10
 a = {'A':90, 'B':80, 'C':70}
 b=a.pop('B')
 print(a)
 print(b)
#%%
Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5] 
b=set(a)
b
c=list(b)
c
#%%
Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
 
 
 
 
 
 
 
 