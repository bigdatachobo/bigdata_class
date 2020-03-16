# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:42:16 2019

@author: sundooedu
"""

import os
os.environ

os.getcwd
os.system("dir")
os.mkdir('d:/pytest') #디렉토리 생성
os.rmdir('d:/pytest') #디렉토리 삭제

with open('d:/pytest/test.txt','w',encoding='utf-8') as f:
    f.write('파이썬')    
    
os.path.isdir('d:/pytest')    
os.path.exists('d:/pytest') #디렉토리 존재여부 확인
if (os.path.exists('d:/pytest/test2.txt')):
    with open('d:/pytest/test2.txt','r',encoding='utf-8') as f:
        f.write('파이썬')
print("정상종료")        

os.rename('d:/pytest/test3.txt', 'd:/pytest/test2_copy.txt')	

os.remove('d:/test2_copy.txt') # 파일 지우기
os.unlink('d:/test2_copy.txt') # 파일 지우기

import shutil
shutil.move('d:/pytest/test2_copy.txt',"d:/test2_copy.txt")
#%%
os.path.getsize('test.txt')

import time
time.ctime(os.path.getctime('test.txt')) # 생성시간 
time.ctime(os.path.getmtime('test.txt')) # 변경시간 modified time => mtime
time.ctime(os.path.getatime('test.txt')) # 접근시간 Last access times => atime
#%%
char='svm_abcd.py'
char.index(".py")
bool(char.find(".java")==-1) #.java 미포함

char.startswith("svm") #svm 시작여부                         *** 암기
char.endswith(".py") #.py로 종료여부(py 파일                  *** 암기
bool(char.find('abcd') != -1) # 찾는 문자열 포함여부 확인     *** 암기
"abcd" in char # 찾는 문자열 포함여부 확인 (SQL과 비슷)
#%%
a=os.listdir('C:/Users/sundooedu/.spyder-py3/py_day_11') # 여기서는 "*"을 인식 못함.
import glob # glob에서만 "*"를 인식한다.
os.chdir('C:/Users/sundooedu/.spyder-py3')
b=glob.glob("**/*.py",recursive=True)  # "*"의 의미는 모든 글자를 의미. 글자수는 상관없음. "*"을 생략말자.

b.sort()                                         # ./
############################################################################
os.chdir('C:/Users/sundooedu/.spyder-py3')  # 외우기 웹스크롤링때 사용됨.
b=glob.glob("**/*.py",recursive=True)
for file in b:
    print(os.path.abspath(file))
############################################################################
for file in a:
    if file.endswith(".py"): # "**" 모든 하위 디렉토리를 탐색 .py 리스트
        print(file) # abspath() 절대경로
        
h=[ file for file in a if file.endswith(".py")]        
print(os.path.abspath(h))

os.chdir('C:/Users/sundooedu/.spyder-py3')
#%% c드라이브에 있는 .jpg 파일 찾기
os.chdir('C:/') 
b=glob.glob("**/*.jpg",recursive=True)
for file in b:
    print(os.path.abspath(file))
#%%
측시
시작시간
:
종료시간

코드블록 실행시간 = 종료시간 - 시작시간

APM (Application Performance Monitor)

import time

starting_time=time.time()
os.chdir('C:/') 
b=glob.glob("**/*.jpg",recursive=True)
for file in b:
    print(os.path.abspath(file))
end_time=time.time()
print(f'실행시간 = {end_time-starting_time} 초')    
#%%

def find_file(path,extension):
    import time
    st=time.time()
    os.chdir(path)
    file_list_py=glob.glob('**/*.'+extension, recursive=True)
    for file in file_list_py:
        print(os.path.abspath(file))
    et=time.time()
    print(f'실행시간 = {et-st} 초')
    
if __name__='__main__':    

find_file('C:/','jpg')        
    
import file_util_test
file_util_test.find_file('C:/','.py')






 
