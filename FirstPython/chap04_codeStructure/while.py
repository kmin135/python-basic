'''
while ~ else 구문
break로 탈출하지 않은 경우 else구문이 실행됨.
'''
numbers = [1, 3, 5]
while numbers:
    number = numbers.pop()
    if number % 2 == 0:
        print('found even!')
        break
else:
    print('cannot find even...')