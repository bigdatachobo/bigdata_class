# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:26:36 2019

@author: sundooedu
"""

#%%
# Quiz

class Employee:
    empCount= 1
    def __init__(self,empNo,name,salary):
        self.empNo= empNo # 기본 식별 정보 ( primary key ) 사번
        self.name= name
        self.salary= salary
        Employee.empCount += 1
    
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
    def setName(self,name):
        name=[]
        name=name.append(name)
        self.name= name
    def setSalary(self,salary):
        salary=[]
        salary=salary.append(salary)
        self.salary= salary
        
    def __str__(self):
        return f'직원수:{Employee.empCount}, 명단:{self.name}, 봉급:{self.salary}'
    
h=Employee()

h.setName('호구다')
h.setSalary('열정Pay')
h.empCount()

print(h)
#%% 선생님 답안
class Employee2:
    empCount=0
    def __init__(self,empNo,name,salary):
        self.empNo= empNo # 기본 식별 정보 ( primary key ) 사번
        self.name= name
        self.salary= salary
        Employee2.empCount += 1 # 자동을 호출되는 함수이므로 여기에 empCount를 배치한다.
    def displayEmpCount(self):
        print(f'전체 직원수:{Employee2.empCount}')
    def displayEmpInfo(self):
        """
        직원 사번 이름 월급을 출력
        """
        print(f'사번:{self.empNo}, 이름:{self.name}, 월급:{self.salary}')
    #def __str__(self):
    def __repr__(self): # regular expression
        """
        직원 사번 이름 월급을 리턴
        """
        return f'사번:{self.empNo}, 이름:{self.name}, 월급:{self.salary}'

def youRFired(e):  # 퇴사시 실행하는 함수를 새로 정의함.
    del e
    Employee2.empCount -= 1               

emp= Employee2("홍길동",1000) # C
emp.displayEmpInfo() # R P
emp.displayEmpCount()
emp.salary=emp.salary*1.1 # U   #월급 10% 인상
emp.displayEmpInfo()

# 트랜잭션(논리적인 작업(퇴사) 단위) 
del emp # D
Employee2.empCount -= 1
# 위 두개를 묶어 하나의 함수로 만듦.
youRFired(emp2) 

emp2= Employee2("홍진영",20000)
emp2.displayEmpInfo()
emp2.displayEmpCount()
#%% 
# 가상 테이블
employee2_list= []
emp= Employee2('001',"홍길동",1000)
employee2_list.append(emp)
emp2= Employee2('002',"류현진",2000)
employee2_list.append(emp2)        
emp3= Employee2('003',"추신수",3000) 
employee2_list.append(emp3) 
emp4= Employee2('004',"추신수",4000)
employee2_list.append(emp4)  

#전체 직원 객체(행) 가져와서 출력(sql의 SELECT * FROM 절)
for e in employee2_list:        
    e.displayEmpInfo() # e에 객체주소(id) e=0x12345 call by reference

for e in employee2_list: # sql의 SELECT * FROM EMPLOYEE2_LIST
    if e.name =="추신수" and e.salary == 3000: # SQL에서 WHERE E.NAME = "류현진"
        e.displayEmpInfo()

for e in employee2_list: 
    if e.name > "추신수":  # ㅎ이 ㅊ보다 높은 숫자로 배치되어있어 홍길동 출력됨
        e.displayEmpInfo()        
        
for e in employee2_list:  # (SELECT * FROM EMPLOYEE_LIST)
    if e.name > "추신수":
        e.displayEmpInfo()  

pname=input("이름 일부 : ")
for e in employee2_list: # (SELECT * FROM EMPLOYEE_LIST)
    if pname in e.name: # WHERE E.NAME LIKE "%신수%" 
        e.displayEmpInfo()  

aname=input("이름: ")
for e in employee2_list:
    if e.name == aname:
        e.salary=e.salary*(1.1) # (update * set )  # U (update)
        e.displayEmpInfo()  
        
aname=input("이름: ")
for e in employee2_list: 
    if e.name == aname:
        employee2_list.remove(e) # delete from set       
        
aname=input("이름: ")
employee2_list=list(filter(lambda e: aname != e.name,employee2_list))  # delete from set

sort_list=sorted(employee2_list,key=lambda e:e.salary,reverse=True)  # SQL ORDER BY reverse= False 면
                                                                    #순정렬, True면 역정렬       
for e in employee2_list:
    print(e)
    
help(Employee2)    # 자세한 도움말 출력.

     
    
    
#%%
plus=[2,6,16]
two=[4,36,256]

import functools
hap=functools.reduce(lambda x,y: x+y, two) #reduce(folding):값을 접어가면서(혹은 줄여가면서) 하나의 결과값을 도출하는 함수.
#%%
# Q10

import os
os.mkdir("d:/doit")
os.chdir("d:/doit")

f= os.popen("dir","r") # os.popen은 시스템 명령어(셀 명령어)를 실행한 결괏값을
print(f.read())    #읽기 모드 형태의 파일 객체로 돌려준다.

import glob
glob.glob("d:/doit/*.txt")






