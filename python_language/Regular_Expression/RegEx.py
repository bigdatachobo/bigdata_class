# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:18:00 2019

@author: sundooedu
"""

# =============================================================================
# [ ]	문자 클래스
# .	    \n을 제외한 모든 문자와 매치 (점 하나는 글자 하나를 의미)
# *	    0회 이상 반복 (없어도 상관 없음)
# +	    1회 이상 반복 (무조건 한번 이상 등장해야 함)
# {m, n}	m회 이상 n회 이하
# |	    or 조건식을 의미
# ^	    문자열의 시작 의미
# $	    문자열의 끝을 의미
# ?	    0회 이상 1회 이하
# \	    이스케이프, 또는 메타 문자를 일반 문자로 인식하게 한다
# ( )	그룹핑, 추출할 패턴을 지정한다.
# =============================================================================


# <원래표현식>  <축약>  <부연설멸>                          <사용처>
# =============================================================================
# [0-9]	            \d	숫자를 찾는다	                    숫자
# [^0-9]	        \D	숫자가 아닌 것을 찾는다	            텍스트 + 특수문자 + 화이트스페이스
# [ \t\n\r\f\v]	    \s	whitespace 문자인 것을 찾는다	    스페이스, TAB, 개행(new line)
# [^ \t\n\r\f\v]	\S	whitespace 문자가 아닌 것을 찾는다	텍스트 + 특수문자 + 숫자
# [a-zA-Z0-9]	    \w	문자+숫자인 것을 찾는다. (특수문자는 제외. 단, 언더스코어 포함) / 텍스트 + 숫자
# [^a-zA-Z0-9]	    \W	문자+숫자가 아닌 것을 찾는다.	    특수문자 + 공백
# =============================================================================

import re
text = input("에러 표현을 입력하시오 : ")  # "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류" 입력
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group())

# up-version
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+") # 문자열(에러)+ 공백(\s) + 1개이상의 숫자(\d+)
mc = regex.findall(text) # 리스트 형식으로 값 반환.
print(mc)
# 출력: ['에러 1122', '에러 1033']

#%%
text = input("전화번호가 포함된 문장을 적으세요 : ") # "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)

# up-version
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})') # (\d{3}) >>> group(1) (지역번호) / (\d{3}-\d{4}) >>> group(2)
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num) # 032 232-3245

# up-version 2
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})') # "?P<name>정규식" 형식으로 정규식 앞에 
matchobj = regex.search(text)                               # ?P<name>을 붙이면 그룹명으로 호출할 수 있다.
areaCode = matchobj.group("area")                           # group("name") 이런 형식으로 호출함.
num = matchobj.group("num")
print(areaCode, num) # 032 232-3245
#%%
# match 함수
import re
p = re.compile('[a-z]+') #[a-z]+ : 소문자 a부터 z까지 1개 이상(+) 나오는것

m = p.match("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>

m = p.match("3 python") # 3이 처음에 나오므로 정규식과 match 되지 않아 "None" 리턴
print(m)  # None 


p = re.compile('\S+') #정규표현식 \S+ : 단어를 의미
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')
#%%
# search() 함수
m = p.search("python")
print(m) # <re.Match object; span=(0, 6), match='python'>

m = p.search("3 python")
print(m)  # <re.Match object; span=(0, 1), match='3'>
#%% 
# findall() 함수
result = p.findall("life is too short") # p = re.compile('\S+') \S : 공백을 제외한 <문자+숫자+특수문자> 전부
print(result)
# ['life', 'is', 'too', 'short']

result = re.compile("\S+").findall("life is too short") # \S+:단어 찾기
print(result)                                           # \S : 단일 알파벳 "l,i,f"
# ['life', 'is', 'too', 'short']

result=re.match("\S+","life is too short")
print(result)

result = re.compile("\S").findall("life is too short") # \S:단일 문자 찾기
print(result)
# ['l', 'i', 'f', 'e', 'i', 's', 't', 'o', 'o', 's', 'h', 'o', 'r', 't']

#%%
# finditer() 함수
result = p.finditer("life is too short")
print(result) # <callable_iterator object at 0x000001456C3050F0>
                 
for r in result: 
    print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
#%%
# match()   메소드 함수들
# group()	매치된 문자열을 돌려준다.
# start()	매치된 문자열의 시작 위치를 돌려준다.
# end()	    매치된 문자열의 끝 위치를 돌려준다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.    

import re
p = re.compile('\S+')
m = p.match("python")
m.group()
# 'python'
m.start()
# 0
m.end()
# 6
m.span()
# (0, 6)

import re
p = re.compile('[a-z]+') 
m = p.search("3 python")
m.group()  # 정규표현식이 "\S+"일 경우 # '3'이 리턴됨
# python
m.start()
# 2
m.end()
# 8
m.span()
# (2, 8)
#%%
import re
p = re.compile('[a-z]+') 
m = p.search("python")

# 축약형
m = re.match('[a-z]+', "python") # re.compile(정규식)을 줄여서 re.match(정규식, 문자열) 로 한번에 표현

#%%
# 1. DOTALL (S) : \n 포함 모든 문자 매치
p = re.compile('a.b', re.S) # re.DOTALL
m = p.match('a\nb')
print(m)
# <re.Match object; span=(0, 3), match='a\nb'>

# 2. IGNORECASE (I) : 대/소 문자 상관없이 매치
p = re.compile('[a-z]', re.I)
p.match('python')
# <re.Match object; span=(0, 1), match='p'>
p.match('Python')
# <re.Match object; span=(0, 1), match='P'>
p.match('PYTHON')
# <re.Match object; span=(0, 1), match='P'>


# 3. MULTILINE (M) : 여러줄과 매치할 수 있도록함
p = re.compile("^python\s\w+") # python 문자열로 시작 (^python)/ 화이트스페이스(\s) / 단어(\w+)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one']

# up-version

import re
p = re.compile("^python\s\w+", re.M) # re.MULTILINE

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one', 'python two', 'python three']

# 4.VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.X)  # re.VERBOSE       

#%% 
# 메타 문자
# 1. | (or) / A|B : A 또는 B
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
# <re.Match object; span=(0, 4), match='Crow'>

# 2. ^ / 문자열의 맨 처음과 일치함
print(re.search('^Life', 'Life is too short'))
#<re.Match object; span=(0, 4), match='Life'>

print(re.search('^Life', 'My Life')) # 처음에 Life가 없으면 매치되지 않음
#None

# 3. $ / 문자열의 끝과 매치함
print(re.search('short$', 'Life is too short'))
# <re.Match object; span=(12, 17), match='short'>

print(re.search('short$', 'Life is too short, you need python'))
# None

# 문자 그 자체로 매치하고 싶은 경우에는 \^, \$ 로 사용

# 4. \A / 문자열의 처음과 매치됨/ re.M과 함께 사용시 "전체" 문자열 처음과 매치됨. 
import re
p = re.compile('\ALife', re.M)
m = p.match('''Life is Good.
               but without money it turns out to Hell.''')
# <re.Match object; span=(0, 4), match='Life'>

# 5. \Z / 문자열의 끝과 매치됨 / re.M과 함께 사용시 "전체" 문자열 처음과 매치됨. 
import re
p = re.compile('Hell\Z', re.M)
m = p.match('''Life is Good.
               but without money it turns out to be Hell.''')
m
# 6. \b / 단어 구분자(Word boundary)이다. 보통 단어는 whitespace(\s)에 의해 구분
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  
# <re.Match object; span=(3, 8), match='class'>

print(p.search('the declassified algorithm')) # whitespae(\s)에 의해 구분되지 않으므로 매치 안됨.
# None

print(p.search('one subclass is')) # sub-가 있으므로 매치 안됨.
# None

# 7. \B / \b 메타 문자와 반대의 경우이다. 즉 whitespace(\s)로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  # 앞뒤가 공백이 있으므로 매치 안됨.
# None

print(p.search('the declassified algorithm')) # 앞뒤가 공백이 없으므로 매치.
# <re.Match object; span=(6, 11), match='class'>

print(p.search('one subclass is')) # 뒷부분에 공백이 있으므로 매치 안됨.
# None

p2 = re.compile(r'\Bclass\b')
print(p2.search('one subclass is')) # 앞-막힘(\B),뒤-공백(\b)이므로 sub(class)과 매치됨.
# <re.Match object; span=(7, 12), match='class'>

#%%
# Grouping

# 1. "( )" 그룹을 만들어 주는 메타문자
import re
p = re.compile('(ABC)+') 
m = p.search('ABCABCABC OK?')
print(m)
# <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())
# ABCABCABC

# 2. "\w+\s+\d+[-]\d+[-]\d+"은 "이름 + "공백" + 전화번호"
# \w+(이름) + \s(공백) + \d+(010) + [-](하이푼) + \d+(1234) + [-](하이푼) + \d+(1234)
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

# 3. 이름 부분만 선택 출력. "(\w+)" >>> \w+에 "()"를 묶어준다.
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
# park

# =============================================================================
# <<<group(인덱스)	설명>>>
# group(0) == group()	매치된 전체 문자열
# group(1)	첫 번째 그룹에 해당되는 문자열
# group(2)	두 번째 그룹에 해당되는 문자열
# group(n)	n 번째 그룹에 해당되는 문자열
# =============================================================================

# 4. 전화번호 부분만 선택 출력.
# (\d+[-]\d+[-]\d+) >>> "\d+[-]\d+[-]\d+"에 "()"를 묶어준다.
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
# 010-1234-1234

# 5. 국번 부분만 선택 출력
# ((\d+)[-]\d+[-]\d+) >>>  "(\d+)[-]\d+[-]\d+"에서 앞쪽 "\d+"에 "()"를 묶어준다.
# 그룹이 중첩되어 있는 경우는 바깥쪽부터 시작하여 안쪽으로 들어갈수록 인덱스가 증가
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
# 010

# 6. 정규식 "(\b\w+)\s+\1"은 "(그룹1) + "공백" + (\1)그룹과 동일한 단어"
# "\1"은 정규식의 그룹 중 첫 번째 그룹
# "\2"은 두 번째 그룹
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()
# the the

# 7. 그룹에 이름 붙이기
# (\w+) >>> (?P<name>\w+) >>> (?P<그룹명>정규식)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
# park

# 8. (?P=그룹명) / 그룹 이름을 사용하면 정규식 안에서 재참조하는 것도 가능
# (?P<word>\b\w+)\s+(?P=word) 
# (?P<word>\b\w+)
# (?P=word) >>> (?P=그룹명)
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()
# the the

# 9. 긍정형 전방탐색
# .+ >>> .(1글자의 모든 단어) + (1개 이상) >>> .+(모든 단어를 의미)
# (?=:) >>> (?="검색문자") 검색문자 자리에 ":"가 왔고 검색에는 사용되지만 결과 출력에는 제외됨.
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# http

# .*[.].*$ >>> "파일 이름(.*) + .([.]) + 확장자(.*$)"
# ex) foo.bar, autoexec.bat, sendmail.cf

# bat 파일은 제외할때
# .*[.][^b].*$ (불완전) >>> ex) "foo.bar" 도 걸러냄 
# .*(파일명) / [.](.) / [^b](b는 제외).*$(확장자)

# 10. 부정형 전방탐색
# .*[.](?!bat$).*$
# (?!bat$)
# 확장자가 bat가 아닌 경우에만 통과됨.

# "exe"도 같이 포함시키지 않을때.
# .*[.](?!bat$|exe$).*$
# (?!bat$|exe$)
# "|" (or)를 줘서 "bat" 또는 "exe"를 제외시킴.

# 11. 문자열 바꾸기
# sub() 메소드
# p.sub("바꿀 문자열", "대상 문자열",count=n(반복횟수))
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes') # p.sub("바꿀 문자열", "대상 문자열" )
# colour socks and colour shoes

# 한번만 바꾸고 싶을때.
p.sub('colour', 'blue socks and red shoes', count=1) # 끝에 "count=1"을 넣어준다.
# colour socks and red shoes

# subn()
p = re.compile('(blue|white|red)')
p.subn( 'colour', 'blue socks and red shoes')
# ('colour socks and colour shoes', 2)  >>> (바꿀결과, 바꾼 횟수)

# sub() 메소드 사용시 참조구문 사용
# "이름 + 전화번호"의 문자열을 "전화번호 + 이름"
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# "\g<그룹이름>" 사용하여 정규식 그룹이름 사용가능.
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 010-1234-1234 park

# sub()메소드와 group() 같이 적용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")

print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", m.group("name")+" "+m.group("phone")))

# 010-1234-1234 park

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value) # 받은 숫자를 16진수로 리턴함.

p = re.compile(r'\b\d+\b') # \d+ 숫자 정규표현식
# \b\d+\b >>> 숫자 앞뒤에 공백이 있는 단일 숫자만 찾는 정규표현식
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
# 'Call 0xffd2 for printing, 0xc000 for user code.'

# 12. Greedy VS non-Gredy
#  "*" 메타 문자는 매우 탐욕스러워서 매치할 수 있는 최대한의 문자열인 <html><head><title>Title</title> 문자열을 모두 소비
s = '<html><head><title>Title</title>'
len(s)
# 32
print(re.match('<.*>', s).span())
# (0, 32)
print(re.match('<.*>', s).group())
# <html><head><title>Title</title>
# <            .*                > 이와같이 인식하여 전체 를 출력함.

# non-Greedy 문자인 "?" 사용하면 "*"의 탐욕 제한함.
print(re.match('<.*?>', s).group())
# <html>

# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용하며
# 가장 최소한의 반복만 수행.




















