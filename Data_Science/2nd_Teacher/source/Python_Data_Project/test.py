# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:09:29 2019

@author: sundooedu
"""
#%%
import time
from datetime import datetime
import sys

def loadingbar (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '|' * filledLength+'-' * (barLength - filledLength)
    sys.stdout.write('\r%s <%s> %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


today=(str(datetime.today()))[11:19]
print("{} 시에 이프로그램을 실행시키셨습니다.".format(today))
h,m,s=int(today[0:2]),int(today[3:5]),int(today[6:8])
now_sec=h*60*60+m*60+s
put=input("몇시퇴근입니까? 1)5시 30분 2)8시 30분 : ")
if "1"==put:
    lim_sec=62700-now_sec
elif "2"==put:
    lim_sec=73500-now_sec

_=1
print("{}시부터 퇴근5분전까지 남은시간은 {}초입니다".format(today,lim_sec-_))
for i in range(0, lim_sec-_):
    time.sleep(1)
    loadingbar(i, lim_sec, '{}초남음'.format(lim_sec-_), 'Complete', 1, 50)
    _+=1
print("야호퇴근이다")
print("퇴근축하해 :D")
input()