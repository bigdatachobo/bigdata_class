# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:11:49 2019

@author: sundooedu
"""
#%%
import bs4
with open('myblog2.html','r',encoding='utf-8') as fp:
    soup = bs4.BeautifulSoup(fp,'html.parser') # 파일내용 html객체가 만들어짐.
    #all_div = soup.find_all('div') # 모든 div 요소를 가지고 오겠다.
    all_div = soup.select('div') # 모든 div 요소를 가지고 오겠다.
    for i,div in enumerate(all_div): # 모든 div 요소를 순서대로 찾아서 가져온다.
        print(f'{i+1}. {div.text}')       # enumerate는 인덱스 번호를 같이 적용하는 함수임.
        print('-'*18)     # div.string 해도되고 div.getText(), div.text 해도됨
   #---------------------------------------------------------------------------
                    # css에선 '#'이 id를 의미함
    #elem = soup.select_one('div#tag_section > p.para') # select_one에서 "_one"은 한개만 가지고 오라는 의미
    para = soup.select('p.para') # CSS 선택지 표기법 (권장됨)
    for i,p in enumerate(para): # 모든 div 요소를 순서대로 찾아서 가져온다.
        print(f'{i+1}. {p.string}')       # enumerate는 인덱스 번호를 같이 적용하는 함수임.
        print('-'*18)
        
    para = soup.select('p[class=para]') # HTML 표기법
    print(para)    
        
        
        
        
        