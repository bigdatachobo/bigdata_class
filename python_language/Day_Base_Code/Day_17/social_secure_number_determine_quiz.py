# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:01:51 2019

@author: sundooedu
"""

# =============================================================================
# 4. 사용자로부터 생년월일을 문자열로 받아서 올바른 생년월일인지를 검사하는 프로그램을 작성하라. 
# 예를 들면 “19991301”과 같은 문자열은 올바른 생년월일이 아니다. 13월 1일은 올바르지 않다. 
# 생년월일을을 입력하시오: 19700123
# 올바른 생년월일입니다.
# =============================================================================
# 선생님 풀이
def leap_year(year):
    res='평년'
    if (year%4 ==0 and year%100 != 0) or (year%400 == 0):
        res='윤년'    
    return res

while True:
    bstring=input("생년월일을 입력하시오:")
    # 1.분리
    year = int(bstring[:4]) # 년으로 해석
    print(leap_year(year))
    
    month = int(bstring[4:6]) # 월로 해석
    day = int(bstring[6:]) # 일로 해석
    
    if month in range(1,13):
        if day in range(1,32): # 일검증
            print("올바른 생년월일입니다.")
        else:
            print("올바르지 않은 생년월일입니다.")
            break
    else:#월검증
        print('올바르지 않은 생년월일입니다.')
        break
#%%









        