import sys

# 실행 환경에 따라 경로를 수정해서 확인
# sys.path는 파이썬 라이브러리가 설치되어 있는 경로
# 해당 경로값을 직접 제어함으로써 import가 가능하다.
# java로 치면 inline으로 classpath를 추가하는 느낌
sys.path.append('/Users/kwon/study/python-basic/JumpToPython/chap04')
print(sys.path)

import five 

# 또 다른 방법으로 환경 변수 PYTHONPATH에 path를 설정한 뒤 해당 셸에서 실행해도 가능하다
'''
export PYTHONPATH=/Users/kwon/study/python-basic/JumpToPython/chap04

# 위의 sys.path를 주석처리한 뒤에 PYTHONPATH 를 테스트해보자
'''