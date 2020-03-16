# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:12:31 2019

@author: sundooedu
"""

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 정규화: 점수, 등급수 컬럼을 최대값으로 나눔
def norm(col,mx):  # 정규화
    return col / mx

# 국/영 점수    
data = {'kor':[90,80,70,80,75],
        'eng':[100,95,90,80,80]
        }

# 학번 인덱스 추가
df = pd.DataFrame(data,index=np.arange(1,5+1))
# 수학 등급수
math = pd.Series(np.random.randint(1,10+1,5), index=np.arange(1,5+1))

df['math'] = math # df에 컬럼 'math'를 추가하고 값으로 math를 넣는다는 의미.

# 모든열, 모든행에 norm() 함수 적용.
# col(열)이 norm()의 첫번째인자
# max(col)가 norm()의 두번째인자
# list(map(function, 열)) 호출 정규화된 세개의 국/영/수 열(컬럼)이 
# 하나의 새로운 DataFrame으로 병합이 된다.
df1 = df.apply(lambda col: norm(col,np.max(col)),axis=0) # df의 모든 행, 모든값, 모든열의 값들을 함수 norm()을 적용하여 바꿔준다.
# df의 column이 iterable이 되어 lambda col에 들어가게되고 함수 norm(col,mx)에 적용되어 열의 값들이
# 정규화되고 다시 새로운 열들이 만들어지고 이를 모아 apply()함수가 새로운 DataFrame을 만든다. >>> df1
# map을 세번 호출(열이 세개 이므로)하는 거라고 보면된다.

#%%
# up-version

def norm2(col):
    return col/np.max(col) # 함수 내에서 mx를 계산하도록 분모로 넣어준다.

df1=df.apply(norm2,axis=0) # 함수의 인자를 빼고 함수만 적어넣는다.

#%%
# 평균 리턴함수
def avg(row):
    #return np.average(row)
    return row.mean()    

# df1의 각행이 avg() 전달되고 평균이 리턴
avg=df1.apply(avg,axis=1)
avg
df1['avg'] = avg # df1에 'avg'컬럼을 추가하고 값에는 avg 값들을 넣는다.
#%%
# 시각화
#df.plot(kind='bar')
#df1.plot(kind='bar')
#help(plt.plot)
#plt.plot(df,'ro--') # 통합인자 색상=red >>>r / 마커='o'/ 라인= --
#plt.legend(['kor','eng','math']) # 범주 추가해도 색깔 구별이 안되어 주석처리함.
plt.rc('font',family='Malgun Gothic')
plt.xticks(df.index)

plt.plot(df['kor'],'ro--',label='kor') # plot(data,style,label)
plt.plot(df['eng'],'gv-',label='eng')
plt.plot(df['math'],'b^-',label='math')
plt.plot(df1['avg'],'y>-',label='avg')

plt.title('성적',fontsize=20)
plt.xlabel('학번',fontsize=16)
plt.ylabel('점수',fontsize=16)
plt.legend() # 범주명이 적용/ 범주는 항상 마지막에
#%%
plt.figure(figsize=(10,7))

# 첫번째 점수 subplot
plt.subplot(211) # 쉼표없이 표현 가능 plt.subplot(2,1,1)
plt.xticks(df.index)
plt.title('국/영/수 성적',fontsize=20)
plt.plot(df['kor'],'ro--',label='kor') # plot(data,style,label)
plt.plot(df['eng'],'gv-',label='eng')
plt.plot(df['math'],'b^-',label='math')
plt.legend()

# 두번째 평균 subplot
plt.subplot(2,1,2)
plt.xticks(df.index)
plt.title('국/영/수 정규화 평균',fontsize=20)
plt.plot(df1['avg'],'y>-',label='avg')
#plt.bar(df1.index,df1['avg'])

plt.legend() 
plt.tight_layout()

# 최상위 학생 1명 강조 표시.
top = df1.sort_values(by='avg',ascending=False).head(1).index[0]
plt.axvspan(top-0.15,top+0.15,facecolor='gray',alpha=0.5) # alpha >>> 투명도/ (투명)0<= alpha <= 1(불투명)/ 0.5(반투명)

plt.savefig('plt.png') # 분석한 plot 그림파일로 저장

# 상위 점수평균 3개(내림정렬 top-3)
df1.sort_values(by='avg',ascending=False).head(3) # head(n) : 앞에서 n개를 뽑아 출력.

for val in df1['avg']:
    print(val)
    
for idx,val in df1['avg'].iteritems():
    print(idx,val)    
#%%
# quiz
# 과학점수(sci열) 추가
# 평균을 바플롯으로 표현 
# 평균이 60% 이상이면 True 아니면 False인 합격여부(Pass열)를 df1에 추가.
    
# 1.
sci=pd.Series(np.random.randint(5,101,5),index=np.arange(1,5+1))
df['sci'] = sci    
plt.plot(df['sci'],'mo--',label='sci')

# 2.
plt.bar(df1.index,df1['avg'])

# 3.
# 내풀이
def pass_determine(n):
    if n >= 0.6:
        result = True
    else:
        result = False
    return result

pass_deter=df1['avg'].apply(lambda avg:pass_determine(avg))        

df1['pass'] = pass_deter

# 선생님 풀이
df1["pass"] = (df1["avg"] >= 0.6)&(df1["kor"] >= 0.4) #  df1["kor"] >= 0.4 과락 40% 이상인 경우를 뜻함.
#%%

