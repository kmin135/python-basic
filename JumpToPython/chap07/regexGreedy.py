'''
정규식의 Greedy vs Non-Greedy
'''
import re

s = '<html><head><title>Title</title></head></html>'
print(len(s))

# .* 이 매치할 수 있는 최대한을 매칭하여 s 전체가 매칭됨
print(re.match('<.*>', s).span()) # (0, 46)

# * 뒤에 non-greedy 문자인 ?을 붙이면 가장 최소한의 매칭을 수행하도록 함.
# <html> 만 매칭됨
print(re.match('<.*?>', s).span()) # (0, 6)

'''
non-greedy 문자 ?는
*?, +?, ??, {m,n}? 와 같이 사용할 수 있음.
가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 함
'''