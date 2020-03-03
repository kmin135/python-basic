# FileNotFoundError
# f = open('없는파일', 'r')

# ZeroDivisionError
# a = 4 / 0

# IndexError
# a = [1,2,3]
# print(a[4])

# 모든 예외 잡기
# java의 catch (Exception e) 라고 보면 됨
try:
    a = 4 / 0
except:
    print('에러가 발생했음')

# 특정 예외만 잡기
try:
    a = 4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없음')

# 여러 개
try:
    # a = 4 / 0
    b = [1,2,3]
    print(b[4])
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except IndexError:
    print('인덱스 에러!')

# 한 번에 여러 개
try:
    # a = 4 / 0
    b = [1,2,3]
    print(b[4])
except (ZeroDivisionError, IndexError):
    print('0으로 나눌 수 없음. 아니면 인덱스에러인가?')

# 예외에 정의된 에러메시지 받기
try:
    a = 4 / 0
except ZeroDivisionError as e:
    print(e)

# try finally
# java와 달리 f 변수가 try밖에서도 참조가 된다
try:
    f = open('helloFile', 'w')
    f.write('hello py')
finally:
    f.close()

# 예외 무시하기
try:
    a = 3/0
except:
    pass

# except에서 trace 출력
print('#' * 10, 'trace 출력')
import traceback as tb
try:
    a = 2/0
except:
    tb.print_exc()