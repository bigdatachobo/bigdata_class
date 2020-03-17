#!/usr/bin/env python
# coding: utf-8

# In[136]:

#%%
# load libraris 
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

    
from sklearn.model_selection import train_test_split

#Scaling
import scipy
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


#Feature Selection
from sklearn.decomposition import PCA, FactorAnalysis
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer import FactorAnalyzer

#Multicolinearity 
from statsmodels.stats.outliers_influence import variance_inflation_factor

#Regression statsmodel
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

#Decision Tree 
import matplotlib.pyplot as pl
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import validation_curve

#Winsorizer
import scipy.stats


#SVM
from sklearn.svm import SVR
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV, cross_validate

#metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

import time

#%% [FEATURE EXTRACTION] 

#### Data Loading

df = pd.read_csv('../projectdata/onion_columns_all_merge_final.csv')

df=df.iloc[:,3:]
X = df.iloc[:,1:]
y = df.iloc[:,0]

#%% Winsorizing for outlier control
winsor = scipy.stats.mstats.winsorize

df_ws = pd.DataFrame()

for i in range(len(df.columns)):
    a = pd.DataFrame(winsor(df.iloc[:, i], limits = [0.01, 0.01]))
    df_ws = pd.concat([df_ws, a], axis = 1)
df_ws.columns=df.columns
df_ws

#%% Data Scaling
df_columns = df_ws.columns.tolist()

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df_ws)
df_scaled = pd.DataFrame(df_scaled, columns = df_columns)

#IV(변수)와 DV(생산량)로 나누기  
X_scaled = df_scaled.iloc[:,1:]
y_scaled = df_scaled.iloc[:,0]

#%%
#다중공선성 가능성 확인 1.Correlation 
corr = pd.DataFrame(X_scaled.corr())
corr[(corr > 0.9) & (corr <1)].stack().reset_index()

#다중공선성 확인 2.VIF 
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(
    X_scaled.values, i) for i in range(X_scaled.shape[1])]
vif["features"] = X_scaled.columns
vif.sort_values('VIF Factor')

#%%
#모든 값이 0인 컬럼: ['적설량 7월', '적설량 8월', '적설량 9월', '적설량 10월', '적설량 5월', '적설량 6월'] 제거 
zeros = []
for i in X_scaled.columns.tolist():
    if X_scaled[i].mean() == 0:
        zeros.append(i)
        
for i in zeros:
    X_scaled.drop(i,axis=1, inplace=True)


#%% [MODELING] 
#Train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.3, random_state=0)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#%% Modeling1. Linear Regression 

#### 1-1. 이상적인 FACTOR 개수 찾기1(eigen value) --> eigen value가 1이 넘는 지점 factor#<22
fa = FactorAnalyzer(n_factors=11,  rotation=None)
fa.fit(X_scaled)
ev, v =fa.get_eigenvalues()
ev = pd.DataFrame(ev)
ev1 = ev[ev[0] >= 1]
plt.scatter(range(0,len(ev1)),ev1)
plt.plot(range(0,len(ev1)),ev1)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

####1-1.이상적인 FACTOR 개수 찾기2(Cummulative Variance) --> 최소 60% 이상의 설명력 갖는 지점 factor# >6
for i in range(4,7):  
    fa = FactorAnalyzer(n_factors=i,  rotation=None)
    fa.fit(X_scaled)
    print(fa.get_factor_variance()[2])

#### 2.Factor 개수별 모델 score 확인 
for i in range(6,23):
    fa = FactorAnalyzer(n_factors=i,  rotation=None)
    fa.fit(X_scaled)
    X_fc = pd.DataFrame(fa.transform(X_scaled))
   
    X_train, X_test, y_train, y_test = train_test_split(X_fc, y_scaled, test_size=0.2, random_state=0)

    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    y_train_pred = regressor.predict(X_train)
    
    print('\n# of factors: %s' %i)
    #Metrics 
    print('Test MAE:', mean_absolute_error(y_test, y_pred))  
    print('Test RMSE:', np.sqrt(mean_squared_error(y_test, y_pred)))

    #Adjusted Test R-squared 
    SS_Residual = sum((y_test-y_pred)**2)       
    SS_Total = sum((y_test-np.mean(y_test))**2)     
    r_squared = 1 - (float(SS_Residual))/SS_Total
    adjusted_r_squared = 1 - (1-r_squared)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)
    print ('R-squared:' ,r_squared,'\nAdjusted R-squared:',adjusted_r_squared)
    
#### Regression with ideal # of factor = 6 (점수 저장)
fa = FactorAnalyzer(n_factors=6,  rotation=None)
fa.fit(X_scaled)  
X_fc = pd.DataFrame(fa.transform(X_scaled))

X_train, X_test, y_train, y_test = train_test_split(X_fc, y_scaled, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)


MAE_lr =  round(mean_absolute_error(y_test, y_pred),3)
RMSE_lr = round(np.sqrt(mean_squared_error(y_test, y_pred)),3)
R_lr = round(regressor.score(X_test,y_test),3)

#### Factor 요소 설명
variable = X_scaled.columns.tolist()
factor_df = pd.DataFrame(fa.loadings_, index=variable)
 
for item in factor_df.columns.tolist():
    print(item, ':', factor_df[factor_df[item]>=0.5].index.values)


