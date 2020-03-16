# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:35:43 2019

@author: sundooedu
"""

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#파일을 파이썬 변수에 읽음 
credit = pd.read_csv('credit_card_data.csv',encoding='utf-8')
credit.head()
#연령대별 월카드이용 총금액
credit.groupby(by="ages")['monthly_card_spend'].sum()
credit.groupby(by="ages")['monthly_card_spend'].mean()
#지역별 월카드이용 총금액

res=credit.groupby(by="city",group_keys=True)["monthly_card_spend"].sum()
#지역별 월카드이용금액의 다중 집계
res2=credit.groupby(by="city")["monthly_card_spend"].agg(['sum','count','max','mean','min'])
#지역별 월카드이용금액의 다중 집계결과에 내림정렬 적용
res3 = res2.sort_values(by="sum",ascending=False)

#월카드이용 최대금액
res.max()
res[res==res.max()].index[0]

#지역별,월별 카드결제 총금액 
crd1=pd.pivot_table(credit,index=["city"],columns=["month"],values="credit_card_payment",aggfunc="sum")
crd1=pd.pivot_table(credit,index=["city","month"],values="credit_card_payment",aggfunc="sum")

#20대의 총대출 금액
#1.연령대별 카드 대출 금액
crd1=pd.pivot_table(credit,index=["ages"],values="monthly_loan",aggfunc=np.sum)
#2.행과 열 인덱싱
crd1.loc["20대"]["monthly_loan"]
crd1.iloc[1][0]

crd1=credit[credit["ages"]=="20대"]["monthly_loan"] # "20대"인 행들과 "monthly_loan"열의 교집합
crd1=credit.query("ages=='20대'")["monthly_loan"]
crd1.sum()

crd2=credit.query("ages=='30대'")["monthly_loan"]
crd2.sum()
# 20대와 30대 대출 금액 행병합
crd20=credit[credit["ages"]=="20대"].loc[:,["ages","monthly_loan"]]
crd30=credit[credit["ages"]=="30대"].loc[:,["ages","monthly_loan"]]
res=pd.concat([crd20,crd30],ignore_index=True) # row bind(행방향) >>> axis=0
res["ages"].value_counts()
# 20대와 30대 대출 금액을 파일 저장
res.to_csv("data2030.csv",encoding='utf-8',index=False)
del res
res=pd.read_csv('data2030.csv')

#%% matplotlib quiz
# <내풀이>
# 20대 카드 월별 결제 금액 바플롯 표현
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
crd20=credit[credit["ages"]=="20대"].loc[:,["ages","month","monthly_card_spend"]]
month_crd20=crd20.groupby("month")["monthly_card_spend"].mean()
plt.figure(figsize=(10,7))
plt.title('20대 카드 월별 평균 결제 금액',fontsize=15)
plt.xlabel('월',fontsize=16)
plt.ylabel('평균 카드 사용량',fontsize=16)

plt.bar(month_crd20.index,month_crd20)
#%% 선생님 풀이 (아래 전부) / 바로 밑만 제외
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
# 20대 월별 카드 이용 금액의 그래프
crd2 = pd.pivot_table(credit,index=["ages","month"],values="credit_card_payment")
crd2.loc["20대"]

# 바 플롯
plt.figure(figsize=(10,6))
plt.bar(crd2.loc["20대"].index,crd2.loc["20대"]['credit_card_payment'])
plt.title("20대 월 카드 이용 금액")
plt.xlabel("월")
plt.ylabel("금액")

# Seaborn 사용하여 그래프 작성
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# bar-plot
plt.figure(figsize=(10,7))
#sns.barplot(x=crd2.loc["20대"].index,y='credit_card_payment',data=crd2.loc["20대"]) 
sns.barplot(crd2.loc["20대"].index,crd2.loc["20대"]['credit_card_payment']) # 결과는 위와 동일
plt.title("20대 월 카드 이용 금액")
plt.xlabel("월")
plt.ylabel("금액")

# line-plot
plt.figure(figsize=(10,7))
plt.plot(crd2.loc["20대"].index, crd2.loc["20대"]['credit_card_payment'],'rs--',lw=5,ms=20,mfc="b",mec="y",mew=5)
plt.title("20대 월 카드 이용 금액")
plt.xlabel("월")
plt.ylabel("금액")




