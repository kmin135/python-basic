# 파일카피 등
import shutil, sys

print(sys.argv[0])

shutil.copy(sys.argv[0], 'targetFile')