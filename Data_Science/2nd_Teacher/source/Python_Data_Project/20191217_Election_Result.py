# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:42:48 2019

@author: sundooedu
"""
#%%
'''6-1. Selenium과 Beautiful Soup을 이용한 데이터 획득 준비 작업'''
#%%
import pandas as pd
import numpy as np

import platform
import matplotlib.pyplot as plt

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
from selenium import webdriver
import time
#%%
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=VC&secondMenuId=VCCP09")
#%%
'''대통령선거 버튼 클릭'''
driver.find_element_by_id("electionType1").click()
#%%
'''대통령선거 옵션에서 >>> 제19대 선택'''
driver.find_element_by_id("electionName").send_keys("제19대")
#%%
'''선거 >>> 대통령선거 선택'''
driver.find_element_by_id("electionCode").send_keys("대통령선거")
#%%
sido_list_raw = driver.find_element_by_xpath("""//*[@id="cityCode"]""")
sido_list = sido_list_raw.find_elements_by_tag_name("option")
sido_names_values = [option.text for option in sido_list]
sido_names_values = sido_names_values[2:]
sido_names_values
#%%
'''6-2. 19대 대선 개표 결과 데이터 획득하기'''
#%%
import re

def get_num(tmp):
    return float(re.split('\(', tmp)[0].replace(',',''))
#%%
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 웹페이지 로딩 자동화(EC)
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

def move_sido(name): # 도시를 하나씩 던져준다.
    element = driver.find_element_by_id("cityCode")
    element.send_keys(name)
    make_xpath = """//*[@id="searchBtn"]""" # 버튼 누르기
    wait.until(EC.element_to_be_clickable((By.XPATH,make_xpath)))
    driver.find_element_by_xpath(make_xpath).click()
#%%
def append_data(df, sido_name, data):
    for each in df[0].values[1:]:
        data['광역시도'].append(sido_name)
        data['시군'].append(each[0])
        data['pop'].append(float(each[2])) # float // pop>>> 인구수(population)
        data['moon'].append(get_num(each[3]))
        data['hong'].append(get_num(each[4]))
        data['ahn'].append(get_num(each[5]))
#%%
# append_data() 함수의 data 자리에 들어가는 dictionary        
election_result_raw = {'광역시도' : [],
                       '시군' : [],
                       'pop' : [],
                       'moon' : [],
                       'hong' : [],    
                       'ahn' : [] }
#%%
from bs4 import BeautifulSoup

for each_sido in sido_names_values:
    move_sido(each_sido)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    
    # read_html()은 HTML 프레임에 여러 개의 테이블이 있을 수 있는 데이터 프레임 목록을 생성
    df = pd.read_html(str(table))
    
    append_data(df, each_sido, election_result_raw)        
#%%

election_result = pd.DataFrame(election_result_raw, 
                               columns=['광역시도', '시군', 'pop', 'moon','hong','ahn'])
election_result
#%%
election_result.to_csv('../data/05. election_result.csv', encoding='utf-8', sep=',')   
#%%
driver.close()
#%%
'''6-3. 각 후보의 득표율과 지역 ID 정리하기'''
#%%
election_result = pd.read_csv('../data/05. election_result.csv', encoding='utf-8', 
                              index_col=0)
election_result.head()
#%%
sido_candi =  election_result['광역시도']
sido_candi = [name[:2] if name[:2] in ['서울','부산','대구','광주','인천','대전','울산']
                                    else '' for name in sido_candi]
sido_candi
# ''(공백처리) >>> 제주특별시 , 경기도,..., 강원도, 충청남도, 충청북도,...
#%%
# 중랑구 >>> 중랑, 마포, 의왕...
# 지도상 표기 코드와 맞추기 위한 밑작업.
def cut_char_sigu(name):
    return name if len(name)==2 else name[:-1]
# 이름이 2개면 그냥 출력
# 아니면 상록구에서 '구' 빼고 '상록'만 리턴하는 함수
#%%
import re

sigun_candi = ['']*len(election_result) #  250개

