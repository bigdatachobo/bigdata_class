# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:24:16 2019

@author: sundooedu
"""

class Card9:
    __w= 0 # <--이게 클래스 변수 선언
    __h= 0
    def __init__(self,pattern,num):
        p_list=['스페이드','클로버','다이아몬드','하트']
        if not pattern in p_list:
            pattern= p_list[0]
        self.__pattern= pattern
        self.__num= num
       
    def getPattern(self): 
        return self.__pattern
    def getNum(self):
        return self.__num
    
    @classmethod # 클래스메소드
    def getW(cls): #cls <-- 클래스명 Card8
        return cls.__w # 클래스(cls)의(.) 변수(__w)
    @classmethod
    def getH(cls):
        return cls.__h
    
    def setPattern(self,pattern):
        self.__pattern= pattern
    def setNum(self,num):    
        self.__num= num
        
    @classmethod    
    def setW(cls,w): # 클래스 변수는 객체 변수 사용불가! 
        cls.__w= w
    @classmethod
    def setH(cls,h):
        cls.__h= h 
        
    #def toString(self): #관례에 맞지 않음
    def __str__ (self): #개발자들 관례에 맞음
        return f'''__pattern={self.__pattern}, __num={self.__num},
                   __w={Card9.__w}, __h={Card9.__h}'''
                   
             
    
    