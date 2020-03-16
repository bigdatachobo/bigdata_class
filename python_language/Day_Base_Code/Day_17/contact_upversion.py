# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:16:02 2019

@author: sundooedu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:33:37 2019

@author: sundooedu

1. 연락처 데이터를 객체화
2. 연락처 객체 CRU(상세검색 기능 누락)DP (Read : 전부조회, 정렬조회, 상세검색 누락됨), 
               A(분석,max,min,빈도수)
               
상세검색 로직
결과 (결과화면) : Name,Phone Number, E-mail, Address
입력 (결과화면) : Name
입력 -> 결과 산출 과정(제어) 연락처.Address=새값
: if (Name 일치하는 연락처) print_info()             
"""
import os
import collections
import random
#
class Contact:        #ID 추가
    def __init__(self, ID, name, phone_number, e_mail, addr):
        self.ID= ID
        self.name= name
        self.phone_number= phone_number
        self.e_mail= e_mail
        self.addr= addr
# =============================================================================
#   def print_info(self):
#        print("Name: ", self.name)
#        print("Phone Number: ", self.phone_number)
#        print("E-mail: ", self.e_mail)
#        print("Address: ", self.addr)
# =============================================================================
        """
        표준 __str__(self)로 변경
        f-format으로 변경
        """
    def __str__(self): # ID 추가
        print(f'ID:{self.ID}')
        print(f'Name:{self.name}')
        print(f'Phone Number:{self.phone_number}')
        print(f'E-mail:{self.e_mail}')
        print(f'Address:{self.addr}')
                   
def set_contact():
    ID=input("ID: ")
    name= input("Name: ") 
    phone_number= input("Phone Number: ")               
    e_mail= input("E-mail: ")
    addr= input("Address: ")
    contact= Contact(ID, name, phone_number, e_mail, addr) #클래스에 입력 자료 넘김
    return contact #클래스 리턴

def print_contact(contact_list):
    for contact in contact_list:
        contact.__str__()

def delete_contact(contact_list, ID, name): # 삭제가 불완전함 ( ShinSu 삭제 명령시 먼저 들어온 추신수만 삭제)
    return [contact for contact in contact_list if contact.ID != ID and contact.name != name] 
            
def load_contact(contact_list):
    if os.path.exists("contact_db.txt"): # contact_db.txt 존재하는지 확인하는 라인.
        #f = open("contact_db.txt", "rt")
        with open("contact_db.txt","rt",encoding="utf-8") as f:
            """
            with open as f: 로 변경
            """
            lines = f.readlines()
            num = len(lines) / 5 # 4에서 5로 바꿈
            num = int(num)
        
            for i in range(num):
                ID= lines[5*i].rstrip('\n')
                name= lines[5*i+1].rstrip('\n')
                phone= lines[5*i+2].rstrip('\n')
                email= lines[5*i+3].rstrip('\n')
                addr= lines[5*i+4].rstrip('\n') 
                contact= Contact(ID, name, phone, email, addr)
                contact_list.append(contact)
            #f.close()

def store_contact(contact_list):
#    f = open("contact_db.txt", "wt",)
    with open("contact_db.txt","wt",encoding="utf-8") as f:
        """
        with 구문으로 대체
        """
        for contact in contact_list:
            f.write(contact.ID + '\n')
            f.write(contact.name + '\n')
            f.write(contact.phone_number + '\n')
            f.write(contact.e_mail + '\n')
            f.write(contact.addr + '\n') 
#    f.close()

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 이름 기반 상세 검색")
    print("5. 연락처 빈도수 정렬")
    print("6. 연락처 최빈값 출력")
    print("7. 연락처 주소 수정")
    print("8. 종료")
    menu = int(input("메뉴선택: ")) # int(menu)에서 menu= int(input())으로 변경
    return menu

def search_contact(contact_list,name): # 검색 기능 함수 추가
# =============================================================================
#     for i, contact in enumerate(contact_list):
#         if contact.name == name:
#             contact_list[i].__str__() # print()는 사용 못하고 __repr__()을 사용하여 출력함.
# =============================================================================
    # 선생님 코드
    for contact in contact_list:
        if contact.name == name:
            contact.__str__()        

# 연락처에 있는 (이름:빈도수) 빈도수 기준으로 내림차순(역정렬) 정렬 리스트
def order_contact(contact_list):
    # 이름 리스트 생성 [1]
    c_list=[]
    for contact in contact_list:
        c_list.append(contact.name)
    print(sorted(c_list))
    # 단어(이름) 빈도수 사전 생성[2]
    c_dict = collections.Counter(c_list)        
    ordered_list = sorted(c_dict.items(),key=lambda x:x[1],reverse=True)
    print("정렬 리스트 : ",ordered_list)   
    return ordered_list # 1.리턴 ordered_list 

def max_contact(contact_list):
    # 2. ordered_list 리턴값을 받기 위해 order_contact() 함수 호출
    ordered_list = order_contact(contact_list)
    m = max(ordered_list,key=lambda x:x[1])
    print("-"*30)
    print("최빈값 : ",m)
    print("-"*30)
    
def updat_contact(contact_list):
    name = input("Name: ")
    for contact in contact_list:
        if contact.name == name:
            addr = input("수정할 주소: ")
            contact.addr = addr
            contact.__str__()    
        
def run(): # 메뉴번호와 함수매핑 분기자, 스위처, 컨트롤러, 매니저
    contact_list=[]
    load_contact(contact_list)
    while 1: # True와 같이 bool 값으로 항상 True 임을 의미함
        menu= print_menu()
        if menu == 1: # 연락처 입력
            contact= set_contact()
            contact_list.append(contact)
        elif menu == 2: # 연락처 출력
            print_contact(contact_list)
        elif menu == 3: # 연락처 삭제
            ID= input("ID: ")
            name= input("Name: ")
            # contact_list가 변경된 새 리스트를 return 받음.
            contact_list = delete_contact(contact_list, ID, name)
        elif menu == 4: # 이름으로 연락처 검색
            name= input("Name: ")
            search_contact(contact_list, name)
        # 메뉴5 경우,order_contact() 분기(호출)    
        elif menu == 5: # 이름 빈도수 내림차순 정렬
            order_contact(contact_list)
        elif menu == 6: # 이름 빈도수 최빈값 출력
            max_contact(contact_list)
        elif menu == 7: # 주소 수정
            updat_contact(contact_list)             
        elif menu == 8: # 종료
            store_contact(contact_list)
            break
            # 이름 리스트 생성
# =============================================================================
            # 메뉴 5번을 로직으로 짝을 경우의 코딩
            #메뉴 5번은 함수를 이용한 경우.
#             c_list=[] # 이름 리스트 생성
#             for contact in contact_list:
#                 c_list.append(contact.name)
#             print(sorted(c_list))
#             #이름:빈도수를 사전에 저장
#             c_dict=dict()
#             for name in set(c_list):# 고유 이름집합
#                 ## 이름: 빈도수 아이템을 사전에추가
#                 c_dict[name]=c_list.count(name)
#                 # 키(key) 기준 items() 정렬 리스트
#             #orderd_c_list=sorted(c_dict.items())
#             # key 값 기준이 아닌 value(빈도수)값 기준 items() 정렬 리스트        # (key:value) 튜플로 묶여 리스트에 들어가므로 
#                                                                                  #  x[0]:x[1] 형태가 되어 x[1]이 value 값을 뜻함
#             orderd_c_list=sorted(c_dict.items(),key=lambda x:x[1],reverse=True) # x는 item, x[1] value(빈도수) 값
#             print("연락처 이름:빈도수 리스트",orderd_c_list)       # reverse True는 역정렬을 뜻함               
#             
# =============================================================================
            

if __name__ == "__main__":
   run()


    