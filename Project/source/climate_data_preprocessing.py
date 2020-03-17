# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:24:32 2020

@author: sundooedu
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def df_group(data):
    df = pd.read_excel(data)  
    df = df.drop(['조사지역'], axis=1)
    df['지역(시)']= df['지역(시)'].map({'부산':'부산광역시',
                                       '대구':'대구광역시',
                                       '인천':'인천광역시',
                                       '광주':'광주광역시',
                                       '대전':'대전광역시',
                                       '울산':'울산광역시',
                                       '제주특별자치도':'제주도',
                                       '서울':'서울',
                                       '강원도':'강원도',
                                       '충청남도':'충청남도',
                                       '충청북도':'충청북도',
                                       '경기도':'경기도',
                                       '전라북도':'전라북도',
                                       '전라남도':'전라남도',
                                       '경상북도':'경상북도',
                                       '경상남도':'경상남도'})
    date_series = pd.Series(df['거래일자'])
    date_f =pd.to_datetime(date_series, format='%Y%m%d', errors='ignore')
    df['거래일자'] = date_f
    df['month_year'] = pd.to_datetime(df['거래일자']).dt.to_period('M')
    df.drop(['거래일자'], axis=1, inplace=True)
    
    df_group = df.groupby(['지역(시)','month_year']).mean()
    df_group.reset_index(inplace=True)
    return df_group

# 단편적으로 지역 12개월 정보만 들어있는 DataFrame 생성하여 for 문 돌릴때 사용할 함수
def df_local(df_group,local): 
    df_local = df_group.loc[df_group['지역(시)']==local,:]
    return df_local
        
def df_flat(df_group):
    year=str(df_group.iloc[0,1])[0:4]
    local = str(df_group.iloc[0,0])
    df_group = df_group.drop(['지역(시)'],axis=1)
    
    df_T = df_group.T # Transpose --> 행/열을 바꿔준다.
    df_T.columns = df_T.loc['month_year',:]
    df_T.drop('month_year',axis=0,inplace=True)
    df_T_res = df_T.reset_index()
    df_T_drop = df_T_res.drop(['index'], axis=1)
    
    col_name = df_T.index.values
    
    col_list=[]
    for i in range(len(col_name)):
        temp = col_name[i]
        for j in range(12):
            col_list.append(temp+' '+str(j+1)+'월')
            
    df_flat = pd.DataFrame(df_T_drop.values.flatten().reshape(1,-1),
                           columns=col_list,
                           index=[year+'_'+local])     
    return df_flat
    
if __name__ == "__main__":
    os.chdir('C:/Users/Fam/Downloads/Python/Project/source')
    files = glob.glob('../data/Raw_forecast_*')
    
    df=pd.DataFrame()
    for data in files:
        df_temp = df_group(data)
        for local in df_temp['지역(시)'].unique():
            temp = df_local(df_temp, local)
            df=pd.concat([df,df_flat(temp)], axis=0)
    
    df.reset_index(inplace=True)
    df.rename(columns={'index':'year_local'}, inplace=True)    
    df.to_excel('../data/climate_in_a_row.xls',index=False)    
