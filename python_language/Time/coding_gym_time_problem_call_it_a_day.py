# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:23:56 2019

@author: sundooedu
"""
#%%
import datetime as dtt
# 현재시간
c_time = dtt.datetime.now()
# 퇴근시간
l_time = c_time.replace(hour=17, minute=50, second=0)

# 남은 시간 계산 (퇴근 시간이 지난 경우 익일 퇴근까지의 시간)
dif_sec = (l_time - c_time).total_seconds()
dif_sec = dif_sec + 60 * 60 * 24 if dif_sec < 0 else dif_sec

print(f"남은 시간 {dtt.timedelta(seconds=dif_sec)}({dif_sec:,.0f}초)")
