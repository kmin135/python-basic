# 시간 관련 함수
import time

# unix time을 초단위로 리턴.
print(time.time())

# unix time을 년, 월, 일 등의 튜플로 정리하여 리턴
lt = time.localtime(time.time())
print(lt.tm_year)

# 지정된 시간을 기본 포맷팅하여 리턴
print(time.asctime(time.localtime(time.time())))

# 현재시간을 포맷팅하여 리턴
print(time.ctime())

# 시간 커스텀 포맷팅. bash의 그것과 유사해보인다.
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

# Thread.sleep(). 초단위임.
print('3초 슬립...')
time.sleep(3)
print('3초 슬립 끝')