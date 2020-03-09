'''
10미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
(단, 3과 5의 공배수는 1번씩만 더해야한다.)
'''

# 3의 배수의 개수? n/3 = 대충 333개
# 5의 배수의 개수? n/5 = 대충 200개

# 사이트 풀이외에 두 수의 배수를 이용한 방법
threeBaesu = 3
fiveBaesu = 5
baesu = 2
maxVal = 1000
baesuSum = 0
while threeBaesu < maxVal or fiveBaesu < maxVal:
    baesuSum += threeBaesu
    baesuSum += fiveBaesu if fiveBaesu < maxVal and fiveBaesu % 15 != 0 else 0

    threeBaesu = 3 * baesu
    fiveBaesu = 5 * baesu
    baesu += 1
print(baesuSum)

# 사이트 풀이. brute force
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)