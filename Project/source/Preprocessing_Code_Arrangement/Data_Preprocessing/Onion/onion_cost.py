# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:35:34 2020

@author: sundooedu
"""

import pandas as pd
import numpy as np

cost = pd.read_excel('../projectdata/가락시장월별양파도매가격_2004_2019.xlsx',sheet_name=1)
cost = cost.iloc[1:]


year = []
for i in cost['거래일자']:
    year.append(i[0:4])

cost.reset_index(inplace=True)
cost['year'] = pd.Series(year)

cost = cost.iloc[:,1:]
cost.set_index('거래일자', inplace=True)

cost = cost.astype(int)

cost['양파 평균 1kg'] = cost.drop('year', axis=1).apply(lambda x: x.mean(), axis=1)

cost.groupby('year').mean().to_csv('onion_price.csv')


