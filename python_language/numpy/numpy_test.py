# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:45:11 2019

@author: sundooedu
"""
# 0으로 초기화시킨 1행
lst = [0 for i in range(5)] # [0,0,0,0,0]

lst1=[]
lst2=[]

# 1로 초기화
for i in range(2): # 행개수
    for j in range(3): # 열개수
        lst1.append(1) # 1개의 행이 완성
    lst2.append(lst1)
    lst1=[] # lst1 초기화        

# lst2의 모든 요소를 0으로 초기화
for i in range(2): # 행개수
    for j in range(3): # 열개수
        lst2[i][j]=0
print(lst2)        

#%%
# 리스트 내포방식으로 축약

# 1로 초기화
lst2 = [ [ 1 for j in range(3)] for i in range(3) ] # [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# 0으로 초기화
lst2 = [ [ 0 for j in range(3)] for i in range(3) ] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


lst2 = [ [ j*i for j in range(3)] for i in range(3) ] # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# 단위 행렬 생성 내포 리스트
lst2 = [ [ 1 if i == j else 0 for j in range(1000) ] for i in range(1000) ] 

lst1 = [0,1,2] # 1차 리스트
lst2 = [[0,1,2],
        [3,4,5]] # 2차 리스트
#%%

import numpy as np # numpy 별명을 np로 많이씀
list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a)
print(type(list1))
print(type(a))

print(a.shape) # (4, ) 4행
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # (2, 3) # 행과 열의 개수 표현
print(len(b)) # 행개수 표현
print(b.ndim) # 차원 표시할때 
print(b.size) # 요소의 갯수

print(b[0,0]) # 1 # 좀 더 직관적인 표현
print(b[0][1])
# 요소의 데이터 타입 변경
b = np.array([[1,2,3],[4,5,6]],dtype=np.int64)
b = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
c = np.array(lst2)
print(c.ndim)
b= np.linalg.norm(c)
#%%
# numpy 배열 -> list
lst = b.tolist()
#%%
# 단일값 초기화 
import numpy.linalg

a=np.zeros((2,2)) # 2x2 행렬 만든 후 0으로 초기화
print(a)
a=np.full((2,2),5) # 2x2 행렬 만든 후 5초 채운다.
print(a)
a=np.ones((2,2)) # 2x2 행렬 만든 후 1초 채운다.
print(a)
# 항등 행렬
a=np.eye(3) # 3x3 행렬 만든 후 i=j인 대각선만 1로 채운다.
print(a)
b= np.linalg.norm(a) # 벡터a의 크기 np.sqrt(3) == (3)**1/2
print(b) # (3)**(1/2)
a = np.diag([i for i in range(3)]) # i=j 대각선에 range() 범위의 수를 나열한다.
print(a)

# 벡터b 크기
b= numpy.linalg.norm(a)
print(b)
#%%
# 다중값 초기화
a=np.array(range(20))
print(a)
a=np.array(range(20)).reshape(4,5) # 4x5 행렬로 모양을 바꿈.
print(a)
a=np.arange(20) # array + range = arange
print(a)
a=np.arange(0,20,2) # 짝수만 표현
print(a)
a=np.arange(0,20,2,np.float64) # 숫자 타입을 float64로 변경
print(a)
a=np.array(range(0,20,2),str) # 문자열로 바꿔서 표현
print(a)
a=np.arange(20).reshape(4,5) # 축약어 arange()와 reshape()함수를 같이씀.
print(a)
# 9개 균등 분할.
a=np.linspace(0,20,10)
print(a)
# 10개 균등 분할.
a=np.linspace(0,1,11)
print(a)
# 끝점 미포함.
a=np.linspace(0,1,5,endpoint=False)
print(a)
#%%
# 크기만큼(6) 균등비율로 난수(0~1 실수) 초기화
a = np.array(np.random.rand(6))
print(a)
a = np.array(np.random.rand(2,3)) # 2x3 행렬로 0~1 사이의 난수 행렬 생성.
print(a)
# 크기(개수)만큼 난수(0~5 정수) 초기화, size는 갯수를 의미
a = np.array(np.random.randint(low=0,high=6,size=6))
print(a)

# 평균 2.0, 표준편차 1.0, shape(행렬수)
# 확률변수값 6개가 정규분포한다.
a=np.random.normal(2.0,1.0,(3,3)) # 평균:2/ 표준편차:1/ 3x3행렬 크기로 난수 행렬 생성
print(a)
# 평균 0, 표준편차 1.0 인 표준정규분포(표준 가우시안 정규분포) N(0,1)
a=np.random.randn(5,5)
print(a)
#%%
# numpy 슬라이싱
# 1. 연속 슬라이싱
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
arr = np.array(lst)
# 슬라이스
a = arr[0:2, 0:2]
print(a)

# 기본 인덱스는 '행'인덱스 arr[2]로 적으면 2행이 됨
a = arr[0:2] # 0~1행, 모든열
a = arr[0:2, :] # 0~1행, 모든열
print(a)

# 2열의 모든행
a = arr[:,2]
print(a)

# 1행의 모든열
a = arr[1,:]
a = arr[1]
print(a)

a = arr[1:, 1:]
print(a)

# 한개 요소 성분 추출 arr [행 엔덱스, 열 인덱스] 
a = arr[1,1]
print(a)

a = arr[1:, 1:] = 0 # 슬라이싱한 범위 행렬을 0으로 초기화
print(arr)

a=1 # a 변수값이 arr[1:, 1:]에서 1로 바뀜.
#%%
# numpy 슬라이싱
# 2. 비연속 슬라이싱

import numpy as np
lst = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
a = np.array(lst)
# 정수 인덱싱
b= a[[0,2],[1,3]] # (0행, 1열) / (2행, 3열)  >>> 2, 12
print(b)
b = a[[0,2],1:3] # 0행, 2행 / 1열부터 2열까지 (3열 포함 안됨)
print(b)
b = a[0:2,[1,3]] # 0행부터 1행까지(2열 미포함) \ 1열, 3열
print(b)

b = a[2,[1,3]] # 10, 12| 2행 / 1열, 3열
print(b)
#%%
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
arr = np.array(lst)
# 확장 슬라이싱
# 세번째 인자가 해당 인덱스의 증가치(간격)
a = arr[0:2:1]
print(a)

a = arr[0:2:1, 0:3:2]
print(a)

# arr[::] 처음부터 끝까지 모든행.
a = arr[::-1] # 역순으로 마지막행부터 출력
print(a) # 행의 순서를 뒤바꿈.
#%%
# 불린 인덱싱(or 불 인덱싱) (정수 기반이 아님.)
import numpy as np
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
a = np.array(lst)
# 배열 a 에 대해 짝수면 True, 홀수면 False
bool_indexing = (a % 2 == 0)
print(bool_indexing)
print(a[a%2==0]) # True 결과값만 출력.

# 출력: 부울린 인덱싱 배열
# [[False True False]
# [ True False True]
# [False True False]]
# 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
print(a[bool_indexing]) 
print(a[a%2==0])

bool_indexing = (a > 5)
print(bool_indexing)
print(a[bool_indexing])

a[a > 5]
# 행의 불린 인덱싱 True / False
a[a[:,2] > 5] # 모든행의 2열 요소 중에 (any) 5보다 큰 행들이 있으면 True

a[a[:,2] < 5]  # 모든행의 2열 요소 중에 5보다 작은 행들이 있으면 True

a[(a[:,2] > 2) & (a[:,2] < 7)] # 각행의 2열 요소가 2보다 크고 7보다 작은 행들

#%%
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

arr=np.random.normal(2.0,1.0,(2,3)) # (2,3) >>> 2행 3열 행렬로 reshape
print(arr)
np.sort(arr) # 오름차순정렬 행마다 
np.sort(arr)[::-1] # 행자체를 요소로 보고 역정렬함. 즉, 행 역정렬
np.sort(arr)
# 1차 배열로 바꾸고
arr=arr.flatten() # 1자로 핀후(1차 배열로 펼침)
arr
arr = np.sort(arr)[::-1]  # 역정렬(2차일땐 뒤집는 역할)(or 내림 정렬(1차일땐 내림정렬))
# 2차 배열로 reshape
arr.reshape(2,3)
#%% up-version

arr=np.random.normal(2.0,1.0,(2,4)) # (2,3) >>> 2행 3열 행렬로 reshape
print(arr)
np.sort(arr) # 오름차순정렬 행마다 
np.sort(arr)[::-1] # 행자체를 요소로 보고 역정렬함. 즉, 행 역정렬
np.sort(arr)
# 1차 배열로 바꾸고
arr=arr.flatten() # 1자로 핀후(1차 배열로 펼침)
arr
arr = np.sort(arr)[::-1]  # 역정렬(2차일땐 뒤집는 역할)(or 내림 정렬(1일땐 내림정렬))
# 2차 배열로 reshape
arr.reshape(2,4)
#상위 5% 인덱스 요소
arr[int(0.05 * len(arr))]
#상위 10% 인덱스 요소
arr[int(0.2 * len(arr))]
#상위 20% 내의 인덱스 요소
bool_indexing = arr >= arr[int(0.2*len(arr))]
print(bool_indexing)
print(arr[bool_indexing])
#%%
# 문자열
# 고객명
names = np.array(["Charles", "Kilho", "Hayoung", "Charles", "Hayoung", "Kilho", "Kilho"])

a=names[names == "Charles"]
print(a)
a=names[(names == "Charles") | (names == "Kilho")]
print(a)

# 해당 고객의 상세 데이터
data = np.array(
[[ 0.57587275, -2.84040808, 0.70568712, -0.1836896 ],
 [-0.59389702, -1.35370379, 2.28127544,  0.03784684],
 [-0.28854954,  0.8904534 , 0.18153112,  0.95281901],
 [ 0.75912188, -1.88118767,-2.37445741, -0.5908499 ],
 [ 1.7403012 ,  1.33138843, 1.20897442, -0.58004389],
 [ 1.11585923,  1.02466538,-0.74409379, -1.55236176],
 [-0.45921447,  2.53114818, 0.5029578 , -0.24088216]])
# names 배열의"Charles" index [0,3]을 구함
data[names == "Charles", :]  # 고객과 상세 데이터 간의 결합.
#>>> data[[0,3],:]처럼 바뀌게 됨. 
# 0행, 3행/ 모든 열.

data[(names == "Charles") | (names == "Kilho"),:]
# >>> data[[0,1,3,5,6],:]처럼 바뀌게 됨.
# 0행, 1행,3행,5행, 6행/ 모든 열.



