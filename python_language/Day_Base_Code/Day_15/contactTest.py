# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:33:37 2019

@author: sundooedu
"""

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
        표준 __repr__(self)로 변경
        f-format으로 변경
        """
    def __repr__(self): # ID 추가
        print(f'ID:{self.ID}')
        print(f'Name:{self.name}')
        print(f'Phone Number:{self.phone_number}')
        print(f'E-mail:{self.e_mail}')
        print(f'Address:{self.addr}')
         
          
def set_contact():
    ID=int(input("ID: ")) # 숫자만 입력하도록 int() 조건 추가
    name= str(input("Name: ")) # 문자만 입력하도록 str() 조건 추가
    phone_number= input("Phone Number: ")               
    e_mail= input("E-mail: ")
    addr= input("Address: ")
    contact= Contact(ID, name, phone_number, e_mail, addr) #클래스에 입력 자료 넘김
    return contact #클래스 리턴

def print_contact(contact_list):
    for contact in contact_list:
        contact.__repr__()

def delete_contact(contact_list, name): # 삭제가 불완전함 ( ShinSu 삭제 명령시 먼저 들어온 추신수만 삭제)
    pass
            
def load_contact(contact_list):
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
    print("4. 연락처 검색")
    print("5. 종료")
    menu = int(input("메뉴선택: ")) # int(menu)에서 menu= int(input())으로 변경
    return menu

def search_contact(contact_list,name): # 검색 기능 함수 추가
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            contact_list[i].__repr__() # print()는 사용 못하고 __repr__()을 사용하여 출력함.
        

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu= print_menu()
        if menu == 1: # 연락처 입력
            contact= set_contact()
            contact_list.append(contact)
        elif menu == 2: # 연락처 출력
            print_contact(contact_list)
        elif menu == 3: # 연락처 삭제
            name= str(input("Name: "))
            delete_contact(contact_list, name)
        elif menu == 4: # 이름으로 연락처 검색
            name= str(input("Name: "))
            search_contact(contact_list, name)
        elif menu == 5: # 종료
            store_contact(contact_list)
            break

if __name__ == "__main__":
   run()

    