# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:39:58 2019

@author: sundooedu
"""

import mode1
print(mode1.add(3,4))

print(mode1.sub(5,100))

from mode1 import add
add(3, 4)

from mode1 import * #add, sub
add(4,5)
sub(3,2)

if __name__ == "__main__": 의 의미

def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__": # 내가 작성한 이줄 아래 코드가 
    print(add(1, 4))       # 친구와 공유한 모듈이 친구 코드에서 
    print(sub(4, 2))       # 실행되지 않도록하기 위함이다.

import math 

print(" %0.48f " % math.pi)
print(" %0.51f " % math.e)

math.factorial(5)

import mymod.mod3

print(mod3.mul(5,3))

from mymod import mod3 as m3 # "from" 다른패키지명 "import" 모듈명 "as" 모듈별명

print(m3.mul(5,3))

from datetime import datetime
print(datetime.now())

import urllib.request
response= urllib.request.urlopen('https://www.myprotein.com/')
content=response.read().decode('utf-8')
response

import a.b.your_math
a=add(3,4)

print(a.b.your_math.__name__)

from a.b import your_math
add(3,4)

import sys # 파이썬 표준 모듈, 외부 파일 가져오는 모듈
sys.path.append('D:\ml')

import mysvm
print(mysvm.fit('학습데이터','레이블데이터'))
print(mysvm.predict('다른학습데이터'))
