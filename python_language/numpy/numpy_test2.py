# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:40:59 2019

@author: sundooedu
"""
#%% numpy 함수
import numpy as np
a=[[1,2.74,-3],
   [4,np.nan,6.45]]

arr=np.array(a)

np.abs(arr) # 절대값.
np.abs(arr[0][2])

np.square(arr) # 제곱
np.sqrt(arr) # 루트
np.exp(arr) # e(오일러 상수)의 지수함수
np.log(arr) # 밑이 e인 로그함수/ 0을 집어넣으면 "-"무한대가 됨.
np.log10(arr) # 밑이 10인 로그함수

np.ceil(arr) # 소수점 0자리에서 올림
np.floor(arr) # 소수점 0자리에서 내림
np.around(arr,1) # 소수점 첫째자리에서 0.5 이상이면 올림, 미만이면 내림

np.isnan(arr) # 1행 1열 요소만 True 떨어짐
np.isinf(np.log10(0)) # 무한대면 True, 아니면 False를 각 요소별로 반환

# degree 를  radian 으로 변환 : degree * np.pi/180 
np.deg2rad(180) # degree를 radian으로 변환해주는 함수
np.rad2deg(1) # radian을 degree로 바꿔주는 함수
# numpy는 radian을 씀.
np.sin(np.pi/2) # sin(x) 함수
np.cos(np.pi) # cos(x) 함수
#%%
a=[[1,2.74,-3], 
   [4,np.nan,6.45]]
arr=np.array(a)

arr[np.isnan(arr)]=0 #np.nan >>> 0으로 바꿈.
arr
#%%
# 집계 함수.

arr = np.arange(1,5)
np.sum(arr)

np.cumsum(arr) #array([ 1,  3,  6, 10], dtype=int32) 각 성분까지의 구분 누적합을 보여줌.
               # [1, 1+2, 1+2+3, 1+2+3+4]
np.cumprod(arr) # array([ 1,  2,  6, 24], dtype=int32) 각 성분까지의 누적곱을 보여줌.

np.mean(arr) # 평균을 구함
np.var(arr) # 분산을 구함
np.std(arr) # 표준편차를 구함
#%%
a=[[1,2,-3], 
   [4,np.nan,6]]
# numpy 배열은 모든 요소의 자료형이 동일해야됨.
arr=np.array(a) 
np.sum(arr) # np.nan 제외
arr[np.isnan(arr)]=np.mean(arr)
# np.nan, np.inf(이사값, 이상치, 불측치(숫자로 관측이 안됨)) 제외, 요서를 0값으로 정제.                
arr[np.isnan(arr)]=0
#arr[np.isinf(arr)]=0
arr[np.isnan(arr)]=np.mean(arr[np.isnan(arr)==False]) 
arr                        # isnan(arr)이 True이므로 이것을 False로 바꾸어 isnan(arr)이 True인것을 제외하여 평균을구함.
# axis=0 >>> 행방향 / axis=1 >>> 열방향
np.sum(arr, axis=0) # 행방향 >>> 행에 수직 벡터가 바로 방향
np.sum(arr, axis=1) # 열방향 >>> 열에 수직 벡터가 바로 방향
np.max(arr, axis=0)
arr=np.array([1,1,2,2])
e=np.eye(3)
np.unique(e) # 중복된 값을 제거하고 종류를 리턴.
#%%
# 2차 배열 >>> 1차원배열 / 차원 축소
arr2=arr.reshape(2,2) # 2차원 배열
arr2.reshape(4) # 1차원 배열
arr2.reshape(arr.size)
arr2.flatten() # 인자가 필요없이 1차원 배열로 바꿀 수 있음.
arr2.ravel()
#%%
# 배열명. 함수 호출
# 통계나 정렬 함수배열명. 함수 호출
arr.sum()
arr.sort()
arr










 
