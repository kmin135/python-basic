# python3의 문자열은 바이트 배열이 아닌 유니코드 문자열

# 1. \u와 4자리의 16진수는 는 기본 다국어 평면의 유니코드
# - \u0000 ~ \uffff
# - 첫 번째 두 숫자는 평면 번호 (00~FF)
# - 다음 두 숫자는 평면에 있는 문자 인덱스
# - ex) 평면 00은 아스키코드이고, 그 다음 00~FF는 아스키코드의 번호와 같음

# 2. 높은 평면의 다국어일수록 비트수가 더 필요. 
# 이를 위해서는 대문자 U를 이스케이프 시퀀스로 사용하고 8자리의 16진수를 사용함
# 숫자에 남는 공간은 왼쪽에 0을 채움
# - ex) \U0001f47b

# 3. 모든 문자는 표준 이름 \N{name} 으로 지정할 수 있음.
# - ex) \N{LATIN CAPITAL LETTER A}
# - ref. www.unicode.org/charts/charindex.html

def unicode_debug(character):
    import unicodedata
    name = unicodedata.name(character)
    lookupedChar = unicodedata.lookup(name)
    print(f'char {character}, name : {name}, value : {lookupedChar}')

unicode_debug('A')
unicode_debug('권')
unicode_debug('\u00a2') # EURO SIGN
unicode_debug('\u2603')

# len 함수는 바이트가 아닌 문자수를 센다
print(len('$') == len('\U0001f47b'))

# 파이썬3는 유니코드 인코딩으로 UTF-8 사용
'''
UTF-8은 동적 인코딩 방식
* 1바이트 : 아스키코드
* 2바이트 : 키릴 문자를 제외한 대부분의 파생된 라틴어
* 3바이트 : 기본 다국어 평면의 나머지
* 4바이트 : 아시아 언어 및 기호를 포함한 나머지
'''

print(len('a'.encode('utf-8')), 'bytes') # 1바이트
print(len('권'.encode('utf-8')), 'bytes') # 3바이트

snowman = '\u2603'
# print(snowman.encode('ascii', 'strict')) # UnicodeEncodeError 발생.
# encode 함수는 디폴트로 strict 방식으로 동작하며 해당 인코딩으로 인코딩 불가능한 문자는 예외 발생

# 아래는 주어진 인코딩으로 인코딩이 불가할 때 예외처리 방식을 지정하는 방법들임
print(snowman.encode('ascii', 'ignore')) # 해당 인코딩에 없는 문자는 무시
print(snowman.encode('ascii', 'replace')) # 알 수 없는 문자는 ?로 대체
print(snowman.encode('ascii', 'backslashreplace')) # 유니코드 이스케이프처럼 파이썬 유니코드 문자의 문자열 생성
print(snowman.encode('ascii', 'xmlcharrefreplace')) # 유니코드 이스케이스 시퀀스 출력

# 이하 디코딩
cafe = 'caf\u00e9'
print(cafe, type(cafe))
cafe_bytes = cafe.encode('utf-8')
print(cafe_bytes, type(cafe_bytes))
cafe_decoded = cafe_bytes.decode('utf-8')
print(cafe_decoded)
