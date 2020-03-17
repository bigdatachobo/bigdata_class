# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:46:58 2020

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np

# 데이터 불러오기
soil = pd.read_csv('../data/토양정보.csv')
proportion = pd.read_csv('../data/논밭비율.csv')

# 필요없는 컬럼 제거
soil.drop(['Unnamed: 0','년도'], axis=1, inplace=True)
proportion.drop(['Unnamed: 0','년도'], axis=1, inplace=True)

# 필요없는 행 제거
proportion.drop(index=proportion[proportion['시도']=='계'].index, axis=0,inplace=True)
proportion.reset_index(inplace=True)
proportion.drop(['index'], axis=1, inplace=True)

soil.drop(index=soil[soil['화학성']=='벤조(a)피렌'].index, axis=0, inplace=True)
soil.reset_index(inplace=True)
soil.drop(['index'], axis=1, inplace=True)

# 결측치 바꾸기
soil.replace('-',0,inplace=True)

# soil 컬럼 이름 변경
soil.rename(columns={'년도':'year'},inplace=True)

#데이터 프레임 합치기
def two_mean(df):
    num=(float(df['논'])*(x)+float(df['밭'])*(y))/2
    return num
    
df=pd.DataFrame()
for i,sido in enumerate(proportion.year_sido):
    x=float(proportion.loc[i,'논비율']) #논비율
    y=float(proportion.loc[i,'밭비율']) #밭비율
    for j in soil.year.unique():
        df_temp=soil.loc[soil['year']==j, :]
        df_temp['value']=df_temp.apply(two_mean,axis=1)
           
    df_tmp=pd.DataFrame(df_temp['value'].values.reshape(1,-1),
                        columns=df_temp['화학성'],
                        index=[sido])
    df=pd.concat([df,df_tmp], axis=0)

df.to_csv('../data/soil_proportion.csv')
