# 자주 사용하는 앱에서 바로 AI를 사용해 보세요 … Gemini를 사용하여 초안을 생성하고 콘텐츠를 다듬고, Google의 차세대 AI가 지원되는 Gemini Pro를 이용하세요.
# 100%
# # 연습문제 
# 2번 문제
import MySQLdb
from dotenv import load_dotenv
import os

load_dotenv()

config_data = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),   # port는 숫자 처리
    'charset':os.getenv('DB_CHARSET'),
}

def genderFunc():
    conn = None
    cursor = None

    try:
        conn = MySQLdb.connect(**config_data)
        cursor = conn.cursor()
        sql = """
            SELECT jikwongen, COUNT(*), AVG(jikwonpay)
            FROM jikwon
            WHERE jikwongen IN ('남', '여')
            GROUP BY jikwongen
            ORDER BY jikwongen
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        print("성별","직원수","평균급여")

        for row in data:
            print(row[0], row[1], row[2], sep="  ")

    except Exception as e:
        print('에러: ', e)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    genderFunc()
