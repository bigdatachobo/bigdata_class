# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:28:33 2019

@author: sundooedu
"""

a="hobby"
a.count('b')
a.find('b') #0부터 세서 0,1,2 세번째 위치가 2인 위치여서 2를 출력
a.index('b')
b = "Python is the best best choice"
b.find('best')
b.index('k')
",".join('abcd')
",".join(['a', 'b', 'c', 'd'])
a = "you"
a.upper()
 a = "HI"
a.lower()
a = " hi "
a.lstrip()
a= " hi "
a.rstrip()
a = "           hi         "
a.strip()
a="      \nPython is the best best choice"
a.strip().count('best')
a.strip()
a.count('best')
a.strip().count('best')
print(a)

a = "Life is too short"
a.replace("Life", "Your leg")

b="You should do your best everytime"
b.replace("everytime","everysection")

c="Life is too short, you need python"
c.split()
d="a:b:c:d:e:f"
d.split(':')
a="py@naver.com"
b=a[:-10]
print("아이디={0}".format(b))

email="py@naver.com"
at_finder=email.find('@')
before_at=email[:at_finder]
print("아이디={0}".format(before_at))

a="py@naver.com"
b=a.find('@')
d=a[:b]
print("아이디={0}".format(d))

a="py@naver.com"
b=a.split('@')
print("아이디={0}".format(b[0]))

a="py@naver.com"
b=a.split('@')
c=b[1].split('.')
print("도메인={0}".format(c[0]))

a="py@naver.com"
b=a.find('@')
c=a.find('.')
d=a[b+1:c]
print("도메인={0}".format(d))

a = [1, 2, 3]
print(str(a[2]) + "hi")

a = [1, 2, 3]
a[2] = 4
a
print(a)