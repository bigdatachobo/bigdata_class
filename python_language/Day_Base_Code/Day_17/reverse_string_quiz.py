# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:01:11 2019

@author: sundooedu
"""

# =============================================================================
# 3. 사용자가 입력한 문자열을 역순으로 만들어서 출력하는 프로그램을 작성한다. 
# 예를 들어서 사용자가 “abcd”와 같이 입력하면 “dcba”와 같이 출력한다. 
# 
# 문자열을 입력하시오: Welcome to python
# nohtyp ot emocleW
# =============================================================================
def reverse_string(string):
    string_list=string.split(' ')
    string_list2=[]
    for i in range(3):
        string_list2.append(string_list[i][::-1])
    string_list2.reverse()    
    result=' '.join(string_list2)    
    return result

reverse_string("boys be ambitious")

# =============================================================================
# 풀이과정
# string="Welcome to python"
# string_list=string.split(' ')
# string_list2=[]
# for i in range(3):
#     string_list2.append(string_list[i][::-1])
# string_list2.reverse()    
# ' '.join(string_list2)    
# =============================================================================
#%% 선생님 풀이 

def reverse(str):
# =============================================================================
#     size = len(str)
#     print(sys.getsizeof(str))
#     reverseStr=''
#     for i in range(size-1,-1,-1):
#         reverseStr +=str[i]
#     return reverseStr
# =============================================================================
    return ''.join(reversed(str))

reverse('python is no good')
