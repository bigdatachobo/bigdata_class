# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:30:17 2019

@author: sundooedu
"""
# 13 자리 문자와 숫자가 섞인 비밀번호 리턴 함수 만들기

import random
import string

def secure_num_char():
    password = ''
    string_pool = string.ascii_letters + string.digits
    for i in range(18):
        rand=random.randrange(62)
        password = password + string_pool[rand]
    return password

secure_num_char()
