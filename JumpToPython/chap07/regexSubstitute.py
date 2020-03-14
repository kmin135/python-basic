import re
'''
문자열 바꾸기 : sub 메서드
정규식과 매칭되는 부분을 다른 문자열로 변경
'''

p = re.compile('(blue|red|white)')
print(p.sub('colour', 'blue socks and red shoes and white hat'))

# 변경 회수 제한
print(p.sub('colour', 'blue socks and red shoes and white hat', count=2))

# subn : sub와 달리 치환한 결과문자열과 치환된 횟수를 튜플로 묶어 리턴
print(p.subn('colour', 'blue socks and red shoes and white hat'))

'''
sub 메서드를 그룹핑과 사용하기

sub의 바꿀 문자열에 \g<그룹이름> 의 문법으로 정규식의 그룹 이름을 참조할 수 있음
'''

data =  '''
kwon 123456-1234567
kim 181818-1929321
'''

pat = re.compile("(\d{6})[-](\d{7})")
# 뒤의 숫자 masking
print(pat.sub("\g<1>-*******", data))
# 순서 바꾸기
print(pat.sub("\g<2>-\g<1>", data))


'''
sub 메서드의 첫 번째 매개변수로 함수 사용하기
매치된 부분마다 함수가 적용된다
'''

def toHex(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
ret = p.sub(toHex, 'Call 65490 for printing, 49152 for user code.')
print(ret)

p = re.compile(r'\d+')
ret = p.sub(lambda match : 'odd' if int(match.group()) % 2 is 1 else 'even', '123 hahaha 234')
print(ret)