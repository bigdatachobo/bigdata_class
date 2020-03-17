# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:57:14 2020

@author: sundooedu
"""

#%% Import Libraries
import pandas as pd
import numpy as np

#%% 

soil = pd.read_excel('용도별토양정보_1997_2018.xlsx', header=None)

soil=soil.transpose()

soil.columns = ['년도','화학성','논','밭']


soil = soil[soil['화학성'] != '지점수 (개)']

soil.reset_index(inplace=True)
soil = soil.iloc[1:,1:]

#당해 년도 중복 제거
year_chem = []
for i in np.arange(0,len(soil)):
    year_chem.append(str(soil['년도'].iloc[i]) + '_' + str(soil['화학성'].iloc[i]))

soil['year_chem'] = year_chem
soil= soil.drop_duplicates(subset = 'year_chem', keep='first')

soil['년도'] = soil['년도'].astype(int)
#soil = soil[soil['년도'] >= 2009]

#%% 
area = pd.read_excel('양파재배면적_1975_2019.xlsx', skiprows=[1])
area = area.fillna(method='pad')


area['시도별'] = area['시도별'].astype(str)
sido_name = []
for i in area['시도별']:
    sido_name.append(i.replace('\n\n',''))

area['시도별'] = sido_name

years = []
for i in list(np.arange(1975,2020)):
    years.append(str(i))

area[years] = area.loc[:, years].replace('-',0).astype(int)
area_pivot = area.pivot_table(index='시도별', columns=['종류별'], values=years)

for i in np.arange(0,134,2):
    area_pivot.iloc[:,i] = round(area_pivot.iloc[:,i] /(area_pivot.iloc[:,i] + area_pivot.iloc[:,i+1] ),3)
    area_pivot.iloc[:,i+1] = round(area_pivot.iloc[:,i+1] /(area_pivot.iloc[:,i] + area_pivot.iloc[:,i+1] ),3)
    

area_pivot.fillna('0', inplace=True)

area = area_pivot.melt()

area['시도'] = pd.Series((area_pivot.index.tolist())*(2019-1975+1)*3)
area.set_index('시도', inplace=True)
area.columns = ['년도','용도','비율']

col_name = area.index.values

index = []
for i in range(0,len(area)):
    index.append(area.iloc[i,0] + '_' + col_name[i])

area['year_sido'] = index


non = area[area['용도'] == '논']
non.rename(columns={"비율": "논비율"}, inplace=True)
non = non.drop('용도',axis=1)


bat = area[area['용도'] == '밭']
bat.rename(columns={"비율": "밭비율"}, inplace=True)
bat = bat.drop('용도',axis=1)

bat.reset_index(inplace=True)

proportion = pd.merge(bat, non, on=['year_sido', '년도'])
proportion.rename(columns = {'년도':'year'}, inplace=True)


#%% 

chem_name = soil['화학성'].unique().tolist() #18
sido_name #17
years = np.arange(1997,2020) #11

       
#%% 

soil_T=soil.transpose()
soil_T.columns = soil_T.iloc[0,:]
soil_T.drop('년도',axis=0, inplace=True)
soil_T = soil_T.iloc[:-1,:]


soil.to_csv('../projectdata/토양정보.csv')
proportion.to_csv('논밭비율.csv')