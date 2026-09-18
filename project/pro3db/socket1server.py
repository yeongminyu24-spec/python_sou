# 1회용 서버
from socket import *


# socket 객체 생성
serversock = socket(AF_INET, SOCK_STREAM)  # socket(소켓 종류, 소켓 유형)
# socket을 이용해 특정 컴과 바인딩(서버의 IP와 Port 연결)
serversock.bind(('192.168.0.22', 8888))

# 연결 대기 상태로 전환
serversock.listen(5)
print('서버 서비스 중...')


# 클라이언트의 접속 대기
conn, addr = serversock.accept()
print('cleient addr : ', addr)

# 클라이언트가 보낸 데이터 수신
msg = conn.recv(1024).decode()
print('from client message : ', msg)

# 연결 종료
conn.close()
serversock.close()