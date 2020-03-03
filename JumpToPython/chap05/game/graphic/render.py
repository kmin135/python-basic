'''
render.py를 직접 실행시키면 아래 에러가 발생한다
ImportError: attempted relative import with no known parent package
이는 상대경로를 이용한 import는 기준을 __name__ 값으로 잡는데
직접 실행할 경우 __name__ 값이 "__main__" 이 되고 인터프리터는 이를 기준으로 상대경로를 잡을 수 없어서 에러가 난다

굳이 실행시키고자 하면 render2.py 참고
출처 : https://blog.doosikbae.com/52
'''
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

