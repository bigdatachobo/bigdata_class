# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:44:46 2019

@author: sundooedu
"""
import os
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    contact_list=[contact for contact in contact_list if contact != name]

def load_contact(contact_list):
    if os.path.exists("contact_db.txt"): # contact_db.txt 존재하는지 확인하는 라인.
        f = open("contact_db.txt", "rt",encoding="utf-8")
        lines = f.readlines()
        num = len(lines) / 4
        num = int(num)

        for i in range(num):
            name = lines[4*i].rstrip('\n')
            phone = lines[4*i+1].rstrip('\n')
            email = lines[4*i+2].rstrip('\n')
            addr = lines[4*i+3].rstrip('\n')
            contact = Contact(name, phone, email, addr)
            contact_list.append(contact)
        f.close()

def store_contact(contact_list):
    f = open("contact_db.txt", "wt",encoding="utf-8")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ == "__main__":
    run()

#%%  중복값 해결이 안됨.
c_list= ['a','b','a','a']
# i는 반복할때마다 1씩 증가
for contact in c_list:
    if contact == 'a':
        del c_list[c_list.index(contact)] # 변경된 인덱스 새로구함
#%%
c_list= ['a','b','a','a']   
c_list=[contact for contact in c_list if contact != 'a'] 











        