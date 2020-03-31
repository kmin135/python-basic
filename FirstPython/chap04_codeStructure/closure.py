# 내부 함수

def knight(saying):
    def inner():
        return "We are the knights who say: '%s'" % saying
    return inner()

print(knight('khs'))

# 내부 함수를 이용해 클로져처럼 행동
# 클로져(closure) : 외부 함수에 의해 동적으로 생성되고, 그 함수의 변수값을 알고 있는 함수

def knight2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    # inner2를 호출하지 않고 그대로 리턴. 이 때 inner2는 saying을 기억하는 특별한 inner2 함수의 복사본
    return inner2   

k1 = knight2('khs')
k2 = knight2('kwon')

# k1은 함수이자 클로져 
print(type(k1), k1)

print(k1())
print(k2())