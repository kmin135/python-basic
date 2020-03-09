# 이름대로 os 자원 제어 지원

import os

# 환경변수 얻기
print(os.environ)
print(os.environ['PATH'])
# 현재 위치
print(os.getcwd())
# 현재 위치 변경
os.chdir('..')
print(os.getcwd())

# 명령어 실행
os.system('ls -al')

# 명령어 실행후 결과를 파일로 얻기
f = os.popen('ls -al')
print(f.readlines())

# 디렉토리 생성제거
os.mkdir('testdir')
os.rmdir('testdir')
f = open('removeFile', 'w')
# 현재 경로의 모든 파일목록 얻기
print(os.listdir(os.getcwd()))
# 리네임
os.rename('removeFile', 'removeFile2')
print(os.listdir(os.getcwd()))
# 파일제거
os.unlink('removeFile2')
print(os.listdir(os.getcwd()))