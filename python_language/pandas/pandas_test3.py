# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:27:51 2019

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np

credit = pd.read_csv('data/credit_card_data.csv',encoding='utf-8',sep=',')
credit.head()

age_month_sum = credit.groupby(by="ages")['monthly_card_spend'].sum()
age_month_mean = credit.groupby(by="ages")['monthly_card_spend'].mean()

city_month_sum = credit.groupby("city")['monthly_card_spend'].sum()
format(city_month_sum.max(),',') # 1000 단위마다 ',' 붙여준다.

city_month_mean = credit.groupby("city")['monthly_card_spend'].mean()

# 지역별 월카드의 다중 집계
city_month_agg = credit.groupby("city")['monthly_card_spend'].agg(['sum','count','max','mean','min'])
# 지역별 월카드 이용금액의 다중 집계결과에 내림정렬 적용
city_month_agg.sort_values(by="sum",ascending=False)

# 월카드이용 최대금액

#지역별, 월별카드결제 총금액
crd1 = pd.pivot_table(credit,index='city',columns='month',values='credit_card_payment',aggfunc='sum')
crd2 = pd.pivot_table(credit,index=['city','month'],values='credit_card_payment',aggfunc='sum')

# 20대의 총대출 금액
# 1. 연령대별 카드 대출 금액
crd3 = pd.pivot_table(credit,index="ages",values='monthly_loan',aggfunc=np.sum)
# 2. 행과 열 인덱싱
format(crd3.loc["20대"]['monthly_loan'],',') # 1000단위마다 ',' 붙임.
# 3. 인덱싱 기반 표시
tw=credit[credit["ages"]=="20대"]['monthly_loan']
tw.sum()
#4. query 기반 표시
credit.query("ages=='20대'")['monthly_loan'].sum()

# 20대와 30대 대출 금액 행병합 through (concat)
crd20=credit[credit["ages"]=="20대"].loc[:,["ages","monthly_loan"]]
crd30=credit[credit["ages"]=="30대"].loc[:,["ages","monthly_loan"]]
res=pd.concat([crd20,crd30],ignore_index=True) # row bind(행방향) axis=0
res["ages"].value_counts()

# 20대 30대 대출 금액 파일 저장
res.to_csv("data/data2030.csv",encoding='utf-8',index=False)
del res # Ram에서 삭제
res = pd.read_csv('data/data2030.csv')
#%%





