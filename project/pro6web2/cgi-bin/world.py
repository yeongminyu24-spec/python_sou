# cgi-bin/world.py : 웹용 파이썬
import sys
sys.stdout.reconfigure(encoding='utf-8')  # 한글 깨짐 방지


v1 = "자료1"
v2 = "두번째 자료"

print("Content-Type:text/html; charset=utf-8")
print()


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

    <img src="../images/images.jpeg" />

    <br/>
    <a href="../index.html">메인으로</a>   # 한 단계 상위폴더 

</body>
</html>
""".format(v1,v2))   # 전체 열을 문자열로 처리해버리는 
# """   """  이렇게 하면 관리하기 쉽다. 





