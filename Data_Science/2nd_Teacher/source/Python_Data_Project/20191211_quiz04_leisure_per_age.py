# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:56:08 2019

@author: sundooedu
"""
#%%
import glob
fil_name="quiz_report_age_leisure_pie_chart.txt"
loading=glob.glob(f'../data/{fil_name}')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
    
plt.rcParams['axes.unicode_minus'] = False   
#그래프에서 마이너스 기호가 표시되도록 하는 설정입니다.

read_fil=pd.read_table(loading[0])

read_fil['합계']=np.sum(read_fil.iloc[:,3:],axis=1)

per_age=read_fil.loc[read_fil["대분류"]=="연령별",:]
per_age.reset_index(inplace=True)
del per_age['index']

import matplotlib.pyplot as plt

def plt_pie(*args):
    col_list=[*args]
    plt.figure(figsize=(16,5+len(col_list))) # 배경 크기를 입력된 요소 크기에 맞게 조절 다만 가로길이는 그대로 유지
    for i,col in enumerate(col_list):
        plt.subplot(len(col_list)//3, 3, i+1)  # 행의 개수를 3으로 나눈 몫으로 적용한다.
        plt.pie(per_age[col], labels=per_age['분류'], autopct='%1.1f%%', explode=(0.02,0.02,0.02,0.02,0.02,0.02))
        plt.title('연령별'+' '+col)
    plt.show() 
        

plt_pie("여행야외나들이","TV 또는 비디오시청","문화예술관람")
        


