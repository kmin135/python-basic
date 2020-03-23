'''
함수, 클래스 등 몸체 시작 부분에 문서화를 할 수 있다. (javadoc)


좀 더 구체적인 케이스는 아래와 같이 구글의 pyguide를 참고하자
https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
'''
def echo(anything):
    '''
    echo returns its input argument
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print hte *first* argument.
    '''
    return anything

'''
help : docstring 조회용 내장함수. 
man 처럼 실행되며 코드내에 있을 경우 이후 실행이 중지된다.
'''
# help(echo)

# docstring 을 단순히 실행할 때는 아래 처럼
# __doc__ : docstring 내부 이름인 함수 내의 변수
print(echo.__doc__)