#%% Modeling2. SVR  
#SVR kernel='linear'
def svr_model_lr(X_train, y_train, X_test, y_test):
    tic=time.time()
    #best parameter extraction
    gsc = GridSearchCV(
        estimator=SVR(kernel='linear'),
        param_grid={
            'C': [0.1, 1, 100, 1000],
            'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]},
        cv=10, scoring='r2', verbose=1, n_jobs=-1)

    grid_result = gsc.fit(X, y)
    best_params = grid_result.best_params_
    
    #best model
    best_svr = SVR(kernel='rbf', C=best_params["C"], epsilon=best_params["epsilon"], gamma='auto',
                   coef0=0.1, shrinking=True,
                   tol=0.001, cache_size=200, verbose=False, max_iter=10000)
    
    #Fitting based on best model
    best_svr.fit(X_train, y_train)
    y_pred = best_svr.predict(X_test)
    
    #socres 
    global R_svr_li, MAE_svr_li, RMSE_svr_li
    R_svr_li = round(best_svr.score(X_test,y_test),3)
    MAE_svr_li = round(mean_absolute_error(y_test,y_pred),3)
    RMSE_svr_li = round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
    toc=time.time()    
    return ('Rsquare:',best_svr.score(X_test,y_test),
            '\nMAE:',mean_absolute_error(y_test,y_pred),
            '\nRMSE:',np.sqrt(mean_squared_error(y_test,y_pred)),
            '\nTime:',toc-tic)

#Training 
svr_model_lr(X_train,y_train,X_test,y_test)

#%%

#SVR kernel='rbf'
def svr_model_rbf(X_train, y_train, X_test, y_test):
    gsc = GridSearchCV(
        estimator=SVR(kernel='rbf'),
        param_grid={
            'C': [0.1, 1, 100, 1000],
            'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10],
            'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5]},
        cv=10, scoring='r2', verbose=0, n_jobs=-1)

    grid_result = gsc.fit(X_train, y_train)
    best_params = grid_result.best_params_
    best_svr_rbf = SVR(kernel='rbf', C=best_params["C"], epsilon=best_params["epsilon"], gamma=best_params["gamma"],
                   coef0=0.1, shrinking=True,
                   tol=0.001, cache_size=200, verbose=False, max_iter=10000)
    
    #Fitting based on best model
    best_svr_rbf.fit(X_train, y_train)
    y_pred = best_svr_rbf.predict(X_test)
    
    #socres 
    global R_svr_rbf, MAE_svr_rbf, RMSE_svr_rbf
    R_svr_rbf = round(best_svr_rbf.score(X_test,y_test),3)
    MAE_svr_rbf = round(mean_absolute_error(y_test,y_pred),3)
    RMSE_svr_rbf = round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
        
    return ('Rsquare:',best_svr_rbf.score(X_test,y_test),
            '\nMAE:',mean_absolute_error(y_test,y_pred),
            '\nRMSE:',np.sqrt(mean_squared_error(y_test,y_pred)))
    
#Training 
svr_model_rbf(X_train, y_train, X_test, y_test)


#%% XGboost

def xgb_reg(X_train,y_train,X_test,y_test):
  #최적의 파라미터 추출
    xgb_param_grid={
        'n_estimator' : list(range(1000,2000,100)),
        'learning_rate' : list(np.arange(0.0260,0.031, 0.0001)),
        'max_depth' : list(range(1,4,1))}
    xgb = GridSearchCV(XGBRegressor(),
                        param_grid=xgb_param_grid,
                        n_jobs=-1,
                        verbose=1,
                        scoring='r2')
    xgb_result = xgb.fit(X_train,y_train)
    best_params = xgb_result.best_params_
    
    #최적의 모델
    best_xgb = XGBRegressor(learning_rate=best_params["learning_rate"], 
                           max_depth=best_params["max_depth"], 
                           n_estimators=best_params["n_estimator"],
                           verbose=1, 
                           max_iter=10000)
    #최적의 모델로 데이터 핏팅
    best_xgb.fit(X_train, y_train)
    y_pred = best_xgb.predict(X_test)

    #점수 저장 
    global R_xgb, MAE_xgb, RMSE_xgb
    R_xgb = round(best_xgb.score(X_test,y_test),3)
    MAE_xgb = round(mean_absolute_error(y_test,y_pred),3)
    RMSE_xgb = round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
    
    return (best_xgb.score(X_test,y_test),
            mean_absolute_error(y_test,y_pred),
            np.sqrt(mean_squared_error(y_test,y_pred)))

xgb_reg(X_train,y_train,X_test,y_test)
            
#%% 

print('=====Linear Regression====')
print('MAE:', MAE_lr)
print('RMSE:', RMSE_lr)
print('R-squared', R_lr)

print('====SVR kernel linear====')
print('MAE:', MAE_svr_li)
print('RMSE:', RMSE_svr_li)
print('R-squared', R_svr_li)

print('====SVR kernel rbf====')
print('MAE:', MAE_svr_rbf)
print('RMSE:', RMSE_svr_rbf)
print('R-squared', R_svr_rbf)

print('====XgBoost====')
print('MAE:', MAE_xgb)
print('RMSE:', RMSE_xgb)
print('R-squared', R_xgb)

#%% 
'''
=====Linear Regression====
MAE: 0.128
RMSE: 0.158
R-squared 0.422
====SVR kernel linear====
MAE: 0.175
RMSE: 0.208
R-squared -0.008
====SVR kernel rbf====
MAE: 0.127
RMSE: 0.154
R-squared 0.451
====XgBoost====
MAE: 0.133
RMSE: 0.163
R-squared 0.384
'''
