# 커피 자판기 프로그램, 클래스의 포함관계 연습문제

class CoinIN:   # 커피 객체(자판기에 보관될 클래스)


    def __init__(self, coin=0, change=0):  # 객체로부터 값을 입력하게끔 근데 초기값을 설정해준거
        self.price=200    
        self.coin=coin
        self.change=change
        
    def culc(self, CupCount):
        
        self.CupCount=CupCount
        
        self.change = self.coin-self.CupCount*self.price # 잔돈은 (내가 넣은 금액)-(내가 원하는 커피 잔 수)*200

        if self.change<0:   # 넣은 돈이 부족할 때, 원하는 것이 많을 때
            self.change=self.change*-1
            print('-'*30)
            print("요금이 부족합니다",self.change,"원이 부족합니다")
        elif self.change == 0:
            print('-'*30)
            print("커피",self.CupCount,"잔을 출력합니다.")

        elif self.change >0:  # 잔돈이 남을 떄
            print('-'*30)
            print("커피", self.CupCount,"잔을 출력합니다", "잔돈",self.change,"원")



class Machine:

    
    def __init__(self):
        self.Machine=CoinIN()   # 클래스의 포함관계 

    def ShowData(self):
        print('-'*30)
        self.Machine.coin=int(input("동전을 입력하세요 : "))
        

        self.Machine.CupCount=int(input("몇 잔을 원하세요 : "))

        self.Machine.culc(self.Machine.CupCount)


if __name__ == "__main__":
    Machine().ShowData()
