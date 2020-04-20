'''
generator : 파이썬의 시퀀스를 생성하는 객체
한 번에 메모리에 생성&정렬하지 않고 잠재적으로 아주 큰 시퀀스를 순회할 수 있음
제네레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환함

range() 함수도 제네레이터임.
'''

print(sum(range(1,10)))

'''
잠재적으로 큰 시퀀스를 생성하고, 제네레이터 컴프리헨션에 대한 코드가 길다면 제네레이터 함수를 정의할 수 있음
제네레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환함

일반 함수와 달리 yield 키워드로 값을 반환
'''

def my_range(first=0,last=10,step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)
mr = my_range(1,10)
print(mr)

print(sum(mr))