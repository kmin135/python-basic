# self가 아니라 self등 마음대로 지정해도 되는데 pylint가 self 를 권장하는거보면 관례인듯
# self 는 this 의 역할을 한다고 보면 될듯
# 모든 메서드에는 self가 첫번째 파라미터로 온다
class Cal:
    # 생성자
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
    def pretty(self):
        return f'pretty {self.result}'

    def empty():
        print('나는 스태틱인가... pylint는 no-method-argument라고 경고를 띄운다')

cal = Cal()
# cal. 자체가 self와 맵핑된다고 이해하면 된다
print(cal.add(5))
print(cal.add(2))

cal2 = Cal()
print(cal2.add(2))

'''
용어 정리
cal은 Cal의 인스턴스다
cal은 객체다
즉, 인스턴스는 특정 객체(cal)가 어떤 클래스(Cal)의 객체인지를 관계위주로 설명할 때 사용
'''

print(type(cal))    # <class '__main__.Cal'>
print(cal.pretty())

# 클래스를 통해 메서드를 호출할 때는 self 파라미터를 직접 넘긴다.
# 뭔가 언어적으로 나중에 class 개념을 끼워넣은 부자연스러움이 느껴진다.
Cal.add(cal, 10)
print(Cal.pretty(cal))
print(cal.result)

# empty메서드는 cal을 받을 self가 없으니 에러가 난다.
# print(cal.empty())  # TypeError: empty() takes 0 positional arguments but 1 was given

# 이건 된다. 근데 pylint는 경고를 띄운다. static 개념은 비권장인걸까?
Cal.empty()

# 상속
class SumCal(Cal):
    def minus(self, arg):
        self.result -= arg
        return self.result
    # 메서드 이름이 같으면 그냥 오버라이딩한다. 인자는 영향을 주지 않으니 오버로딩은 없는듯.
    def add(self, a, b):
        self.result += a + b
        return self.result

sCal = SumCal()
# sCal.add(1)   # 오버로딩은 없고 오버라이딩만 되나보다
sCal.add(1, 2)
sCal.minus(3)
print(sCal.pretty())

class Family:
    lastname = "권"
    def pretty():
        # print(lastname)   # 에러난다. 정적메서드 개념은 없나보다. NameError: name 'lastname' is not defined
        pass

print(Family.lastname)
f1 = Family()
f2 = Family()
print(id(f1.lastname) == id(f2.lastname)) # 클래스 변수니까 주소도 같다