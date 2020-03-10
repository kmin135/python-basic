import re

data =  '''
kwon 123456-1234567
kim 181818-1929321
'''

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******", data))