# tuple은 ()로 감싼다
# tuple은 값을 바꿀 수 없다
# 그 외에는 list와 동일하다. immutable한 list로 볼 수 있다.

t1 = ()
t2 = (1)
print(t2)
t3 = (1, 2, 3)
t4 = 1, 2, 3    # 괄호 생략 가능
t5 = (1, 2, ('a', 'b'))
print(t5)

t4_1 = t4[1:]
print(t4)
print(t4_1)

# t5[1] = 'error' # TypeError: 'tuple' object does not support item assignment