# w모드로 열면 파일이 생성됨
f = open('newFile', 'w')
f.close()   # file descriptor 는 직접 닫아주는게 좋다

# mode는 r, w, a 가 있다.
# w는 기존 내용상관없이 덮어씌운다.

f = open('newFile', 'w')
for v in range(10):
    f.write(f'{v+1}번째 줄입니다.\n')
f.close()

f = open('newFile', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()

# 모든 내용을 리스트로 읽기
f = open('newFile', 'r')
for line in f.readlines():
    print(line, end='')
f.close()

# append
f = open('newFile', 'a')
f.writelines(['야\n', '호\n'])
f.close()

# 모든 내용을 string 으로 얻기
f = open('newFile', 'r')
print(f.read())
f.close()

# file 의 스코프 제한. with 구문 종료와 함께 파일 자동 close (java의 try-with-resources)
with open('newFile', 'r') as f:
    print(f.read())