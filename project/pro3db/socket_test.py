# socket : 소켓은 프로세스가 네트워크 세계로 데이터를 내보내거나
# 혹은 그 세계로부터 데이터를 받기 위한 실제적인 창구 역할을 한다.
# 그러므로 프로세스가 데이터를 보내거나 받기 위해서는 반드시 소켓을 열어서
# 소켓에 데이터를 써보내거나 소켓으로부터 데이터를 읽어들여야 한다.
# 프로그램과 프로그램이 네트워크를 통해 데이터를 주고 받기 위해 사용하는
# 연결지점 + socket 이란 TCP/IP의 프로그래머 인터페이스이다.
# 통신 기기간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다.

#  TCP : 연결을 맺고 신뢰성 있게 데이터를 전달하는 연결지향 프로토콜
#      : 클라이언트 프로그램 -> socket -> 네트워크 -> 서버 프로ㅓ그램

#  UDP : 연결 없이 빠르게 데이터를 전달하는 비연결지향 프로토콜


# socket 통신 확인
import socket

# 서비스 이름과 프로토쿨 이름을 사용해 서비스 기본 포트 확인
print(socket.getservbyname('http','tcp'))     # 80    www
print(socket.getservbyname('https','tcp'))    # 443
print(socket.getservbyname('ftp','tcp'))      # 21   파일 전송 서비스
print(socket.getservbyname('ssh','tcp'))      # 22   원격 컴 접속
print(socket.getservbyname('smtp','tcp'))     # 25   메일 송수신
print(socket.getservbyname('pop3','tcp'))     # 110   이메일
print()

# 특정 웹서버의 ip address 확인
print(socket.getaddrinfo('www.daum.net', 80, proto=socket.SOL_TCP))
# [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('211.249.220.24', 80))]
#      주소 체계              ,소켓 타입,  프로토콜 번호, 실제접속주소

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.200.219', 80)),
# (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.192.247', 80)),
# (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.192.248', 80)), 
#  (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.200.236', 80))]








