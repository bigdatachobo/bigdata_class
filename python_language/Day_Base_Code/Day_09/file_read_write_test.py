# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:13:20 2019

@author: sundooedu
"""
#  해당파일 없으면 빈파일 생성
#  해당파일 있으면 덮어쓰기
f=open("test_data.txt",'w',encoding='utf-8')
f.write('0 번줄')
f.close()

f=open("20191016.txt",'w',encoding='utf-8')
f.write('파이썬 배우는 날')
f.close()
#%%  메모장에 입력한 그대로 입력된 후 저장 코드
from datetime import datetime

prompt='줄입력 : '
line= input(prompt)
fstr='%Y%m%d'
today_str=datetime.strftime(datetime.now(),fstr)
file_name= today_str +'.txt'

f=open(file_name,'w',encoding='utf-8')
f.write(line)
f.close()
print(file_name + '생성완료')
#%%
f = open("test_file.txt", 'w',encoding='utf-8')
for i in range(1, 11):
    if i<10:
        data = "0{0}번째 줄입니다.\n".format(i)
    else:
        data = "{0}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()
#%%
f = open("test_file.txt", 'w',encoding='utf-8')
for i in range(1, 101):
    if i<10:
        data = "00{0}번째 줄입니다.\n".format(i)
    elif i<100:
        data = "0{0}번째 줄입니다.\n".format(i)
    else:
        data = "{0}번째 줄입니다.\n".format(i)
    f.write(data)
    f.flush() # 중간 중간 저장하는 함수; 강제저장!
f.close() # 최종 저장 함수
#%%
lst=['1번째 줄입니다.\n','2번째 줄입니다.\n']

f=open("test_list.txt",'w',encoding='utf-8')
f.writelines(lst)
#f.close()
#f.write(str(100)) # write에는 문자열이 와야되서 100을 str() 함수를 이용해 문자열로 바꿈.
f.write("%d번째 줄입니다.\n" % 3)
f.write("{0}번째 줄입니다.\n".format(4))
f.close()
#%%
last_number=input("마지막 숫자를 입력하세요: ")
number_length=len(last_number)

for i in range(1, last_number):
    if i<10:
        data = "00{0}번째 줄입니다.\n".format(i)
    elif i<100:
        data = "0{0}번째 줄입니다.\n".format(i)
    else:
        data = "{0}번째 줄입니다.\n".format(i)
#%%
lst=['11번째 줄입니다.\n','12번째 줄입니다.\n']

f=open("test_list.txt",'a',encoding='utf-8')
f.writelines(lst)
f.close()        
#%% 일기장 ver 2.0
from datetime import datetime

prompt='줄입력 : '

total_line='' #입력된 모든줄
while True:
    line = input(prompt)
    if(line == '!quit'):break
    total_line += line + "\n"
    
fstr='%Y%m%d'
today_str=datetime.strftime(datetime.now(),fstr)
file_name= today_str +'.txt'

f=open(file_name,'w',encoding='utf-8')
f.write(total_line)
f.close()
print('오늘자 파일'+'('+file_name+')'+'생성완료')        
#%% 읽기~

f = open("test_list.txt", 'r',encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
#%%

f = open("20191016.txt", 'r',encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
#%%
f = open("20191016.txt", 'r',encoding='utf-8')
lines = f.readlines() # -s가 붙어서 모든 줄을 읽어들인다.
for line in lines:
    print(line)
f.close()
#%%
# 모든 개행문자까지 포함한 모든줄 <문자열>
f=open("test_list.txt",'r',encoding='utf-8')
# data = f.read(3) # 3문자
data=f.read() # 모든 문자
print(data)
f.close()
#%%
filename = input('파일명 : ')
fp=open(filename,'w',encoding='utf-8') #fp=file pointer
data = '기계학습의 정확도 95%'
fp.write(data)
fp.flush()
fp.close()
#%%
fp=open(filename,'r',encoding='utf-8') #fp=file pointer
data = fp.read()
print("파일내용 : ",data)
fp.close()
#%%
#fp=file pointer
filename = input('파일명 : ')
fp=open(filename,'w+',encoding='utf-8')  # w+: +는 쓰기와 읽기가 가능하다는 의미
data = '기계학습의 정확도 95%'
fp.write(data)
fp.flush()
#fp.close()

#fp=open(filename,'r',encoding='utf-8') #fp=file pointer
fp.seek(0) # Home 키와 같이 커서가 맨앞으로 이동하게하여 줄을 읽을 수 있는 위치로 옮겨줌.
data = fp.read()  # 위쪽에서 글을 쓴 후에 커서가 맨뒤로 이동해 있기 때문에
print("파일내용 : ",data) # 그대로 두면 read() 함수가 줄을 읽을 수 없기에 
fp.close()        # fp.seek(0)을 두어서 커서를 맨앞으로 이동시켜 거기서부터 읽기 시작한다.    
                  # 한글은 한글자가 3바이트이기에 index가 3진수로 index가 결정된다. [0], 3바이트=[1], 6바이트=[2]
#%%
filename = input('파일명 : ')
fp=open(filename,'w',encoding='utf-8') #fp=file pointer
data = '기계학습의 정확도 95%'
fp.write(data)
fp.flush()
fp.close()
#%%
fp=open(filename,'r',encoding='utf-8') #fp=file pointer
data = fp.read()
print("파일내용 : ",data)
fp.close()   
#%%
prompt="""
# ====================
# 여러줄 일기장 작성
# 1.쓰기
# 2.읽기
# 3.종료시 !quit
# ====================

