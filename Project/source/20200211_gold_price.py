# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:59:42 2020

@author: sundooedu
"""
#%%
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import os

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Project/source')

def gold_price(page):
    url = f'https://finance.naver.com/marketindex/goldDailyQuote.nhn?&page={page}'
    result = requests.get(url)
    soup = BeautifulSoup(result.content,'html.parser')
    price = soup.find_all('td')
    
    line = []
    price_each = []
    for i,p in enumerate(price):
        if (i)%9 == 0:
            line.append(p.text)
        elif (i)%9 == 1:
            line.append(p.text)     
        elif (i)%9 == 2:
            line.append(p.text) 
        elif (i)%9 == 3:
            line.append(p.text) 
        elif (i)%9 == 4:
            line.append(p.text) 
        elif (i)%9 == 5:
            line.append(p.text) 
        elif (i)%9 == 6:
            line.append(p.text) 
        elif (i)%9 == 7:
            line.append(p.text)
        elif (i)%9 == 8:
            line.append(p.text)
            price_each.append(line)
            line=[]
    price_arr = np.array(price_each)
    return price_arr        

if __name__=='__main__':
    
    table = pd.DataFrame()
    for i in range(330):
        temp = pd.DataFrame(gold_price(i+1))
        table = pd.concat([table,temp],axis=0)
        
    table.columns=['날짜','매매기준율','전일대비','사실때','파실때',
                   '입금시','해지시','기준국제_금_시세','기준_원달러_환율']
    table.reset_index(inplace=True)
    table.drop('index',axis=1,inplace=True)
    table.to_excel('../data/gold_price.xlsx',
                   index=False)
