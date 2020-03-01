'''
for문 기본 구조
for 변수 in iterable(리스트, 튜플, 문자열):
    문장1
    ...
'''

for i in [1,2,3]:
    print(i)

for (a, b) in [(1,2), (3,4), (5,6)]:
    print(f'{a}, {b}')

# break, continue는 while과 동일

# range : 숫자 리스트 생성용 내장함수
a = range(10)   # [0, 10)
print(a, type(a))

for v in a:
    print(v)

a = range(1, 10) # [1, 10)
sum = 0
for v in a:
    sum += v
print(f'sum [1, 10) is {sum}')

# tip : print 한줄로 출력. end 값으로 종결문자 (아마 디폴트는 \n) 를 조정할 수 있음
print('a', end='')
print('b')

# 리스트 내포 (List comprehension)
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)

# 위의 result를 리스트 내포를 이용하면 쉽게 만들 수 있다
result2 = [ num * 3 for num in a]
print(result == result2)    # True

# 조건식도 가능
# 짝수만 담기
result3 = [ num for num in a if num % 2 == 0]
print(result3)

# n개의 리스트 내포를 동시에 사용할 수 있음
# 구구단 결과 만드는 예제
gugu_result = [ a * b for a in range(2,10)
                      for b in range(1,10)]
print(gugu_result)