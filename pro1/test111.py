class CoinIN:

    def __init__(self,coin=0,change=0):
        self.coin=coin
        self.change=change

    def calc(self,cupcount):

        self.cupcount=cupcount
        self.price=200
        self.change=self.coin-self.cupcount*self.price

        if self.change<0:  # 돈이 부족한 경우
            print(f"{-self.change}만큼 돈이 부족합니다")

        else: # 돈이 부족하지 않은 경우
            print(f"커피 {self.cupcount}잔과 잔돈 {self.change}원")


class Machine:
    

        def __init__(self):
            self.Machine=CoinIN()

        def ShowData(self):
            while True:

                self.Machine.coin=int(input("동전을 입력하세요"))

                self.Machine.cupcount=int(input("몇잔을 원하세요"))

                self.Machine.calc(self.Machine.cupcount)   # 컵카운트 받으면 실행하라는 뜻

                answer=input("계속 커피를 뽑으시겠습니까? (y/n)")

                if answer.lower() == 'n':
                    print("종료합니다")
                    break


if __name__=="__main__":
    Machine().ShowData()

        



