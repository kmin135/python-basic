import time
import threading

def long_task():
    time.sleep(2)
    print('working end...')

print('Start')

threads = []
for i in range(5):
    # t = threading.Thread(target=long_task,daemon=True)    # 데몬으로 실행
    t = threading.Thread(target=long_task)
    threads.append(t)

for i in range(5):
    threads[i].start()

'''
모든 쓰레드의 종료를 기다리려면 join 사용
join을 안하면 아래의 'End' 가 먼저 출력된다.
'''
# for i in range(5):
#     threads[i].join()

print('End')