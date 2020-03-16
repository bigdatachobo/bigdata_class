# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:16:27 2019

@author: sundooedu
"""
quiz_line=['가나다\n','라마바\n']
quiz_line=list(reversed(quiz_line))

with open("quiz.txt",'w',encoding='utf-8') as f:
    f.writelines(quiz_line)

    
with open("quiz.txt",'r',encoding='utf-8') as fp:
    answer=fp.readlines()    
    print(answer)

#%% 

# 코드 리팩토링
with open('quiz.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    
lines.reverse()

with open('quiz.txt','w',encoding='utf-8') as f:
    for line in lines:
        f.write(line) #라인쓰기
        f.write('\n') # 줄바꿈 문자 삽입
#%%
a= ['1','3','2']  
a=sorted(a)      
a.sort()  
b= ['1','3','2','2','3','1']         
c=set(b)
c=sorted(list(c))
print(c)


