#!/usr/bin/env python
# coding: utf-8

# #### Feature Selection 

#%% load libraris 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
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
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#Feature Selection
from sklearn.decomposition import PCA, FactorAnalysis
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer import FactorAnalyzer

#Multicolinearity 
from statsmodels.stats.outliers_influence import variance_inflation_factor

#Regression statsmodel
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

#SVM
from sklearn.svm import SVR
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV, cross_validate

#metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

#XGboost
from xgboost import XGBRegressor

#Winsorize
import scipy.stats

import time

#%% Data Loading 
df = pd.read_csv('../oniondata/onion_columns_all_merge_final.csv')
df=df.iloc[:,3:]

#%% Data Scaling 
df_columns = df.columns.tolist()
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = df_columns)
#%%
# IV(변수)와 DV(생산량)로 나누기  
X_scaled = df_scaled.iloc[:,1:]
y_scaled = df_scaled.iloc[:,0]

#%% multicolinearity 
# 다중공선성 가능성 확인 1.Correlation 
corr = pd.DataFrame(X_scaled.corr())
corr[(corr > 0.9) & (corr <1)].stack().reset_index()

# 다중공선성 확인 2.VIF 
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(
    X_scaled.values, i) for i in range(X_scaled.shape[1])]
vif["features"] = X_scaled.columns
vif.sort_values('VIF Factor')


#%% Feature Reduction - Stepwise


#전진선택법(step=1)

def forward(X, y, predictors):
    # 데이터 변수들이 미리정의된 predictors에 있는지 없는지 확인 및 분류
    remaining_predictors = [p for p in X.columns.difference(['const']) if p not in predictors]
    results = []
    for p in remaining_predictors:
        results.append(processSubset(X=X, y= y, feature_set=predictors+[p]+['const']))
    # 데이터프레임으로 변환
    models = pd.DataFrame(results)

    # AIC가 가장 낮은 것을 선택
    best_model = models.loc[models['AIC'].idxmin()] # index
    print("Processed ", models.shape[0], "models on", len(predictors)+1, "predictors in")
    print('Selected predictors:',best_model['model'].model.exog_names,' AIC:',best_model[0] )
    return best_model


# 후진선택법(step=1)
import itertools

def backward(X,y,predictors):
    results = []
    # 데이터 변수들이 미리정의된 predictors 조합 확인
    for combo in itertools.combinations(predictors, len(predictors) - 1):
        results.append(processSubset(X=X, y= y,feature_set=list(combo)+['const']))
    models = pd.DataFrame(results)
    # 가장 낮은 AIC를 가진 모델을 선택
    best_model = models.loc[models['AIC'].idxmin()]
    print("Processed ", models.shape[0], "models on", len(predictors) - 1, "predictors in")
    print('Selected predictors:',best_model['model'].model.exog_names,' AIC:',best_model[0] )
    return best_model

# Subset 
def processSubset(X,y, feature_set):
            X = sm.add_constant(X)
            model = sm.OLS(y,X[list(feature_set)]) # Modeling
            regr = model.fit() # 모델 학습
            AIC = regr.aic # 모델의 AIC
            return {"model":regr, "AIC":AIC}


# 단계선택법
def Stepwise_model(X,y):
    Stepmodels = pd.DataFrame(columns=["AIC", "model"])
    predictors = []
    Smodel_before = processSubset(X,y,predictors+['const'])['AIC']
    # 변수 1~10개 : 0~9 -> 1~10
    for i in range(1, len(X.columns.difference(['const'])) + 1):
        Forward_result = forward(X=X, y=y, predictors=predictors) # constant added
        print('forward')
        Stepmodels.loc[i] = Forward_result
        predictors = Stepmodels.loc[i]["model"].model.exog_names
        predictors = [ k for k in predictors if k != 'const']
        Backward_result = backward(X=X, y=y, predictors=predictors)
        if Backward_result['AIC']< Forward_result['AIC']:
            Stepmodels.loc[i] = Backward_result
            predictors = Stepmodels.loc[i]["model"].model.exog_names
            Smodel_before = Stepmodels.loc[i]["AIC"]
            predictors = [ k for k in predictors if k != 'const']
            print('backward')
        if Stepmodels.loc[i]['AIC']> Smodel_before:
            break
        else:
            Smodel_before = Stepmodels.loc[i]["AIC"]
    return (Stepmodels['model'][len(Stepmodels['model'])])


