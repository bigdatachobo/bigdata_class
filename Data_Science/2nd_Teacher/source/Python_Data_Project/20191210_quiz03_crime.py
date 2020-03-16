# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:59:58 2019

@author: sundooedu
"""
#%%
import googlemaps

gmaps_key="AIzaSyBKRq7_4cl5CG-p7rpn4jAAsayRK4qoWYc"
gmaps=googlemaps.Client(key=gmaps_key)

gmaps.geocode('서울중부경찰서', language='ko')
#%%
import numpy as np
import pandas as pd

crime_anal_police=pd.read_csv('../data/02. crime_in_Seoul.csv', thousands=',', encoding='euc-kr')
crime_anal_police.head()
#%%
station_name=[]

for name in crime_anal_police['관서명']: # 경찰서 이름 정제
    station_name.append('서울'+str(name[:-1])+'경찰서') 

station_name
#%%
station_address=[] # 주소
station_lat=[] # 위도
station_lng=[] # 경도

for name in station_name: # 주소 정제
    tmp=gmaps.geocode(name, language='ko')
    station_address.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")
    
    station_lat.append(tmp_loc['location']['lat']) # 위도
    station_lng.append(tmp_loc['location']['lng']) # 경도
    
    print(name + '-->' + tmp[0].get("formatted_address"))

station_address  # 주소   # 결과값이 들어갔을때.
station_lat        
station_lng    
#%%
gu_name=[] 

for name in station_address: # 구-이름 정제
    tmp = name.split()
    tmp_gu = [gu for gu in tmp if gu[-1]=='구'][0]
    gu_name.append(tmp_gu)
    
crime_anal_police['구별']=gu_name
crime_anal_police.head()   
#%%
crime_anal_police[crime_anal_police['관서명']=='금천서']
#%%
# 파일로 저장
crime_anal_police.to_csv('../data/02. crime_in_Seoul_include_gu_name.csv',
                         sep=',', encoding='utf-8')
crime_anal_police.head()
#%%
'''
범죄 데이터 구별로 정리하기
'''
# 파일 불러오기
crime_anal_raw=pd.read_csv('../data/02. crime_in_Seoul_include_gu_name.csv',
                           encoding='utf-8')
crime_anal_raw.head()
#%%
'''
Unnamed 인덱스 제거
index_col=0 옵셥 추가.
'''
crime_anal_raw=pd.read_csv('../data/02. crime_in_Seoul_include_gu_name.csv',
                           encoding='utf-8', index_col=0)
crime_anal_raw.head()    
#%%
'''
구별을 기준으로 데이터를 합침.
'''
crime_anal=pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
crime_anal.tail(20)    
#%%
crime_anal['강간검거율']=crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율']=crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율']=crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율']=crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율']=crime_anal['폭력 검거']/crime_anal['폭력 발생']*100 

del crime_anal['강간 검거']   
del crime_anal['강도 검거']  
del crime_anal['살인 검거']  
del crime_anal['절도 검거']  
del crime_anal['폭력 검거']  

crime_anal.head(20)
#%%
con_list=['강간검거율','강도검거율', '살인검거율', '절도검거율', '폭력검거율']    

for column in con_list:
    crime_anal.loc[crime_anal[column] > 100, column]=100
                  #         행,               열      
crime_anal.head()    
#%%
'''
컬럼 이름 바꿈.
'''
crime_anal.rename(columns={'강간 발생':'강간',
                           '강도 발생':'강도',
                           '살인 발생':'살인',
                           '절도 발생':'절도',
                           '폭력 발생':'폭력'},inplace=True)
crime_anal.head()    
#%%
'''
데이터를 정규화 시킴
standardScaler
RobustScaler
MinMaxScaler
Normalizer
'''
from sklearn import preprocessing  # 데이터 전처리

col=['강간','강도','살인','절도','폭력']

x=crime_anal[col].values
min_max_scaler=preprocessing.MinMaxScaler()

x_scaled=min_max_scaler.fit_transform(x.astype(float)) # 변환
crime_anal_norm=pd.DataFrame(x_scaled, columns=col, index=crime_anal.index)

'''
원본자료 그대로 사용
'''
col2=['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm[col2]=crime_anal[col2]
crime_anal_norm.head()
#%%
'''
CCTV 자료를 먼저 불러온 후
정제한 데이터프레임에 추가.
'''
result_CCTV=pd.read_csv('../data/01. CCTV_result.csv',encoding='utf-8',
                        index_col='구별')

crime_anal_norm[['인구수','CCTV']]=result_CCTV[['인구수','소계']]
crime_anal_norm.head()
#%%
col=['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄']=np.sum(crime_anal_norm[col], axis=1) # axis=1(열-방향) 행 연산
crime_anal_norm.head()
#%%
'''
전체 집계
'''
col=['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거']=np.sum(crime_anal_norm[col],axis=1) # axis=1(열-방향) 행 연산
crime_anal_norm.head()
#%%
'''
Visualization
'''
#%%
import matplotlib.pyplot as plt
import seaborn as sns
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
sns.pairplot(crime_anal_norm, vars=["강도","살인","폭력"], kind='reg', size=3)
plt.show()
#%%
sns.pairplot(crime_anal_norm, x_vars=["인구수","CCTV"],
             y_vars=["살인","강도"],kind='reg',size=3)
#%%
sns.pairplot(crime_anal_norm, x_vars=["인구수","CCTV"],
             y_vars=["살인검거율","폭력검거율"],kind='reg',size=3)
plt.show()
#%%
sns.pairplot(crime_anal_norm, x_vars=["인구수","CCTV"],
             y_vars=["절도검거율","강도검거율"],kind='reg',size=3)
plt.show()
#%%
tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거']=crime_anal_norm['검거'] / tmp_max*100
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거',ascending=False)
crime_anal_norm_sort.head()
#%%
'''
히트맵
'''
target_col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']

crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거',ascending=False)

plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col],annot=True, fmt='f',
            linewidths=.5, cmap='RdPu')
plt.title('범죄 검거 비율(정규화된 검거의 합으로 정렬)')
plt.show()
#%%
target_col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']

crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5
crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄',ascending=False)

plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col],annot=True, fmt='f',
            linewidths=.5, cmap='RdPu')
plt.title('범죄 검거 비율(정규화된 발생 건수로 정렬)')
plt.show()
#%%
crime_anal_norm.to_csv('../data/02. crime_in_Seoul_final.csv',sep=',',
                       encoding='utf-8')
#%%
'''
"pip install folium" 
anaconda prompt에서 
지도 모율 설치
'''
#%%
'''
Folium
'''
import folium
map_osm = folium.Map(location=[45.5236,-122.6750])
map_osm
#%%
import folium
stamen = folium.Map(location=[45.5236,-122.6750],zoom_start=13)
stamen
#%%
import folium
stamen = folium.Map(location=[45.5236,-122.6750],
                    tiles='Stamen Terrain',zoom_start=13)
stamen
#%%
map_1 = folium.Map(location=[45.5236,-122.6972],
                    tiles='Stamen Terrain',zoom_start=12)
folium.Marker([45.3288, -121.6625],popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')).add_to(map_1)

folium.Marker([45.3288, -121.7113],popup='Timberline Lodge',
              icon=folium.Icon(icon='cloud')).add_to(map_1)
map_1
#%%
'''
color 추가
'''
map_1 = folium.Map(location=[45.5236,-122.6972],
                    tiles='Stamen Terrain',zoom_start=12)
folium.Marker([45.3288, -121.6625],popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')).add_to(map_1)

folium.Marker([45.3288, -121.7113],popup='Timberline Lodge',
              icon=folium.Icon(color='green')).add_to(map_1)

folium.Marker([45.3300, -121.6823],popup='Some Other Location',
              icon=folium.Icon(color='red',icon='info-sign')).add_to(map_1)
map_1
#%%
'''
tiles='Stamen Toner' 옵셥을 바꿔서 지도 스타일을 바꿀 수가 있다.
위에서는 
tiles='Stamen Terrain' 을 사용.
'''
map_2 = folium.Map(location=[45.5236,-122.6972],
                    tiles='Stamen Toner',zoom_start=13)

folium.Marker([45.3288, -121.6699], popup='The WaterFront').add_to(map_2)

'''
서클로 마커로 활용.
'''
folium.CircleMarker([45.5215,-122.6261],radius=50,
                    popup='Laurelhurst Park',color='#3186cc',
                    fill_color='#3186cc').add_to(map_2)
map_2                    
#%%
map_5 = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

'''3각형'''
folium.RegularPolygonMarker([45.5012,-122.6655],
                            popup='Ross Island Bridge', fill_color='#132b5e',
                            number_of_sides=3,radius=10).add_to(map_5)

'''4각형'''
folium.RegularPolygonMarker([45.5132,-122.6708],
                            popup='Hawthorne Bridge', fill_color='#45647d',
                            number_of_sides=4,radius=10).add_to(map_5)    
                
'''6각형'''
folium.RegularPolygonMarker([45.5275,-122.6692],
                            popup='Steel Bridge', fill_color='#769d96',
                            number_of_sides=6,radius=10).add_to(map_5)

'''8각형'''
folium.RegularPolygonMarker([45.5318,-122.6745],
                            popup='Broadway Bridge', fill_color='#769d96',
                            number_of_sides=8,radius=10).add_to(map_5)

map_5
#%%
'''
범죄율에 대한 지도 시각화
'''
#%%
'''
json 파일
'''
import json
geo_path = '../data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))
#%%
map =folium.Map(location=[37.5502, 126.982], zoom_start=10,
                tiles='Stamen Toner')
# choropleth 명령으로 json 파일과 지도에 표현하고 싶은 데이터를 입력.
map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['살인'],
               columns = [crime_anal_norm.index, crime_anal_norm['살인']],
               fill_color = 'PuRd', # PuRd, YIGnBu
               key_on='feature.id')
            # key_on 옵션 >>> 지도의 id
map
#%%
'''
경찰서별 검거현황과 구별 범죄발생 현황을 표현하기
'''
#%%
crime_anal_raw['lat']=station_lat
crime_anal_raw['lng']=station_lng

col = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()
crime_anal_raw['검거']=np.sum(tmp, axis=1) # '검거' 열 추가.
crime_anal_raw.head()
#%%
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in crime_anal_raw.index: # 행 인덱스 반복 출력
    folium.Marker([crime_anal_raw['lat'][n],
                   crime_anal_raw['lng'][n]]).add_to(map)
    
map
#%%
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in crime_anal_raw.index: # 행 인덱스 반복 출력
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]], # [위도, 경도]
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc', fill_color='#3186cc',
                        fill=True).add_to(map)
#%%
map =folium.Map(location=[37.5502, 126.982], zoom_start=11)
# choropleth 명령으로 json 파일과 지도에 표현하고 싶은 데이터를 입력.
map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['범죄'],
               columns = [crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color = 'PuRd', # PuRd, YIGnBu
               key_on='feature.id')
            # key_on 옵션 >>> 지도의 id

for n in crime_anal_raw.index: # 행 인덱스 반복 출력
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc', fill_color='#3186cc',
                        fill=True).add_to(map)            
map
#%%
'''
파일 저장
'''
map.save('../data/02. map1.html') # 파일이 저장될 위치
#%%
'''
<quiz>

경찰서별 검거율과 구별 범죄율을 시각화한 자료에
1) 경찰서 이름, 검거율 등의 정보를 추가해 보세요.
2) 적절한 아이콘도 추가해 보세요.
'''
#%%
'''
검거율 평균 구하고
crime_anal_norm 에 '검거율' 열에 추가.
'''
map=folium.Map(location=[37.5502,126.982], zoom_start=10)

map.choropleth(geo_data = geo_str, 
              data=crime_anal_norm['범죄'],
              columns=[crime_anal_norm.index, crime_anal_norm['범죄']],
              fill_color='PuRd', #PuRd, YIGnBu 
               key_on='feature.id')

for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n],
                   crime_anal_raw['lng'][n]],
                   icon=folium.Icon(icon='cloud', color='green'),  
                   popup=crime_anal_raw['관서명'][n],
                   tooltip = int(sum(crime_anal_raw.iloc[n,2:12:2]) / sum(crime_anal_raw.iloc[n,1:11:2]) * 100)).add_to(map)
    
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n],
                         crime_anal_raw['lng'][n]], 
                         radius = crime_anal_raw['검거'][n], 
                         color = '#3186cc', 
                         fill_color='#3186cc', 
                         fill=True).add_to(map)                         
    
map
#%%
'''
ClusterMarker 이용하여 확대/축소 시에 popup이 모였다 흩어졌다를 표현함.
'''
import numpy as np
from folium.plugins import MarkerCluster

map=folium.Map(location=[37.5502,126.982], zoom_start=10)

marker_cluster = MarkerCluster().add_to(map) 

map.choropleth(geo_data = geo_str, 
              data=crime_anal_norm['범죄'],
              columns=[crime_anal_norm.index, crime_anal_norm['범죄']],
              fill_color='PuRd', #PuRd, YIGnBu 
               key_on='feature.id')

for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n],
                   crime_anal_raw['lng'][n]],
                   icon=folium.Icon(icon='cloud', color='green'),  
                   popup=crime_anal_raw['관서명'][n],
                   tooltip = int(sum(crime_anal_raw.iloc[n,2:11:2]) / sum(crime_anal_raw.iloc[n,1:11:2]) * 100)).add_to(marker_cluster)
   
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n],
                         crime_anal_raw['lng'][n]], 
                         radius = crime_anal_raw['검거'][n]*10, 
                         color = '#3186cc', 
                         fill_color='#3186cc', 
                         fill=True).add_to(marker_cluster)                         
map.save('map.html')    
map
#%%







