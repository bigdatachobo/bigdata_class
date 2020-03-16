# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:11:49 2019

@author: sundooedu
"""
from shapeTest import Shape
#클래스 상속
class Rect(Shape): 
    #리터럴 (literal)=상수(constant)
    #PI=3.14  #변수 추가   
    #getRound 메소드 재정의
    def getRound(self):
        print("RectRound")
        return self.length *4
    #getArea 메소드 재정의
    def getArea(self):
        print("RectArea")
        return self.length *2
    #메소드 추가
    #def getRoundAndArea(self):
        #return self.getRound(),self.getArea()
 
    r= Rect()
    print(id(r))
    r.getRound()
