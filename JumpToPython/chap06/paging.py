'''
함수 이름은? getTotalPage
입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
출력하는 값은? 총 페이지수
'''

# param : 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# return : 총 페이지수
def getTotalPage(m, n):
    return (m // n) + (1 if m % n > 0 else 0)

for i in range(1, 5):
    print(getTotalPage(10, i))