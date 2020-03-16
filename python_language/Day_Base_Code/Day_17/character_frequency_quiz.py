# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:00:42 2019

@author: sundooedu
"""

# =============================================================================
# 2. 사용자가 입력한 문자열에서 특정한 문자의 빈도를 계산하는 프로그램을 작성해보자. 
# 예를 들어서 “Welcome to Python”에서 문자 “o”의 빈도를 계산하는 프로그램을 작성한다. 
# 
# 문자열을 입력하시오: Welcome to Python
# =============================================================================
import collections
def char_frequency(string,alphabet):
    string_list=list(string)
    string_list=[elements for elements in string_list if elements != ' '] # 공백제거
    char_dict = collections.Counter(string_list)
    return char_dict[alphabet]

char_frequency("Welcome to Python",'o')
    
# =============================================================================
# 풀이 과정
# string="Welcome to Python"
# string_list=list(string)
# string_list=[elements for elements in string_list if elements != ' ']
# 
# c_dict = collections.Counter(string_list)
# 
# c_dict['o']    
# 
# =============================================================================
#%% 선생님 풀이
s=input("문자열을 입력하시오: ") # Welcome to Python 집어넣기
print(s.count('o'))







