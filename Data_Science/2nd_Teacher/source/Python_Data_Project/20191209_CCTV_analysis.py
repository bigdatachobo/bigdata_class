# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:59:39 2019

@author: sundooedu
"""
#%%
'''https://github.com/PinkWink/DataScience/blob/master/source_code/01.%20Basic%20of%20Python%2C%20Pandas%20and%20Matplotlib%20%20via%20analysis%20of%20CCTV%20in%20Seoul.ipynb'''
#%%
import pandas as pd
''' <1. Analysis of CCTV in Seoul> '''
CCTV_Seoul=pd.read_csv('../data/01. CCTV_in_Seoul.csv',encoding='utf-8') # ".." 뒤로가기
CCTV_Seoul.head()

CCTV_Seoul.columns
CCTV_Seoul.columns[0]

CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()
#%%
''' <2.엑셀파일 읽기 - 서울시 인구현황> '''
#%%
pop_Seoul = pd.read_excel('../data/01. population_in_Seoul.xls',encoding='utf-8')
pop_Seoul.head()
#%%
pop_Seoul= pd.read_excel('../data/01.population_in_Seoul.xls', # ".." 뒤로가기
                        header=2, # 0 인덱스 기반에서 위에서 3번째부터 읽어 드린다는 의미.
                        parse_cols='B,D,G,J,N',
                        encoding='utf-8')
pop_Seoul.head()
#%%
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'},inplace=True)
pop_Seoul.head()
#%%
''' <3. CCTV 데이터 파악하기> '''
#%%
CCTV_Seoul.head()
CCTV_Seoul.sort_values(by='소계', ascending=True).head(5) # default가 5개.
#%%
CCTV_Seoul['최근증가율']=(CCTV_Seoul['2016년']+CCTV_Seoul['2015년']+CCTV_Seoul['2014년']/CCTV_Seoul['2013년도 이전']*100)
CCTV_Seoul.sort_values(by='최근증가율',ascending=False).head(5)
#%%
'''<4.서울시 인구 데이터 파악하기> '''
#%%
pop_Seoul.head()

pop_Seoul.drop([0], inplace=True) # 행 삭제
pop_Seoul.head()

pop_Seoul['구별'].unique() # 결측치 확인 >>> nan

pop_Seoul[pop_Seoul['구별'].isnull()]

pop_Seoul.drop([26], inplace=True) # 행 삭제
#%%
pop_Seoul['외국인비율']=pop_Seoul['외국인'] / pop_Seoul['인구수']*100
pop_Seoul['고령자비율']=pop_Seoul['고령자'] / pop_Seoul['인구수']*100
pop_Seoul.head()
#%%
pop_Seoul.sort_values(by='인구수',ascending=False).head() # 송파구
#%%
pop_Seoul.sort_values(by='외국인비율',ascending=False).head(5) # 영등포구
#%%
pop_Seoul.sort_values(by='고령자',ascending=False).head() # 강서구
#%%
pop_Seoul.sort_values(by='고령자비율',ascending=False).head() # 강북구
#%%
''' <5.CCTV 데이터와 인구 데이터 합치고 분석하기> '''
#%%
data_result = pd.merge(CCTV_Seoul, pop_Seoul,on='구별') # on >>> 공통 컬럼으로 두 DataFrame을 합친다.
data_result.head()
#%%
''' drop >>> 행- 삭제, 
    del >>> 열- 삭제'''
    
'''필요없는 열을 삭제'''
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

data_result.head()
#%%
data_result.set_index('구별',inplace=True) # "구별"열을 인덱스로 사용
data_result.head()
#%%
''' CCTV 개수와 고령자 비율은 큰 의미가 없음'''
import numpy as np
np.corrcoef(data_result['고령자비율'],data_result['소계'])
'''array([[ 1.        , -0.28078554],
          [-0.28078554,  1.        ]])'''
#%%
''' CCTV 개수와 외국인 비율과는 큰 의미가 없음'''
np.corrcoef(data_result['외국인비율'],data_result['소계'])
'''array([[ 1.        , -0.13607433],
          [-0.13607433,  1.        ]]) '''
#%%
''' 인구수와는 0.3으로 약한 상관관계'''
np.corrcoef(data_result['인구수'],data_result['소계'])
'''array([[1.        , 0.30634228],
          [0.30634228, 1.        ]])'''
#%%
data_result.sort_values(by='소계',ascending=False).head(5) # 강남구 
''' CCTV 많은곳 순위'''
#%%
data_result.sort_values(by='인구수',ascending=False).head(5) # 송파구
#%%
'''6.CCTV와 인구현황 그래프로 분석하기'''
#%%
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
    
plt.rcParams['axes.unicode_minus'] = False   
#그래프에서 마이너스 기호가 표시되도록 하는 설정입니다.
#%%
plt.figure()
data_result['소계'].plot(kind='barh',grid=True, figsize=(10,10))
plt.show()
#%%
''' 정렬
sort_values() >>> default가 내림차순!'''
data_result['소계'].sort_values().plot(kind='barh',grid=True,figsize=(10,10))
plt.show()
#%%
'''인구수 대비 CCTV 개수 비율'''
data_result['CCTV비율']= data_result['소계'] / data_result['인구수']*100
data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
#%%
''' 산점도 '''
plt.figure(figsize=(6,6))

plt.scatter(data_result['인구수'],data_result['소계'],s=50)

plt.xlabel('인구수')
plt.ylabel('CCTV')

plt.grid()

plt.show()
#%%
# polyfit >>> 1차 방정식을 그려주는 함수
fp1 = np.polyfit(data_result['인구수'],data_result['소계'],1) 
# data_result['인구수']와 data_result['소계']의 관계에서
# 기울기, 절편을 구하고 1차원 직선으로 그리겠다.
help(np.polyfit)
fp1
           # 기울기           절편
'''array([1.30916415e-03, 6.45066497e+02])'''
#%%
f1=np.poly1d(fp1)
''' 매개변수로부터 모델 생성 '''
fx=np.linspace(100000,700000,100) 
              # 시작, 끝(포함), 갯수

plt.figure(figsize=(10,10))

plt.scatter(data_result['인구수'], data_result['소계'],s=50)

plt.plot(fx,f1(fx), ls='dashed', lw=3, color='g')  # >>> 기준선이라고 생각하면됨.
plt.xlabel('인구수')
plt.ylabel('CCTV')

plt.grid()

plt.show()
#%%
''' 7. 조금더 설득력 있는 자료 만들기'''
#%%
fp1 = np.polyfit(data_result['인구수'],data_result['소계'],1) 
f1=np.poly1d(fp1)
fx=np.linspace(100000,700000,100) 
''' "오차" 열을 추가함'''
data_result['오차']=np.abs(data_result['소계'] - f1(data_result['인구수']))

df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()
#%%
plt.figure(figsize=(14,10))
# X축, Y축, 점의 색깔(color)과 크기(size)
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'],s=50)
plt.plot(fx,f1(fx), ls='dashed', lw=3, color='g')

for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.987, df_sort.index[n], fontsize=15)
''' 
df_sort['인구수'][n]*1.02 >>> x축 방향으로 위치 조정
df_sort['소계'][n]*0.987 >>> y축 방향으로 위치 조정
'''
plt.xlabel('인구수')
plt.ylabel('인구당비율')

plt.colorbar()
'''
우측에 있는 컬러바를 말한다.
'''

plt.grid()

plt.show()
#%%




