# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:38:48 2019

@author: sundooedu
"""
import numpy as np
import pandas as pd 

ratings = pd.read_csv('data/ratings.csv',encoding='utf-8')
users = pd.read_csv('data/users.csv',encoding='utf-8')
movies = pd.read_csv('data/movies.csv',encoding='utf-8')

ratings.tail()
users.tail()
movies.tail()

ratings.shape

# 파일변수 관계 ((ratings - users) - movies )
data = pd.merge(pd.merge(ratings,users),movies)

# 유저 평점개수(=userId 개수)의 순위
x = pd.DataFrame(data.groupby('userId').size())
y = x.sort_values(by=0,ascending=False) # 정렬해야하는 열-명은 0으로 준다.

# 불리언 인덱스 (['userId']==600)로 행 필터링
data[data['userId']==600].tail() 

# 각 영화(행-인덱스 = 타이틀)의 성별(열-인덱스 = gender) 평점(value) 평균(집계)
# 단, 결측치(NA)는 0으로 정제

mo = data.groupby(by='title')['rating'].mean()
mean_ratings = data.pivot_table(index='title',columns='gender',values='rating',fill_value=0,aggfunc='mean')
# 평점이 100개 이상인 영화명 (영화명의 개수)

rating_by_title = data.groupby(by='title').size()
# 138개
rating_by_title_gt100 = rating_by_title.index[rating_by_title >= 100]
type(rating_by_title_gt100) # 인덱스 객체
rating_by_title_gt100.value_counts()
rating_by_title_gt100


# 평점이 100개 이상인 영화들의 성별 평균 평점
# 1. 피봇테이블에서 평점이 100개 이상인 영화 성별 평균 평점을 필터링
mean_ratings_gt100 = mean_ratings.loc[rating_by_title_gt100]

# 여성이 선호한 영화 top-10
top10_female_ratings = mean_ratings_gt100.sort_values(by='F',ascending=False)

top10_female_ratings.iloc[:10,:]

# 남성이 선호한 영화 top-10
top10_male_ratings = mean_ratings_gt100.sort_values(by='M',ascending=False)

top10_male_ratings.iloc[:10,:]

# 남여간의 평균평점 차이 컬럼(diff)을 mean_ratings에 추가
#df["net_points"] = df["points"] - df["penalty"] /from : pandas_test.py
mean_ratings["rate_diff"] = (mean_ratings["F"] - mean_ratings["M"]) # 양수면 여성의 평점이 높았고
                                                                    # 음수면 남성의 평점이 높았다는걸 알 수 있다.
#모든 영화 대상으로 평점의 표준편차가 큰 영화 138개 추출
      
# 내풀이                                                              
movie_title_std = data.groupby(by='title')['rating'].std() 
top_std = movie_title_std.sort_values(ascending=False) 

# 선생님풀이
ratings_by_std = data.groupby('title')['rating'].std() 
ratings_by_std = ratings_by_std[rating_by_title_gt100] # 미리뽑아놓은 영화 타이틀 100개를 인덱스로사용.
ratings_by_stds = ratings_by_std.sort_values(ascending=False)


