# html에서 성별 넣어줘야 함 

# cgi-bin/friend.py : 웹용 파이썬 - 클라이언트에서 전송한 값 수신

# -*- coding : utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')  # 한글 깨짐 방지

import os
import urllib.parse

# get / post 요청 구분
method = os.environ.get("REQUEST_METHOD","GET")

if method == "POST":
    length = int(os.environ.get("CONTENT_LENGTH",0))
    body = sys.stdin.read(length)
else:   # get 일때
    body = sys.viron.get("QUERY_STRING","")

params = urllib.parse.parse_qs(body)

irum = params.get("name", [""])[0]
junhwa = params.get("phone", [""])[0]
gen = params.get("gen", [""])[0]


print("Content-Type:text/html; charset=utf-8")

print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world</title>
</head>
<body>
    <b>world 페이지</b>
    <br/>
    자료 출력 : 이름은 {0}, 전화는 {1}, 성별은 {2}
    <br/>
    <a href="../index.html">메인으로</a>   # 한 단계 상위폴더 

</body>
</html>
""".format(irum,junhwa,gen)) 

