'''
아래와 같이 __main__ 으로 실행된 경우 절대경로를 sys.path 에 추가하는 방법을 이용할 수 있다
'''

if __name__ == '__main__':
    if not __package__:
        import sys
        from os import path
        print(path.dirname( path.dirname( path.abspath(__file__) ) ))
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from sound.echo import echo_test
    else:
        from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

if __name__ == '__main__':
    render_test()

'''
또 다른 방법으로 대상 패키지들의 루트 디렉토리로 이동한 뒤 (여기서는 [...]/chap05)
아래와 같이 패키지명을 지정하여 실행하는 것도 가능하다.

python3 -m game.graphic.render2

반면에 game 디렉토리까지 들어간뒤
python3 -m graphic.render2 로 시도하면 아래 에러가 발생한다
ValueError: attempted relative import beyond top-level package
'''