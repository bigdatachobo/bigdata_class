# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:18:10 2019

@author: sundooedu
"""
import os
import glob
import time

def find_file(path,extension):
    
    st=time.time()
    os.chdir(path)
    file_list_py=glob.glob('**/*.'+extension, recursive=True)
    for file in file_list_py:
        print(os.path.abspath(file))
    et=time.time()
    print(f'실행시간 = {et-st} 초')
    
   