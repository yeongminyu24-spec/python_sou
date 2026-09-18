# cgi-bin/my.py : 웹용 파이썬 - 클라이언트에서 전송한 값 수신


# -*- coding : utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')  # 한글 깨짐 방지


import os
import urllib.parse



# 클라이언트 URL뒤에 ?변수=값&변수=값 하고 주면 환경변수 QUERY_STRING에 넣어줌
query = os.environ.get("QUERY_STRING","")
params = urllib.parse.parse_qs(query)
# 문자열을 딕셔너리 형태로 변환하게 됨 
# {'name':['홍길동'],'age':['23']}

# 값 꺼내기 - 첫번째 값 꺼내기는 [0]
irum = params.get("name",[""])[0]    # 값이 없으면 [""]
nai = params.get("age",[""])[0]    
print(f"서버에서 출력 :  {irum}님은 {nai}살")


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
    자료 출력 : {0}, {1}
    <br/>
    <a href="../index.html">메인으로</a>   # 한 단계 상위폴더 

</body>
</html>
""".format(irum,nai))   # 전체 열을 문자열로 처리해버리는 
# """   """  이렇게 하면 관리하기 쉽다. 






