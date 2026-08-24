# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용)
# 포함 관계 : 다른 클래스(객체)를 마치 자신의 멤버 처럼 선언하고 사용 

# import test24Pohamhandle 이 방법은 부르기가 너무 귀찮다.
from test24Pohamhandle import Pohamhandle

class PohamCar:
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        self.ownerName=ownerName
        self.Handle=Pohamhandle()    # 포함카 클래스에서 포함카핸들 클래스를 객체의 핸들의 데이터로 받음 (클래스의 포함관계 : has a)

    def turnHandle(self,q):
        # 회전량(q):양수면 우회전, 음수면 좌회전, 0이면 직진이라고 가정
        self.q=q

        if q>0:  # 우회전
            self.turnShowMessage= self.Handle.RightTurn(q)  # 포함카가 포함핸들 객체를 생성해서 그거를 self.Handle에 넣어놨으니깐 self.Handle만 찍어도 RightTurn이 뜬다.

        elif q<0:
            self.turnShowMessage= self.Handle.leftTurn(q)

        elif q==0:
            self.turnShowMessage = "직진"


if __name__ == "__main__":
    tom = PohamCar("미스터 톰")
    tom.turnHandle(10)
    print(tom.ownerName + "의 회전량은", tom.turnShowMessage, " " + \
        str(tom.Handle.quantity))


    print()
    suji = PohamCar("미스터 수지")
    suji.turnHandle(-20)
    print(suji.ownerName, "의 회전량은", suji.turnShowMessage, " " + \
        str(suji.Handle.quantity))