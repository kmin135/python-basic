rows = range(1,4)
cols = range(1,3)

# list comprehension (함축, 내포)를 통한 cells list 정의
# [ 표현식 for 항목 in iterable ]
cells = [(row, col) for row in rows for col in cols]
print(cells)

# 언패킹으로 출력
for row, col in cells:
    print(row, col)

# dictionary comprehension 을 활용한 문자열의 알파벳별 개수 세기
# { 키 표현식 : 값 표현식 for 표현식 in iterable }
word = 'letters'
result = {letter : word.count(letter) for letter in set(word)}
print(result)

# set comprehension
# { 표현식 : for 표현식 in iterable }
# comprehension에는 아래 처럼 조건도 지정 가능함. (당연히 list, dict comprehension도 가능)
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

# tuple comprehension은 없음
# 아래일 것 같지만 아래는 generator 객체임.
iam_not_tuple = (num for num in range(1,5))
print(type(iam_not_tuple))

# generator도 iterable함.
# 하지만 즉석에서 값을 생성하고 값을 처리한 뒤 이 값을 기억하지 않음.
first_consume = list(iam_not_tuple)
second_consume = list(iam_not_tuple)
print('f:', first_consume)
print('s:', second_consume)