# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:52:53 2019

@author: sundooedu
"""
#%%
from konlpy.tag import Kkma
kkma = Kkma()
#%%
kkma.sentences('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어 분석을 시작합니다', '재미있어요~~']
'''
#%%
'''명사분석'''
kkma.nouns('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어', '분석']
'''
#%%
'''형태소(pos) 분석'''
kkma.pos('한국어 분석을 시작합니다 재미있어요~~')
'''
[('한국어', 'NNG'),
 ('분석', 'NNG'),
 ('을', 'JKO'),
 ('시작하', 'VV'),
 ('ㅂ니다', 'EFN'),
 ('재미있', 'VA'),
 ('어요', 'EFN'),
 ('~~', 'SW')]
'''
#%%
from konlpy.tag import Hannanum
hannanum=Hannanum()

'''명사분석'''
hannanum.nouns('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어', '분석', '시작']
'''
#%%
'''형태소  분석'''
hannanum.morphs('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어', '분석', '을', '시작', '하', 'ㅂ니다', '재미있', '어요', '~~']
'''
#%%
hannanum.pos('한국어 분석을 시작합니다 재미있어요~~')
'''
[('한국어', 'N'),
 ('분석', 'N'),
 ('을', 'J'),
 ('시작', 'N'),
 ('하', 'X'),
 ('ㅂ니다', 'E'),
 ('재미있', 'P'),
 ('어요', 'E'),
 ('~~', 'S')]
'''
#%%
from konlpy.tag import Twitter
t=Twitter()
#%%
'''명사분석'''
t.nouns('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어', '분석', '시작']
'''
#%%
t.morphs('한국어 분석을 시작합니다 재미있어요~~')
'''
['한국어', '분석', '을', '시작', '합니다', '재미있어요', '~~']
'''
#%%
t.pos('한국어 분석을 시작합니다 재미있어요~~')
'''
[('한국어', 'Noun'),
 ('분석', 'Noun'),
 ('을', 'Josa'),
 ('시작', 'Noun'),
 ('합니다', 'Verb'),
 ('재미있어요', 'Adjective'),
 ('~~', 'Punctuation')]
'''
#%%
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
#%%
''' 앨리스 텍스트 워드 카운팅 및 사진에 겹치기'''
text=open('../data/09. alice.txt').read()
alice_mask=np.array(Image.open('../data/09. alice_mask.png'))

stopwords = set(STOPWORDS)
stopwords.add("said")
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
plt.figure(figsize=(8,8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
'''워드 카운팅'''
wc=WordCloud(background_color='white',max_words=2000, mask=alice_mask, stopwords=stopwords)
wc=wc.generate(text)
wc.words_
#%%
''' 카운팅된 단어를 앨리스 그림에 겹쳐 보이게 한다. '''
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
'''스타워즈 A New Hope 텍스트 및 스톱 트루퍼 이미지 위에 겹쳐보이게 한다.'''
text2=open('../data/09. a_new_hope.txt').read()

text2=text2.replace('HAN', 'Han')
text2=text2.replace("LUKE'S",'Luke')

star_wars_mask = np.array(Image.open('../data/09. stormtrooper_mask.png'))
#%%
'''특수어처리 단어를 처리'''
stopwords2 = set(STOPWORDS)
stopwords2.add("int")
stopwords2.add("ext")
#%%
'''워드 클라우드 불러오기'''
wc2=WordCloud(max_words=1000, mask=star_wars_mask, stopwords=stopwords2, margin=10, random_state=1).generate(text2)
default_colors=wc2.to_array()
#%%
import random
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)
#%%
plt.figure(figsize=(12,12))    
plt.imshow(wc2.recolor(color_func=grey_color_func, random_state=3), interpolation='bilinear')
plt.axis('off')
plt.show()
#%%
'''8-4 육아휴직 관련 법안에 대한 분석'''
import nltk

from konlpy.corpus import kobill
files_ko = kobill.fileids()
doc_ko=kobill.open('1809890.txt').read()
'''1809890.txt >>> KoNLPy 내부문서'''
#%%
doc_ko
#%%
'''Twitter 분석기로 명사분석!'''
from konlpy.tag import Twitter; t=Twitter()
tokens_ko=t.nouns(doc_ko)
tokens_ko
#%%
ko=nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')
print(len(ko.tokens))
print(len(set(ko.tokens)))
ko.vocab()
#%%
'''쓸데없는 단어도 있어서 case-by-case로 지정'''
plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()
#%%
stop_words=['.','(',')',',',"'",'%','-','X',').','x','의','자','에','안','번','호','을','이','다','만','로','가','를']
ko=[each_word for each_word in ko if each_word not in stop_words]    
ko
#%%
'''
이제 조금 더 좋아보이고
stop_words 변수에 의미없어 보이는 단어를 추가하면됨.'''
ko=nltk.Text(ko, name='대한민국 국회 의안 제 1809890호')

plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()
#%%
'''
어떤 단어가 문서 내에서 몇 번 언급되었는지 확인 가능
'''
ko.count('초등학교')
#%%
plt.figure(figsize=(12,6))
ko.dispersion_plot(['육아휴직','초등학교','공무원'])
#%%
'''
원하는 단어가 문서 내에서 어느 위치에 있는지 개략적으로 분량과 함께 알 수 있다.
단어 주변부 단어까지 같이 확인 가능.
'''
ko.concordance('초등학교')
#%%
'''
또 어떤 단어들이 연어(collocation)로 사용되었는지 알 수 있다.
'''

# ko.collocations()
print('; '.join(ko.collocation_list()))
#%%
data = ko.vocab().most_common(150)

# for win : font_path='c:/Windows/Fonts/malgun.ttf'
wordcloud = WordCloud(font_path='/Library/Fonts/malgun.ttf',
                      relative_scaling = 0.2,
                      background_color='white',
                      ).generate_from_frequencies(dict(data))
plt.figure(figsize=(12,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#%%
'''
8-5 Naive Bayes Classifier의 이해-영문
'''
from nltk.tokenize import word_tokenize
import nltk

train=[('i like you','pos'),
       ('i hate yuou','neg'),
       ('you like me','neg'),
       ('i like her','pos')]
#%%
all_words=set(word.lower() for sentence in train for word in word_tokenize(sentence[0]))
all_words
'''
말뭉치
{'hate', 'her', 'i', 'like', 'me', 'you', 'yuou'}
'''
#%%
t=[({word:(word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
t
#%%
classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()
'''
Most Informative Features
                    yuou = False             pos : neg    =      1.7 : 1.0
                     her = False             neg : pos    =      1.7 : 1.0
                      me = False             pos : neg    =      1.7 : 1.0
                       i = True              pos : neg    =      1.7 : 1.0
                    like = True              pos : neg    =      1.7 : 1.0
                    hate = False             pos : neg    =      1.7 : 1.0
                     you = False             neg : pos    =      1.0 : 1.0
'''
#%%
test_sentence2 = 'i like MeRui'
test_sent_features2={word.lower():
                                 (word in word_tokenize(test_sentence2.lower()))
                                 for word in all_words}
test_sent_features2
#%%
'''
8-6. Naive Bayes Classifier의 이해 - 한글
'''
from konlpy.tag import Twitter
pos_tagger = Twitter()
#%%
train=[('메리가 좋아','pos'),
       ('고양이도 좋아','pos'),
       ('난 수업이 지루해','neg'),
       ('메리는 이쁜 고양이야','pos'),
       ('난 마치고 메리랑 놀거야','pos')]
#%%
'''
말뭉치 만들기
'''
all_words=set(word.lower() for sentence in train for word in word_tokenize(sentence[0]))
all_words
'''
{'고양이도',  # 다른 단어로 잡힘
 '고양이야',  #     //
 '난',
 '놀거야',
 '마치고',
 '메리가',    # 다른 단어로 잡힘
 '메리는',    #       //
 '메리랑',    #       //
 '수업이',
 '이쁜',
 '좋아',
 '지루해'}
'''
#%%
t=[({word:(word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
t
#%%
classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()
'''
Most Informative Features
                       난 = True              neg : pos    =      2.5 : 1.0
                      좋아 = False             neg : pos    =      1.5 : 1.0
                     놀거야 = False             neg : pos    =      1.1 : 1.0
                     마치고 = False             neg : pos    =      1.1 : 1.0
                     메리가 = False             neg : pos    =      1.1 : 1.0
                      이쁜 = False             neg : pos    =      1.1 : 1.0
                     메리랑 = False             neg : pos    =      1.1 : 1.0
                     메리는 = False             neg : pos    =      1.1 : 1.0
                    고양이야 = False             neg : pos    =      1.1 : 1.0
                    고양이도 = False             neg : pos    =      1.1 : 1.0
'''
#%%
test_sentence = '난 수업이 마치면 메리랑 놀거야'
#%%
'''
긍정적 결과가 나와야 할 것 같은 위 테스트 문장 적용
'''
test_sent_features = {word.lower():
                                    (word in word_tokenize(test_sentence.lower()))
                                    for word in all_words}
test_sent_features    
'''
{'난': True,
 '마치고': False,
 '고양이도': False,
 '지루해': False,
 '수업이': True,
 '좋아': False,
 '이쁜': False,
 '메리랑': True,
 '고양이야': False,
 '놀거야': True,
 '메리는': False,
 '메리가': False}
'''
#%%
''' 부정적이라고 뜸. '''
classifier.classify(test_sent_features)
''' 'neg' '''
help(classifier)
#%%
'''
한글 형태소 분석 함수
'''
def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

train_docs=[(tokenize(row[0]),row[1]) for row in train]
train_docs
'''
[(['메리/Noun', '가/Josa', '좋다/Adjective'], 'pos'),
 (['고양이/Noun', '도/Josa', '좋다/Adjective'], 'pos'),
 (['난/Noun', '수업/Noun', '이/Josa', '지루하다/Adjective'], 'neg'),
 (['메리/Noun', '는/Josa', '이쁘다/Adjective', '고양이/Noun', '야/Josa'], 'pos'),
 (['난/Noun', '마치/Noun', '고/Josa', '메리/Noun', '랑/Josa', '놀다/Verb'], 'pos')]
'''
#%%
''' 전체 말뭉치 생성 '''
tokens = [t for d in train_docs for t in d[0]]
tokens
'''
['메리/Noun',
 '가/Josa',
 '좋다/Adjective',
 '고양이/Noun',
 '도/Josa',
 '좋다/Adjective',
 '난/Noun',
 '수업/Noun',
 '이/Josa',
 '지루하다/Adjective',
 '메리/Noun',
 '는/Josa',
 '이쁘다/Adjective',
 '고양이/Noun',
 '야/Josa',
 '난/Noun',
 '마치/Noun',
 '고/Josa',
 '메리/Noun',
 '랑/Josa',
 '놀다/Verb']
'''
#%%
def term_exists(doc):
    return {word: (word in set(doc)) for word in tokens}
#%%
train_xy = [(term_exists(d), c) for d,c in train_docs]    
train_xy
#%%
classifier=nltk.NaiveBayesClassifier.train(train_xy)
#%%
'''
형태소 분석을 안 했을때 부정되었던 문장을 다시 가지고 테스트 진행
'''
test_sentence=[("난 수업이 마치면 메리랑 놀거야")]
#%%
'''
형태소 분석
'''
test_docs = pos_tagger.pos(test_sentence[0])
test_docs
'''
[('난', 'Noun'),
 ('수업', 'Noun'),
 ('이', 'Josa'),
 ('마치', 'Noun'),
 ('면', 'Josa'),
 ('메리', 'Noun'),
 ('랑', 'Josa'),
 ('놀거야', 'Verb')]
'''
#%%
'''
형태소 분석
'''
test_sent_features = {word: (word in tokens) for word in test_docs}
test_sent_features          

'''
{('난', 'Noun'): False,
 ('수업', 'Noun'): False,
 ('이', 'Josa'): False,
 ('마치', 'Noun'): False,
 ('면', 'Josa'): False,
 ('메리', 'Noun'): False,
 ('랑', 'Josa'): False,
 ('놀거야', 'Verb'): False}
'''
#%%
classifier.classify(test_sent_features)
''' 'pos' '''
'''
긍정의 의미가 잘 드러남.
'''
#%%
'''
8-7. 문장의 유사도 측정
'''
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df = 1)
contents = ['메리랑 놀러가고 싶지만 바쁜데 어떻하죠?',
                   '메리는 공원에서 산책하고 노는 것을 싫어해요',
                   '메리는 공원에서 노는 것도 싫어해요. 이상해요.',
                   '먼 곳으로 여행을 떠나고 싶은데 너무 바빠서 그러질 못하고 있어요']
#%%
X = vectorizer.fit_transform(contents)
vectorizer.get_feature_names()
'''
['것도',
 '것을',
 '곳으로',
 '공원에서',
 '그러질',
 '너무',
 '노는',
 '놀러가고',
 '떠나고',
 '메리는',
 '메리랑',
 '못하고',
 '바빠서',
 '바쁜데',
 '산책하고',
 '싫어해요',
 '싶은데',
 '싶지만',
 '어떻하죠',
 '여행을',
 '이상해요',
 '있어요']
'''
#%%
X.toarray().transpose()
'''
array([[0, 0, 1, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 1],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 1]], dtype=int64)
'''
#%%
X = vectorizer.fit_transform(contents)
num_samples, num_features = X.shape
num_samples, num_features
'''
(4, 22)
'''
#%%
new_post = ['메리랑 공원에서 산책하고 놀고 싶어요']
new_post_vec = vectorizer.transform(new_post)
new_post_vec.toarray()
'''
array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]],
      dtype=int64)
'''
#%%
import scipy as sp

def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())
#%%
best_doc = None
best_dist = 65535
best_i = None

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    d = dist_raw(post_vec, new_post_vec)
    
    print("== Post %i with dist=%.2f   : %s" %(i,d,contents[i]))
    
    if d<best_dist:
        best_dist = d
        best_i = i
'''
== Post 0 with dist=2.45   : 메리랑 놀러가고 싶지만 바쁜데 어떻하죠?
== Post 1 with dist=2.24   : 메리는 공원에서 산책하고 노는 것을 싫어해요
== Post 2 with dist=2.65   : 메리는 공원에서 노는 것도 싫어해요. 이상해요.
== Post 3 with dist=3.46   : 먼 곳으로 여행을 떠나고 싶은데 너무 바빠서 그러질 못하고 있어요
'''
#%%
from konlpy.tag import Twitter
t = Twitter()
#%%
contents_tokens = [t.morphs(row) for row in contents]
contents_tokens
'''
[['메리', '랑', '놀러', '가고', '싶지만', '바쁜데', '어떻하죠', '?'],
 ['메리', '는', '공원', '에서', '산책', '하고', '노', '는', '것', '을', '싫어해요'],
 ['메리', '는', '공원', '에서', '노', '는', '것', '도', '싫어해요', '.', '이상해요', '.'],
 ['먼',
  '곳',
  '으로',
  '여행',
  '을',
  '떠나고',
  '싶은데',
  '너무',
  '바빠서',
  '그러질',
  '못',
  '하고',
  '있어요']]
'''
#%%
contents_for_vectorize = []

for content in contents_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
        
    contents_for_vectorize.append(sentence)
    
contents_for_vectorize
'''
[' 메리 랑 놀러 가고 싶지만 바쁜데 어떻하죠 ?',
 ' 메리 는 공원 에서 산책 하고 노 는 것 을 싫어해요',
 ' 메리 는 공원 에서 노 는 것 도 싫어해요 . 이상해요 .',
 ' 먼 곳 으로 여행 을 떠나고 싶은데 너무 바빠서 그러질 못 하고 있어요']
'''
#%%
X = vectorizer.fit_transform(contents_for_vectorize)
num_samples, num_features = X.shape
num_samples, num_features
'''
(4, 20)
'''
#%%
vectorizer.get_feature_names()
'''
['가고',
 '공원',
 '그러질',
 '너무',
 '놀러',
 '떠나고',
 '메리',
 '바빠서',
 '바쁜데',
 '산책',
 '싫어해요',
 '싶은데',
 '싶지만',
 '어떻하죠',
 '에서',
 '여행',
 '으로',
 '이상해요',
 '있어요',
 '하고']
'''
#%%
X.toarray().transpose()
'''
array([[1, 0, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 0],
       [0, 0, 0, 1],
       [1, 1, 1, 0],
       [0, 0, 0, 1],
       [1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 1],
       [0, 1, 0, 1]], dtype=int64)
'''
#%%
new_post = ['메리랑 공원에서 산책하고 놀고 싶어요']
new_post_tokens = [t.morphs(row) for row in new_post]

new_post_for_vectorize = []

for content in new_post_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
        
    new_post_for_vectorize.append(sentence)
    
new_post_for_vectorize

'''
[' 메리 랑 공원 에서 산책 하고 놀고 싶어요']
'''
#%%
new_post_vec = vectorizer.transform(new_post_for_vectorize)
new_post_vec.toarray()
'''
array([[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]],
      dtype=int64)
'''
#%%
import scipy as sp

def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())
#%%
best_doc = None
best_dist = 65535
best_i = None

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    d = dist_raw(post_vec, new_post_vec)
    
    print("== Post %i with dist=%.2f   : %s" %(i,d,contents[i]))
    
    if d<best_dist:
        best_dist = d
        best_i = i
'''        
== Post 0 with dist=3.00   : 메리랑 놀러가고 싶지만 바쁜데 어떻하죠?
== Post 1 with dist=1.00   : 메리는 공원에서 산책하고 노는 것을 싫어해요
== Post 2 with dist=2.00   : 메리는 공원에서 노는 것도 싫어해요. 이상해요.
== Post 3 with dist=3.46   : 먼 곳으로 여행을 떠나고 싶은데 너무 바빠서 그러질 못하고 있어요
'''
#%%
print("Best post is %i, dist = %.2f" % (best_i, best_dist))
print('-->', new_post)
print('---->', contents[best_i])
'''
Best post is 1, dist = 1.00
--> ['메리랑 공원에서 산책하고 놀고 싶어요']
----> 메리는 공원에서 산책하고 노는 것을 싫어해요
'''





