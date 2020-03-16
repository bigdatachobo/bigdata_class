# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:31:29 2020

@author: sundooedu
"""
#%%
import pandas as pd
import sqlite3
con=sqlite3.connect("../data/library.db")
lib=pd.read_csv("../data/Library_Usage.csv")
lib.to_sql('../data/library_sql',con)
library=pd.read_sql('../data/library.db',con)
#%%
import re
age=lib['Age Range'].split(' ')