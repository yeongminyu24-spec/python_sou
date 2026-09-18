# client
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.22', 8888))      # 이 컴퓨터에 접속할거야 서버의 고유번호를 확인할 수 있는 게 8888
clientsock.send("안녕 서버".encode())

clientsock.close()

# server 실행 중 - client 실행 - server가 메세지 수신 후 종료