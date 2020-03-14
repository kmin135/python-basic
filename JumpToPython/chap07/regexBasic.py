# 정규표현식의 기초, 메타 문자

import re
'''
[] : [] 사이의 문자들과 매치
[a-zA-Z] : 모든 알파벳
[0-9] : 숫자
[] 안에서 ^는 not의 의미로 사용
[\d] : 숫자. [0-9] 와 동일
[\D] : 숫자가 아닌 것. [^0-9]
[\s] : whitespace. [ \t\n\r\f\v]
[\S] : not whitespace. [^ \t\n\r\f\v]
[\w] : 알파벳+숫자+언더바. [a-zA-Z0-9_]
[\W] : not \w. [^a-zA-Z0-9_]
'''
p = re.compile('[abc]')
print(p.findall('beforea'))

'''
Dot(.) : 개행문자(\n)을 제외한 모든 문자. re.DOTALL옵션을 주면 \n도 포함.
[.] : []안에서는 문자그대로 dot을 의미함.
'''
p = re.compile('a.b')
print(p.match('a!b'))

'''
* : 0번 이상 반복. (메모리가 허용되는 한도까지라고 볼 수 있음)
{0,} 과 동일함.
'''
p = re.compile('ca*t')
print(p.findall('ct'))

'''
+ : 1번 이상 반복.
{1,} 과 동일.
'''

'''
? : {0,1}

ab?c : a + b(있어도 되고 없어도 됨) + c
'''
p = re.compile('ca?t')
print(p.match('cat'))
print(p.match('ct'))

'''
{m,n} : [m,n] 만큼 반복
{m,} : m번 이상
{,n} : n번 이하
{m} : m번
*, +, ? 는 모두 {m,n}으로도 표현 가능함.
'''
p = re.compile('ca{2}t')
print(p.match('cat'))
print(p.match('caat'))

# 일련의 흐름
# 1. 정규식을 컴파일하여 패턴 객체 생성
pattern = re.compile('[a-z]+')
# 2. 패턴 객체가 제공하는 메서드로 문자열 검색

'''
match : 문자열의 처음부터 정규식과 매핑되는지 조사하여 Match 객체 리턴
매칭되는게 없으면 None 리턴
'''
m = pattern.match(' python')
if m:
    print('Match found : ', m.group())
else:
    print('No Match :-<')
# search : 문자열 전체를 검색하여 정규식과 매핑되는지 조사하여 Match 리턴
print(pattern.search(' python'))
# findall : 정규식과 매칭되는 모든 문자열을 리스트로 리턴
pattern = re.compile('[a-z]')
print(pattern.findall(' python'))
# finditer() : 정규식과 매칭되는 모든 문자열을 Match의 iterable 로 리턴
for searched in pattern.finditer(' python'):
    print(searched, end=', ')

'''
match 객체의 메서드

group() : 매치된 문자열
start() : 매치된 문자열의 시작 위치 (match메서드로 얻은 경우 None이 아니라면 항상 0일 것.)
end() : 매치된 문자열의 끝 위치
span() : 매치된 문자열의 (시작, 끝) 튜플
'''

print('\n###9')
pattern = re.compile(r'[\w]*')
m = pattern.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# re모듈의 match 메서드로 축약할 수 있음
print(re.match('[\w]*', 'python'))