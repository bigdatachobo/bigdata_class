# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:12:43 2019

@author: sundooedu
"""
#%%
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # 기저조건
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # 메모이제이션
 
    return memo[n]


