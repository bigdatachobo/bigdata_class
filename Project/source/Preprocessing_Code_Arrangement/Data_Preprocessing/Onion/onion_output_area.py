# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:50:07 2020

@author: sundooedu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False

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
    
output = pd.read_excel('../projectdata/양파면적_생산량_1981_2019.xlsx', header=None)
output.set_index(0, inplace=True)

output = output[output.index != '서울특별시']
output = output[output.index != '세종특별자치시']
output = output[output.index != '계']

output.columns = output.iloc[0,:]
output = output.iloc[1:,-30:]

#%% unit output 
unit_output = output.iloc[1:,np.arange(1,30,3)]

df_unit = pd.DataFrame()
for i in range(len(unit_output)):
    each_sido = pd.DataFrame({'area':unit_output.index[i], 'year':unit_output.iloc[i,:].index ,
                              '10a당 생산량 (kg)':unit_output.iloc[i,:].values,'year_local':unit_output.iloc[i,:].index+'_'+unit_output.index[i]})
    df_unit = pd.concat([df_unit,each_sido])
    
df_unit.set_index('year_local',inplace=True)

df_unit.to_csv('onion_unit_ouput.csv')

#%% total_output 

total_output = output.iloc[1:,np.arange(2,30,3)]

df_total = pd.DataFrame()
for i in range(len(total_output)):
    each_sido = pd.DataFrame({'area':total_output.index[i], 'year':total_output.iloc[i,:].index ,
                              '총 생산량 (톤)':total_output.iloc[i,:].values,'year_local':total_output.iloc[i,:].index+'_'+total_output.index[i]})
    df_total = pd.concat([df_total,each_sido])
    
df_total.set_index('year_local',inplace=True)

df_total.to_csv('onion_total_ouput.csv')

#%% area
onion_area = output.iloc[1:,np.arange(0,30,3)]

df_area = pd.DataFrame()
for i in range(len(onion_area)):
    each_sido = pd.DataFrame({'area':onion_area.index[i], 'year':onion_area.iloc[i,:].index ,
                              '재배면적 (ha)':onion_area.iloc[i,:].values,'year_local':onion_area.iloc[i,:].index+'_'+total_output.index[i]})
    df_area = pd.concat([df_area,each_sido])
    
df_area.set_index('year_local',inplace=True)

df_area.to_csv('onion_area.csv')


