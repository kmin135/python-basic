'''
4.9 데코레이터
데코레이터는 자바의 어노테이션과 유사하다
소스 코드를 수정하지 않고 기존 함수의 기능을 확장할 수 있다.

1. *args와 *kwargs
2. 내부 함수
3. 함수 인자
'''

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(1,2))
# 수동으로 데코레이터 적용
new_add_ints = document_it(add_ints)
print(new_add_ints(1,2))

@document_it
def add_ints_with_deco(a, b):
    return a + b

print(add_ints_with_deco(3,4))

def let_it_be(func):
    def new_function(*args, **kwargs):
        print('Let it be')
        return func(*args, **kwargs)
    return new_function

# 2개 이상일 때는 def와 가장 가까운 데코레이터가 먼저 적용됨
# 위치를 바꿔서 실행해보자
@document_it
@let_it_be
def add_ints_with_two_deco(a, b):
    return a + b

print(add_ints_with_two_deco(4,5))