# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:43:29 2019

@author: sundooedu
"""
#%%
import os
import sys
# 직접 예외 클래스 만들기
class MyException(Exception):
    def __init__(self,errmsg):
        self.errmsg = errmsg #오류 메세지
    def __str__(self):
        return self.errmsg
    def warn(self):
        print("경고. 하지만 프로그램 중지x")
    def error(self):
        print("오류. 따라서 프로그램 중지O")
        #os.exit(1) 
        sys.exit()
    def send_status(self):
        print("로그전송")

su = -2
merr = None # 값이 없는 변수선언
try:
    if(su < 0): # 예외 발생 조건 
        merr = MyException("음수불가")
        raise merr # 예외 발생
except MyException as e:        
    #pass
    print(e) 
    #merr.warn() # 예외수준 경고
    merr.error() # 예외수준 오류
    #print(e.__str__()) # 원래는 이렇게 해야하지만 print() 함수가 자동으로 해줌.
finally:
    if merr != None: # AttributeError 해결 merr이 None이 아니면
        #merr.warn() # 재확인
        merr.send_status()
        
print("판다스2차분석")        