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

# 가변 인자(위치 기반) : tuple로 전달
def print_args(*args):
    print(args)
print_args(1, 2, 3)

# 가변 인자(키워드 기반) : dictionary로 전달
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1, b='hahaha', c=(1,2,3))