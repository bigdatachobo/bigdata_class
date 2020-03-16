# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:12:04 2019

@author: sundooedu
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 균일분표 따르는 0 ~ 1 사이 난수
np.random.rand(10)

# 가우시안 정규분포 따르는 난수
np.random.randn(10)
np.random.randn(5,2) # (5행, 2열) array로 행렬 표현

# 정수 난수
np.random.randint(1,10,size=10) # size : 갯수

# cumsum() : 누적합
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
plt.Line2D
# 열마다 선이 그려진다.
df = pd.DataFrame(np.random.randn(10, 4).cumsum(axis=0),
                           columns=["A", "B", "C", "D"],
                           index=np.arange(0, 100, 10))
# 선그림 ( 그래프 )
df.plot()

# 선택한 열-만 그래프 그릴때
df['B'].plot(x='A',y='B')
df.plot(x='A',y='B')
df.plot(x='A',y=['B','C'])

# =============================================================================
# plt.plot(df)
# plt.plot([1,2,3,7],[5,6,7,8]) # 기본이 y축-[5,6,7,8] 리스트
# =============================================================================

#%%
# bar plot
s2 = pd.Series(np.random.rand(16), index=list("abcdefghijklmnop"))
# 표현이 다르지만 같다.
s2.plot(kind="bar")
s2.plot.bar()

# 눕혔을때
s2.plot(kind="barh")
s2.plot.barh()

# 열(분석 대상 4개로 유한) 별로 바-플롯을 그린다.
# 열-범주 자동 생성 <<< 난수 분포 함수에 의해 자동 생성. 
df2 = pd.DataFrame(np.random.rand(6, 4), # 6행 4열 난수 분포
index=["one", "two", "three", "four", "five", "six"],
columns=pd.Index(["A", "B", "C", "D"], name="Genus"))

df2.plot(kind="bar") # 세로 그래프
df2.plot(kind="barh") # 가로 그래프

df2.plot(kind="bar",stacked=True) # 세로 단막대 중첩 그래프
df2.plot(kind="barh",stacked=True) # 가로 단막대 중첩 그래프

# plot 산점도
df2.plot.scatter(x='A',y='B',label='GroupAB',color='red')
df2.plot.scatter(x='C',y='D',label='GroupCD',color='green')

# 교재 산점도
x1 = np.random.normal(1, 1, size=(100, 1))
x2 = np.random.normal(-2, 4, size=(100, 1))
X = np.concatenate((x1, x2), axis=1)

df3 = pd.DataFrame(X, columns=["x1", "x2"])
plt.scatter(df3["x1"], df3["x2"])

# 히스토그램
s3 = pd.Series(np.random.normal(0, 1, size=200))
s3.hist(bins=50) # bins 늘릴 수록 더 잘개 쪼개진다.
s3.hist(bins=100,normed=True) # normed = True 시에 더 부드럽게 정규화가 된다.

#%%
# ax >>> 축
# 그래프 중첩.
ax = df2.plot.scatter(x='A',y='B',label='GroupAB',color='red')
df2.plot.scatter(x='C',y='D',label='GroupCD',color='green',ax=ax)


