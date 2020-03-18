# while의 else 구문과 마찬가지로 break로 탈출하지 않을 때 else 구문 실행됨
datas = []
for data in datas:
    print('found data!')
    break
else:
    print('cannot find data...')

'''
for는 range() 함수로 특정 범위의 숫자 스트림을 순회할 때 사용하기 좋음.
스트림이므로 메모리를 전부 사용하지 않고, 프로그램의 충돌 없이 아주 큰 범위를 생성할 수 있음.

[start, stop)
range(start, stop, step)
'''

for x in range(2, -1, -1):
    print(x)
