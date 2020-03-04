# 내장함수들

print(abs(-3.2))

# 인수의 iterable이 모두 참이면 true
print(all([True, 1, 'abc']))
# 인수의 iteralbe중 하나라도 참이면 true
print(any([True, False, 0]))

# 아스키 코드값 -> 아스키코드문자
print(chr(65))
# 아스키코드문자 -> 아스키 코드값
print(ord('A'))

# 객체가 가지는 멤버변수, 메서드 조회
print(dir('a'))

# 나머지 연산에서의 몫과 나머지
print(divmod(7,3))
# (7//3, 7%3)