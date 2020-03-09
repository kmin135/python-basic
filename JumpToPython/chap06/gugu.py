# x단 결과를 리스트로 리턴
def gugu(x):
    results = []
    for i in range(9):
        results.append(x * (i + 1))
        i += 1
    return results

print(gugu(9))