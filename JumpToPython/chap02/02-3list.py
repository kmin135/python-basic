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

# 리스트에 값이 있나 확인
print(2 in a)

a[1] = 'a'
# del은 파이썬 구문
del a[2]
print(a)
# del에 슬리이싱 기법으로 n개 제거 가능
del a[1:]
print(a)

# 리스트 함수
a = [1,2,3,4]
a.append(5) # 끝에 element 1개 추가 (push)
a.sort()    # 리스트 자체를 정렬한다.
b = sorted(a)   # 리스트의 정렬된 복사본을 반환

a.sort(reverse=True)    # 역순 정렬
a.reverse()             # 위와 동일

a.index(3) # 값으로 index찾기. 3의 첫번째 idx. string 처럼 없으면 에러다
a.insert(0, 'a') # index 지정하여 리스트에 추가
a.remove('a') # 값으로 제거. 첫번째 'a'를 찾아 제거
# a.remove('b') # 없는걸 지우려해도 에러
print(a)
a.pop()     # stack의 pop. -1을 인자로 줘도 동일.
a.pop(0)    # 위치지정이 가능. 0이면 dequeue인 셈.
print(a)
# list내의 특정 값이 몇 개 있나 세기
print(a.count(2))
# extend : 다른 리스트 병합
e1 = [1,2,3]
e1.extend(['a', 'b'])
e2 = [1,2,3] + ['a', 'b']
print(f'e1 is {e1}')
print(f'e2 is {e2}')
print(e1 == e2) # True

# list copy하기
# copy함수는 shallow라고 주석에 나와있음. 다른 것도 알아서 deep copy가 되지는 않을 것 같고 shallow가 아닐까?
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]