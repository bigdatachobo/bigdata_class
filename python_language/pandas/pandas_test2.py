# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:35:44 2019

@author: sundooedu
"""
#%%
# 피봇(pivot) 테이블
import pandas as pd
import numpy as np

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, np.nan, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]}
df = pd.DataFrame(data)

# NA가 포함된 열이 제거("서울, 2010")
df.pivot_table(index="도시",columns="연도",values="인구")

# Na가 fill_value로 채워지게 된다.
df.pivot_table(index="도시",columns="연도",values="인구", fill_value=9762546)

# sum 대상에 nan 이 있으면 0값으로 바뀌게 된다.
df.pivot_table(index="도시",columns="연도",values="인구", aggfunc='sum')

df.pivot_table(index="도시",columns="연도",values="인구", fill_value=9762546,aggfunc=np.sum)

#margins: 행별, 열별 aggfunc로 소계
df.pivot_table(index="도시",columns="연도",values="인구", fill_value=9762546,margins=True)

# 열선택함수 ("열명 연산자 값")
df.query("도시=='서울'")

df.query("도시=='서울' or 도시 == '부산'")
df.query("도시=='서울' | 도시 == '부산'")

df.query("도시==['서울','부산']")
df.query("도시 in ['서울','부산']")

df.query("도시 not in ['서울','부산']") # 부정
#%%
# 부모 DF
# 공통열(인덱스, 키) - 고객번호 기준으로 병합 (JOIN)
df_left = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
})
# 자식 DF
df_right = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
})

# SQL inner JOIN 과 같은 기능
# INNER( 양쪽 DF에 모두 인덱스(키) 존재하는 데이터만 노출)  /NaN 없음
pd.merge(df_left,df_right, how='inner')

# left outer ( left DF 데이터 모두 출력 )  /NaN 노출
pd.merge(df_left,df_right, how='left')  # df_left에 있는 값은 다 나오게되고 없는 right 값은 NaN으로 표시된다.

# right outer ( right DF 데이터 모두 출력 ) /NaN 노출
pd.merge(df_left,df_right, how='right')

# full outer ( 양쪽 DF 데이터 모두 출력 )  /NaN 노출
pd.merge(df_left,df_right, how='outer')

pd.merge(df_left,df_right, on='고객번호')


#%%
# 리스트 내부에 사전 형식 행들이 위치
# concat : 공통열(인덱스, 키) 없이 병합(주로 행들을 위/아래 병합시 사용)
df1 = pd.DataFrame([
          {'name': 'John',  'job': "teacher"}
        , {'name': 'Candy', 'job': "student"}
        , {'name': 'Fred',  'job': "developer"}

    ])
#추가행
df2 = pd.DataFrame([
        {'name': 'Ed',  'job': "engineer"}
      , {'name': 'Jack',  'job': "farmer"}
      , {'name': 'James', 'job': "student1"}
    ])
# 추가열
df3 = pd.DataFrame([
        {'sal': 500,  'email': "engineer@naver.com"}
      , {'sal': 1000,  'email': "farmer@naver.com"}
      , {'sal': 1000, 'email': "student1@naver.com"}
      , {'sal': 1000, 'email': "student1@naver.com"}
      , {'sal': 1000, 'email': "student1@naver.com"}
    ])
pd.concat([df1,df2], ignore_index=True,axis=0) # 행-방향 # row bind (행-방향)/ ignore_index=True ( 기존 인덱스 무시 )

pd.concat([df1,df3], ignore_index=False,axis=1) # column bind(열-방향)  # 기존 인덱스를 유지
pd.concat([df1,df3], ignore_index=True,axis=1) # column bind(열-방향) # 열-방향 / 기존 인덱스 무시
#%%
# 확장자가 CSV 인 경우.
import pandas as pd
import numpy as np
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

# csv 파일 저장 (행-index 배제)
# 1. 컬럼 헤더를 함께 저장
df.to_csv('data.csv',mode='w',encoding='utf-8',index=False) # index=False 줘서 인덱스는 같이 저장 안함.

# 2. 컬럼 헤더를 비저장
df.to_csv('data.csv',mode='w',encoding='utf-8',index=False, header=False) # 행-index 배제, 컬럼-index 배제

# 3.추가
df.to_csv('data.csv',mode='a',encoding='utf-8',sep=',',index=False,header=False) # 'a' >>> append (추가모드) (컬럼명도 같이 붙게된다.) 
                                                                     # header=False 시에 header가 지워지고 추가된다.
# 4.컬럼 헤더 없이 / csv 파일 읽기                                                                     
df2=pd.read_csv('data.csv',header=None) # header=None 헤더를 제거.

# 5.컬럼 헤더 있을때 / csv 파일 읽기
df2=pd.read_csv('data.csv',names=["names","year","points"]) # 읽어올때 열-index를 따로 지정해준다.
df2

#%%
import pandas as pd
import numpy as np
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

# 분리자 공백()
df.to_csv('data.txt',mode='w',encoding='utf-8',sep=' ',header=False)
df2 = pd.read_table('data.txt',sep='\s+') # \s+ : 공백 찾기 (정규표현식)
df2

#%%
# 이상값이 들어갔을때 정제하는 법
import pandas as pd
import numpy as np
data = {"names": ["Kilho", "Kilho", "Kilho", "$", "?"],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

df.to_csv('data.txt',mode='w',encoding='utf-8',sep=' ')

# "$","?" NaN으로 바꿈
# 헤더행이 '0'이므로 4,5를 제거.
df2 = pd.read_table('data.txt',sep='\s+',na_values=["$","?"],skiprows=[4,5])  # NaN으로 바껴서 읽어온다.
df2                                                                           # skiprows는 선택한 행을 제외하고 읽어온다.
#%%





