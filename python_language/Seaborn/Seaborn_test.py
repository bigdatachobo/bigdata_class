# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:56:22 2019

@author: sundooedu
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
import seaborn as sns
#%%
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
    
matplotlib.rcParams['axes.unicode_minus'] = False   
#그래프에서 마이너스 기호가 표시되도록 하는 설정입니다. 
#%%

iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")    # 여객운송 데이터
#%%
# Seaborn을 이용한 그래프 그리기
sns.countplot(x="day", data=tips)
plt.title("요일별 팁을 준 횟수")
plt.show()

# Boxplot
sns.boxplot(x="day", y='total_bill',data=tips) # y축 <총-청구 금액>
plt.title("요일별 전체팁 boxplot")

sns.boxplot(x="day", y='total_bill',hue='smoker',data=tips) # y축 <총-청구 금액>
plt.title("요일별 전체팁 boxplot")

# Barplot
# 데이터가 2차원이고 실수값, 카테고리(범주) 값이 섞여 있는 경우
# x 자료의 이산적(범주형) 분포
# y 자료의 연속적(숫자) 분포
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("요일 별, 전체 팁")
plt.show()
# 편차 >>> 에러바로 표시
# 평균 >>> 바-높이

plt.figure(figsize=(7,6))
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
plt.title("요일 별, 성별 전체 팁의 Histogram")
plt.show()

# scatter-plot
# 데이터가 2차원이고 모두 연속적인 실수값이면 >>> 스캐터 플롯
sns.jointplot(x='day',y='total_bill',data=tips)
sns.jointplot(x='total_bill',y='day',data=tips)
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
plt.suptitle("꽃받침의 길이와 넓이의 Joint Plot", y=1.02)
plt.show()

# distplot (분포plot)
x = iris.petal_length.values
sns.distplot(x, kde=True, rug=True)
plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Distribution Plot")
plt.show()

#x=tips['tip'] # 기본이 열 일때 df[[C1,C2]][R1:R2]
#x=tips.loc[:,'tip'] # 기본이 행일때 df.loc[행1:행2,열1:열2]
x=tips.tip # 시리즈
x=tips.tip.values # 넘파이 1차 배열
x=tips.tip.values.tolist() # 1차 리스트
sns.distplot(x,kde=True, rug=True, hist=True) # x자리에 1d-array만 들어갈 수 있음.
plt.title("tips 데이터 중, tip에 대한 Distribution Plot")
plt.show()
#%%
# lmplot: 스캐터 + 선형회귀 분석이 표현(열간의 상관관계를 확인)
# 흡연 여부에 상관, 비흡연자가 흡연자에 비해서 팁을 더주는 분포
plt.figure(figsize=(9,9))
sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips)

plt.figure(figsize=(9,9))
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, markers=['o','x'])

# 성별(남 / 녀), 시간별(점심 / 저녁)로 나누어서 표현
sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips,row='sex',col='time')
#%%
sns.countplot(x="class",hue='sex', data=titanic)
plt.title("타이타닉호의 각 클래스별,성별, 승객 수")
plt.show()
#%%
# heatmap()
titanic_size = titanic.pivot_table(index="class", columns="sex", aggfunc="size")
sns.heatmap(titanic_size, annot=True,fmt='d') # cmap=sns.light_palette("gray", as_cmap=True)
plt.title("Heatmap")
plt.show()
#%%
# pclass별 개수 파이플롯으로 표현
# value 기준으로 정렬하면 인덱스 순서 재배치
titanic = sns.load_dataset("titanic")
pclass = titanic['pclass'].value_counts(sort=False) # value_counts 내부적으로 정렬을 사용하므로 sort=False를 준다.
pclass2 = titanic.groupby('pclass').size()
plt.pie(pclass2,labels=pclass.index, autopct='%0.1f%%',shadow=True,explode=(0.1,0))
#%%
# pclass 별 개수
# 플롯, 수치로 표현
titanic.isnull().sum()
# NA 행삭제시 많은 행이 삭제되므로 이 방법은 곤란함
#titanic.dropna(how='any')

#deck열(NA 비율이 높다.) 삭제
titanic.drop('deck',axis=1,inplace=True) # axis=1 >>> 열방향

# seaborn 사용하지 않았을때.
pclass = titanic['pclass'].value_counts(sort=False)
plt.bar(pclass.index,pclass) # x=pclass.index, y=pclass

# seaborn으로 한줄로 끝낼 수 있다./ plt.bar 방식으로 두줄로 해야함.
sns.countplot(x='pclass',data=titanic) # 'pclass' >>> 열을 가리킴.

pclass2 = titanic.groupby('pclass').size()
sns.barplot(pclass2.index,pclass2) 

sns.countplot(x='class',data=titanic)
#%%
# 성별 승객수
t_sex = titanic['sex'].value_counts()
plt.pie(t_sex,labels=t_sex.index,autopct='%0.f%%',explode=(0.1,0.1)) # explode: 간격
help(plt.pie)

# 남/여 사망자 수
# 남성 사망자 수
# 내풀이
man_alived=titanic[(titanic['alive']=='no')&(titanic['sex']=='male')]
man_die = man_alived['alive'].value_counts()

# 선생님 풀이
n=len(titanic.loc[(titanic['sex']=='male')&(titanic['survived']==0)])
man=titanic[titanic['sex']=='male']
m=len(man)
man_alive=m*(1-n/m)
man_death_rate=round((n/m)*100,2)

# 여성 사망자 수
nw=len(titanic.loc[(titanic['sex']=='female')&(titanic['survived']==0)])
woman=titanic[titanic['sex']=='female']
w=len(woman)
woman_alive=w*(1-nw/w)
woman_death_rate=round((nw/w)*100,2)

#%%
# 성별 생존, 사망자수를 알 수 있다.
import pandas as pd
array = pd.crosstab(titanic['sex'],titanic['survived'])
# 성별 생존, 사망자수 countplot
sns.countplot(x='sex', hue='survived',data=titanic)
#%%
# 등급별 생존, 사망자수 플롯
sns.countplot(x="pclass", hue='survived', data=titanic)
# 등급별 나이 플롯
sns.boxplot(x='pclass',y='age',data=titanic)
# 나이에 따른 요금 추이
plt.figure(figsize=(20,6))
sns.pointplot(x='age',y='fare',data=titanic)
# 나이와 요금에 따른 생존여부
# 1. point-plot
plt.figure(figsize=(20,6))
sns.pointplot(x='age',y='fare',hue='alive',data=titanic)
# 2. bar-plot
plt.figure(figsize=(20,6))
sns.barplot(x='age',y='fare',hue='alive',data=titanic)

# quiz
# 클래스별 성별 구분 승객수(pivot-table 기반)

# 자료형이 Series 임
s = titanic.groupby(['pclass','sex']).size()

# Series를 DataFrame으로 변환하는 방법.
titanic_size = pd.DataFrame(s.values, index=s.index) 

# 피봇테이블 히트맵 (데이터프레임을 인자로 지정)
titanic_size=titanic.pivot_table(index='class',columns='sex',values='fare',aggfunc='size')
sns.heatmap(titanic_size, annot=True,fmt='d')









