# 임시파일 도움 모듈
import tempfile as tf

# 중복되지 않는 임시 파일의 이름을 무작위로 만들어줌
# mac에서 돌려보니 /var/folders/2m 하위로 만들어졌음. os마다 다를듯.
nextFilename = tf.mkstemp()
print(nextFilename)

# 임시 파일 생성. close하면 제거됨.
f = tf.TemporaryFile()
f.close()