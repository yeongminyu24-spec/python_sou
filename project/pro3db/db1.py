# SQLite : 개인용 DB, python 에 기본 내장, 경량 DBMS 
# 서버를 운영하지 않음 시스템 내에서 별도의 자원을 사용할 필요가 없다. 

import sqlite3

print(sqlite3.sqlite_version)
print()
# conn = sqlite3.connect('exam.db') # 파일에 데이터 보관, db 연결 담당
conn = sqlite3.connect(':memory:') # ram에서만 작업, 휘발성


try :             # 네트워크 작업하면 다 예외처리 해줘야 한다. 
    cur = conn.cursor();  # SQL 처리를 위한 객체 생성, SQL 실행 담당

    # 테이블 생성
    cur.execute("create table if not exists friends(name text, phone text, addr text)") 

    # 자료 입력
    cur.execute("insert into friends values('홍길동', '010-1111-1111', '서초 1동')")
    cur.execute("insert into friends values(?,?,?)", ('이기자', '1111-1111', '서초 2동'))

    inputdatas = ('신기해','111-1234','서초 3동')
    cur.execute("insert into friends values(?,?,?)", inputdatas)

    inputdatas2 = [('신기한','111-3333','역삼 1동0'),('신기루','111-4444','역삼 2동')]
    cur.executemany("insert into friends values(?,?,?)", inputdatas2) # 여러개 입력
    conn.commit()

    # 자료 보기
    cur.execute("select * from friends") # select 결과를 cur에 담는다.
    # print(cur.fetchone()) # 한 개의 행(레코드) 읽기 - record pointer가 있는 지점의 자료만 읽음
    # print(cur.fetchone())
    print(cur.fetchall())    # 모든 행(레코드) 읽기[('홍길동', '010-1111-1111', '서초 1동'), ...
    print()   
    cur.execute("select name, phone, addr from friends")
    for r in cur:
        # print(r) 
        print(r[0], '님의 주소는', r[1], ' ', r[2]) # 튜플로 출력됨

except Exception as e:
    print('err : ', e)  # err의 원인은 e이다.
    conn.rollback()
finally :
    conn.close()  # 연결 종료