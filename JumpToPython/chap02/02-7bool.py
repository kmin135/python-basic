# a = true  # 첫 자리 대문자임
a = True
b = False

# type : 자료형 체크 내장함수
print(type(a))

# 참, 거짓 분류
# 참 : "python", [1,2,3], 1
# 거짓 : "", [], (), {}, set(), 0, 0.0, None

# 활용
iter = [1,2,3]
while iter:
    print(iter.pop())

# bool : 인수가 어떤 bool type인지 반환
print(bool('python'))
print(bool(None))