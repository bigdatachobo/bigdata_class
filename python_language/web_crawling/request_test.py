# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:42:19 2019

@author: sundooedu
"""
#exchangeList > li.on > a.head.usd > div > span.value
#oilGoldList > li.on > a.graph_img > img
#exchangeList > li.on > a.head.jpy > div > span.value
#exchangeList > li.on > a.head.eur > div > span.value
import bs4
import urllib.request as req
 
html = req.urlopen('https://finance.naver.com/marketindex/')
bs = bs4.BeautifulSoup(html, 'html.parser')
price = bs.select_one('a.head.eur > div > span.value')
print(price.string)