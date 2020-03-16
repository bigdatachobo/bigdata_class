# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:09:57 2019

@author: sundooedu
"""
'''
statsmodels 패키지 기반 회귀 분석

검정 및 추정 (test and estimation) 회귀 분석 (regression analysis)
시계열 분석 (time-series analysis) 등의 기능을 제공하는 파이썬 패키지다. 

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats, polyval

#data.csv
'''
   3.52 , 2.48
   2.58 , 2.27
   3.31 , 2.47
   4.07 , 2.77
   4.62 , 2.98
   3.98 , 3.05
   4.29 , 3.18
   4.83 , 3.46
   3.71 , 3.03
   4.61 , 3.25
   3.90 , 2.67
   3.20 , 2.53
'''

x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
data = pd.DataFrame({"a":x,"c":y})

data.head()

'''
model변수는 smf의 ols(최소제곱법)을 사용하여 회귀모형을 만든다. 각각의 오차(=잔차)들의 제곱을 합계한 다음 이를 minimize하는 beta를 찾는 것입니다. 즉, 오차제곱합(sum of squared error)을 최소로 하는기울기를 구하는 방법입니다

 Formula = '종속변수~ 독립변수' 형식에 맞춰 분석하고자 하는 종속변수(왼쪽)와 독립변수(오른쪽)를 넣으면된다. data에는 사용하고자하는 데이터를 넣어주면 된다. fit은 모형을 적합시킨다. 
 ~ 연산자가 왼편에 종속변수와 오른편에 설명변수를 구별한다. 
'''
#ordinary least squares(최소제곱법)
model = smf.ols(formula = 'c ~ a', data = data)
result = model.fit()
result.summary()

#예측
result.params
result.predict(exog=dict(a=3.52)) # 2.664105


'''
다중회귀분석

하나의 수치형 종속변수와 2개이상의 수치형 독립변수 사이의 영향 또는 인과관계를 설명하는 분석을 말한다
다중회귀분석에서 formula는 '종속변수 ~ 독립변수1 + 독립변수2 + 독립변수3'과 같이 형식에 맞춰 분석하고자 하는 종속변수(왼쪽)와 독립변수(오른쪽)를 넣으면 된다. 다중회귀분석에 대한 실행결과는 위와 같다.
'''
x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
x2 = [4.52, 2.58, 3.31, 4.05, 4.62, 3.58, 4.29, 4.63, 3.71, 4.61, 3.80, 3.20]
y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
data = pd.DataFrame({"a":x,"b":x2,"c":y})
model = smf.ols(formula = 'c ~ a + b', data = data)
result = model.fit()
result.summary()
#예측
result.params
result.predict(exog=dict(a=3.52,b=4.52))#2.453877
#%%
'''
로지스틱 회귀
규칙을 선형회귀모델 규칙을 제대로 표현 못하는 경우 사용한다
예로 조건에 따른 특정사건이 일어날 확률 맞추기

※ 수학적 정리
설명변수 x를 알때 종속변수=0일확률이 P(종속변수=0|설명변수)이고
종속변수=1일확률 P(종속변수=1|설명변수)라면 오즈비는 다음과 같다.


odds=p/(1-p)
예로 콜레스 정상인경우 비만일확률/(1-비만일확률) =0.11 가정하면  비만일확률이 비만아닐확률보다 0.11배 높다

logit(p)=ln(odds)=w^(wTx+b) :종속변수값이 -무한대에서 +무한대 이것을 logit

종속변수 y 가 0또는 1인 분류 예측 문제를 풀 때는 x  값에 따라 μ(x) 
를 예측한 후 다음 기준에 따라 y를 예측한다.

독립(설명)변수가 어떤 범위를 넘어서면 종속변수가 0에서 1의 상태로 변환
 
y^ ={1  if μ(x)≥0.5 
     0   if μ(x)<0.5  

-로지스틱 함수(Logistic Function) 
logitstic(종속변수=1일확률)=σ(z)=1/1+exp(z) 
logitstic(종속변수=0일확률)=σ(z)=1- 1/1+exp(z) 

-하이퍼볼릭 탄젠트 함수(Hyperbolic tangent) 등 

'''
import pandas as pd
#점수
score = [56, 60, 61, 67, 69, 55, 70, 44, 51, 64, 60, 50, 68, 72, 90, 93, 85, 74, 81, 88, 92, 97, 77, 78, 98]
#합격여부
# 0 불합격
# 1 합격
_pass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

result = pd.DataFrame(
    {"score": score, "_pass": _pass}
)

logis = sm.Logit.from_formula('_pass  ~ score', data=result).fit()
logis.summary()

#예측
logis.params
logis.predict(exog=dict(score=61))#  0.002305
logis.predict(exog=dict(score=85))#0.99997

#plt.scatter(x,y) 점그래프 x,y 좌표에 점 그린다
plt.scatter(score,  _pass, label="y", marker='o', s=100)
# logis.predict(score) 예측값
plt.scatter(score, logis.predict(score),  marker='x',
            s=200, alpha=0.5)
plt.xlim(0, 100)

#시그모이드 lw =굵기
#50점대에서 _pass에서 1이 일부분포 해서 50점이하대에서 
#선높이가 높음 
#X값이  70점대의 어떤 값일때 y 값이 0.5가 넘기 시작하는 것처럼 보이다.
xx = np.linspace(0, 100, 25)
mu = logis.predict(sm.add_constant(xx))
plt.plot(xx, mu, lw=5, alpha=0.5)

plt.xlabel("x")
plt.ylabel("y")
