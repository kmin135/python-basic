# java의 set이다
# 초기화 방법
s_empty = set()
print(f'im not set. i am {type({})}')
s1 = set([1,2,3,1])
s2 = set("hello") # string 도 올 수 있음
s3 = {1,1,2,3}
print(s_empty)
print(s1)
print(s2)
print(s3)

# 중복허용X, 순서가 없다는 점에서 hashset 과 유사
# 순서가 없으니 인덱싱 접근 당연히 안 되고 list나 tuple로 캐스팅하여 접근한다
l1 = list(s1)
t1 = tuple(s1)
print(l1)
print(t1)

# 교집합, 합집합, 차집합
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print(f'교집합 {s1 & s2}, {s1.intersection(s2)}')
print(f'합집합 {s1 | s2}, {s1.union(s2)}')
print(f'차집합 {s1 - s2}, {s1.difference(s2)}')

# 집합 함수
# add 요소 1개 추가
s1 = {1,2}
s1.add(3)
s1.update([1,'a'])
print(s1)
s1.remove('a')
print(s1)