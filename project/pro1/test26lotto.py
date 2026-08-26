# 로또 번호 출력기
# 45개의 넘버링된 볼 객체 생성 후 혼합 후 6개의 공을 출력
# 
# 
import random

class LottoBall:    # num을 입력하면 공 하나(객체)를 가지는 클래스 
    def __init__(self, num):
        self.num = num   # 받은 숫자를 현재 객체 넘버에 저장


class LottoMachine:
    def __init__(self):
        self.ballList=[]    # 우선 빈 리스트를 하나 만듬

        for i in range(1,46):
            self.ballList.append(LottoBall(i))   # 클래스 포함  lottoball의 객체를 다 포함하고 있음 

    def selectBalls(self):
        for a in range(45):   # 왜 0~44일까?->리스트의 인덱스가 0~44여서
            print(self.ballList[a].num, end=' ')

        print()

        
        random.shuffle(self.ballList)

        return self.ballList[0:6]

class LottoUI:
    def __init__(self):
        self.machine=LottoMachine()   # 클래스의 포함 

    def playLotto(self):
        input("로또를 시작하려면 엔터키를 누르세요")

        selectedBalls = self.machine.selectBalls()

        print("여섯개 출력:")

        for ball in selectedBalls:
            print(ball.num)

if __name__ =='__main__':
    # machine =LottoMachine()
    # machine.selectBalls()

    # lot = LottoUI()
    # lot.playLotto()
    LottoUI().playLotto()  # 위 두줄과 실행결과 같음 