for n in election_result.index:
    each = election_result['시군'][n]
    if each[:2] in ['수원', '성남','안양','안산','고양',
                            '용인','청주','천안','전주','포항','창원']:
        sigun_candi[n] = re.split('시', each)[0]+' '+ cut_char_sigu(re.split('시', each)[1])
        # 수원시상록구  >>>  a=[수원, 상록구] >>>  a[0]='수원', a[1]=상록구 >>> cut_char_sigu(a[1])='상록'
    else:
        sigun_candi[n] = cut_char_sigu(each)
        
sigun_candi
#%%    
ID_candi = [sido_candi[n]+' '+sigun_candi[n] for n in range(0,len(sigun_candi))]

ID_candi = [name[1:] if name[0]==' ' else name for name in ID_candi]
ID_candi = [name[:2] if name[:2]=='세종' else name for name in ID_candi]

ID_candi
#%%
election_result['ID'] = ID_candi
election_result.head(10)
#%%
election_result[['rate_moon','rate_hong','rate_ahn']] = \
            election_result[['moon','hong','ahn']].div(election_result['pop'],  axis=0)
election_result[['rate_moon','rate_hong','rate_ahn']] *= 100
election_result.head()
#%%
election_result.sort_values(['rate_moon'], ascending=[False]).head(10)
#%%
election_result.sort_values(['rate_hong'], ascending=[False]).head(10)
#%%
election_result.sort_values(['rate_ahn'], ascending=[False]).head(10)
#%%
# 좌표
draw_korea = pd.read_csv('../data/05. draw_korea.csv', encoding='utf-8', index_col=0)
draw_korea.head()
#%%
set(draw_korea['ID'].unique()) - set(election_result['ID'].unique())
# set() 함수 자체가 .unique() 기능이 있으므로 굳이 달필요는 없다.
# 즉 사족임.
#%%
set(election_result['ID'].unique()) - set(draw_korea['ID'].unique())
#%%
election_result[election_result['ID'] == '고성']
#%%
election_result.loc[125, 'ID'] = '고성(강원)'
election_result.loc[233, 'ID'] = '고성(경남)'

election_result[election_result['시군'] == '고성군']
#%%
election_result[election_result['광역시도'] == '경상남도']
#%%
election_result.loc[228, 'ID'] = '창원 합포'
election_result.loc[229, 'ID'] = '창원 회원'

election_result[election_result['광역시도'] == '경상남도']
#%%
set(draw_korea['ID'].unique()) - set(election_result['ID'].unique())
#%%
set(election_result['ID'].unique()) - set(draw_korea['ID'].unique())
#%%
election_result[election_result['시군'] == '부천시']
#%%
election_result.tail()
#%%
# 지도 데이터 상에는 부천이 ['소사','오정','원미']로 3개로 나뉘어져 있지만
# 선거에선 '부천'으로 하나로 합쳐져 있으므로 이를 지도상에 표기하기 위해 3으로 나누어
# 각 지역으로 분배해서 나누어주어 지도상으로 시각화되게 한다.
ahn_tmp = election_result.loc[85, 'ahn']/3
hong_tmp = election_result.loc[85, 'hong']/3
moon_tmp = election_result.loc[85, 'moon']/3
pop_tmp = election_result.loc[85, 'pop']/3

rate_moon_tmp = election_result.loc[85, 'rate_moon']
rate_hong_tmp = election_result.loc[85, 'rate_hong']
rate_ahn_tmp = election_result.loc[85, 'rate_ahn']

election_result.loc[250] = ['경기도','부천시',pop_tmp,moon_tmp,hong_tmp,ahn_tmp,
                           '부천 소사', 
                           rate_moon_tmp, rate_hong_tmp, rate_ahn_tmp]
election_result.loc[251] = ['경기도','부천시',pop_tmp,moon_tmp,hong_tmp,ahn_tmp,
                           '부천 오정', 
                           rate_moon_tmp, rate_hong_tmp, rate_ahn_tmp]
election_result.loc[252] = ['경기도','부천시',pop_tmp,moon_tmp,hong_tmp,ahn_tmp,
                           '부천 원미', 
                           rate_moon_tmp, rate_hong_tmp, rate_ahn_tmp]
