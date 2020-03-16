# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:16:02 2019

@author: sundooedu
"""
def two_times(num):
    return num*2

def work(key,start,end,sub_total_dict):
    sub_total=0 # start,end 수열 부분합
    for i in range(start,end):
        sub_total+=i
        #print(key,'스레드', sub_total)        
    # sub_total_dict 공유사전에 부분합 추가.    
    sub_total_dict[key] = sub_total 