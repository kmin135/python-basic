'''
4.10 네임스페이스와 스코프

메인프로그램 : 전역 네임스페이스 정의
'''

animal = 'fruitbat'
def change_and_print_global():
    # 전역 변수 animal을 참조하려면 global 키워드로 전역 변수 접근을 명시해야함
    # 이 라인을 제거하면 지역 변수 animal은 없으므로 에러 발생함
    global animal

    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

'''
locals 함수 : 로컬 네임스페이스의 내용이 담긴 딕셔너리 반환
globals 함수 : 글로벌 네임스페이스의 내용이 담긴 딕셔너리 반환
'''

animal2 = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())

change_local()

print('globals:', globals())