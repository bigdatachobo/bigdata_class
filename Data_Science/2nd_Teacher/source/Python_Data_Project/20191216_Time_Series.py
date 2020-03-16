# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:17:11 2019

@author: sundooedu
"""
#%%
'''7장 시계열 데이터를 다뤄보자'''
#%%
'''7-1. Numpy의 polyfit으로 회귀(regression) 분석하기'''
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
pinkwink_web = pd.read_csv('../data/08. PinkWink Web Traffic.csv', 
                                          encoding='utf-8', thousands=',',
                                          names = ['date','hit'], index_col=0)
pinkwink_web = pinkwink_web[pinkwink_web['hit'].notnull()]
pinkwink_web.head()
#%%
pinkwink_web['hit'].plot(figsize=(12,4), grid=True);
#%%
time = np.arange(0,len(pinkwink_web))
traffic = pinkwink_web['hit'].values

fx = np.linspace(0, time[-1], 1000)
#%%
def error(f, x, y):
    return np.sqrt(np.mean((f(x)-y)**2))
#%%
fp1 = np.polyfit(time, traffic, 1)
f1 = np.poly1d(fp1)

f2p = np.polyfit(time, traffic, 2)
f2 = np.poly1d(f2p)

f3p = np.polyfit(time, traffic, 3)
f3 = np.poly1d(f3p)

f15p = np.polyfit(time, traffic, 15)
f15 = np.poly1d(f15p)

print(error(f1, time, traffic))
print(error(f2, time, traffic))
print(error(f3, time, traffic))
print(error(f15, time, traffic))
#%%
plt.figure(figsize=(10,6))
plt.scatter(time, traffic, s=10)

plt.plot(fx, f1(fx), lw=4, label='f1')
plt.plot(fx, f2(fx), lw=4, label='f2')
plt.plot(fx, f3(fx), lw=4, label='f3')
plt.plot(fx, f15(fx), lw=4, label='f15')

plt.grid(True, linestyle='-', color='0.75')

plt.legend(loc=2)
plt.show()
#%%
'''7-2. Prophet 모듈을 이용한 forecast 예측'''
#%%
now=datetime.now()
print(now)
#%%
nowDate=now.strftime('%Y-%m-%d')
print(nowDate)
#%%
df = pd.DataFrame({'ds':pinkwink_web.index, 'y':pinkwink_web['hit']})
df.reset_index(inplace=True)
df['ds'] =  pd.to_datetime(df['ds'], format="%y. %m. %d.")
del df['date']

m = Prophet(yearly_seasonality=True)
m.fit(df)
#%%
'''periods 기간을 설정 predict를 통해 예측( 향후 60일간의 예측값을 확인 )'''
future = m.make_future_dataframe(periods=60) # 60일 후의 데이터를 예측
future.tail()
#%%
'''Prophet 오브젝트의 predict 메소드를 사용'''
'''yhat: 예측 결과, 
   yhat_lower: 예측 최소 값, 
   yhat_upper:예측 최대 값'''
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#%%
m.plot(forecast);  
#%%
m.plot_components(forecast); 
#%%
'''7-3. Seasonal 시계열 분석으로 주식 데이터 분석하기'''
#%%
from pandas_datareader import data

start_date = datetime(2017,1,1) 
end_date = datetime(2017,4,30)
ks = data.get_data_yahoo("^KS11",start_date, end_date) # KOSPI 지수
#ks = data.DataReader("^KS11","yahoo",start_date, end_date)
ks.head()
#%%
'''삼성 주가 가져오기'''
from pandas_datareader import data

start_date = datetime(2009,7,1) 
end_date = datetime(2019,7,31)
ss = data.get_data_yahoo("005930.KS",start_date, end_date) # KOSPI 지수
ss.head()
ss.tail()
#%%
ss['Close'].plot(figsize=(12,6), grid=True);
#%%
ss_trunc = ss[:'2016-12-31'] # 일부 구간을 짤라내어 결과 예측에 사용
ss_trunc
#%%
df = pd.DataFrame({'ds':ss_trunc.index, 'y':ss_trunc['Close']})
df.reset_index(inplace=True)
del df['Date']
df.head()
#%%
m = Prophet(daily_seasonality=True)
m.fit(df);
#%%
future = m.make_future_dataframe(periods=365)
future.tail()
#%%
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#%%
''' 삼성 주시 그리기 '''
m.plot(forecast);
#%%
m.plot_components(forecast);
#%%
'''카카오 주식 가져오기'''
from pandas_datareader import data

start_date = datetime(2009,7,1) 
end_date = datetime(2019,7,31)
kk = data.get_data_yahoo("035720.KS",start_date, end_date) # KOSPI 지수
kk.head()
#%%
kk_trunc=kk[:'2017-12-31'] # 일부 구간을 짤라내어 결과 예측에 사용
#%%
df2 = pd.DataFrame({'ds':kk_trunc.index, 'y':kk_trunc['Close']})
df2.reset_index(inplace=True)
del df2['Date']
df2.head()
#%%
m2 = Prophet(daily_seasonality=True)
m2.fit(df2);
#%%
future2 = m2.make_future_dataframe(periods=365)
future2.tail()
#%%
forecast2 = m2.predict(future2)
forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#%%
''' 카카오 주식 그래프 그리기 '''
m2.plot(forecast2);
#%%
m2.plot_components(forecast2);
#%%
'''삼성 주가 가져오기 및 끝부분제거하고 예측 모델로 실제와 예측값 비교하기.'''
#%%
from pandas_datareader import data

start_date = datetime(2014,1,1) 
end_date = datetime(2017,7,31) 
'''
삼성 주가 = '005930.KS'
'''
KIA = data.get_data_yahoo('005930.KS', start_date, end_date)
KIA['Close'].plot(figsize=(12,6), grid=True);
#%% 
''' 
2017년 5월 31일 이전 날짜 주가만 사용 이후는 예측할려고함.
KIA 주가 불러오는게 에러나서 삼성으로 바꿈.
'''
KIA_trunc = KIA[:'2017-05-31']
KIA_trunc['Close'].plot(figsize=(12,6), grid=True);
#%%
df3 = pd.DataFrame({'ds':KIA_trunc.index, 'y':KIA_trunc['Close']})
df3.reset_index(inplace=True)
del df3['Date']
#%%
m3 = Prophet(daily_seasonality=True)
m3.fit(df3);
#%%
'''
61일간을 예측함. >>> 2달치 예측
'''
future3 = m3.make_future_dataframe(periods=61) 
future3.tail()
#%%
forecast3 = m3.predict(future3)
m3.plot(forecast3);
#%%
plt.figure(figsize=(12,6))
plt.plot(KIA.index, KIA['Close'], label='real')
plt.plot(forecast3['ds'], forecast3['yhat'], label='forecast')
plt.grid()
plt.legend()
plt.show()
#%%
'''
7-4 Growth Model과 Holiday Forecast
'''
df4 = pd.read_csv('../data/08. example_wp_R.csv')
df4['y'] = np.log(df4['y'])
df4
#%%
df4['cap'] = 8.5 # 상한값
df4['floor'] = 5 # 하한값
#%%
m4 = Prophet(growth='logistic', daily_seasonality=True)
m4.fit(df4)
#%%
future4 = m4.make_future_dataframe(periods=1826)
future4['cap'] = 8.5 # 상한값
future4['floor'] = 5 # 하한값
fcst = m4.predict(future4)
m4.plot(fcst);
print(future4)
#%%
forecast4 = m4.predict(future4)
m4.plot_components(forecast4);
#%%
'''
holiday
'''
df5 = pd.read_csv('../data/08. example_wp_peyton_manning.csv')
df5['y'] = np.log(df5['y'])
m5 = Prophet(daily_seasonality=True)
m5.fit(df5)
future5 = m5.make_future_dataframe(periods=366)
#%%
df5.y.plot(figsize=(12,6), grid=True);
#%%
playoffs = pd.DataFrame({
  'holiday': 'playoff',
  'ds': pd.to_datetime(['2008-01-13', '2009-01-03', '2010-01-16',
                        '2010-01-24', '2010-02-07', '2011-01-08',
                        '2013-01-12', '2014-01-12', '2014-01-19',
                        '2014-02-02', '2015-01-11', '2016-01-17',
                        '2016-01-24', '2016-02-07']),
  'lower_window': 0,
  'upper_window': 1,
})
superbowls = pd.DataFrame({
  'holiday': 'superbowl',
  'ds': pd.to_datetime(['2010-02-07', '2014-02-02', '2016-02-07']),
  'lower_window': 0,
  'upper_window': 1,
})
holidays = pd.concat((playoffs, superbowls))
#%%
m5 = Prophet(holidays=holidays, daily_seasonality=True)
forecast = m5.fit(df).predict(future5)
#%%
forecast[(forecast['playoff'] + forecast['superbowl']).abs() > 0][
        ['ds', 'playoff', 'superbowl']][-10:]
#%%
m5.plot(forecast);
#%%
m5.plot_components(forecast);
#%%
















