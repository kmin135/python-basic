'''
그룹핑
1. 반복되는 문자열을 찾을 때
2. 매치된 문자열 중에서 특정 부분만 뽑아내기 위해
'''

'''
ABC 문자열이 계속해서 반복되는지 찾으려면 어떻게 할까?
(ABC)+
'''
import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

'''
이름 전화번호 에서 이름만 추출하기
'''
p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('kwon 010-1234-5678')
print(m.group(1))   # 이름
print(m.group(2))   # 전화번호

'''
Match의 group 메서드의 인덱스
0 : 매치된 문자열 전체
1 : 첫 번째 그룹에 해당하는 문자열
2 : 두 번째 ...
n : n 번째 ...
'''

'''
backreferences : 그룹핑된 문자열 재참조하기
한 번 그룹핑된 문자열을 재참조하기
'''

# (\b\w+)\s+ 는 in, 첫번째 the, 두번째 the 모두 매칭돠지만
# 첫번째그룹 \1 이 한 번 더 반복되는건 the the 뿐이다.
# 두번째그룹이 있는 경우는 \2 와 같이 사용 
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring')
print(m.group())

'''
그룹핑된 문자열에 이름 붙이기
?P<그룹명> 형태의 확장 구문 사용
'''

# ?P<name> 문법으로 그룹 이름 지정
p = re.compile(r'(?P<name>\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-2345')
print(m.group('name'))

# 백레퍼런스 (재참조)도 가능
p = re.compile(r'(?P<the>\b\w+)\s+(?P=the)')
m = p.search('Paris in the2 the2 spring')
print(m.group())