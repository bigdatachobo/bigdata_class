# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:31:51 2020

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import platform #운영 체제 
import seaborn as sns
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False 

if platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows':
    path="c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system')

import warnings
warnings.filterwarnings(action='ignore')    

import os

from sklearn.model_selection import train_test_split

#Scaling
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

#metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import *

# model
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import GridSearchCV, cross_validate

#Regression statsmodel
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# time
import time

# itertools
import itertools

import scipy

from sklearn.svm import SVR
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV, cross_validate
#%%

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')

data=pd.read_csv('../data/onion_columns_all_merge_final.csv')

#col=['전라남도','경상남도','경상북도','전라북도']
ela_col=['10a당 생산량 (kg)', '3월 일산화탄소', '10월 이산화질소', '11월 일산화탄소', '12월 아황산가스',
       '습도 1월', '12월 일산화탄소', '4월 일산화탄소', '강수량 5월', '일조시간 8월', '2월 오존',
       '최고기온 3월', '일조시간 7월', '최고기온 2월', '아연 Zn']
'''
df=pd.DataFrame()
for i in col:
    temp=data.loc[data['area']==i, :]
    df=pd.concat([df, temp], axis=0)

df.reset_index(inplace=True)
df.drop(['index'], 
        axis=1, 
        inplace=True)
'''
#df.index=df.year_local
df_ela=data[ela_col]
#%%
# Winsor
winsor = scipy.stats.mstats.winsorize

df_ws = pd.DataFrame()
for i in range(len(df_ela.columns)):
    a = pd.DataFrame(winsor(df_ela.iloc[:, i], limits = [0.01, 0.01]))
    df_ws = pd.concat([df_ws, a], axis = 1)
df_ws.columns=df_ela.columns
#%%
# MinMaxScaler
scaler=MinMaxScaler()
df_sc=scaler.fit_transform(df_ws)

df_mms=pd.DataFrame(df_sc,
                    columns=df_ws.columns)
#%%
df_mms.index=data.year_local
X=df_mms.iloc[:,1:]
y=df_mms['10a당 생산량 (kg)']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    random_state=0,
                                                    test_size=.2)
#%%
'''
xgb=XGBRegressor()

xgb_param_grid={
    'n_estimator' : list(range(1000,2000,100)),
    'learning_rate' : list(np.arange(0.026,0.03, 0.0001)),
    'max_depth' : list(range(1,4,1))
}
xgb_grid = GridSearchCV(xgb,
                        param_grid=xgb_param_grid,
                        n_jobs=-1,
                        verbose=1,
                        scoring='r2')
xgb_grid.fit(X_train, y_train)
print('final params:', xgb_grid.best_params_)
print('best score:', xgb_grid.best_score_)
'''
#%%
'''
model=XGBRegressor(learning_rate=0.02909999999999998,
                   max_depth=1,
                   n_estimators=1000)

model.fit(X_train,y_train)
y_pred=model.predict(X_test)
'''
#%%
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)
#%%
X_test_copy = X_test.copy()
X_test['pred'] = y_pred
X_test_copy['ans'] = y_test
y_pred_ori = scaler.inverse_transform(X_test)
y_test_ori = scaler.inverse_transform(X_test_copy)

y_test_ori[:,-1]
y_pred_ori[:,-1]
#%%
df_test_ori=pd.DataFrame(y_test_ori,
                         columns=X_test_copy.columns)
df_test_ori.rename(columns={'ans':'actual'},inplace=True)

df_pred_ori=pd.DataFrame(y_pred_ori,
                         columns=X_test.columns)
df_pred_ori.rename(columns={'pred':'predicted'},inplace=True)

df_test_ori.index=X_test.index
df_pred_ori.index=X_test.index
result=pd.concat([df_test_ori.iloc[:,-1],df_pred_ori.iloc[:,-1]],axis=1)
result.sort_values(by='year_local',inplace=True)
#%%
result.reset_index(inplace=True)
col=['전라남도','경상남도','경상북도','전라북도']

final=pd.DataFrame()
f_list=[]
for i in col:
    for j,sido in enumerate(result['year_local']):
        if sido.split('_')[1] == i:
            final=pd.concat([final,result.iloc[j,:]],axis=1)
final=final.T
final.sort_values(by='year_local',inplace=True)
final.reset_index(inplace=True)            
final.drop(['index'],axis=1,inplace=True)

final.index=final.year_local
final.drop(['year_local'], axis=1, inplace=True)
final.to_csv('../data/final.csv')            
#%%
plt.figure(figsize=(17,10))
plt.style.use('ggplot')
plt.plot(X_test.index,y_test_ori[:,-1], label='실제단수', c='orange')
plt.plot(X_test.index,y_pred_ori[:,-1], label = '예측단수', c='skyblue')
plt.title('양파 실제 단수와 예측 단수(kg/10a)')
plt.ylabel('단수(kg)')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('../image/onions.png')
plt.show()
#plt.savefig('../image/onions.png')
