# python3 tabToSpace.py src.txt dst.txt

import sys

with open(sys.argv[1], 'r') as srcFile:
    srcContents = srcFile.read()

# dstContents = srcContents.replace('\t', '    ')
dstContents = srcContents.replace('\t', ' ' * 4)

with open(sys.argv[2], 'w') as dstFile:
    dstFile.write(dstContents)