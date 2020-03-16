# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:20:42 2019

@author: sundooedu
"""
#%%
from selenium import webdriver
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("http://www.naver.com")
#%%
driver.save_screenshot('../images/001.png')
#%%
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("http://www.opinet.co.kr/searRgSelect.do")
#%%
gu_list_raw=driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
gu_list = gu_list_raw.find_elements_by_tag_name("option")
                        '''여러개를 가져올시 elements를 쓴다.'''
#%%
'''구-이름 리스트 추출'''
gu_names = [option.get_attribute("value") for option in gu_list]
gu_names.remove('')
gu_names
#%%
# find_element_by_id(id): id 속성으로 요소를 하나 추출
element = driver.find_element_by_id("SIGUNGU_NM0")
element.send_keys(gu_names[10]) # send_keys(value) 키를 입력
'''
제어 당하는 브라우저의 구이름이 변경되는 것을 확인하세요.
'''
#%%
'''조회버튼'''
xpath="""//*[@id="searRgSelect"]""" # 조회버튼
element_sel_gu = driver.find_element_by_xpath(xpath).click() # 조회버튼 클릭!
#%%
'''엑셀버튼'''
xpath2="""//*[@id="glopopd_excel"]""" # 엑셀버튼
element_sel_gu = driver.find_element_by_xpath(xpath2).click() # 엑셀버튼 클릭!
#%%
import time
from tqdm import tqdm_notebook

for gu in tqdm_notebook(gu_names):
    element = driver.find_element_by_id("SIGUNGU_NM0")
    element.send_keys(gu)
    
    xpath="""//*[@id="searRgSelect"]""" # 조회버튼
    element_sel_gu = driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    
    xpath="""//*[@id="glopopd_excel"]""" # 엑셀버튼
    element_sel_gu = driver.find_element_by_xpath(xpath2).click()
    time.sleep(1)
#%%
''' 마지막에 끝나면 드리이버 close() 한다.'''    
driver.close()
#%%
'''
4-5 구별 주유 가격에 대한 데이터의 정리
'''
import pandas as pd
from glob import glob

stations_files = glob('../data/지역*.xls')
stations_files
#%%
tmp_raw = []

for file_name in stations_files:
    tmp = pd.read_excel(file_name, header=2)
    tmp_raw.append(tmp)
    
station_raw = pd.concat(tmp_raw, ignore_index=True) 
'''
ignore_index=True >>> 원래 갖고 있던 인덱스 무시
'''
#%%
station_raw.info()
#%%
station_raw.head()
#%%
stations= pd.DataFrame({'Oil_store':station_raw['상호'],
                        '주소':station_raw['주소'],
                        '가격':station_raw['휘발유'],
                        '셀프':station_raw['셀프여부'],
                        '상표':station_raw['상표']})
stations.head()
#%%
'''
"구" 정보만 가져온다.
'''    
stations['구'] = [eachAddress.split()[1] for eachAddress in stations['주소']]
stations.head()
#%%
stations.loc[stations['구'] == '서울특별시', '구'] = '성동구'
stations['구'].unique()
#%%
stations[stations['구']=='특별시']
#%%
stations.loc[stations['구'] == '특별시', '구'] = '도봉구'
stations['구'].unique() 
#%%
'''
'-'가 없는 값들만 따로 모아 stations에 집어넣는다.
'''
stations = stations[stations['가격'] != '-']   
stations.head()    
#%%
'''
가격을 float 형식으로 바꿔준다.
'''
stations['가격'] = [float(value) for value in stations['가격']]
#%%
stations.reset_index(inplace=True)
del stations['index']
#%%
'''
DataFrame의 정보를 본다.
가격이 float 형식으로 바뀌어있다.
'''
stations.info()
#%%
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
#%% 
stations.boxplot(column='가격', by='셀프', figsize=(12,8))
#%%
import seaborn as sns    
plt.figure(figsize=(12,8))    
sns.boxplot(x="상표", y="가격", hue = "셀프", data = stations, palette=["m","g"])
plt.show()
#%%
plt.figure(figsize=(12,8))
sns.boxplot(x="상표", y="가격", data=stations, palette="Set3")
sns.swarmplot(x="상표",y="가격", data=stations, color=".6")
plt.show()
#%%
'''
4-5 서울시 구별 주유 가격 확인하기
'''
import json
import folium
import googlemaps
import warnings
warnings.simplefilter(action="ignore", category = FutureWarning)

