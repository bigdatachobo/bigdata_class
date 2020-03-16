# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:33:00 2019

@author: sundooedu
"""
import json
 
# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
 
# JSON 인코딩
jsonString = json.dumps(customer,ensure_ascii=False) 
 
# 문자열 출력
print(jsonString)
print(type(jsonString))   # class str

import json
 
# 테스트용 JSON 문자열 -> Python 고객사전으로 변경
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
 
# JSON 디코딩
dict = json.loads(jsonString) # pickle에서 쓰는 load, json에서는 loads s가 하나 더 붙는다.
 
# Dictionary 데이타 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item']) 
#%%
import json    
# JSON 강아지 객체의 문자열   
json_str='{"이름":"식빵","종류":["웰시코기","푸들"],"나이":1,"몸무게":2.14}'    
json_dict=json.loads(json_str) #json 문자열이 파이썬 사전으로 변환됨. <- json 디코딩
print(json_dict["종류"])

# dict를 json 파일로 출력
with open("dog.json",'w',encoding='utf-8') as f:  # 암기 권장.
    json.dump(json_dict,f,ensure_ascii=False,indent='\t')
    
#%%
# JSON 문자열 <- dict (JSON 인코딩)
json_str=json.dumps(json_dict,ensure_ascii=False,indent='\t') #Json 문자열 <- dict
print(json_str)
#%%
# json 파일에서 dict를 입력(적제)
with open("dog.json",'r',encoding='utf-8') as f:    
    json_str2=json.load(f)
print(json_str2)    

    
















