import sys

# 명령행인수 출력
print(sys.argv)

# 현재 참조중인 path
print(sys.path)
# append로 path 추가 가능
sys.path.append('.')

# 강제종료
sys.exit()