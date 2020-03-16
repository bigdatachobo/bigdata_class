# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:18:56 2019

@author: sundooedu
"""
#%%
'''
1. 2008~2017까지 출생한 전체 남,녀 수의 합을 구하세요.

2. 년도별 남,여 출생 추이 그래프를 그리세요.

3. 성별에 따른 빈도수가 가장 높은 이름 10개만 출력해 보세요.

4. Emma, Jacob 이름의 시대별 추이를 그래프로 그리세요.
'''
#%%
''' 1. 2008~2017까지 출생한 전체 남,녀 수의 합을 구하세요.'''
#%%
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name_file=glob.glob('../data/20191209_National_data_names/yob20*')

selected_name=[]
for i in name_file:
    if int(i[-6:-4]) >= 8 and int(i[-6:-4]) <= 17:
        selected_name.append(i)

name=pd.DataFrame()

for i in selected_name:
    df=pd.read_table(i,names=['name','gender','count'],sep=',')
    df['year']=i[-8:-4]
    name=pd.concat([name,df],ignore_index=True)
    
    
