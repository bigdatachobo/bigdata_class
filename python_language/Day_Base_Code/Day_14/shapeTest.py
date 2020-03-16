# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:04:20 2019

@author: sundooedu
"""

class Shape: # 도형 공통 기본(Base)클래스   
    def __init__(self):
        # 변수 variable가 세터,게터를 가질때 속성변수(attribute,property)
        self.length=1 
    # self:method를 호출한 객체 자신 
    def setlength(self,length): #함수(function) ,객체(object)함수(method)
        self.length=length
    def getlength(self):
        return self.length
    def getRound(self):
        print("ShapeRound")
        return self.length  
    def getArea(self):
        print("ShapeArea")
        return self.getlength() 