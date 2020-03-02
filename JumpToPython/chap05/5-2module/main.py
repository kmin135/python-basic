# 기본 import. 모듈명. 으로 호출
import mod1
print(mod1.add(1, 2))

# 특정 메서드만 불러오기. 
from mod1 import add
print(add(2, 3))
# ','로 여러 개를 지정할 수 있음
# from mod1 import add, sub

# * 로 전체 import
from mod1 import *
print(sub(1,2))