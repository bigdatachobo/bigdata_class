# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:25:34 2019

@author: sundooedu
"""
# 1.객체구조(클래스)
class Card:
    # def __new__(): # 객체생성자 함수 (자동정의됨)
                    #self : 함수 호출한 객체 자기 자신 
    def setPattern(self,pattern): #self=> c 전달, pattern => '스페이드' 전달 받음
        self.__pattern=pattern  # "self"는 객체라 해석한다. 여기서는 self = 카드 객체
        
        
# 2. 클래스 객체
# c : 객체참조변수,객체명 (아이디) : 객체의 주소(=참조) 저장  
c= Card()  #클래스명() : 생성자 함수(객체를 생성시켜주는)[자동 정의됨]
#print(c)
c.set_pattern('스페이드')
print(c.pattern)
# 3. 클래스 객체 
c2= Card()
c2.set_pattern('다이아몬드')        
#%%
class Card2:
    def __init__(self,pattern):
        self.__pattern= pattern
    def setPattern(self,pattern):
        self.__pattern= pattern  #(언더바 두개) 객체변수 은닉(클래스 외부로부터 보호) 
        
        
c2= Card2('스페이드')
c2.__pattern= '쓰레기' # 오류 발생 않지만 '쓰레기' 실대입X
print(c2.__pattern) # 객체변수 은닉(private __) 상태이고 클래스 외부에서는 안보이게 된다.
c2._Card2__pattern= '쓰레기' # 실제 대입 O, 가능 형식.
dir(c2)
print(c2._Card2__pattern)

#%%
class Card3:
    def __init__(self):  # 기본값(초기값) 설정함수
        self.__pattern= "빈무늬" # 초기자(초기화자) : 기본값(초기값)
    def getPattern(self):
        return self.__pattern # Card3 객체에 self.pattern 미생성됨. (컵은 만들어졌지만 내용물이 텅비어있는 상태)
    def setPattern(self,pattern):
        self.__pattern= pattern
        
        
# 파이썬이 __new__() (진짜 생성자) 호출, 빈객체 생성 -> __init__() 호출 -> __pattern 변수 생성
c3= Card3() #생성자
c3.setPattern('쓰레기')
#print(c3.__pattern)
print(c3.getPattern()) # 변수에 접근 못해서 함수( getPattern() )로 변수에 접근한 후 값을 가져옴

#%%
class Card4:
    def __init__(self,pattern):
        p_list=['스페이드','클로버','다이아몬드','하트'] # 유효값 리스트
        if not pattern in p_list: # 잘못된 (무효) 값 검증
            pattern= p_list[0] #유효값으로 정제
        self.__pattern= pattern
    def getPattern(self):      #작명법  get변수명(self) ; getter라 불림.
        return self.__pattern 
    def setPattern(self,pattern): #작명법 set변수명(self,변수) ; setter라 불림.
        self.__pattern= pattern
        
c4= Card4('쓰레기') # 생성자 값의 강제화(필수입력)
print(c4.getPattern()) 

#c4.Card4('클로버') # 객체.생성자 호출X

#c4.__init__('클로버')  # __init__은 호출 가능하지만 비추천
#print(c4.getPattern())

c4.setPattern('클로버') # 초기값 수정 권장.
print(c4.getPattern()) 
#%%
class Card5:
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
    
    def setPattern(self,pattern):
        self.__pattern= pattern
    def setNum(self,num):    
        self.__num= num

c5= Card5('스페이드',1)
print(c5.getPattern(),c5.getNum())

## 은닉변수 X
'''
c5.__pattern='하트' # 이렇게 직접 변수 넣지 말기.
c5.__num=3
print(c5.__pattern(),c5.__num())  # 오류남.
'''

c5.setNum(2)
c5.setPattern('클로버')
print(c5.getPattern(),c5.getNum())

#%%

class Card6:
    def __init__(self,pattern,num,):
        p_list=['스페이드','클로버','다이아몬드','하트']
        if not pattern in p_list:
            pattern= p_list[0]
        self.__pattern= pattern
        self.__num= num
        
    def getPattern(self): 
        return self.__pattern
    def getNum(self):
        return self.__num
    
    def setPattern(self,pattern):
        self.__pattern= pattern
    def setNum(self,num):    
        self.__num= num   
   
    #def toString(self): #관례에 맞지 않음
    def __str__ (self): #개발자들 관례에 맞음
        return f'__pattern={self.__pattern}, __num={self.__num}'
              # f string format
              
c6= Card6('aa',1)
print(c6.getPattern(),c6.getNum())
#print(c6.toString())
print(c6) # print() 함수는 객체의 <def __str__ (self):> 메소드를 호출

#%%
class Card7:
    def __init__(self,pattern,num,w):
        p_list=['스페이드','클로버','다이아몬드','하트']
        if not pattern in p_list:
            pattern= p_list[0]
        self.__pattern= pattern
        self.__num= num
        self.__w= w
        
    def getPattern(self): 
        return self.__pattern
    def getNum(self):
        return self.__num
    def getW(self):
        return self.__w
    
    def setPattern(self,pattern):
        self.__pattern= pattern
    def setNum(self,num):    
        self.__num= num   
    def setW(self,w):
        self.__w= w    
    #def toString(self): #관례에 맞지 않음
    def __str__ (self): #개발자들 관례에 맞음
        return f'__pattern={self.__pattern}, __num={self.__num},__w={self.__w}'
              # f string format

c74= Card7('스페이드',4,30)
c74.setW(10)
print(c74)
c75= Card7('스페이드',5,30)
print(c75)
c75.setW(10)
c76= Card7('스페이드',6,20)
c76.setW(10)
#%%
# 높이, 너비를 클래스 변수로 선언후 코드 일괄 수정 하기.
class Card8:
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
        return f'__pattern={self.__pattern}, __num={self.__num},__w={Card8.__w}, __h={Card8.__h}'
             
Card8.setW(10) # 클래스 메소드와 변수는 객체명 및 클래스명으로 호출 가능    
               # 클래스 메소드와 변수는 클래스명으로 호출 권장
               # 클래스 메소드와 변수는 클래석 영역에 먼저 저장
               # 뒤에 객체는 힙 영역에 저장
c84= Card8('스페이드',4)
print(c84.getW())
print(c84)
c85= Card8('스페이드',5)
print(Card8.getW())
c86= Card8('스페이드',6)
print(c86.getW())
Card8.setW(20)
Card8.setH(30)
print(Card8.getW())
print(Card8.getH())


# 객체 제거
del c86
#%% 
#from "모듈명" import "클래스명"
from class_module_card_test import Card9
Card9.setH(20)
Card9.setW(20)
c9=Card9('스페이드','K')
print(c9)
#%%
