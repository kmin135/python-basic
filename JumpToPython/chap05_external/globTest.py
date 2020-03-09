import glob, os

# 디렉토리에 있는 파일목록을 얻는다.
# 기본적으로 *, ? 메타 문자 사용이 가능.
# 순회모드를 사용할 경우 ** 지정도 가능.
print(glob.glob(os.getcwd() + '/*'))