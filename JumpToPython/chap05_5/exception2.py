# raise 명령어로 예외를 발생시킬 수 있음
class Bird:
    def fly(self):
        raise NotImplementedError('fly를 구현하라')

class Eagle(Bird):
    pass

class FlyEagle(Bird):
    def fly(self):
        print("I can fly")

try:
    Eagle().fly()
except NotImplementedError as e:
    print(e)

FlyEagle().fly()