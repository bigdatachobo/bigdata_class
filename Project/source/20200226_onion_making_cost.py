# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:33:08 2020

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np
import os

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')

df_local = pd.read_excel('../data/climate_in_a_row.xls')

# 년도_지역 Series
year_local = df_local.loc[16:,'year_local']
year_local = pd.DataFrame(year_local)
year_local.reset_index(inplace=True)
year_local.drop(['index'], axis=1,inplace=True)

df_etc = pd.read_excel('../data/양파_생산비_1991_2019.xlsx')

df_T = df_etc.T
df_T_res = df_T.reset_index()
df_10a = df_T_res.loc[df_T_res.index %2 ==1,:]
df_10a = df_10a.reset_index()
df_10a = df_10a.drop(['level_0'], axis=1)

column = df_T.loc['생산비항목별',:]
col_list=['year']
for col in column.values:
    col_list.append(col)
    
df_10a.columns=col_list    
df_10a.drop(['생산비항목별'],axis=1,inplace=True)

df = pd.DataFrame()
for i in df_10a.index:
    temp=df_10a.iloc[i,:]
    df_temp=pd.DataFrame(temp).T
    for j in range(16):
        df=pd.concat([df,df_temp], axis=0)
        
df.reset_index(inplace=True)        
df.drop(['index'], axis=1, inplace=True)
df['year']=year_local['year_local']
df.replace('-',0,inplace=True)

df.to_excel('../data/onion_making_cost.xls', index=False)
