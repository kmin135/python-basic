# t1과 같이 ,가 들어간 상태로 초기화해도 tuple이다. 다만 ()을 적어주는게 가독성이 좋다.
t1 = 'a',
t2 = 'a', 'b'
print(t1)
print(t2)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
# tuple unpacking 을 활용한 변수 초기화
a, b, c = marx_tuple
print(a, b, c)

'''
tuple의 사용처

1. tuple이 list대비 적은 공간을 사용한다. (정말일까?)
2. immutable한 특성을 활용할 때 -> 변경 불가. 변경불가하므로 딕셔너리의 키로도 사용 가능.
3. named tuple을 객체의 단순한 대안으로 사용 가능
4. 함수의 인자들이 튜플로 전달됨
'''