stations.sort_values(by='가격', ascending=False).head(10)
#%%
stations.sort_values(by='가격',ascending=True).head(10)
#%%
import numpy as np
'''
"구"를 기준을 가격 "가격"을 정렬시 평균값으로 자동적용됨
'''
gu_data = pd.pivot_table(stations, index=["구"], values=['가격'])
gu_data.head()
#%%
geo_path = '../data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map=folium.Map(location=[37.5502, 126.982], zoom_start=10.5,
               tiles='Stamen Toner')
map.choropleth(geo_data = geo_str,
               data=gu_data,
               columns=[gu_data.index, '가격'],
               fill_color='PuRd', # PuRd, YIGnBu
               key_on='feature.id')
                # key_on >>> 지도 id
map
#%%
'''
4-6 서울시 주유 가격 상하위 10개 주유소 지도에 표기하기
'''
oil_price_top10= stations.sort_values(by='가격', ascending=False).head(10)
#%%
oil_price_bottom10 = stations.sort_values(by='가격', ascending=True).head(10)
#%%
gmap_key="AIzaSyBKRq7_4cl5CG-p7rpn4jAAsayRK4qoWYc"
gmaps=googlemaps.Client(key=gmap_key)
#%%
'''
top10 위도/경도 구하여 DataFrame에 넣기
'''
from tqdm import tqdm_notebook

lat = []
lng = []

for n in tqdm_notebook(oil_price_top10.index):
    try:
        tmp_add = str(oil_price_top10['주소'][n]).split('(')[0]
        tmp_map = gmaps.geocode(tmp_add)
        tmp_loc = tmp_map[0].get('geometry')
        lat.append(tmp_loc['location']['lat'])
        lng.append(tmp_loc['location']['lng'])
    except:
        lat.append(np.nan)
        lng.append(np.nan)
        print("Here is nan !")

oil_price_top10['lat'] = lat
oil_price_top10['lng'] = lng
#%%
'''
bottom10 위도/경도 구하여 DataFrame에 넣기
'''
from tqdm import tqdm_notebook

lat = []
lng = []

for n in tqdm_notebook(oil_price_bottom10.index):
    try:
        tmp_add = str(oil_price_bottom10['주소'][n]).split('(')[0]
        tmp_map = gmaps.geocode(tmp_add)
        tmp_loc = tmp_map[0].get('geometry')
        lat.append(tmp_loc['location']['lat'])
        lng.append(tmp_loc['location']['lng'])
    except:
        lat.append(np.nan)
        lng.append(np.nan)
        print("Here is nan !")

oil_price_bottom10['lat'] = lat
oil_price_bottom10['lng'] = lng
#%%
'''
map에 최상10개, 최하10개 주유소 원으로 표시.
'''
map=folium.Map(location=[37.5202,126.975], zoom_start=10.5)

for n in oil_price_top10.index:
    if pd.notnull(oil_price_top10['lat'][n]):
        folium.CircleMarker([oil_price_top10['lat'][n], oil_price_top10['lng'][n]],
                            radius=15,
                            color='#CD3181',
                            fill_color='#CD3181',
                            fill=True).add_to(map)

for n in oil_price_bottom10.index:
    if pd.notnull(oil_price_bottom10['lat'][n]):
        folium.CircleMarker([oil_price_bottom10['lat'][n], oil_price_bottom10['lng'][n]],
                            radius=15,
                            color='#3186cc',
                            fill_color='#3186cc',
                            fill=True).add_to(map)            

map
#%%






