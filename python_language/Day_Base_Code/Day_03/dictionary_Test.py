# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:37:32 2019

@author: sundooedu
"""
#%%
member={'name':'홍길동', 'age':18, 'phone':a}
a=int('01037873146')
#%%
f='1.23'
print(float(f)+1)
print(str(1.23))
print(str(1))
#%%
members = {'name': '황예린', 'age': 22, 'email': 'yerin@codingschool.info'}
print(members)
print(members['name'])
print(members['age'])
print(members['email'])
print('길이 : %d' % len(members))
#%%
name = '홍지수'
scores = {'kor': 90, 'eng': 89, 'math': 95, 'science': 88}
print(scores)
scores['kor'] = 70
print(scores['kor'])
scores['music'] = 100
print(scores)
del scores['science']
print(scores)
print('이름 : %s' % name)
print('국어 : %s' % scores['kor'])
print('영어 : %s' % scores['eng'])
print('수학 : %s' % scores['math'])
#score 함수
print(scores.get('art','미정'))
# in 함수 
'kor' in scores
#%%
#keys 함수
scores.keys()
#values 함수
scores.values()
#items  Key, Value 쌍 얻는 함수
scores.items()
#clear 지우는 함수
scores.clear()
#%%
b=scores.keys() # b(keys()함수로 만들어진 set) 는 불완전해서 list() 함수로 리스트로 변환해야한다.
c=list(b)
c.append('hist')
print(c)
#%% # b(values()함수로 만들어진 set) 는 불완전해서 list() 함수로 리스트로 변환해야한다.
d=scores.values() # value 값은 tuple로 관리되서 append가 안먹어서 list()로 변환해야한다.
e=list(d)
e.append(0)
print(e)
#%%
f=scores.items()
print(f)
g=scores.copy() # backup 소위말하는 변수명에 시간 날짜도 같이 기입해주는것이 좋다.
#ex) scores_copy_191002=scores.copy() <-- 이렇게.
scores.clear() # clear 하기전에 사본을 하나 만들어 원본을 지키고 뭔가 수행을 한다.