# Running Stepwise 
Stepwise_best_model=Stepwise_model(X_scaled,y_scaled)

# Result Summary 
Stepwise_best_model.summary()


#%% Selected Variables from the result
result = pd.DataFrame( {'coefficients': Stepwise_best_model.params, 'pvalue': Stepwise_best_model.pvalues})
result

#select only coefficients with pvalue less than 0.05
variable_list = result[result.pvalue < 0.05].index.values.tolist()
variable_list



#%% 단계적 선택법을 통해 추출된 변수만 적용된 데이터셋 준비  
sw_selected= pd.concat([df[variable_list], df['10a당 생산량 (kg)']],axis=1)

#%% Winsor
winsor = scipy.stats.mstats.winsorize

df_ws = pd.DataFrame()

for i in range(len(sw_selected.columns)):
    a = pd.DataFrame(winsor(sw_selected.iloc[:, i], limits = [0.01, 0.01]))
    df_ws = pd.concat([df_ws, a], axis = 1)
df_ws.columns=sw_selected.columns
df_ws

#%% Scaling 
sw_selected_columns = sw_selected.columns.tolist()

scaler = MinMaxScaler()
df_sw = scaler.fit_transform(df_ws)
df_sw = pd.DataFrame(df_sw, columns = sw_selected_columns)

y_sw = df_sw.iloc[:,-1]
X_sw = df_sw.iloc[:,:-1]
#%% 다중공선성 확인 
#Correlation (변수간 상관관계) 
X_sw_corr = X_sw.corr()
import seaborn as sns 
plt.figure(figsize=(10,8))
sns.heatmap(X_sw_corr,annot = True,  cmap="Blues") #correlation 수치가 높은 변수들이 없으므로 변수 모두 선택

#%% MODELING 

#split 
X_train, X_test, y_train, y_test = train_test_split(X_sw, y_sw, test_size=0.2, random_state=0)

#%% Modeling1. Linear Regression 
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)

#MSE, RMSE 
print('\nTest MAE:', mean_absolute_error(y_test, y_pred))  
print('Test MSE:',mean_squared_error(y_test, y_pred))  
print('Test RMSE:', np.sqrt(mean_squared_error(y_test, y_pred)))

#R-squared 
print('Test R:', r2_score(y_test,y_pred))

MAE_lr =  round(mean_absolute_error(y_test, y_pred),3)
RMSE_lr = round(np.sqrt(mean_squared_error(y_test, y_pred)),3)
R_lr = round(r2_score(y_test,y_pred),3)

#%% Modeling2. SVR  
#SVR kernel='linear'
def svr_model_lr(X_train, y_train, X_test, y_test):
    
    #best parameter extraction
    gsc = GridSearchCV(
        estimator=SVR(kernel='linear'),
        param_grid={
            'C': [0.1, 1, 100, 1000],
            'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]},
        cv=10, scoring='r2', verbose=0, n_jobs=-1)

    grid_result = gsc.fit(X_train, y_train)
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
        
    return ('Rsquare:',best_svr.score(X_test,y_test),
            '\nMAE:',mean_absolute_error(y_test,y_pred),
            '\nRMSE:',np.sqrt(mean_squared_error(y_test,y_pred)))

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
MAE: 0.096
RMSE: 0.126
R-squared 0.634
====SVR kernel linear====
MAE: 0.142
RMSE: 0.169
R-squared 0.34
====SVR kernel rbf====
MAE: 0.102
RMSE: 0.132
R-squared 0.598
====XgBoost====
MAE: 0.139
RMSE: 0.164
R-squared 0.379
'''
