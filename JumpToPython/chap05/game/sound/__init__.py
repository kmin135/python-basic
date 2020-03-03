'''
from game.sound import *
구문은 sound 패키지의 모든 모듈을 import 하는 것처럼 보이는데
sound 패키지의 __init__.py 에 아래와 같이 __all__ 리스트에 지정된 모듈만 import 된다

아래를 주석처리하고 game-init.py 를 실행해보면 아래의 에러가 발생한다
ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package
'''
__all__ = ['echo']