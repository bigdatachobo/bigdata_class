# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:41:45 2019

@author: sundooedu
"""


def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g=mygen()
next(g)
# 제너레이터 표현식
# 제너레이터 내포
gen=list((i*i for i in range(1,1001)))
print(gen)

