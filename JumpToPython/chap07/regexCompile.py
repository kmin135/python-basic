import re

'''
re.DOTALL 또는 re.S : . 이 개행 문자를 포함
'''

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

'''
re.IGNORECASE 또는 re.I : 대소문자 구분 없이 매치
'''

p = re.compile('[a-z]+', re.IGNORECASE)
m = p.match('PyThOn')
print(m)

'''
re.MULTILINE 또는 re.M : 여러 행에 매치
- 주로 ^ 와 $ 와 연관 
- ^ : ~로 시작
- $ : ~로 종료
'''

# re.M을 빼면 python one 만 매칭된다
# re.M 옵션을 줌으로써 각 줄마다 정규식 패턴을 찾는다.
p = re.compile('^python\s\w+', re.M)
data = """python one
life is too short
python two
you need python
python three"""
m = p.findall(data)
print(m)

'''
re.VERBOSE 또는 re.X : 정규식을 읽기 편하게 만들기
1. 컴파일될 때 공백문자가 제거된다. (단, []안의 공백문자는 제외)
2. 정규식내의 주석은 무시된다.
'''
# phone = re.compile('01[\d]-[\d]{4}-[\d]{4}')
phone = re.compile('''
01[\d]      # first three number
-
[\d]{4}     # second 4 num
-
[\d]{4}     # third 4 num
''', re.VERBOSE)
m = phone.match('010-1234-5628')
print(m)