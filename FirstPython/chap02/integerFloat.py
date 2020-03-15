'''
python2 까지는 다른 언어들처럼 int, long을 가졌고 범위도 java와 같았음
python3 부터는 long이 없어졌고 int의 크기가 유연해짐
'''

# java라면 int형은 2^31-1 이겠으나 10^100도 별도 처리 없이 정상 출력됨
googol = 10**100
print(googol)

print(int(123.1))

# 실수형은 float
print(float('123.1'))