#%%
election_result[election_result['시군'] == '부천시']
#%%
election_result.drop([85], inplace=True)
election_result[election_result['시군'] == '부천시']
#%%
set(draw_korea['ID'].unique()) - set(election_result['ID'].unique())
#%%
set(election_result['ID'].unique()) - set(draw_korea['ID'].unique())
#%%
final_elect_data = pd.merge(election_result, draw_korea, how='left', on=['ID'])
final_elect_data.head()
#%%
final_elect_data['moon_v_hong'] = final_elect_data['rate_moon'] - final_elect_data['rate_hong']
final_elect_data['moon_v_ahn'] = final_elect_data['rate_moon'] - final_elect_data['rate_ahn']
final_elect_data['ahn_v_hong'] = final_elect_data['rate_ahn'] - final_elect_data['rate_hong']
final_elect_data.head()
#%%
final_elect_data.sort_values(['moon_v_hong'], ascending=[False]).head(10)
#%%
final_elect_data.sort_values(['moon_v_hong'], ascending=[True]).head(10)
#%%
'''6-4. 19대 대선 결과 득표율 시각화하기'''
#%%
BORDER_LINES = [
    [(5, 1), (5,2), (7,2), (7,3), (11,3), (11,0)], # 인천
    [(5,4), (5,5), (2,5), (2,7), (4,7), (4,9), (7,9), 
     (7,7), (9,7), (9,5), (10,5), (10,4), (5,4)], # 서울
    [(1,7), (1,8), (3,8), (3,10), (10,10), (10,7), 
     (12,7), (12,6), (11,6), (11,5), (12, 5), (12,4), 
     (11,4), (11,3)], # 경기도
    [(8,10), (8,11), (6,11), (6,12)], # 강원도
    [(12,5), (13,5), (13,4), (14,4), (14,5), (15,5), 
     (15,4), (16,4), (16,2)], # 충청북도
    [(16,4), (17,4), (17,5), (16,5), (16,6), (19,6), 
     (19,5), (20,5), (20,4), (21,4), (21,3), (19,3), (19,1)], # 전라북도
    [(13,5), (13,6), (16,6)], # 대전시
    [(13,5), (14,5)], #세종시
    [(21,2), (21,3), (22,3), (22,4), (24,4), (24,2), (21,2)], #광주
    [(20,5), (21,5), (21,6), (23,6)], #전라남도
    [(10,8), (12,8), (12,9), (14,9), (14,8), (16,8), (16,6)], #충청북도
    [(14,9), (14,11), (14,12), (13,12), (13,13)], #경상북도
    [(15,8), (17,8), (17,10), (16,10), (16,11), (14,11)], #대구
    [(17,9), (18,9), (18,8), (19,8), (19,9), (20,9), (20,10), (21,10)], #부산
    [(16,11), (16,13)], #울산
    [(27,5), (27,6), (25,6)],
]
#%%
def drawKorea(targetData, blockedMap, cmapname):
    gamma = 0.75

    whitelabelmin = 20.

    datalabel = targetData

    tmp_max = max([ np.abs(min(blockedMap[targetData])), 
                                  np.abs(max(blockedMap[targetData]))])
    vmin, vmax = -tmp_max, tmp_max

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    
    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, 
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. 
        #(중구, 서구)
        if len(row['ID'].split())==2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2]=='고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if np.abs(row[targetData]) > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()
#%%
drawKorea('moon_v_hong', final_elect_data, 'RdBu')
#%%
drawKorea('moon_v_ahn', final_elect_data, 'RdBu')    
#%%
drawKorea('ahn_v_hong', final_elect_data, 'RdBu')
#%%
import folium
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#%%
pop_folium = final_elect_data.set_index('ID')

del pop_folium['광역시도']
del pop_folium['시군']

pop_folium.head()
#%%
geo_path = '../data/05. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map = folium.Map(location=[36.2002, 127.054], zoom_start=6)
map.choropleth(geo_data = geo_str,
               data = pop_folium['moon_v_hong'],
               columns = [pop_folium.index, pop_folium['moon_v_hong']],
               fill_color = 'PuBu', #PuRd, YlGnBu
               key_on = 'feature.id')

map
