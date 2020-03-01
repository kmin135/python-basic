import sys

# public static void main(String[] args) 의 args
# 0번째는 실행한 파일명
args = sys.argv[:]

for arg in args:
    print(arg)
