# 파이썬 지원 그래픽 모듈 사용

from turtle import *   # 터틀 모듈에 있는 모든 모듈멤버들을 쓰겠다. 

p=Pen()
p.color('red','yellow')   # 색깔 설정
p.begin_fill()

while True:
    p.forward(200)
    p.left(170)  
    if abs(p.pos())<1:
        break

p.end_fill()

input()   # 이거 안하면 끝나자마자 닫힘 