# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:10:37 2019

@author: sundooedu
"""
  
#%%
su=1
while su <= 10:
    if (su%2==0):
        su+=1
        continue
    print(su)
    su+=1
#%%    
year=0
money=int(input("원금을 입력하세요 : "))

while money < 2000:
    year+=1   #year=year + 1
    interest = money*0.07
    money += interest  #money=money + interest
print(year,"돈 : %.4f" % money)    