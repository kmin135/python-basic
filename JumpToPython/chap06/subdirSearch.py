'''
하위 디렉토리의 모든 파일 출력
'''

import os

def searchDir(rootDir):
    dirStack = [rootDir]
    while dirStack:
        nextDir = dirStack.pop(0)

        for f in os.listdir(nextDir):
            fPath = os.path.join(nextDir, f)
            if(os.path.isdir(fPath)):
                dirStack.append(fPath)
            else:
                print(fPath)

target = '/Users/kwon/study/python-basic/JumpToPython'
searchDir(target)