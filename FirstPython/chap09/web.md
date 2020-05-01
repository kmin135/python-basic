# 9.2 웹 서버

* 내장된 테스트용 웹 서버
```bash
# 포트 생략하면 기본 8000
python -m http.server 8080
```
* WSGI (Web Server Gateway Interface) : 파이썬 웹 애플리케이션과 웹 서버 간의 범용적인 API

## 9.2.5 Flask 실습

* virtualenv 로 환경설정
```bash
pip3 install virtualenv
virtualenv venv/path
source venv/path/bin/activate
pip install flask
pip list
# 현재 환경에 설치한 라이브러리 목록 저장 
pip freeze > requirements.txt
```

## 9.2.6 비파이썬 웹 서버

* Flask에 내장된 웹 서버는 디버깅용으로만 사용해야한다
* 배포용 서버로는 다음 두 가지 방식이 일반적
    1. apache web server + mod_wsgi module
    1. nginx + uWSGI app server
        * nginx는 파이썬 모듈이 없고 대신 uWSGI 같은 별도 WSGI 서버를 사용하여 통신함

## 9.2.7 기타 프레임워크

* Flask 같은 작은 프레임워크는 보통 데이터베이스를 직접 지원하지 않음
* 보통 django를 많이 씀
    * 전형적인 CRUD 웹 페이지 생성을 위한 ORM 코드를 포함함
* https://wiki.python.org/moin/WebFrameworks

## 9.3.4 크롤링과 스크래핑

* scrapy 가 유명한 크롤러(crawler) + 스크래퍼(scraper)
* BeautifulSoup와 같은 모듈이 아닌 프레임워크임

## 9.3.5 HTML 스크랩하기

* HTML 파싱용으로 BeautifulSoup 가 유명