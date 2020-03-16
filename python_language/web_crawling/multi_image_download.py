# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:03:53 2020

@author: sundooedu
"""
#%%
import requests as rq
from bs4 import BeautifulSoup as bs

URL="https://pixabay.com/images/search/?cat=animals"

html_img=rq.get(URL).text
soup_img=bs(html_img,"lxml")
img_element=soup_img.select('img')
img_element[0:3]
