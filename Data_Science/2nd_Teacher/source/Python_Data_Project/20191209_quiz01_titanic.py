# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:12:54 2019

@author: sundooedu
"""
#%%
'''
아래 문제를  해결해 보세요.

titanic = sns.load_dataset("titanic")

1. 전체 승객를 나이별로 히스토그램으로 나타내세요.

2. 남/여 승객수를 나타내세요.(countplot)

3. 객실별 승객수를 출력해 보세요.(countplot)

4. 남/여 성별 사망자와 생존자를 나타내 보세요.(countplot)

5. 아래와 같이 2개의 데이터 프레임을 만드세요.

df1 = [{'name': 'John', 'job': "teacher"},
{'name': 'Candy', 'job': "student"},
{'name': 'Fred', 'job': "developer"}]

df2 = [{'name': 'Ed', 'job': "engineer"},
{'name': 'Jack', 'job': "farmer"},
{'name': 'James', 'job': "student1"}]

6. 컬럼 이름을 'name', 'job'으로 주세요.

7. 만드신 2개의 데이터 프레임을 새로운 로우(row)로 합치세요.

8. 데이터프레임을 첫번째 데이터프레임의 새로운 컬럼(column)으로 합치세요.
'''
#%%
import numpy as np
import pandas as pd
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
''' 타이타닉 데이터 '''
titanic = sns.load_dataset("titanic")
#%%
'''
1. 전체 승객를 나이별로 히스토그램으로 나타내세요.
'''
#%%
sns.countplot(x="age", data=titanic)
plt.title("나이별, 승객 수")
plt.show()
#%%
'''
2. 남/여 승객수를 나타내세요.(countplot)
'''
#%%
sns.countplot(x="sex", data=titanic)
plt.title("성별, 승객 수")
plt.show()
#%%
'''
3. 객실별 승객수를 출력해 보세요.(countplot)
'''
#%%
sns.countplot(x="class", data=titanic)
plt.title("객실별, 승객 수")
plt.show()
#%%
'''
4. 남/여 성별 사망자와 생존자를 나타내 보세요.(countplot)
'''
#%%
sns.countplot(x="sex",hue="alive", data=titanic)
plt.title("성별 사망자/생존자, 승객 수")
plt.show()
help(sns.countplot)
#%%
'''
5. 아래와 같이 2개의 데이터 프레임을 만드세요.
'''
#%%
df1 = [{'name': 'John', 'job': "teacher"},
       {'name': 'Candy', 'job': "student"},
       {'name': 'Fred', 'job': "developer"}]

df2 = [{'name': 'Ed', 'job': "engineer"},
       {'name': 'Jack', 'job': "farmer"},
       {'name': 'James', 'job': "student1"}]
t_df1=pd.DataFrame(df1)
t_df2=pd.DataFrame(df2)
#%%
'''
6. 컬럼 이름을 'name', 'job'으로 주세요.
'''
#%%
'''
7. 만드신 2개의 데이터 프레임을 새로운 로우(row)로 합치세요.
'''
#%% 
'''
병합할 DataFrame들을 "[df1,df2]" 대괄호로 묶어준다.
'''
t1_df1_df2=pd.concat([t_df1,t_df2], axis=0)
 #%%
'''
8. 데이터프레임을 첫번째 데이터프레임의 새로운 컬럼(column)으로 합치세요.
'''
#%%
t2_df1_df2=pd.concat([t_df1,t_df2], axis=1)







