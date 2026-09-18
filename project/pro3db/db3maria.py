# mariadb : jikwon, buser table

# 직원번호, 직원명을 입력하여 로그인에 성공하면 해당 직원, 부서 정보 출력

import MySQLdb
import json


# # db 연결 정보 읽기 1 : json 파일 읽기
# with open('dbconnect.json', 'r', encoding='utf-8') as f:  # r은 읽기 전용, encoding='utf-8'은 한글 깨짐 방지
#     config = json.load(f)  # json 파일 읽기


# db 연결 정보 읽기 2 : .env 파일 읽기 
# pip install python-dotenv   설치 해야함
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),     # port는 수자 처리 
    'charset':os.getenv('DB_CHARSET'),
    }

def loginfunc():
    conn = None
    try:
        conn = MySQLdb.connect(**config)  # DB 연결  # dict여서 **를 붙인다.
        cursor = conn.cursor()  # SQL 처리를 위한 객체 생성
        jikwon_no = input('직원번호 : ')
        jikwon_name = input('직원이름 : ')
        if jikwon_no == '' or jikwon_name == '':
            print('로그인 정보를 입력하세요')
            return

        """
        sql = '''
        select jikwonno as 직원번호, jikwonname as 직원명,
        buserloc as 근무지역, jikwonjik as 직급, jikwongen as 성병
        from jikwon
        left outer join buser on jikwon.busernum = buser.buserno
        where jikwonno={0} and jikwonname={1}
        '''.format(jikwon_no, jikwon_name)
        """


        sql = """
        select 
        j.jikwonno as 직원번호, j.jikwonname as 직원명,
        b.busername as 부서명, j.jikwonjik as 직급, j.jikwongen as 성병        
        from jikwon j
        left outer join buser b on j.busernum = b.buserno
        where jikwonno=%s and jikwonname=%s
        """

        # sql 실행
        cursor.execute(sql, (jikwon_no, jikwon_name))  # sql 실행  

        # 로그인 성공 직원 정보 출력
        data = cursor.fetchone()

        if data:
            print('로그인 성공')
            print('직원번호 : ', data[0])
            print('직원명 : ', data[1])
            print('부서명 : ', data[2])
            print('직급 : ', data[3])
            print('성별 : ', data[4])
        else:
            print("로그인 실패 : 입력 자료 확인하세요")

    except Exception as e:
        print('에러:',e)
    finally:
        if conn: 
            conn.close()  # 연결 종료  # 콘이 있다면 


if __name__ == '__main__':
    loginfunc()


