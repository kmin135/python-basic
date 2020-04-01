'''
미리 정의된 __ 로 시작하고 끝나는 변수들은 파이썬 내의 사용을 위해 예약된 변수들

function.__name__ : 함수의 이름
function.__doc__ : docstring
'''

def amazing():
    '''This is amazing docstring'''
    print('func name:', amazing.__name__)
    print('doc:', amazing.__doc__)

amazing()

print('main func name:', __name__)
print('main doc:', __doc__)