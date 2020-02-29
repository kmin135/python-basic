# 문자열 만들기 총 4가지 방법
print("Hello World")
print('Python is fun')
print("""Life is short,
You need Python""")
print('''Life is short,
You need Python''')

# ", ' 자체를 표현하고 싶으면 반대문자로 감싸거나 escape 한다
print("wrap 'quote")
print('wrap " double quote')
print('wrap \' \" various quotes!')

# 문자열이 multiline 이라면 """ 또는 '''
print("""This
is 
multiline
String""")
# 아니면 escape 문자 사용
print("This\nis\nmultiline\nString")

# concatenation
l = "left"
r = "right"
print(l+r)

# multiply
print("=" * 10)
print(l * 3)

# len
print(len(l))

# Indexing 
# [-n, n-1]
str = "String"
print(str[2])
print(str[-1])
# print(str[6]) index out of range!
print(str[-6])
# print(str[-7]) index out of range!

# Slicing
# str[n1:n2] -> [n1, n2)
src = "Slice me"
print(src[0:5])
print(src[1:])
print(src[:])
print(src[0:-1])

# python도 문자열은 immutable 하다
immu = "cannot change me"
# immu[2] = "r" error!

# formatting 기본. %s는 다 받을 수 있음.
print("Python is %s" % "easy")
print("My name is %s. My favriote number is %d" % ("khs", 7))

# formatting format 함수 사용
print("{0} !!".format(123))
print("{0} ... {key} {{중괄호}}".format(111, key="value"))
print("{0:<10} / {0:^10} / {0:0>10}".format("a"))

# formatting f문자열 포매팅 (python3.6+)
v1 = "khs"
dict1 = {'k1': 'v1'}
print(f"Name is {v1}. key is {dict1['k1']}")
f = 1.24
print(f"{v1:>10}, f is {f:10.4f}, {{중괄호}}")

# 대표적인 함수들
# count : 문자열에 포함된 부분문자열 카운트
print("aabc".count('a'))
# find : 문자열에 포함된 부분문자열의 첫번째 idx. 존재하지 않으면 -1
print("abc".find('b'))
# index : find와 유사하나 대상 부분문자열이 존재하지 않을 경우 오류 발생
## print('abc'.index('ccc')) error!
# join : 문자열 삽입. 
print(",".join("abc"))
# upper, lower : 생각하는 그것
# lstrip, rstrip, strip : trim
# replace (all)
print("aa is aa".replace("aa", "bb"))
# split : 지정한 문자열로 리스트로 쪼갬. 지정하지 않으면 공백문자로 쪼갬
print("a b  c".split())