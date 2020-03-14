'''
backslash 문제
'''

import re

target = "\\section"
# \section 이라는 문자열을 찾고싶다면?

# 1. \s가 공백문자 정규식으로 해석되므로 검색 실패
print(re.match('\section', target))

# 2. \\가 문자열 리터럴 규칙에 따라 \로 치환되고 결국 정규식 엔진에는 또 \s가 전달되므로 1번과 동일
print(re.match('\\section', target))

# 3. 4개를 붙여야 정규식 엔진에 \\가 전달되어 \section을 찾을 수 있음
print(re.match('\\\\section', target))

# 4. 정규식앞에 r을 붙여 정규식의 raw string으로 해석하게 하면
# \가 일반 string의 \\와 동일하게 해석된다.
print(re.match(r'\\section', target))
