# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:36:15 2019

@author: sundooedu
"""
#%%
'''
science_data.zip 파일을 이용하여

1. 조회순을 기준으로 그래프를 그려보세요.

2. Prophet모듈을 이용하여 forecast 예측해 보세요.

3. plot_components로 결과를 확인해 보세요.

4. 이 사이트는 유지해야 하나요? 아니면 닫아야 하나요?
'''
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
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from fbprophet import Prophet
from datetime import datetime
import numpy as np
#%%
df=pd.read_excel('../data/science_data/science_data.xlsx')
df.head()
df.fillna(value='미정', inplace=True)

df.plot(figsize=(12,6), x='등록일', y='조회수',color='blue',marker='.')
plt.grid()
#%%
df_pro=pd.DataFrame({'ds':df['등록일'], 'y':df['조회수']})
m=Prophet(daily_seasonality=True, yearly_seasonality=True)
m.fit(df_pro)
future=m.make_future_dataframe(periods=365)
#%%
forecast=m.predict(future)
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail()
#%%
m.plot(forecast,xlabel='연도', ylabel='조회수');
#%%
m.plot_components(forecast);
