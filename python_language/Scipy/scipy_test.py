# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:30:24 2019

@author: sundooedu
"""

#%%
# install  scipy statsmodels   scikit-learn(미리 설치되어 있음)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, polyval # 과학적인 계산 분석 라이브러리

# 식료품 물가상승률 (요소 개수 12) 
x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
# 엥겔지수
y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
# 선형회귀분석(linear regression analysis)함수
model = stats.linregress(x,y)
model
'''
# 회귀식 y = 0.5x+0.9
# 상관성(r-value), 유의성(p-value), 정밀성(stderr=표준오차) 좋다.
# =============================================================================
# <model의 결과값>
# LinregressResult(slope=0.4956032360182905, 
#                  intercept=0.9195814280689418, 
#                  rvalue=0.8929235125385305,    # 0.6 이상이므로 상관성 높다.
#                  pvalue=9.238421943157891e-05, # 0.05 이하이므로 귀무가설 기각! 상관성 높다.
#                  stderr=0.07901935226531728)   # 표준오차.
# =============================================================================
'''
predict = np.poly1d([model.slope, model.intercept])
predict(2.58)  # 2.58일때 "2.198237776996131"로 값이 유사.
ry = polyval([model.slope, model.intercept],x)
ry
#%%
#다음 두줄 묶어서 실행 
#실값들이 선형적 산점도로 나타남 
plt.scatter(x,y,color='red')
#예측값들이 선형적 산점도로 나타남 
plt.scatter(x,ry,color='green')
plt.legend(['original', 'regression'])
#예측값들이 red색 점과 함께 선형적으로 라인으로 나타남 
plt.plot(x, ry, 'ro-')
plt.title('Regression result')

df = pd.DataFrame({ 'x':x,'y':y, 'ry': ry }) 

import seaborn as sns
sns.lmplot(x='x', y='y',data=df) # 실분포
sns.lmplot(x='x', y='ry',data=df) # 식으로 모아서 그래프를 그림.

