# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:30:44 2019

@author: sundooedu
"""
#%%
import sqlite3
import pandas as pd
 
# sqlite db 연결
conn = sqlite3.connect("test.db")
 
# connection 으로부터 cursor 생성
cur = conn.cursor() # sql 쿼리를 실행시켜주는 것.

# SQL 쿼리 실행
cur.execute("select * from employee") 
# result_set = pd.read_sql("select * from customer",conn) #DataFrame에 sql 테이블 넣기

# 1. 모든 데이터 Fetch(적출) 방법 / 적출 방식이므로 다시 자료를 불러드리기 위해선 다시 cursor()를 실행시켜야 한다.
#rows = cur.fetchall() # 결과집합 >>> 리스트 형식 ex) [(1, 'Alex', 1, 'SEA'), (2, 'Alex', 2, 'Sky')]
#for row in rows:    # 단일 행은 >>> 튜플 형식 ex) (1, 'Alex', 1, 'SEA')
#    print(row)

# 2. 모든 데이터 Fetch(적출) 방법
for row in cur: # "cur = conn.cursor()"를 바로 대입하여 적용 가능
    print(row)
# 코드가 끝나면 cur에는 행이 없게된다.(None)
# 다시 아래 코드(for문)를 작동시키기 위해선 다시 cursor()를 실행시켜 행들을 가져와야한다.
cur.execute("select * from customer")     
for row in cur: # 순서대로 실행시 이 코드에서는 결과값이 출력이 안된다.
    print(row)    

# 행을 한개만 가져오고 싶을때.
cur.execute("select * from customer")     
rows = cur.fetchone()
rows # (1, 'Alex', 1, 'SEA') 튜플 형식으로 반환됨.

# 행을 두개만 가져오고 싶을때.
# or 일부 수개 데이터 Fetch(적출) 방법
cur.execute("select * from customer")
two_row = cur.fetchmany(2) # 여러개를 가져오고 싶을때 >>> fetchmany()
two_row # [(1, 'Alex', 1, 'SEA'), (2, 'Alex', 2, 'Sky')] 리스트 형식으로 반환됨


# 페이징 처리 
# 시작 인덱스가 = (페이지 번호 - 1) * 2
# 1번 페이지
cur.execute("select * from customer LIMIT 0,2") # LIMIT (시작 번호, 표시할 개수)
two_row = cur.fetchmany(2)
two_row

# 2번 페이지
cur.execute("select * from customer LIMIT 2,2") # LIMIT (시작 번호, 표시할 개수)

# 3번 페이지
cur.execute("select * from customer LIMIT 4,2")

two_row = cur.fetchmany(2)
two_row

# Connection 닫기
conn.close()
#%%
import sqlite3
 
conn = sqlite3.connect("test.db")
 
cur = conn.cursor()
#%%
sql = "select * from customer where category =: category and region =: region"
cur.execute(sql, {'region':'SEA', 'category':1}) # 튜플로 되어 있음.
rows = cur.fetchall()
for row in rows:
    print(row)
    
sql = "select * from customer where id = :Id"
cur.execute(sql, {"Id": 1})
rows = cur.fetchall()
for row in rows:
    print(row)    
#%% 
conn.close()
 
#%%
sql = "select count(*) from customer"
cur.execute(sql) # 튜플로 되어 있음.
rows = cur.fetchall()
for row in rows:
    print(row[0]) # 결과값이 튜플로 나오므로 (5,), row[0]으로 인덱스 0을 줘서 5만을 뽑아낸다.
#%%    
sql = "select * from customer"
import pandas as pd
df = pd.read_sql(sql,conn) # pandas가 sql을 읽고, DataFrame으로 만들어준다.
df['id'].count() # 결과값 : 5
df

#%%
# 페이징
sql = "select count(*) from customer"
cur.execute(sql)
row = cur.fetchone()
row_count = row[0] # 5
page_per_num=2
import math
last_page_num = math.ceil(row_count / page_per_num)

for p_num in range(1,last_page_num+1):
    print(p_num)

pbunho = int(input('페이지 번호 >>>'))

#%%
# 시작 인덱스 = (페이지번호-1)*2
# 1번 페이지

cur.execute("select * from customer order by id desc limit ?,2",[(pbunho-1)*page_per_num]) # 페이지를 역순으로 보이게 한다. "order by id desc"
print("고객목록")
for row in cur:
    print(row)
conn.close() # 종료 전에 컨넥션 끊어준다.
input("아무 키나 입력하면 종료")


    

















