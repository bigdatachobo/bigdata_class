# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:39:22 2019

@author: sundooedu
"""
# 모듈화 일시에 대한 
from datetime import datetime,timedelta # 나중에 따로 모듈을 생성할 수 있기 때문에
                                        # "from"  "import"를 같이 적어주는게 좋다.    
def print_Reg_Date(regDateTime):
    diff = datetime.now() - regDateTime
    if diff.days > 0 :
        print(diff.days,"일 이전")
    else:
        print(diff.seconds//3600,"시 이전")
        
if __name__== '__main__':        
        
    newsDateTime=datetime(2019,10,16,8,3,0)
    print_Reg_Date(newsDateTime)

from dateutil.relativedelta import relativedelta

diff=relativedelta(datetime.now(),oldDateTime).months # 달수       
diff=relativedelta(datetime.now(),oldDateTime).days   # 일수
diff=relativedelta(datetime.now(),oldDateTime).hours  # 시수

