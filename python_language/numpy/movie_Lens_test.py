# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:14:23 2019

@author: sundooedu
"""
#%%
import numpy as np

movie_data = np.loadtxt("data/ratings.csv",delimiter=',',skiprows=1)

movie_data[:10] # [:10, :] 이렇게 해도됨. (,:)는 모든 열을 가져온다는 뜻.

# 2열 평점 
movie_data[:,[2]] # 모든 2열 표시

movie_data[:,[2]].mean() # 평점 평균

np.mean(movie_data[:,[2]]) # 평점 평균

np.std(movie_data[:10,[2]]) # 평점 표준편차

np.var(movie_data[:10,[2]]) # 평점 분산

user_id = np.unique(movie_data[:,[0]]) # np.unique: 중복제거.
user_id
user_id.shape # .shape : 행수 열수 알아내는 함수

# 사용자별 평점평균 리스트
mean_ratings_by_user_list=[]

for uid in user_id:
    data_for_user = movie_data[movie_data[:,0] == uid] # userId가 uid와 같은 행들 가져온다.
    mean_for_user = np.mean(data_for_user[:,2]) # 해당 사용자 평점평균
    mean_ratings_by_user_list.append([uid,mean_for_user])
    
# 사용자별 평점평균 리스트를 np.array로 변환     
mean_ratings_by_user_array = np.array(mean_ratings_by_user_list, dtype=np.float32)    

mean_ratings_by_user_array[:]

np.savetxt('mean_ratings_by_user.csv', mean_ratings_by_user_array, delimiter=',', fmt='%.2f')

bool( 5 in np.arange(4)) # 포함 여부 확인

#%% quiz
# 사용자 평점평균이 상위 20% 이내의 (userId, 평점평균)
# arr[int(0.2 * len(arr))] 참조
# arr=arr.flatten() 참조



# 평정 내림정렬
reverse_rating = np.sort(mean_ratings_by_user_array[:,1])[::-1] # [:,1]을 줘서 평점만 역정렬
# 평점 중복 제거
reverse_rating2 = np.sort(np.unique(reverse_rating))[::-1] # 여기서 sort()가 깨짐
# 상위 20% 평점
th = reverse_rating2[int(0.2*len(mean_ratings_by_user_array[:,1]))]
# 상위 20% 이내 평점
mean_ratings_by_user_array_20 = reverse_rating2[reverse_rating2 >= th]

# x : 사용자, y : 평점
# 상위 20% 이내 (아이디, 평점)
res = [(int(x),y) for x,y in mean_ratings_by_user_array if y in mean_ratings_by_user_array_20]
res

a=sorted(mean_ratings_by_user_array, key=lambda x:x[1],reverse=True)[:int(0.2*len(mean_ratings_by_user_array))]
a
#%%
import numpy as np
movie_data = np.loadtxt("data/ratings.csv",delimiter=',',skiprows=1)

movie_id = np.unique(movie_data[:,[1]]) # np.unique: 중복제거.
movie_id
movie_id.shape # .shape : 행수 열수 알아내는 함수

# 영화별 평점평균 리스트
mean_ratings_by_movie_list=[]

for mid in movie_id:
    data_for_movie = movie_data[movie_data[:,1] == mid] # movie_id가 mid와 같은 행들 가져온다.(sql group by와 같다.)
                                                        # [:,1]가 movie_id를 의미.
    mean_for_movie = np.mean(data_for_movie[:,2]) # 해당 영화 평점평균
    mean_ratings_by_movie_list.append([mid,mean_for_movie])
    
# 영화별 평점평균 리스트를 np.array로 변환     
mean_ratings_by_movie_array = np.array(mean_ratings_by_movie_list, dtype=np.float32)    

mean_ratings_by_movie_array[:10]

np.savetxt('mean_ratings_by_movie.csv', mean_ratings_by_movie_array, delimiter=',', fmt='%.2f')
















