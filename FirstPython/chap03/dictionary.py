'''
dict 함수 : 두 값으로 이루어진 시퀀스를 딕셔너리로 변환
'''
lol = [['a','b'], ['c','d'], ['e','f']]
print(dict(lol))
lol2 = ['ab', 'cd', 'ef']
print(dict(lol2))

# update() : 딕셔너리 병합. 겹치는 키는 인자로 넘어온 dict가 우선.
src = {'a':1, 'b':2}
add = {'b':3, 'c':4}
src.update(add)
print(src)

# 항목 제거
del src['b']
print(src)

# 키 존재 유무 확인
print('c' in src)
print('d' in src)

src2 = src.copy()
print(src2)