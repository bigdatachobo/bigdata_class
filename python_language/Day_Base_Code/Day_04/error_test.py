# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:08:39 2019

@author: sundooedu
"""

def add_mul(choice, *args): 
    if choice == "add": 
         result = 0  # 0값으로 초기화
         if(args==True):
             for i in args: 
                 result = result + i 
    elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
    return result     


add_mul('add', 1,2,3,4,5)