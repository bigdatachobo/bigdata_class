# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:14:59 2019

@author: sundooedu
"""
#%%
'''
시계열 데이터 분석 : 기아차 주식을 분석하세요.

1. 2009.01.01~ 2017.12.31일 까지의 시세를 확인하세요.

2. 1.의 기간의 종가(Close)를 기준으로 그래프를 그려 보세요.

3. 1년 후, 2018.12.31일 까지의 정보를 예측해 보세요.

4. 700일 간의 데이터를 예측해 보세요.
실제 데이터와 예측값을 그래프로 그려 보세요.
'''
#%%
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
%matplotlib inline

from fbprophet import Prophet
from datetime import datetime
import numpy as np
#%%
path = "c:/Windows/Fonts/malgun.ttf"
import platform
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
'''
1. 2009.01.01~ 2017.12.31일 까지의 시세를 확인하세요.
'''
from pandas_datareader import data

start_date = datetime(2009,1,1) 
end_date = datetime(2019,12,16) # 아싸리 지금현재 시점까지 데이터 불러옮.
'''
기아차 주가 = '000270.KS'
'''
KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
'''
2. 1.의 기간의 종가(Close)를 기준으로 그래프를 그려 보세요.
'''
KIA['Close'].plot(figsize=(12,6), grid=True);
#%%
KIA_trunc = KIA[:'2017-12-31']
KIA_trunc['Close'].plot(figsize=(12,6), grid=True);
#%%
df = pd.DataFrame({'ds':KIA_trunc.index, 'y':KIA_trunc['Close']})
df.reset_index(inplace=True)
del df['Date']
#%%
m = Prophet(daily_seasonality=True)
m.fit(df);
help(Prophet)
#%%
''' 1년치 예상 '''
future = m.make_future_dataframe(periods=365) 
future.tail()
#%%
forecast = m.predict(future)
m.plot(forecast);
#%%
'''700일 예상'''
future2 = m.make_future_dataframe(periods=700) 
future2.tail()
forecast2 = m.predict(future2)
m.plot(forecast2);
#%%
'''1년치 예상 그래프와 실제 데이터'''
plt.figure(figsize=(12,6))
plt.plot(KIA.index, KIA['Close'], label='real')
plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
plt.grid()
plt.legend()
plt.show()
#%%
'''700일치 예상 그래프와 실제 데이터'''
plt.figure(figsize=(12,6))
plt.plot(KIA.index, KIA['Close'], label='real')
plt.plot(forecast2['ds'], forecast2['yhat'], label='forecast')
plt.grid()
plt.legend()
plt.show()
