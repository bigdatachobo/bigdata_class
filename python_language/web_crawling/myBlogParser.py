# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:21:41 2019

@author: sundooedu
"""
import bs4 # 분석할 파일 내용을 BeautifulSoup
with open('myblog.html','r',encoding='utf-8') as fp:
    soup = bs4.BeautifulSoup(fp,'html.parser') # 파일내용 html객체가 만들어짐.
    #all_div = soup.find_all('div') # 모든 div 요소를 가지고 오겠다.
    #print(all_div)
    div = soup.find('div') # 첫번째 div 요소를 찾아서 가져온다.
    print(div)
    h1=div.find('h1') # 첫번째 div의 h1요소를 찾아서 가져온다.
    print(h1)
    print('제목 : ',h1.string) # h1 요소의 텍스트(컨텐츠만)를 찾아서 가져온다.
    #--------------------------------------------------------------------------
    header_div = soup.find('div',attrs={"id":"header"})
    print('제목 : ',header_div.string) # 요소의 텍스트(컨텐츠만)를 찾아서 가져온다.
    #--------------------------------------------------------------------------
    bs_div = soup.find('div',attrs={"id":"bs_section"})
    print('섹션 : ',bs_div.string) 
    #--------------------------------------------------------------------------
    footer_div = soup.find('div',attrs={"id":"footer"})
    print('footer : ',footer_div.string) 
    #--------------------------------------------------------------------------
    tag_div = soup.find('div',attrs={"id":"tag_section"})
    print('tag_section : ',tag_div.string) 
    #--------------------------------------------------------------------------
    tag_div = soup.find('div',attrs={"id":"tag_section"})
    print(tag_div["id"],':',tag_div.string)
    #--------------------------------------------------------------------------
    def getElem(tagname,attrName):
        return soup.find(tagname,attrs={"id":attrName})
'''    
    def getElemTextById(tagname,attrName):
        elem = getElemById(tagname,attrName)
        print(elem['id'],':',elem.string) 
'''
    def getElemText(elem):
        print(elem['id'],':',elem.string) 

getElemText(getElem('div','tag_section'))

class ElemFinder():
    
    def getElem(self,tagname,attrName):
        return soup.find(tagname,attrs={"id":attrName})
    
    def getElemText(self,elem):
        print(elem['id'],':',elem.string)    

e = ElemFinder()
b=e.getElem('div','footer')
e.getElemText(b)
#%%

