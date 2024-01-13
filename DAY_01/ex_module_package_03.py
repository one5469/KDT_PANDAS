# from 모듈명 import *
# => 모듈 내의 모든 변수, 함수, 클래스 포함

# import 패키지명.모듈명
import urllib.request

# from 패키지명 import 모듈명
from urllib import error, parse
from http.client import HTTPResponse

req = urllib.request.Request('https://www.google.co.kr')
response = urllib.request.urlopen(req)
html = response.read()

print(req)
print(response)
print(html)