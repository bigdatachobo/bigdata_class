# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:50:59 2019

@author: sundooedu
"""

class Circle:
    import math
    __pi=math.pi
    
    def __init__(self,r):
        self.__r= r
        
    def getR(self):
        return self.__r
    
    def setR(self,r):
        self.__r= r
    
    def round_length(self,r):
        return round(2*(Circle.__pi)*(self.__r),2)
    
    def area(self,r):
        return round((Circle.__pi)*(self.__r**2),2)
    
    def __str__(self):
        return f'원주율 : {Circle.__pi}, 반지름 : {self.__r},둘레 : {self.round_length(self.__r)}, 면적 : {self.area(self.__r)}'
    
a=Circle(7)
a.setR(9)
a.area(7)
a.round_length(7)
print(a.getR())
print(a)    
#%%

# 업무 : 개념적 객체
# 파이썬 : 선체(선언적 객체 = 클래스), 실체(클래스로 생성된 실객체, instance)
class Circle2:
    import math
    # 리터릴 literal (상수에 대한 변수)
    # 상수 : constant
    __pi= math.pi
    
    def __init__(self): # method를 호출한 객체 자신을 "self"라 한다.
        self.__r= 1 
        
    def getR(self):
        return self.__r # 변수 (variable)가 세터, 게터를 가질때 속성변수(attribute)
    
    def setR(self,r): # 함수(function), 객체(object)함수(method)
        self.__r= r
    
    def getRound(self,r):
        return round(self.getR()*2*Circle2.__pi,2)
    
    def getArea(self,r):
        return round(self.getR()**2*Circle2.__pi,2)
    def __str__(self):
        return f'원주율 : {Circle2.__pi}, 반지름 : {self.__r},둘레 : {self.getRound(self.__r)}, 면적 : {self.getArea(self.__r)}'
    
    
if __name__ == "__main__":
    #객체 참조 변수, 객체명, 객체
    c= Circle2()
    c.setR(10)        
    print(c)        
        
        
        
        
        
    