list1 = [1,2,3]
tuple1 = ('a','b','c','d')

# zip 함수로 iterable 객체들을 묶어 병렬로 순회할 수 있음.
# 이 때 더 짧은쪽에 맞춰짐
for data1, data2 in zip(list1, tuple1):
    print(data1, data2)

# 그 외에도 zip으로 n개의 iterable 타입들을 묶어 list, dict 등으로 만들 수 있음
print(list(zip(list1, tuple1)))
print(dict(zip(list1, tuple1)))

# zip의 결과는 zip class인데 iterable함