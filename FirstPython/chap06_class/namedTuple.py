'''
named tuple의 특징
1. 불변하는 객체처럼 행동함
2. 객체보다 공간, 시간 효율성이 좋음
3. 딕셔너리 형식의 대괄호([]) 대신, 점(.) 표기법으로 속성에 접근할 수 있음
4. 네임드 튜플을 딕셔너리의 키처럼 쓸 수 있음
'''

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill, duck.tail)

# named tuple은 불변임
# duck.bill = 'cannot change'

parts = {'bill':'wide orange2', 'tail':'long2'}
duck2 = Duck(**parts)   # **parts : 키워드 인자
# duck2 = Duck(bill = 'wide orange', tail = 'long') 과 동일
print(duck2)