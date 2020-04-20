def echo(anything):
    print(anything, anything)

echo('hi')

'''
함수로 전달한 값을 인자(argument)라고 부른다.
인자와 함수를 호출하면 인자의 값은 함수 내에서 해당하는 매개변수(parameter)에 복사된다.
'''

def do_nothing():
    pass

print(do_nothing() is None) # 명시적인 리턴이 없으면 None

# 기본 매개변수값 지정
def menu(wine, dessert='pudding'):
    return {'wine':wine, 'dessert':dessert}

print(menu('ghost'))

# 기본 인자값은 함수 실행마다 계산되는게 아니라 함수를 정의할 때 계산됨. 그래서 아래와 같은 버그가 생길 수 있음
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')  # ['b'] 일 것 같지만 ['a', 'b'] 가 출력됨

# 가변 인자(위치 기반) : tuple로 전달
def print_args(*args):
    print(args)
print_args(1, 2, 3)

# 가변 인자(키워드 기반) : dictionary로 전달
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1, b='hahaha', c=(1,2,3))

# 파이썬의 함수는 일등 시민 (매개변수로 전달 가능)
def run_func(func, arg1, arg2):
    return func(arg1, arg2)

def add(arg1, arg2):
    return arg1 + arg2

print(run_func(add, 1, 2))