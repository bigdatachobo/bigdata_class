# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:04:18 2019

@author: sundooedu
"""
#%%
'''
GIS(Geographic Information System)- 지리정보시스템 데이터
데이터의(좌표) 지도 위치를 위도, 경도 기반 표시 
https://www.google.com/maps
pip install folium
'''

import folium
# folium 맵 생성
# 서울특별시청 위도, 경도
map1 = folium.Map(location=[37.566677, 126.978420],zoom_start=14)
map1.save('map.html') # 파일 저장

map1 = folium.Map(location=[37.566677, 126.978420],zoom_start=14)
folium.Marker(location=[37.566677, 126.978420],tooltip='서울시청',popup='서울시청').add_to(map1)
map1.save('map_Marker.html')

folium.CircleMarker(location=[37.566677, 126.978420],tooltip='서울시청',popup='서울시청',color='red',fill_color='green',radius=100).add_to(map1)
map1.save('map_Circle_Marker.html')