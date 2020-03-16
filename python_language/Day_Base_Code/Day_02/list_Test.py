# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:22:11 2019

@author: sundooedu
"""

a=[1,2,3,4,5]
print(a[0])
print(a[0:3])
print(a[0:5:2]) # 세번째 :2는 강격임 짝수번 인덱스는 간격(칸수) =2

#quiz 역방향(-)으로 간격 2로 세어서 온다
print(a[::-2])

#-1은 마지막 요소를 말하고, 간격 1로 0부터 4까지 표시함.
print(a[:-1:1])
sub_a=a[:-1:1] #서브리스트를 [1,2,3,4]
print(sub_a)

b=[0,1,2,3,4,[5,6]]
print(b[5][0])
b.append(7)
print(b)
c=b.insert(7,'칠')
print(c)
del b[6]
b.remove('칠')
del b[-1] #요소의 인덱스 값을 기반으로 값을 제거함.

b[0] = 10 # 값 수정


#오늘이 일요일이라고 하자.
#오늘부터 10일 후에는 어떤 요일이 되는가?
#요일리스트 생성 후 나머지 연산자 %를 사용해보자.

#quiz 1.

d=['일','월','화','수','목','금','토']
w=d[(10%7)]
print("10일 후 요일은 %s요일이다"% w)

d=['일','월','화','수','목','금','토']
today_idx=0
next_idx=(today_idx + 10) % 7
print(d[next_idx]+"요일")

a=[1,4,3,2]
a.sort()
a
a.reverse()
a
a="Three".lower()
a
#특수문자일부 < 숫자문자 < 영문대문자 < 영문소문자 < 한글
a=['3','삼','Three','Three.lower()','!']
len(a)
print('4' in a)
a.index('!')
a.sort()
a
print(ord('A'))
a.index('3')

#stack 리스트를 세로방향으로 세운것을 스택이라 부른다.
a=['3','삼','Three','Three.lower()','!']
a.pop() #마지막 요소 적출(끄집어냄);마지막요소가 리턴 된 후 제거됨
a

'3' in a

#모든 요소 한번에 제거 - CLEAR()
a=['3','삼','Three','Three.lower()','!']
a.clear()
a
#copy 요소를 복사한다.
a=['3','삼','Three','Three.lower()','!']
a2=a.copy()
a3=a[:] #a를 깊은 복사 [변수 복사 및 값(객체)을 같이 복사]
print(a2)
id(a) # a와 a2의 메모리 주소가 다름.
id(a2)
id(a3)
a3=a # 얕은 복사, 동일한 리스트를 참조·공유 하기 위해서, 변수만 복사
     # a3는이를테면 '바로가기' 아이콘과 같은 링크 개념임

a=['3','삼','Three','Three.lower()','!']
a2=a.copy()
a2.clear()
a2
id(a2)

#스냅샷 현재시점의 상태
a=['p','y','t','h','o','n']
s=str(a) #"['p','y','t','h','o','n']" # 그냥 그상태를 " " 인용부호로 감싼다.

ret="".join(a)
print(ret)

ret2=list(ret) #단어를 리스트로 만드는 함수 list()

a="independentday"
"".join(list(a))

a=['p','y','t','h','o','n']
b=sorted(a) #원본 리스트를 완전히 흔들어 순서를 훼손한 상태임.
b           #원본 리스트 훼손을 막아주는것이 튜플이다.

tuple_ex=('y','y','y','y','y','y') #규격정보, 상수 등을 튜플에 저장
d=sorted(tuple_ex) #외부의 수정 기능으로부터 원본데이터 보호!!

print(tuple_ex[0])

g="".join(tuple_ex)
g
a=('p','y','t','h','o','n')
tuple_ex=('y','y','y','y','y','y') 
a= a+tuple_ex
a

myFriends=['James','Robert','Lisa','Mary']

for myFriend in myFriends:
    print(myFriend)
    
print(list(range(0,101,1)))  

for a in range(0,100,1):
    print(a)

print(list(range(101)))

  admins = ['rubato', '12345', 'rubato@naver.com']
  categories=['아이디:','비밀번호:','이메일:']
  for adm,categ in zip(admins,categories):
           print(categ,adm)


# *set (집합 자료구조) 
# 저장되는 자료가 순서가 없고, 중복되어선 안됨.
# 비순서, 비중복   
# 인덱스가 없어서 순서 유지가 안됨         
a={'h','e','l','l','o'}
a.add('python')
a.remove('python')
print(a)

s1={1,2,3,4}
s2={3,4,5,6}

print(s1 | s2) # 합집합
print(s1 & s2) # 교집합
print(s1 - s2) # 차집합        
a={'h','e'}
b,c=a

l=list(a)
l.append('l')
l.append('l')
t=tuple(l)
s=set(t)
print(s)

