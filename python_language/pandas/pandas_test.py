# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:23:22 2019

@author: sundooedu
"""
#%%
import pandas as pd
import numpy as np
obj = pd.Series([4, 7, -5, 3]) # 리스트
# python 리스트나 또는 numpy array 등이 함수 인자로 입력됨.
obj = pd.Series(np.array([4,7,-5,3])) # numpy array
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c']) # 요소의 개수와 인덱스 갯수를 맞춰준다.
#인덱싱이 "키" 또는 "정수" 가능

obj.index
obj2.index
obj.values

a=obj2[['a','b','c','d']] # ','로 key값을 표시할때는 []로 묶어준다.
a=obj2[:]
a=obj2['a':'c']
a
a=obj2[0:2] # 숫자 인덱스로도 출력 가능. but 권장하지 않음.: 이미 key 값을 정의 했으므로 key값을 써야되기 때문.
#%%
import pandas as pd
import numpy as np
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])

lst=[[1,np.nan],[2,-3],[0.75,np.random.randint(1,10)]]
arr=np.array(lst)
df = pd.DataFrame(arr,columns=['one','two'],index=['a','b','c'])
df.columns
df.index

df['a':'c'] # 문자로 슬라이싱시 맨끝자리도 포함되어 표시됨.
df[0:2] # 정수 인덱스 가능 O
df['one'] # 열 인덱싱이 기본임. *df[열][행]
df['two']['a'] # 열/행 순으로 표기.
df['one':'two'] # 결과값 안나온다. # 행이 ':'으로 표기 / 열은 df[[열1, 열2]]처럼 표시
df[['one','two']] #인덱스 리스트 O(됨) # df[[C1,C2]][R1:R2] [C1,C2]:열은 ','로 구분/ [R1:R2]:행은 ':'슬라이싱 기반으로 구분함.

#행슬라이싱
df['a':'b'] # 슬라이싱 O
df[['a','b']] # 인덱스 리스트 X (안됨) / 열만 이런 형식으로 슬라이싱됨.


df = pd.DataFrame(arr)
df[[0,1]] # 정수 인덱스 X
df[0][0]
#%%
# 행-인덱스와 열-인덱스를 동시에 함께 지정.

# df.loc[:,:] : 구간 선택시 슬라이싱으로 한다.
# df.loc[[],[]] : 개별 행/열 선택시 "[]"를 [행-영역,열-영역]에 집어넣어준다.

df.loc['a':'b'] 
df.loc['a':'b',:] # 일반화하여 행선택시: [R1:R3,:] / 열 선택시: [:,C1:C4] 선택하지 않은 영역에도 ':'을 붙여준다.
df.loc[:,:] # 전체 선택시
df.loc['a'] # loc는 기본 행명으로 인지
df.loc[:,'one'] # df.loc[R1:R2, C1:C2]  [R1:R2]:행 ':'로 구분 / [C1:C2]:열은 ':'로 구분
# df.loc[:,C1] : 행전체 불러오고/ C1 열만 추출할 경우.

df.loc[:,'one':'two'] # 행전체 불러오고/ one에서 two까지 불러오기
df.loc[['a'],['one']] # loc[행-명,컬럼-명]
df.loc[:,:]

df.loc[['a','c'],['one','two']] # 특정 행/열을 가져올때는 [['R2','R7'], ['C1','C9']] 형식으로 "[]"를 "행,열" 영역에 적용한다.
#%%
# df.i(index)loc/ 기본 df.loc에 인덱스를 사용하는 방법일뿐 같음.
df.iloc[0:2]
df.iloc[0:2,:]
df.iloc[0] # 오류 iloc는 기본 행명
df.iloc[:,0]

df.iloc[:,0:2]
df.iloc[[0],[0]] # loc[행명, 컬럼명]
df.iloc[[0,2],[0,1]]
#%% 
# .loc/ .iloc 상관없이 둘다 혼용해용 사용 가능한 함수.
df.ix['a':'b']
df.ix[0:2]
#%%
# -> DataFrame
# 키값이 컬럼명
# 운전자 이름/ 년도/ 벌점
import pandas as pd
import numpy as np
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

# 행명 추가
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
"year": [2014, 2015, 2016, 2015, 2016],
"points": [1.5, 1.7, 3.6, 2.4, 2.9]}
# 열-순서 변경, 새로운 penalty(nan = null) 추가
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])

#%%
df.loc['one','points']
df.loc[:,'names'] # 모든 운전자 조회
df.iloc[0,:]
df.iloc[0]
df.loc[:,['names','points']]
df.iloc[:,[0,2]]

df["penalty"] = [0.1, 0.2, 0.3, 0.4, 0.5] # key값으로 "penalty"주고 value 값으로 리스트로 추가하기
df["zeros"] = np.arange(5) # key값으로 "zeros"주고 value 값으로 np.arange(5)로 array로 준다.

# 붙이려고한 테이블 index와 붙일 자료형의 index를 일치시켜준다.
#val = pd.Series([-1.2, -1.5, -1.7, -1.1, -1.4],index=["one", "two", "three", "four", "five"])
#df["debt"] = val
val = pd.Series([-1.2, -1.5, -1.7, -1.1, -1.5])
df["debt"] = val
df["debt"] = -1.0

c=np.random.rand(5)
# where ( c<0.5 면 >>> 0으로 아니면 c(원래값))
# where (if c<0.5: return 0 / else: c)
c=np.where(c<0.5,0,c) # c 요소 성분이 0.5 미만이면 (c<0.5) / 0으로 바꿔서 출력하고 (0) / 0.5보다 크면 원래값으로 출력 (c)
val = pd.Series(-c) # c 앞에 '-' 붙여주면 음수가됨.
df["debt"] = val
df.loc[0,'debt']=-1
df.debt=val

# 기존열에 계산된 파생열을 추가할 수 있음.
df["net_points"] = df["points"] - df["penalty"]
df["high_points"] = df["net_points"] > 2.0

#%%
df.loc[df["year"] > 2014]

df.loc[df["names"] == "Kilho", ["names", "points"]]

df.loc[(df["points"] > 2) & (df["points"] < 3), :] # "&" : AND / "|" : OR
df.loc[(df["points"] == 2.4) | (df["points"] == 2.9), :]
#%%
df.columns
# 5행 모든 열에 리스트를 집어넣는다.
# 행-추가
df.loc[5,:] = ['Smith',2014,4.0,0.1,5,0.7]
df.loc[6,:] = ['Scott',2017,3.5,0.3,6,0.4]
df.loc[:,:]

df["net_points"] = df["points"] - df["penalty"]
df["high_points"] = df["net_points"] > 2.0
#%%
pd.date_range('20191114',freq='D',periods=6)
pd.date_range('20191114',periods=6)
# MS( >>> 각 월의 첫날) 6개
pd.date_range('20191114',freq='MS',periods=6)
pd.date_range('20191114',freq='H',periods=6)
pd.date_range('20191114',freq='S',periods=6)
#%%
df.loc[0,"points"]=np.nan
df.iloc[0,2]=np.nan
df.loc[df.isnull()["points"],:]
#%%
df4=df.drop(6) # 6행 삭제
df4=df.fillna(2) # NaN 2로 채운다.
#%%
df2 = pd.DataFrame(np.random.randn(6, 4))
df2.columns = ["A", "B", "C", "D"]
df2.index = pd.date_range("20160701", periods=6)

df2["F"] = [1.0, np.nan, 3.5, 6.1, np.nan, 7.0]

# df3에 실행값을 넣어 df2의 원본 자료는 살려둔다.
df3 = df2.dropna(how="any") # 그행에서 1개라도 NaN 값이 있는경우 행을 삭제
df2.dropna(how="all") # 그행의 모든 열-값이 NaN인 경우 삭제

df2.fillna(value=5.0)

# 열-방향 삭제
df2.drop("F", axis=1) # axis=1 >>> 열-방향
df2.drop(["B", "F"], axis=1,inplace=False) # 각각의 복수-열 삭제/ inplace=True 일경우 원본내에서 삭제를 진행 원본훼손됨.

# 행-방향 삭제
df2.drop(pd.to_datetime("20160701"))
df2.drop([pd.to_datetime("20160702"), pd.to_datetime("20160704")]) # 날짜형 행-인덱스 각각 삭제하기.
# df2.drop(0)
#%%
# df.sum()은 자료 출처가 dict()형식이라 모두 같은 형식으로 되어있어 따로 형변환이 일어나지 않고 숫자는 숫자대로 합쳐지게된다.
df.sum(axis=0) # 행-방향 sum
df.sum(axis=1) # 열-방향 sum

df["points"].sum() # df[열][행]의 기본 인덱싱은 "열"이므로 .loc(기본 "행")을 쓰지 않아도 된다.

# 열-방향 집계는 하지 않는다. ∵문자가 섞여 있으면 하나의 문자열로 합쳐지기 때문.
# 행/열-방향 집계시 비수치(문자)는 가급적 필터링을 해준다. <<< NaN은 자동필터링 / 문자는 수동필터링 >>>
# 열-방향 집계는 무의미 but <유관된 열들(자료형이 같다.)>의 집계는 유의!!!

df.iloc["b"].sum() # df.loc[행,열]
# <<< 리스트(단일 자료형)는 모든 요소가 문자로 변환 >>>
# df.sum() 을 해버리면 모두 문자형으로 변환된채로 합쳐져 하나의 문자열로 변한다.
#%%
import numpy as np
import pandas as pd
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
"year": [2014, 2015, 2016, 2015, 2016],
"points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

# 행명 추가 
df = pd.DataFrame(data,index=["one", "two", "three", "four", "five"])
df["points"].sum()
df["points"].mean()
df["points"].median()
df["points"].var()
df["points"].std()
df["points"].max()
df["points"].min()
df["points"].argmax()
df["points"].argmin()
df["points"].count()# NA 빠짐
df.loc[:,"points"].sum()
df.loc["one",["year","points"]].sum()
df.describe()#열별 통계요약
df.head(5) # 처음 5개 일부 데이터
df.head(3) # 처음 3개 일부 데이터
df.tail(3) # 마지막 3개 일부 데이터
#%%

df.groupby("year").mean()
df.groupby("year").count()
df.groupby("year").size() # year 그룹개수

df.sort_values(by="year")
df.sort_values(by="year",ascending=False)
df.sort_values(by=["year","points"],ascending=[True,False])

# points 값별로 개수
df["points"].value_counts()
df["year"].value_counts()
df["points"].isin([2.4,2.9]) # 행-인덱스 리턴
df.loc[df["points"].isin([2.4,2.9]),["year","points"]] # 행/ 열을 동시에 지정할려면 df.loc를 사용한다.

#%%

df3 = pd.DataFrame(np.random.randn(4, 3), columns=["b", "d", "e"],
index=["Seoul", "Incheon", "Busan", "Daegu"])
func = lambda x: x.max() - x.min()
df3.apply(func, axis=0) # 열(x) 별로 함수 적용(방향은 행방향 axis=0)
df3.apply(func, axis=1) # 행(x) 별로 함수 적용 (방향은 열방향 axis=1)
df3['f']=df3.apply(func, axis=1) # func 적용 결과를 신규 열로 추가.






