# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:11:58 2019

@author: sundooedu
"""
#%%
from shapeTest import Shape
#클래스 상속
class Circle(Shape): 
    #리터럴 (literal)=상수(constant)
    PI=3.14  #변수 추가   
    #getRound 메소드 재정의
    def getRound(self):
        print("CircleRound")
        return self.length *2 *Circle.PI
    #getArea 메소드 재정의
    def getArea(self):
        print("CircleArea")
        return self.length **2 *Circle.PI
    #메소드 추가
    def getRoundAndArea(self):
        return self.getRound(),self.getArea()
    
#%%
# 클래스 외부  
if __name__ == "__main__":
   print(__name__) 
   # c :객체참조변수 ,객체명, 객체
   c = Circle() # c에는 객체주소 =참조 =reference가 저장
   print(id(c))
   c.setlength(5)
   res1=c.getRound()
   res2=c.getArea()
   result =f'반지름={c.getlength()},둘레={res1},너비={res2}'
   print(result)
    
    