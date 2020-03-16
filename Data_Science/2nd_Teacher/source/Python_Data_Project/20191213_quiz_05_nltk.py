# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:33:11 2019

@author: sundooedu
"""
#%%
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import pandas as pd
from PIL import Image
import glob
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
'''
국문키워드 / 영문키워드 따로 추출 후 csv 파일로 저장 후 open().read() 함수 돌린다.
'''
a=glob.glob('../data/nltk_quiz_201*')
df=pd.DataFrame()
for exl in a:
    tmp=pd.read_excel(exl)
    df=pd.concat([df,tmp],axis=0)

df_kor=pd.DataFrame()
df_kor=pd.concat([df_kor,df['국문키워드']])

df_eng=pd.DataFrame()
df_eng=pd.concat([df_eng,df['영문키워드']])

df_kor.to_csv('../data/total_exel_kor.txt',encoding='utf-8',index=False,header=False)
df_eng.to_csv('../data/total_exel_eng.txt',encoding='utf-8',index=False,header=False)
#%%
'''
key_word_kor
'''
text_kor=open('../data/total_exel_kor.txt',encoding='utf-8').read()
key_word_mask=np.array(Image.open('../data/black_book_nltk_quiz.png'))

stopwords = set(STOPWORDS)
stopwords.add(";")  
#%%
plt.figure(figsize=(10,8))
plt.imshow(key_word_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
wc = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',background_color='white', max_words=2000, mask=key_word_mask, stopwords = stopwords)
wc = wc.generate(text_kor)
wc.words_
#%%
plt.figure(figsize=(10,8))    
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
'''
key_word_eng
'''
text_eng=open('../data/total_exel_eng.txt',encoding='utf-8').read()
key_word_mask=np.array(Image.open('../data/black_book_nltk_quiz.png'))

stopwords = set(STOPWORDS)
stopwords.add(";")  
#%%
plt.figure(figsize=(10,8))
plt.imshow(key_word_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
wc = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',background_color='white', max_words=2000, mask=key_word_mask, stopwords = stopwords)
wc = wc.generate(text_eng)
wc.words_
#%%
plt.figure(figsize=(10,8))    
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()    
#%%
''' key_word_eng graph'''
#%%
from nltk import regexp_tokenize
pattern=pattern = r'''[a-z]+'''
tokens_en = regexp_tokenize(text_eng,pattern)
tokens_en
#%%
import nltk
eng=nltk.Text(tokens_en, name='English Key Word')
print(len(eng.tokens))
print(len(set(eng.tokens)))
eng.vocab()
#%%
plt.figure(figsize=(12,6))
eng.plot(100)
plt.show()













