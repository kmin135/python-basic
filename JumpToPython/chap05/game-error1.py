import game

game.sound.echo.echo_test()

'''
AttributeError: module 'game' has no attribute 'sound'
위의 에러 발생!

import game을 수행하면 game 디렉토리의 모듈 또는 game 디렉토리의 __init__.py에 정의한 것만 참조할 수 있다
'''