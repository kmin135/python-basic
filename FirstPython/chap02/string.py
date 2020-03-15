'''
문자열은 시퀀스이다.
문자열은 불변이다.
'''

# casting. 문자열 보간이 이루어질때도 내부적으로 사용함.
print(str(99.9))

# slice : [start:end:step]
# [start,end) 를 step만큼 건너띄면서 slice.

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[4:20:3])
# step을 이용한 역순 출력
print(letters[::-1])

# join()
print(':'.join(['a', 'b', 'c']))

s1 = '''first the
hahaha
second the...'''
print(s1.find('the'))
print(s1.rfind('the'))  # 끝에서부터 찾기
print(s1.strip('.'))    # strip은 trim을 말하며 제거할 문자를 직접 지정할 수 있음

s1 = "A duck GOES into a bar"
print(s1.capitalize())  # 첫번째 단어의 첫글자만 대문자로 변환
print(s1.title())       # 모든 단어의 첫글자를 대문자로 변환
# upper, lower는 예상대로 동작
print(s1.swapcase())    # 대문자와 소문자를 토글