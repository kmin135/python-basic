def add(a, b):
    return a + b
def sub(a, b):
    return a - b

'''
__name__ 은 이 파일이 직접 실행된경우 "__main__" 이고
다른 모듈에서 import되어 호출될 때는 자신의 모듈명인 "mod1" 이다

모듈을 import 하면 print() 등도 모두 실행되므로 이를 막을 때 __name__ 변수를 활용할 수 있다
'''
# print(f'My name is {__name__}')
if __name__ == "__main__":
    print('i am mod1!')