# key, value 형태의 자료형. java의 map, js의 연관배열

dic = {'name':'kwon', 'phone':'010-1111-2222', 1:'a', 'list':[1, 2]}
print(dic)
# error_list_dic = {[1,2]:'a'}  # TypeError: unhashable type: 'list'
tuple_dic = {(1,2):'tuple v'}
# tuple은 키로도 사용 가능. 즉, immutable한 자료형만 key로 올 수 있다. (같은 이유로 map도 key가 될 수 없음)
print(tuple_dic)

# 딕셔너리 요소 추가
dic = {'key1':'v1'}
dic[0] = 'v0'
dic['key2'] = 'v2'
print(dic)

# 딕셔너리 요소 삭제
del dic[0]
print(dic)

# 당연히 key가 중복되면 안 됨

# 딕셔너리 함수들

# key list 
dic = {'k1':'v1', 'k2':'v2'}
print(dic.keys())   # 2.7까지는 key의 list를 리턴했으나 3.0부터는 dict_keys 타입을 리턴
for k in dic.keys():    # dict_keys도 itertable 이긴 하다
    print(f'k is {k}')

key_list = list(dic.keys()) # list로 casting
print(key_list)

# value list
print(dic.values()) # dict_values 타입

# key, value pair. key, value 쌍을 튜플로 묶어서 리턴함.
print(dic.items())  # dict_items 타입

# clear
dic.clear()
print(dic == {}) # True

# key로 value 얻기
dic = {'k1':'v1', 'k2':'v2'}
print(dic['k1'])
print(dic.get('k1'))
# print(dic['nokey'])   # error!
print(dic.get('nokey')) # None
print(dic.get('nokey', 'default'))  # 값이 없을 경우의 디폴트값 지정

# 딕셔너리에 key 존재 유무 확인
print('k1' in dic)
print('nokey' in dic)