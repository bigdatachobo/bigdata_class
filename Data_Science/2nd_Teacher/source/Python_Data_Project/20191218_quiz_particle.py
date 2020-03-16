# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:25:26 2019

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np
import glob

import platform
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')    

plt.rcParams['axes.unicode_minus'] = False
#%%
file_bag=glob.glob('../data/dust/*.csv')
#%%
air_1=pd.read_csv(file_bag[4],engine='python')
air_2=pd.read_csv(file_bag[3],engine='python')
air_3=pd.read_csv(file_bag[7],engine='python')
air_4=pd.read_csv(file_bag[0],engine='python')
air_5=pd.read_csv(file_bag[8],engine='python')
air_6=pd.read_csv(file_bag[6],engine='python')
air_7=pd.read_csv(file_bag[5],engine='python')
air_8=pd.read_csv(file_bag[1],engine='python')
air_9=pd.read_csv(file_bag[11],engine='python')
air_10=pd.read_csv(file_bag[10],engine='python')
air_11=pd.read_csv(file_bag[9],engine='python')
air_12=pd.read_csv(file_bag[2],engine='python')
#%%
df_list=[air_1,air_2,air_3,air_4,air_5,air_6,air_7,air_8,air_9,air_10,air_11,air_12]
#%% nan값 전처리
for air in df_list:
    del air['Unnamed: 0']

nan_1_list=[air_9,air_7,air_2,air_12]
for i in nan_1_list:
    del i['X31']

del air_5['X29']
del air_5['X30']
del air_5['X31']
#%% 컬럼이름 변경
for name in df_list:
    name.rename(columns=lambda x: x.replace('...1', '구'), inplace=True)
#%% 컬럼별 데이터 타입 확인
for df in df_list:
    print(df.dtypes)         
#%% 데이터프레임 병합
air_qual=pd.DataFrame()
for df in df_list:
    air_qual=pd.concat([air_qual,df],axis=1)            

del air_qual['구']            
air_qual.index=air_1['구']
air_qual.columns=range(365)
#%%
air_index={'수치':[0,1,2,3],
           '평가':['좋음','보통','나쁨','매우나쁨']} 
air_qual_index=pd.DataFrame(air_index)
#%%
air_qual_char=air_qual.astype(str)

air_qual_char=np.transpose(air_qual_char)

air_qual_char.groupby
#%%

