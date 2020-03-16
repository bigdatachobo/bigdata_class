# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:02:22 2019

@author: sundooedu
"""

# =============================================================================
# 5. 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.  
# 또 숫자 중에서 평균을 상회하는 숫자가 몇 개나 되는지 출력하여 보자.           
# 정수를 입력하세요: 10
# 정수를 입력하세요: 20
# 정수를 입력하세요: 30
# 정수를 입력하세요: 40
# 정수를 입력하세요: 50
# 평균= 30.0
# 평균을 상화하는 숫자의 개수= 2
# =============================================================================
import numpy # 통계 라이브러리

def input_average():
    num_list=[]
    for i in range(5): 
        input_num=int(input('정수를 입력하세요: '))
        num_list.append(input_num)
    average_over=list(filter(lambda x: x > numpy.mean(num_list),num_list))
    return (f"""
평균: {numpy.mean(num_list)}
평균을 상회하는 숫자의 개수: {len(average_over)}개
분산: {numpy.var(num_list)}
표준편차: {numpy.std(num_list)}""")

print(input_average())
