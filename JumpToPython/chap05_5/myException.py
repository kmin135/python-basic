class MyError(Exception):
    def __init__(self, msg='MyError Occur!'):
        self.msg = msg
    '''
    __str__은 print(e) 에서 객체의 대표 출력값으로 사용된다. java의 toString()
    
    참고로 아래 예제를 __str__ 을 주석처리하고 출력하면 MyError raise때 지정한 인수값이 출력된다.
    인수값 없이 __init__에 정의된 디폴트값을 쓰도록 해봤는데 이 경우에는 print(e)는 빈값이고 print(e.msg)는 "MyError Occur!"가 출력됐다.
    나름의 규칙이 있겠지만 헷갈리니까 명시적으로 __str__을 잘 정의하는게 좋겠다.
    '''
    def __str__(self):
        return "__str__로 정의된 메시지"

def say_nick(nick):
    if nick == '바보':
        raise MyError('바보가 아닙니다')
    print(nick)

try:
    say_nick('바보')
except MyError as e:
    print(e)
    print(e.msg)


