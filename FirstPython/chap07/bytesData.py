'''
파이썬에서 이진데이터 다루기

byte는 immutable
bytearray는 mutable
'''

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
# the_bytes[1] = 127 # TypeError: 'bytes' object does not support item assignment

the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

'''
바이트 혹은 바이트배열 데이터를 출력할 때 출력불가한 바이트는 \\xxx 양식을 사용하고
출력할 수 있는 바이트는 아스키코드 값을 사용함
(\\x0a 대신 \n 가 출력되는 것처럼 일부 아스키코드 값은 일반적인 이스케이프 문자를 사용하여 출력됨)
'''
blist = bytes(range(0, 256))
print(blist)
