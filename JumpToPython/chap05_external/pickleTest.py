import pickle

# binary로 데이터 쓰기
f = open('object.binary', 'wb')
data = {1: 'python', 2: 'java', 'a': '한글 되나?'}
pickle.dump(data, f)
f.close()

# binary로 데이터 읽기
f = open('object.binary', 'rb')
readData = pickle.load(f)
print(readData)