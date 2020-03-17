# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:34:11 2020

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np
import os
# os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')

# 기후 정보
clima=pd.read_csv('../data/adjusted_climate.csv')
# clima.drop(['Unnamed: 0'],axis=1,inplace=True)
na = clima.isna().sum()

# 대기 정보
air_co=pd.read_csv('refined_co.csv',encoding='euc-kr')
air_dust=pd.read_csv('refined_dust.csv',encoding='euc-kr')
air_no2=pd.read_csv('refined_no2.csv',encoding='euc-kr')
air_o3=pd.read_csv('refined_o3.csv',encoding='euc-kr')
air_so2=pd.read_csv('refined_so2.csv',encoding='euc-kr')

# na값이 든 행 제거.
df_list=[air_co, air_dust, air_no2, air_o3, air_so2]
atmo_na=[]
for df in df_list:
    temp=df.isna().sum()
    df.dropna(inplace=True)
    atmo_na.append(temp)

# 대기 DataFrame을 air로 합치기
df_list2=[air_dust, air_no2, air_o3, air_so2]
air=air_co

for df in df_list2:
    air=pd.merge(air,
                 df,
                 on=['year_local','area','year'])

# 토양 정보
soil=pd.read_csv('../data/soil_proportion.csv',encoding='utf-8')
soil.rename(columns={'Unnamed: 0.1':'year_local'}, inplace=True)
soil.drop(['Unnamed: 0'], axis=1, inplace=True)
soil.columns
soil.drop(['시안 CN'], axis=1, inplace=True)
soil.drop(['불소 F'], axis=1, inplace=True)
soil.drop(['유기인'], axis=1, inplace=True)
soil.drop(['유류'], axis=1, inplace=True)
soil.drop(['테트라클로로에틸렌 PCE'], axis=1, inplace=True)
soil.drop(['트리클로로에틸렌 TCE'], axis=1, inplace=True)
soil.drop(['페놀류'], axis=1, inplace=True)
soil.drop(['폴리클로리네이티드비페닐 PCB'], axis=1, inplace=True)

# soil df 컬럼 정렬
soil=pd.concat([soil['year_local'],
                soil['area'],
                soil['year'],
                soil.iloc[:,1:-2]], 
                axis=1)
soil_na = soil.isna().sum()

# 단위 면적당 양파 생산량
onion_unit=pd.read_csv('../data/onion_unit_output.csv',encoding='utf-8')
onion_unit.columns
onion_unit['10a당 생산량 (kg)'].replace('-',np.nan, inplace=True)
onion_unit_na = onion_unit.isna().sum()
onion_unit.dropna(inplace=True)

# 컬럼 합치기
element_list = [clima, air, soil]
element=onion_unit
for elem in element_list:
    element=pd.merge(element,
                     elem,
                     on=['year_local','area','year'])
    
element.to_csv('../data/onion_columns_all_merge.csv', 
               index=False, 
               encoding='utf-8')    

