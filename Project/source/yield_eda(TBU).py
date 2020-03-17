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


#%% unit output 
unit_output = output.iloc[:,np.arange(1,118,3)]
unit_output.columns = unit_output.iloc[0,:]
unit_output = unit_output.drop(unit_output.index[[0,1]])
unit_output = unit_output.iloc[:,29:]

df_unit = pd.DataFrame()
for i in range(len(unit_output)):
    each_sido = pd.DataFrame({'area':unit_output.index[i], 
                              'year':unit_output.iloc[i,:].index ,
                              '10a당 생산량 (kg)':unit_output.iloc[i,:].values,
                              'year_local':unit_output.iloc[i,:].index+'_'+unit_output.index[i]})
    df_unit = pd.concat([df_unit,each_sido])
    
df_unit.set_index('year_local',inplace=True)
df_unit = df_unit[df_unit['area'].values != '세종특별자치시']
df_unit = df_unit[df_unit['area'].values != '계']

df_unit.to_csv('onion_unit_ouput.csv')

#%% total_output 

total_output = output.iloc[:,np.arange(3,117,3)]
total_output.columns = total_output.iloc[0,:]
total_output = total_output.drop(total_output.index[[0,1]])
total_output = total_output.iloc[:,28:]

df_total = pd.DataFrame()
for i in range(len(total_output)):
    each_sido = pd.DataFrame({'area':total_output.index[i], 
                              'year':total_output.iloc[i,:].index ,
                              '총 생산량 (톤)':total_output.iloc[i,:].values,
                              'year_local':total_output.iloc[i,:].index+'_'+total_output.index[i]})
    df_total = pd.concat([df_total,each_sido])
    
df_total.set_index('year_local',inplace=True)
df_total = df_total[df_total['area'].values != '세종특별자치시']
df_total = df_total[df_total['area'].values != '계']

df_total.to_csv('onion_total_ouput.csv')

#%% area
onion_area = output.iloc[:,np.arange(1,117,3)]
onion_area.columns = onion_area.iloc[0,:]
onion_area = onion_area.drop(onion_area.index[[0,1]])
onion_area = onion_area.iloc[:,29:]

df_area = pd.DataFrame()
for i in range(len(onion_area)):
    each_sido = pd.DataFrame({'area':onion_area.index[i], 
                              'year':onion_area.iloc[i,:].index ,
                              '재배면적 (ha)':onion_area.iloc[i,:].values,
                              'year_local':onion_area.iloc[i,:].index+'_'+total_output.index[i]})
    df_area = pd.concat([df_area,each_sido])
    
df_area.set_index('year_local',inplace=True)
df_area = df_area[df_area['area'].values != '세종특별자치시']
df_area = df_area[df_area['area'].values != '계']

df_area.to_csv('onion_area.csv')

#%%  Data EDA 

df_unit['10a당 생산량 (kg)'] = pd.Series(df_unit['10a당 생산량 (kg)'].astype(int))

# PLOT 년도별 10a당 생산량 
plt.style.use('ggplot')

pd.pivot_table(df_unit, 
               values='10a당 생산량 (kg)', 
               index=['year'],
               aggfunc=np.mean, 
               fill_value=0).plot()

plt.title('년도별 양파 10a당 생산량(kg)', fontsize=8)
plt.tight_layout()
plt.show()
plt.savefig('output_unit_year.png')

# PLOT 년도별 총 생산량 
total_output_pivot= pd.pivot_table(df_total, 
                                   values='총 생산량 (톤)', 
                                   index=['year'],
                                   aggfunc=np.mean, 
                                   fill_value=0)

df_total['총 생산량 (톤)'] = pd.Series(df_total['총 생산량 (톤)'].astype(int))
plt.style.use('ggplot')

pd.pivot_table(df_total, 
               values='총 생산량 (톤)', 
               index=['year'],
               aggfunc=np.mean, 
               fill_value=0).plot()

plt.title('년도별 총 양파 생산량(톤)', fontsize=8)
plt.tight_layout()
plt.show()
plt.savefig('output_unit_year.png')


# 지역별 10a당 생산량
unit_output_pivot_area = pd.pivot_table(df_unit, 
                                        values='10a당 생산량 (kg)', 
                                        index=['area'],
                                        aggfunc=np.mean, 
                                        fill_value=0)
plt.style.use('ggplot')
unit_output_pivot_area.plot()
plt.title('지역별 양파 10a당 생산량(kg)', fontsize=8)
plt.tight_layout()
plt.xticks(np.arange(16),unit_output_pivot_area.index, rotation=40, fontsize=8)
#plt.show()
#plt.savefig('output_unit_area.png')

# 지역별 양파 총 생산량 
total_output_pivot_area= pd.pivot_table(df_total, values='총 생산량 (톤)', index=['area'],aggfunc=np.mean, fill_value=0)
df_total['총 생산량 (톤)'] = pd.Series(df_total['총 생산량 (톤)'].astype(int))
plt.style.use('ggplot')
total_output_pivot_area.plot()
plt.xticks(np.arange(16),total_output_pivot_area.index, rotation=40, fontsize=8)
plt.title('지역별 총 양파 생산량(톤)', fontsize=8)
plt.tight_layout()
plt.show()
plt.savefig('output_total_area.png')



#%%
plt.plot(unit_output_pivot_area, 
         label='10a당 생산량(kg)')
plt.plot(total_output_pivot_area, 
         label = '총생산량(톤)')
plt.xticks(np.arange(16),
           total_output_pivot_area.index, 
           rotation=40, 
           fontsize=8)
plt.legend()
plt.savefig('onion_output.png')

total_output_pivot_area.plot()

