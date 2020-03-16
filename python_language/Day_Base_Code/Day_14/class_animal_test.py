# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:08:24 2019

@author: sundooedu
"""

class Animal:
    def __init__(self,name= "동물"): #매개변수 초기자
        self.name= name
    def move(self):
        print("이동")
    def speak(self): 
        pass # 오버라이딩 유도(재정의 유도)
    
    
class Dog(Animal): # 클래스가 상위클래스의 한 종류이면 상속
    def __init__(self,name= "강아지"): #매개변수 초기자
        self.name= name
    def move(self):
        print("달린다")
        super().move() # super(): 부모 클래스 
    def speak(self):
        print("멍멍") # 메소드 오버라이딩(재정의)함
        
class Poodle(Dog):
    def hunt(self):
        print("사냥")

class Cat(Animal):
    def __init__(self,name= "나비야"):
        self.name= name
    def speak(self):
        print("야옹~야옹~")
    def likeHight():
        print("높은곳 선호")
        
dog= Dog('백구') #부모 생성자 호출 "백구" 생략시 미오류 "강아지"
dog= Dog()
print(dog.name)        
dog.move()
dog.speak()        
#관리 객체들 컬렉션(컨테이너)에 모아서 그룹화 일괄처리(CRUDP)
p= Poodle("푸들")
print(p.name)
p.hunt()
p.move()
print('-'*10)

p2=Poodle("푸들2")
print(p2.name)
p2.hunt()
p2.move()
print('-'*10)

cat= Cat('야옹아')
cat= Cat()
print(cat.name)
cat.move()
cat.speak()

# 동일변수 : 동일메소드로 접근호출
#실객체 다양하므로 실행결과 다양하다 <-- 다형성 

for a in [p,p2,dog]:
    print(a.name)
    a.move()
    print('-'*10)


