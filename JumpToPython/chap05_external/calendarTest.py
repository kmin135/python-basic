import calendar as cal

# 특정년도 달력 출력
# print(cal.calendar(2020))
cal.prcal(2020)

# 특정년도, 월 달력 출력
cal.prmonth(2020, 3)

# 년, 월, 일의 요일정보
# 0: 월요일 ~ 6: 일요일
print(cal.weekday(2020, 3, 8))

# 년, 월의 1일이 무슨 요일인지와 그 월이 며칠까지 있는지 튜플로 리턴
print(cal.monthrange(2020, 3))  # 2020.03.01은 일요일이니 (6, 31)