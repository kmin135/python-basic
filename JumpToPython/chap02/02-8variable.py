a = [1,2,3]
b = [1,2,3]
# id : 변수의 메모리주소 반환
print(id(a))
print(id(b))
# 동일한 객체인지는 is 연산자로 확인
print(a is b)   # False
print(a == b)   # True
b = a
print(a is b)   # True

# list copy
a = [1,2,3]
b = a[:]    # slicing 활용

from copy import copy
b = copy(a) # copy 모듈 이용
print(b)

# 다중 초기화
a, b = (1, 2)
(a, b) = (1, 2)
(a, b) = 1, 2
a, b = 1, 2
# ()를 각각 [] (리스트) 로 치환해도 동일한 결과를 얻을 수 있다

a = b = c = 'hahaha'
print(f'a is {a}, b is {b}, c is {c}')
print(id(a), id(b), id(c))  # 모두 같음

# 두 변수의 값 변경
a, b = 1, 2
a, b = b, a
print(f'a is {a}, b is {b}')