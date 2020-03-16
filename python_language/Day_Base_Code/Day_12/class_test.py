# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:14:19 2019

@author: sundooedu
"""
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
#%% 클래스 사용법
class Cookie:
    pass

a = Cookie()
b = Cookie()
#%%
class FourCal:
    def __init__(self, first, second): # 생성자(=초기자)
       self.first = first
       self.second = second
    """def setdata(self, first, second): #변수를 하나씩만 사용한다. 아래처럼.
       self.first = first
       self.second = second"""
    def set_first(self,first): # first변수에 대한 setter 메소드
        self.first = first
    def set_second(self,second): # second변수에 대한 setter 메소드
        self.second = second    
    def add(self):
        result = self.first + self.second
        return result

#객체변수에 필수입력 유도 할 수 있다.       
a=FourCal(4,2) #[ __init__() ]이렇게 호출은안됨 | [클래스명()] 호출로 이렇게 호출해야됨, 이때 객체가 주기억장치에 생성됨.
a.set_first(9) #초기값을 선택적으로 선택 수정할 수 있는 메소드다. ('세터': "set"으로 시작하는 함수)
#r=a.first + a.second # 이런식으로 직접 접근하지 말고 매소드를 호출하여 처리한다.
a.set_second(8) # setter를 이용하면 새로운 객체를 생성하지 않고도/ 선택적으로 변수의 값을 수정할 수 있다.
a.add()
b=FourCal()



a.setdata(4,2)
b.setdata(3,6)






