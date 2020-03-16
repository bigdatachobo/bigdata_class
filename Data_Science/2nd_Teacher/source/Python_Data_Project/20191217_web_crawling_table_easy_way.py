# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:08:43 2019

@author: sundooedu
"""
#%%
import pandas as pd
df = pd.read_html('https://finance.naver.com/sise/sise_quant.nhn')
df
df[0].to_excel('../data/20191217_quiz_read_html_table_easy.xlsx')
#%%
import urllib.request as req
import pandas as pd

url = "https://finance.naver.com/sise/sise_quant.nhn"
res = req.urlopen(url).read()

content = res.decode('euc-kr','replace').encode('utf-8','replace')

df = pd.read_html(content)
df