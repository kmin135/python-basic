a = 5
if a > 4:
    print('a is bigger than 4')
elif a > 2:
    print('a is bigger than 2')
else:
    print('a is small')

'''
조건문과 같이 계층구조인 경우 indent가 강제됨
문법적으로는 공백문자1개든 tab이든 계층구조간의 일정한 indent가 유지되면 동작함

보편적인 권장사항은 tab 또는 공백문자4개 이고 뭐가 됐든 프로젝트에서 컨벤션으로 통일하는게 중요함
요즘은 공백문자4개가 대세라고 함
'''

# if, for, def, class 등의 문장 끝에는 콜론(:) 이 항상 들어감

# and, or, not은 그대로 사용함 (&&, ||, ! 없음)
print(True and True)
print(True or False)
print(not False)

# in 연산자 : 리스트, 튜플, 문자열과 같은 iterable 자료형에 대상이 존재하는지 유무 반환
print(1 in [1,2,3])
print('a' in "abc")

# pass 아무일도 안 하고 넘기곡 싶을때
have_roles = ['admin', 'normal']
if 'admin' in have_roles:
    pass
else:
    print('you are not admin')

# oneline if
if True: pass
else: print("false")

# 삼항 연산자는 없고 조건부 표현식으로 대체가능
# [참인 경우] if [조건식] else [거짓인 경우]
score = 80
msg = 'success' if score > 70 else 'fail'
print(msg)