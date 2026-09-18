# 원격 데이터 베이스
# MariaDB : 
# 준비1) IP(네트워크에서 컴퓨터나 장치를 구분하기 위한 규악)) 주소 필요.
# 준비2) 연결용 Driver file 필요


# pip install mysqlclient

import MySQLdb

# conn = MySQLdb.connect(
#     host='127.0.0.1',        # 192.168.0.32, localhost   # 127.0.0.1은 자기 자신을 의미, 즉 내 컴퓨터를 의미
#     user='root',             # 사용자 계정
#     password='123',         # 사용자 계정 비밀번호
#     database='test'
#     ,         # 접속할 DB 이름
#     port=3306                # MariaDB/MySQL 서버가 기본적으로 사용한 포트  
# )


# 연결 정보 매핑 방법 2
# config_data = {
#     "host": "127.0.0.1",
#     "user": "root",
#     "password": "123",
#     "database": "test",
#     "port": 3306,
#     "charset": "utf8"
# }
# 연결 정보 매핑 방법 3 
# 별도 저장된 json 파일 읽기
import json

with open('dbconnect.json', 'r', encoding='utf-8') as f:  # r은 읽기 전용, encoding='utf-8'은 한글 깨짐 방지
    config_data = json.load(f)  # json 파일 읽기

def myFunc():
    try:
        # 방법 2,3
        conn = MySQLdb.connect(**config_data)  # DB 연결  # dict여서 **를 붙인다. 
        cursor = conn.cursor()  # SQL 처리를 위한 객체 생성
        # conn.autocommit(True)  # 자동 커밋 설정, commit()을 생략 가능
        # conn.autocommit(False)  # 수동 커밋 : 기본값   , 수동이 좋은 방법임 


        # 자료 추가
        # isql = "insert into sangdata values(5,'마스크',5,'3000')"  # 파이썬은 수동 데이터는 로컬에만 저장
        # cursor.execute(isql)

        # isql = "insert into sangdata values(%s,%s,%s,%s)"  # 파이썬은 수동 데이터는 로컬에만 저장
        # # ins_data =(6,'커피',10,5000)  # 튜플 타입
        # ins_data = 6,'커피',10,5000  # 튜플 타입

        # cursor.execute(isql, ins_data)  # SQL 실행
        # conn.commit()  # 원격 db에 저장됨 


        # 자료 수정
        """
        usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"  #   code는 primary key이므로 수정 불가
        up_data = '물티슈', 3, 1000, 5     # (물티슈, 3, 1000, 5) 튜플 타입
        cursor.execute(usql, up_data)
        conn.commit()  # 원격 db에 저장됨
        """

        """
        usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"  #   code는 primary key이므로 수정 불가
        up_data = '콜라', 11, 3000, 6     
        # insert, update, delete는 성공하면 성공 갯수, 실패하면 0을 반환 
        cou = cursor.execute(usql, up_data)
        cursor.execute(usql, up_data)
        print("수정 개수 : ", cou)
        conn.commit()  # 원격 db에 저장됨
        """

        # 자료 삭제
        code = '6';
        # dsql = "delete from sangdata where code=" + code
        # 참고 : secure coding 가이드라인에 맞게 프로그래밍 해야 한다. 
        # # 해킹 위험 : sql 인젝션은 사용자의 입력값을 검증하지 않는 웹 애플리케이션의 허점을 악용


        dsql = "delete from sangdata where code='{0}'".format(code)  # 추천 1
        dsql = "delete from sangdata where code=%s"  # 추천2 : 권장
        # cursor.execute(dsql,(code,))   # 추천 2  이게 가장 좋은 방법!!
        # cursor.execute(dsql,code)   # 추천 1
        
        cou = cursor.execute(dsql,code)   # 삭제 후 반환 값 얻기
        if cou != 0:
            print("삭제 성공")
        else:
            print("삭제 실패")

        conn.commit()  # 원격 db에 저장됨
        print(dsql)



        # 자료 읽기
        # sql = "select * from gogek"
        sql = "select code,sang,su,dan from sangdata"
        cursor.execute(sql)  # SQL 실행
        for data in cursor.fetchall():
            # print(data)
            print("%s %s %s %s"%data)

        print()
        cursor.execute(sql)
        for data in cursor:
            print(data[0], data[1], data[2], data[3]*1000)

        print()

        cursor.execute(sql)
        for san in cursor:
            print(san[0], san[1], san[2], san[3] * 1000)


        cursor.execute(sql)
        for a, b, 수량, 단가 in cursor:
            print(a, b, 수량, 단가*1000)

    except Exception as e:
        print('처리 오류 : ', e)
    finally:
        conn.close()  # 연결 종료

if __name__ == '__main__':
    myFunc()
