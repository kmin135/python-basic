import os

# path로부터 확장자 얻기
def getExt(path):
    ext = os.path.splitext(path)[-1]
    return ext[1:] if len(ext) > 0 else ''

target = '/Users/kwon/study/python-basic/JumpToPython/chap06'

# os.walk를 이용하면 손쉽게 하위 디렉토리를 리커시브하게 순회가 가능함
# 아래는 target dir을 순회하며 (path, ext) 의 튜플을 출력하는 예제
for (path, dir, files) in os.walk(target):
    for f in files:
        fPath = os.path.join(path, f)
        print((fPath, getExt(fPath)))