번호 입력 : 
"""
hand_input=input(prompt)

from datetime import datetime

def writeDiary():
    fstr='%Y%m%d'
    today_str=datetime.strftime(datetime.now(),fstr)
    file_name= today_str +'.diary'
    
    lst=[] 
    #total_line='' #입력된 모든줄
    while True:
        line = input('내용을 입력하세요:')
        if(line == '!quit'):break
        #total_line += line + "\n"
        lst.append(line+'\n')
        
    with open(file_name,'w',encoding='utf-8') as f:
    #f.write(total_line)
        f.writelines(lst)
    #f.close()
    print('오늘자 파일'+'('+ file_name +')'+'생성완료')      

def readDiary():
    filename = input('일기파일명 : ')
    with open(filename,'r',encoding='utf-8') as fp:
    #data=fp.read()
        data=fp.readlines()
    print("파일내용 : ",data)
    #fp.close()

def errorDiary():
    print('미존재 메뉴번호')    

menu='읽기 1 쓰기 2 : '
menu_bunho=input(menu)

if menu_bunho == '1' :
    readDiary()
elif menu_bunho == '2' :
    writeDiary()   
else:
    errorDiary()
#%%
import pickle # 모든 자료형을 받아줌.
f = open("test.txt", 'wb') # wb= write binary (이진코드로 저장!:사람은 이해불가)
data = {1: 'python', 2: 'you need'} # dictionary 형태를 그대로 파일에 던짐.
pickle.dump(data, f)
f.close()    

import pickle # 읽을때는 로드로 한다. * read가 아닌 load
f = open("test.txt", 'rb') # rb = read binary
data = pickle.load(f)
print(data) # dictionary 형태로 다시 돌려받음.
#%%
import pickle # 모든 자료형을 받아줌.
f = open("test.txt", 'wb') # wb= write binary (이진코드로 저장!:사람은 이해불가)
data = {1: '파이썬', 2: '배우자'} # dictionary 형태를 그대로 파일에 던짐.
pickle.dump(data, f)
f.close()    

import pickle # 읽을때는 로드로 한다. * read가 아닌 load
f = open("test.txt", 'rb') # rb = read binary
data = pickle.load(f)
print(data)

#%%
import pickle

with open('test.txt','wb') as fp:
    data1='30대 기혼 직장인 화장품 쿠폰반응 YES 유의\n'
    data2='30대 기혼 여성 직장인 구매 확률 90% 유의\n'
    
    pickle.dump({'dt':data1,'nb':data2},fp) # 기본적으로 문자열만 저장 가능함
                                
#fp.close()

fp=open('test.txt','rb')
data=pickle.load(fp)
#print(data['dt'])
print(data.get('svm','미존재키')) #get()을 쓰면 오류가 안나고 None을 반환함

for k in data.keys():  # 키값들 반복 추출 dictionary 형식에서
    print(k,end=' ')
    
for k in data.keys():  # value 값을  반복 추출 dictionary 형식에서  
    print(data[k])
    
for v in data.values():
    print(v)
      
for i in data.items(): # 자료형이 튜플로 반환됨.
    print(i)    
    
#%%
import pickle 
f = open("test.txt", 'wb')
data = {1: '파이썬', 2: '배우자'}
pickle.dump(data, f)
f.close()    

import pickle
f = open("test.txt", 'rb') 
data = pickle.load(f)
print(data[2])

for k in data.keys():  # 키값들 반복 추출 dictionary 형식에서
    print(k,end=' ')



















