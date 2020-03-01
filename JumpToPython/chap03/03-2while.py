num = 0
while num != 1:
    num = int(input())
    print(f'num is {num}')
    if num == 99:
        break
    if num == 98: continue

while True:
    print('무한루프는 Ctlr+C로 빠져나갈 수 있음')
