# list는 []로 감싼다

# empty
empty_list = []
empty_list2 = list()
print(empty_list == empty_list2) # True

# lists. list 는 어떤 자료형도 포함 가능
odd = [1, 3, 7]
e = [1, 2, ['Life', 'is']]

# indexing, slicing 은 문자열을 다루는 것과 거의 동일함
print(e[2][1])
print(e[1:])

# 리스트 더하기
print([1,2,3] + ['a','b'])

# 리스트 곱셈
print([1,2,3] * 2)

# 리스트 길이
print(len([1,2,3,]))

# 리스트 조작
a = [1, 2, 3, 4]
a[1] = 'a'
# del은 파이썬 내장 함수
del a[2]
print(a)
# del에 슬리이싱 기법으로 n개 제거 가능
del a[1:]
print(a)

# 리스트 함수
a = [1,2,3,4]
a.append(5) # 끝에 element 1개 추가 (push)
a.sort()
a.reverse()
a.index(3) # 3의 첫번째 idx. string 처럼 없으면 에러다
a.insert(0, 'a') # index 지정하여 리스트에 추가
a.remove('a') # 첫번째 'a'를 찾아 제거
# a.remove('b') # 없는걸 지우려해도 에러
print(a)
a.pop()
a.pop(0) # 위치지정이 가능.
print(a)
# list내의 element 세기
print(a.count(2))
# extend
e1 = [1,2,3]
e1.extend(['a', 'b'])
e2 = [1,2,3] + ['a', 'b']
print(f'e1 is {e1}')
print(f'e2 is {e2}')
print(e1 == e2) # True