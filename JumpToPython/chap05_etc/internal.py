# 내장함수들

print(abs(-3.2))

# 인수의 iterable이 모두 참이면 true
print(all([True, 1, 'abc']))
# 인수의 iteralbe중 하나라도 참이면 true
print(any([True, False, 0]))

# 키 코드값 -> 아스키코드문자
print(chr(65))
# 아스키코드문자 -> 아스키 코드값
print(ord('A'))

# 객체가 가지는 멤버변수, 메서드 조회
print(dir('a'))

# 나머지 연산에서의 몫과 나머지
print(divmod(7,3))
# (7//3, 7%3)

# iterable 자료형을 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
# 순회중에 index를 알아야할 필요가 있을 때 유용
for i, value in enumerate(['body', 'foo', 'bar']):
    print(i, value)

# 말그대로 evaluation
print(eval('1+2+3'))

# filter : 대상 iterable 중 filter에 지정한 함수의 조건을 만족하는 것만 골라내어 filter타입으로 리턴한다. java8에서 보던 그것
def isOdd(x):
    return x % 2 == 0

print(list(filter(isOdd, [1,2,3,4,5])))
# 함수가 None이면 iterable중 true로 취급되는 것만 필터링한다는 의미
print(list(filter(None, [1,0,'a',None,True,False])))
# 람다를 활용하면 더 간단
print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5])))

# map : 대상 iterable에 일괄적으로 함수를 적용한다
print(list(map(lambda x : x * 2, [1,2,3])))

# 8진수, 16진수
print(oct(8))
print(hex(15))

# 객체 주소값 구하기
print(id('a'))

# 표준입력
# a = input('Enter : ')
# print(a)

# casting
print(int('3'), int(3.7))
# 진법 변환 "2진수 101을 10진수로 변환"
print(int('101', 2))
# 입력된 객체를 문자열로 캐스팅
print(str(123))
print(str([1,2,3]))

# isinstance 이름그대로 특정 객체의 인스턴스인지 구분
class Person: pass
print(isinstance(Person(), Person))
print(isinstance('abc', Person))
print(isinstance('abc', str))

# len : 인자로 넘어온 iterable 의 길이
print(len('abcd'))
print(len([1,2,3]))

# list : iterable을 받아 list로
print(list('abc'))
print(list([1,2,3]))
print(list({'x','y','z'}))

# tuple : iterable을 받아 tuple로
print(tuple([1,2,3]))

# set : iterable을 받아 set으로
print(set([1,2,3]))

# max, min : iterable을 받아 max, min얻음
print(max([1,2,3]))
print(min('bca'))

# sum : 숫자타입을 가지는 iterable 객체를 받아 합계를 리턴
print(sum([1,2,3]))

'''
open : 파일열기. 모드를 생략하면 디폴트로 'r' 모드.
w, r, a, b 모드가 있음
b 모드는 w, r, a와 함께 사용
'''
# f = open('binaryfile', 'rb')

# 제곱
print(pow(2,3))

'''
range : start, stop, step 조건으로 특정 범위의 숫자값을 얻을 수 있는 iterable한 range 객체를 반환
'''
# stop만 지정하면 0부터. [0,1,2]. [0,n)
print(list(range(3)))

# start까지 지정하면. [s,0)
print(list(range(1,3)))
print(list(range(-10,-1)))

# step은 간격. 위의 예제들은 step이 1인 것.
print(range(1,10,2))
# 음수도 가능하다 [-1,-3,-5,-7,-9]
print(list(range(-1,-10,-2)))

# 반올림. 두번째 인수는 소수점 자리수 지정
# python2는 익숙한 사사오입방식
# python3는 오사오입법. 통계학적으로는 오사오입이 더 유용하다나 뭐라나 (나무위키)
print(round(4.5))
print(round(4.6))
print(round(4.555, 2))

# 입력을 정렬한 후 결과를 리턴함. 입력객체 자체가 정렬되는게 아님.
a = [3,2,1]
b = sorted(a)
print(a)
print(b)

# list의 sort 메서드는 자신을 정렬한다는 점이 다름
print(a.sort()) # 자신을 정렬할 뿐이므로 리턴이 None
print(a)

# 인수의 자료형 리턴
print(type('abc'))

# zip 동일한 개수로 이루어진 iterable을 n개 받아 묶어준다
# 개수가 서로 다르면 가장 개수가 작은 쪽에 맞춰진다
print(tuple(zip([1,2,3], ['a','b','c'])))
