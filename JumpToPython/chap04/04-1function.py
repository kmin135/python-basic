'''
함수 구조
def 함수명(매개변수):
    문장1
    문장2
    ...
'''

def add(a, b):
    return a+b
print(add(1,2.2))

# 매개변수 지정
print(add(b=2, a=1))

def noReturn():
    pass

print(noReturn()) # None : 결과값 

# 가변 인자
def add_mul(operator, *nums):
    # print(type(nums))   # tuple로 넘어온다
    if operator == 'sum':
        result = 0
        for num in nums:
            result += num
        return result
    elif operator == 'mul':
        result = 1
        for num in nums:
            result *= num
    else:
        pass
    return result

print(add_mul('sum', 1,2,3,4,5))
print(add_mul('mul', 1,2,3,4,5))
# print(add_mul('wrong', 1,2,3)) # 이건 에러난다. 변수 스코프 개념이 자바랑 다름. UnboundLocalError: local variable 'result' referenced before assignment

# kwargs (keyword arguments)
# dictionary로 인자 받기

def dic_print(**kwargs):
    # print(type(kwargs)) # dictionary 임
    print(kwargs)

dic_print(name='kwon', age=30)

# 결과값은 항상 하나
def returnTwo(a, b):
    return a, b

ret1 = returnTwo(1, 2)
print(ret1) # 리턴이 여러개면 (1, 2) 와 같이 tuple 1개로 리턴된다
print(type(ret1))

r1, r2 = returnTwo(3, 4)
print(r1, r2)   # tuple이니 당연히 이렇게도 받을 수 있다

def passpass(a):
    pass
    print('passpass pass')
    if(a == 1):
        return
    print('a is not 1')

passpass(2)

# 인자 초기값 지정
def func(name, old, man=True):
    print(name, old, man)

func('kwon', 25)
func('kwon', 25, False)

# error! 디폴트 인자는 논디폴트 인자 뒤로 와야함
# def func2(name, man=True, old):
    # print(name, old, man)

# 변수 스코프
a = 1
def asum(a):
    a += 1
    print(f'asum a is {a}')
asum(a)
print(a)
# 함수와 함수밖은 독립적인 변수 스코프 가짐

# global. 변수 스코프를 혼란시키므로 사용자제
b = 1
def bsum():
    global b
    b += 1
bsum()
print(f'b is {b}')

# lambda 
# 인라인 함수로 쓰임
# return 을 안 씀
add = lambda a, b : a+b
# add2 = lambda a, b : return a+b # error!
print(add(1,2))