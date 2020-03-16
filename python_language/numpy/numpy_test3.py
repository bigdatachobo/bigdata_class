# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:15:55 2019

@author: sundooedu
"""
#%%
import numpy as np

a=np.array([[1,2],
            [3,4]])

b=np.array([[5,6],
            [7,8]])

c=a+b             # 덧셈
c=np.add(a,b) 
c
c=a-b             # 뺄셈
c=np.subtract(a,b)

c=a*b             # 곱셈
c=np.multiply(a,b)

c=a/b             # 나눗셈
c=np.divide(a,b)

np.maximum(a,b) # 최대값을 가진 행렬 자체를 리턴

np.minimum(a,b) # 최소값을 가진 행렬 자체를 리턴

# 즉, 행렬끼리 비교하여 큰 행렬 자체를 리턴.
#%%
# 벡터 혹은 행렬 요소와 scalar 연산이 가능
c=a+2
c=a*2
c=a**2
c=np.add(a,2)
#%%
# 벡터 내적
import numpy as np
a=np.array([1,2,3]) # 내적시 행벡터로
b=np.array([4,5,6]) # 내적시 열벡터로 바뀜.
# 두 벡터간의 차원(길이, 개수) 동일
np.dot(a,b) # numpy 내장함수 / 내적시 (a,b) = (행벡터, 열벡터) ≒ (가로방향, 세로방향) 연산결과가 스칼라값인 1개로 나오게된다.
np.inner(a,b) # 파이썬 내장함수
#%%
# cosΘ 구하기 
a=np.array([1,2,3])
b=np.array([4,5,6])
a_size=np.sqrt(np.sum(np.square(a)))
b_size=np.sqrt(np.sum(np.square(b)))
c=np.sqrt(14)
d=np.sqrt(16+25+36)
cos_setah=np.dot(a,b)/(a_size*b_size) # 두 벡터 사이의 cos 값
import math
setah_radian=math.acos(cos_setah)
np.rad2deg(setah_radian)
#함수화
def between_vector(a,b):
    import math
    import numpy as np
    vector_a = np.array(a)
    vector_b = np.array(b)
    
    a_size = np.linalg.norm(vector_a) # 벡터 크기
    b_size = np.linalg.norm(vector_b)
    
    cos_setah = np.dot(a,b)/(a_size*b_size)
    
    setah_radian = math.acos(cos_setah)
    setah_angle = np.rad2deg(setah_radian)
    return (f'cos : {round(cos_setah,3)}, radian : {round(setah_radian,3)}, 180 angle : {round(setah_angle,3)}')

between_vector([1,3,5],[6,7,2])
#%%
#외적
np.cross(a,b) #numpy 내장함수 / array([-3,  6, -3]) 연산결과가 벡터로 나오게된다.
np.outer(a,b) #array([[ 4,  5,  6],
              #       [ 8, 10, 12],
              #       [12, 15, 18]]) 둘의 결과값이 다르게 나오게 된다.
              # 파이썬 내장 함수
              
#%% quiz
a=np.array([1,2])
b=np.array([4,5])              
# 내적
np.dot(a,b)
np.inner(a,b)
# 외적
np.cross(a,b)
np.outer(a,b)
#%%
a=np.array([[1,2],
            [3,4]])
# 전치행렬 함수    
np.transpose(a) # 전치행렬 / # 행과 열이 바뀌게됨.  
# array([[1, 3],
#        [2, 4]]) 
#%%
# 역행렬 구하기
import numpy as np
import math

a=np.array([[1,2],
            [3,4]])
    
a=math.sin(np.pi) # 파이썬은 값을 근사치로 가져간다.
a
    
np.eye(2) # 단위행렬
np.linalg.inv(a)
inv_a = np.linalg.inv(a) # 역행렬

b=(np.dot(a,inv_a)) #array([[ True,  True],
                            #        [ True,  True]])
np.eye(2)
# 행렬.(내적)역행렬 = 단위행렬
#%%%%
# 벡터간의 거리 (유사도) >>> 유클리드 거리
# [(a1-b1)^2 + (a2-b2)^2]^(1/2)
a=np.array([1,2])
b=np.array([3,4])
import math
vector_distance = math.sqrt(sum((a-b)**2)) # 두 벡터간 거리
vector_length = np.sqrt(np.sum(np.square(a-b))) # 벡터간 길이

between_vector([1,2],[3,4])
#%% 
import numpy as np
a=np.array([1,3])
b=np.array([3,2])

# 합집합 : 중복제거 후 요소들 정렬
np.union1d(a,b) 

# 차집합
np.setdiff1d(a,b) # a를 기준으로 1 리턴
np.setdiff1d(b,a) # b를 기준으로 2 리턴

#%%
# array를 파일로 저장할때
arr=np.array([1,2,3]) # 정수
np.savetxt("arr.csv", [arr], fmt='%d', delimiter=',', newline='\n',header='칼라,texture,position',comments='', encoding='utf-8')

arr=np.array([1.5674984,np.pi,np.e]) # 실수
np.savetxt("arr2.csv", arr2, fmt='%f', delimiter=',', newline='\n',header='실수,파이,오일러상수',comments='', encoding='utf-8')

arr=np.array([[1,2,3],[4,5,6]])
np.savetxt("arr2.csv", arr2, fmt='%f', delimiter=',', newline='\n',header='칼라,texture,position',comments='', encoding='utf-8')

np.loadtxt("arr2.csv",delimiter=',',skiprows=1,encoding='utf-8') # header는 데이터가 아니므로 skiprows=1 로하여 1개를 건너뛰어 데이터만 읽어온다.
# skiprows=1 : 1행은 건너뛴다. (index로 0행을 건너 뛴다는 의미.)

# max_rows=1 : 읽어드릴 최대 1개
arr2=np.array([[1.5674984,np.pi,np.e],
              [1.5674984,np.pi,np.e]])
np.loadtxt("arr2.csv",delimiter=',',skiprows=1,encoding='utf-8',max_rows=1) # 2중에 1개만 읽어드린다.
#%%
lst=[[1,2,3],
     [4,5,6]]

lst2=[[1,2,3],
      [4,5,7]]

arr = np.append(lst,lst2,axis=0) # axis=0 : 행방향으로 추가, 행렬구조 유지

np.savetxt("arr_matrix.csv", arr, fmt='%d', delimiter='::' )

np.loadtxt("arr_matrix.csv",delimiter='::')
