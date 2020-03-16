# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:44:31 2019

@author: sundooedu
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

import mod3
print(mod3.mul(4,2))


sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
import mathod
ace=reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])


Student=(student.name,student.blood_type,student.age)

student_objects = [
                    Student('john', 'A', 15),
                    Student('jane', 'B', 12),
                    Student('dave', 'B', 10),
                  ]

sorted(student_objects, key=lambda student: student.age)