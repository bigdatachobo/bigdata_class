# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:06:23 2019

@author: sundooedu
"""
import datetime
import multiprocessing as mp
from mpwork import *

def main():
    with mp.Pool(processes=7) as pool: # 2개의 프로세스 지정
        for result in pool.map(two_times, range(100)):
            print(result)

start_time = datetime.datetime.now()
main()        
print('실행시간 : ',datetime.datetime.now() - start_time)
