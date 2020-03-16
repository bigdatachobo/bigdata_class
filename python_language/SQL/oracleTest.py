# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:16:06 2019

@author: sundooedu
"""

#%%
#pip install cx_Oracle
#한글처리
import os    
os.putenv("NLS_LANG", ".AL32UTF8")

# cx_Oracle 패키지 모듈들을 import
import cx_Oracle as oci

# Oracle 서버와 연결
conn = oci.connect('hr/hr@localhost:1521/xe')
conn.version

cur = conn.cursor()
sql = 'SELECT * FROM EMP'
cur.execute(sql)
for row in cur:
    print(row)
    
sql = 'SELECT SAL*(1.1) FROM EMP WHERE DEPTNO="10"'    
