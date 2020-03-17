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

import time

#%% Data Loading 
df = pd.read_csv('../oniondata/onion_columns_all_merge_final.csv')

df=df.iloc[:,3:]

#%% Data Scaling 
df_columns = df.columns.tolist()

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = df_columns)


# In[ ]:


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

X_sw = sw_selected.iloc[:,:-1]
y_sw = sw_selected.iloc[:,-1]

#%% 다중공선성 확인 
#Correlation (변수간 상관관계) 
X_sw_corr = X_sw.corr()
import seaborn as sns 
plt.figure(figsize=(10,8))
sns.heatmap(X_sw_corr,annot = True,  cmap="Blues") #correlation 수치가 높은 변수들이 없으므로 변수 모두 선택

#%% MODELING 




