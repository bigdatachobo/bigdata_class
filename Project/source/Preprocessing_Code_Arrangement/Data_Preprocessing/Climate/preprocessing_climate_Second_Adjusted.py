# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:53:19 2020

@author: sundooedu
"""
#%%
# 연도순으로 분리
import pandas as pd
import numpy as np
import os
import glob
os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')
load=pd.read_excel('../data/climate_in_a_row.xls')

for i in range(0,480,16):
    temp=load.iloc[i:i+16,:]
    temp.to_csv(f'../data/after_data/{load.loc[i,"year_local"].split("_")[0]}.csv',
                index=False,
                encoding='utf-8')
#%%
# 작년 7월 시작 ~ 올해 6월 끝으로 바꿈.
files=glob.glob('../data/after_data/*.csv')

def last_split(file):
    indx=list(range(1,121,12)) # 컬럼 12개씩 짜르는 인덱스
    table=pd.read_csv(file,encoding='utf-8') # 위에서 연도별로 구분한 파일을 여는 코드
    
    temp1=pd.DataFrame() # 평균기온 컬럼
    temp2=pd.DataFrame() # 최고기온 컬럼
    temp3=pd.DataFrame() # 최저기온 컬럼
    temp4=pd.DataFrame() # 강수량 컬럼
    temp5=pd.DataFrame() # 일조시간 컬럼
    temp6=pd.DataFrame() # 일사량 컬럼
    temp7=pd.DataFrame() # 습도 컬럼
    temp8=pd.DataFrame() # 운량 컬럼
    temp9=pd.DataFrame() # 적설량 컬럼
    temp10=pd.DataFrame() # 순간최대풍속 컬럼
    
    temp_list=[temp1, temp2, temp3, temp4, temp5,
               temp6, temp7, temp8, temp9, temp10] # DF 변수를 리스트에 담아 
                                                   # for문 돌릴때 꺼낸다.
    
    for i,tmp in enumerate(temp_list): # enumerate로 index도 같이 돌려준다.
        temp=table.iloc[:,indx[i]:indx[i]+12].iloc[:,6:] # 12개씩 끊고/ 7월~12월까지 DF에 담는다.
        tmp=pd.concat([tmp,temp],axis=1)
        temp_list[i] = tmp # temp_list에 계산한 결과를 축적함!!!
        
    return temp_list

def this_split(file):
    indx=list(range(1,121,12))
    table=pd.read_csv(file,encoding='utf-8')
    
    tmp1=pd.DataFrame()
    tmp2=pd.DataFrame()
    tmp3=pd.DataFrame()
    tmp4=pd.DataFrame()
    tmp5=pd.DataFrame()
    tmp6=pd.DataFrame()
    tmp7=pd.DataFrame()
    tmp8=pd.DataFrame()
    tmp9=pd.DataFrame()
    tmp10=pd.DataFrame()
    
    tmp_list=[tmp1, tmp2, tmp3, tmp4, tmp5,
              tmp6, tmp7, tmp8, tmp9, tmp10]
    
    for i,tmp in enumerate(tmp_list):
        temp=table.iloc[:,indx[i]:indx[i]+12].iloc[:,:6]
        tmp=pd.concat([tmp,temp],axis=1)
        tmp_list[i] = tmp

    return tmp_list

if __name__ == "__main__":
    
    df=pd.DataFrame()
    for i in list(range(0,29)):
        # year_local 뽑아내기
        sido=pd.read_csv(files[i+1],encoding='utf-8') # 시도를 뽑아낼 DF
        year=pd.Series(list(map(lambda x: x.split('_')[0],sido['year_local']))) # 'year_local'컬럼에서 숫자로된 연도 부분을 추출
        area=pd.Series(list(map(lambda x: x.split('_')[1],sido['year_local']))) # 한글로된 'area' 추출
       
        df_temp=pd.DataFrame()
        for last, this in zip(last_split(files[i]), this_split(files[i+1])): # 작년 7~12월까지 데이터 / 이번년도 1~6(수확)월 데이터 zip으로 묶어줘서 반환한다.
            temp=pd.concat([last,this],axis=1)
            df_temp=pd.concat([df_temp,temp],axis=1)
            
        df_temp=pd.concat([sido['year_local'],area,year,df_temp], axis=1) # 맨앞에 'year_local', 'area', 'year' 컬럼이 오게 pd.Series 형식으로 concat 해준다. 
        df_temp.rename(columns={0:'area',1:'year'}, inplace=True)      
        df=pd.concat([df,df_temp],axis=0)
    
    df.to_csv('../data/adjusted_climate.csv',
              encoding='utf-8', # 구글드라이브에서 브라우저 상에서 바로 볼 수 있게 'utf-8'로 인코딩 해준다.
              index=False)    
    


    
    
        