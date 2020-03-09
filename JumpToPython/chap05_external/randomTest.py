import random as rand

# [0.0, 1.0) 실수
print(rand.random())

# [a, b] 정수
print(rand.randint(1, 5))

# 리스트에서 랜덤한 인덱스의 값 얻기
def random_pop(d):
    idx = rand.randint(0, len(d)-1)
    return d.pop(idx)

print('# random_pop')
data = [1,2,3,4,5]
while data:
    print(random_pop(data))

# random_pop을 choice로 구현. 리스트에서 무작위로 요소를 선택하여 리턴.
def random_pop2(d):
    val = rand.choice(d)
    d.remove(val)
    return val

print('# random_pop2')
data = [1,2,3,4,5]
while data:
    print(random_pop2(data))

# 리스트 셔플
data = [1,2,3,4,5]
rand.shuffle(data)
print(data)