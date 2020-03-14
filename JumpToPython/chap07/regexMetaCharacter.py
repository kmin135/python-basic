import re

'''
| : or
^ : 문자열의 맨 처음과 일치함을 의미. re.MULTILINE과 쓰면 여러 줄의 문자열일 때 각 줄의 처음과 일치
$ : 문자열의 맨 끝과 일치. ^와 반대
\A : ^와 기본적으로 동일. 단, re.M과 쓰일 때는 줄과 상관없이 전체 문자열의 처음하고만 매치
\Z : $와 기본적으로 동일. \A의 특성과 동일
\b : 단어 구분자(word boundary). 보통 whitespace 를 의미
'''

print(re.match('Crow|Servo', 'CrowHello'))

# \b 는 기본 string에서는 backspace를 의미하므로 raw string으로 사용해야 동작함
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

'''
\B : \b와 반대. 즉 whitespace가 아닌 것.
'''