# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:11:53 2019

@author: sundooedu
"""

from xml.etree import ElementTree as et

tree= et.parse('dog.xml') # xml 분석
root=tree.getroot()
print(tree)
et.dump(tree) # xml 출력
dog_type= root.find('종류') #특정요소(태그) 찾기아서 dog_type 이라는 변수로 받는다.
print(dog_type.text)

dog_type.text= '웰시코기&푸들' # 웰시코기를 -> 웰시코기 & 푸들로 수정. 
                                # 원본 파일에는 변화가 없음. dog.xml
dog_name= root.find('이름')
print(dog_name.text)
tree.write('dog2.xml')
#%%
output_xml= '<?xml version="1.0" encoding="UTF-8"?>\n' + et.tostring(root,encoding='utf-8').decode('utf-8')

with open('dog2.xml','w',encoding='UTF-8') as f:
    f.write(output_xml)

