# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:25:53 2019

@author: sundooedu
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xdata=[i for i in range(10,50,10)]
ydata=[i for i in range(1,5,1)]

# 한글 폰트 설정
plt.rc('font',family='Malgun Gothic')

# 제목
plt.title('라인플롯')
plt.xlabel('x축레이블(흡연량)')
plt.ylabel('y축레이블(사망)')

# 바둑판
plt.grid(True)

# line-plot 그리기
plt.plot(xdata,ydata)

# figure 설정/ figure >>> plot 배경 도화지
# 다중 플롯[Axes] (Axis: 축 / Ax: 단일 plot / Axes: 다중 plot) 표현 가능
# figure는 Axes를 Sub-Plot으로 인지
plt.figure(figsize=(10,5))

# 함수로 하나로 묶기
def show_plot(xdata,ydata):
    plt.title('라인플롯')
    plt.xlabel('x축레이블(흡연량)')
    plt.ylabel('y축레이블(사망)')
    plt.xlim(10,100) # X축  구간 범위 제한
    plt.grid(True)
    plt.plot(xdata,ydata,label='흡연범주')
    plt.legend(loc=1) # 반시계 방향 / 수학 사분면과 같다.
    #plt.legend(['흡연범주']) # 범례 / 범주를 그릴때.
                # [ ] 로 둘러싸야 글자 전체가 나오게된다.   
help(plt.legend)                
# 함수 호출
show_plot(xdata,ydata)
#%%
import numpy as np
plt.plot(np.random.randn(30), color="m", marker='.', linestyle=":")

# figure 설정/ figure >>> plot 배경 도화지
plt.figure(figsize=(10,10))

# marker 속성(색(mec/marker edge color), 두께(mew/marker edge width), 스타일(ms/marker style))
plt.plot(np.random.randn(30), color="r", marker='D', ls="-",lw=1,ms=10,mec='g',mew=1,mfc='y') # lw = 선 두께
plt.legend(['흡연범주']) # 범례 / 범주를 그릴때./ plot 다음에 위치시켜야 범주 생성됨.     
           # [ ] 로 둘러싸야 글자 전체가 나오게된다.   
help(plt.plot)

#%%
# 0~5 균등하게 5개 수를 가지는 등차수열
x1=np.linspace(0,5,5)
# 0~360도 균등하게 360개 수를 가지는 등차수열
x2=np.linspace(0,360,360)

y1=x1*2
#y2=np.cos(2*np.pi*x2)
#y2=np.cos(np.deg2rad(x2)) # np.deg2rad(): 180도 단위를 라디안 값으로 바꾸는 함수
y2=np.sin(np.deg2rad(x2))

plt.subplot(2,1,1)
plt.title('첫번째 서브플롯')
plt.plot(x1, y1, ls='--',marker='8')

plt.subplot(2,1,2)
plt.title('두번째 서브플롯')
plt.plot(x2, y2, ls='-')

plt.tight_layout()
#%% 4분면에 직선, sin, cos, tan 그려보기
plt.figure(figsize=(7,7))
x1=np.linspace(0,5,5)
# 0~360도 균등하게 360개 수를 가지는 등차수열
x2=np.linspace(0,360,360)

y1=x1*2
#y2=np.cos(2*np.pi*x2)
#y2=np.cos(np.deg2rad(x2)) # np.deg2rad(): 180도 단위를 라디안 값으로 바꾸는 함수
y2=np.sin(np.deg2rad(x2))
y3=np.cos(np.deg2rad(x2))
y4=np.tan(np.deg2rad(x2))

plt.subplot(2,2,1)
plt.title('직선 서브플롯')
plt.plot(x1, y1, ls='--',marker='8')

plt.subplot(2,2,2)
plt.title('sin(x) 서브플롯')
plt.plot(x2, y2, ls='-')

plt.subplot(2,2,3)
plt.title('cos(x) 서브플롯')
plt.plot(x2, y3, ls='-')

plt.subplot(2,2,4)
plt.title('tan(x) 서브플롯')
plt.plot(x2, y4, ls='-')

plt.tight_layout()
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
plt.figure(figsize=(5,5))
#x=np.linspace(0,5,5)
#x=np.random.randint(0,5,4)
x=[2,3,4,5,1]
y=np.arange(len(x))
plt.title('바-플롯')
plt.xlabel('X-위치')
plt.ylabel('X-크기')
plt.gca().invert_yaxis() # y-축 뒤집기 / 역 y축/ y축 내림정렬
#plt.yticks(sorted(y,reverse=True))
plt.bar(x,y)
np.arange(5)
help(plt.gca())
#%%
# 파이-형태 그래프
plt.figure(figsize=(5,5))
label=['백인','황인','흑인'] # 인종
rate=[30,40,30] # 크기 백분률
color=['red','green','blue']
plt.pie(rate,labels=label,colors=color,autopct='%.1f%%') # autopct : auto- -> 백분율 비율 표시
#%%
# x=np.random.normal(100) >>> (평균, 표준편차, 크기)도 같이 줘야 100개가 샘플링됨. 설정 안하면 값이 1개만 리턴됨.

# 값을 100개 얻기 위해서는 평균 혹은 표준편차 변경
x=np.random.normal(0,1,size=100) # 샘플 100개
# 값을 100개 얻기 위해서는 평균 혹은 표준편차 지정
y=np.random.normal(0,1,size=100)

# 값 100개를 얻은 후에 pd.Series로 변환.
y= pd.Series(np.random.normal(0, 1, size=100))

plt.scatter(x,y,marker='.')












