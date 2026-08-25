# 교수님이 만든 코드 


class CoinIN():
    def __init__(self):
        self.price=200

    def calc(self,coin, cupcount):
        # self.coin=coin
        # self.cupcount=cupcount
        totalprice=self.price*cupcount

        if coin<totalprice:
            return None, None
        else:
            change=coin-totalprice
            return cupcount, change

###self가 붙었다는 것은 각각의 객체마다 존재하는 변수라는 뜻임 

class Machine():
    def __init__(self):
        self.CoinIN=CoinIN()   # 클래스 포함


    def ShowData(self):
        while True:
            coin = int(input("동전을 입력하세요"))
            cup = int(input("몇 잔을 원하세요"))
            cupcount, change =self.CoinIN.calc(coin,cup)   # 오른쪽은 실행하라 왼쪽은 실행한 값을 저장하라, 왜 저장? 밑에 if문을 실행시키기 위해 

            if cupcount is None:
                print("요금이 부족합니다")

            else:
                print(f"커피{cupcount}잔과 잔돈은 {change}원")

            #계속 실행 여부

            answer = input("계속할까요?(y/n) : ")

            if answer.lower() =='n':
                print("종료합니다")
                break




if __name__=="__main__":
    Machine().ShowData()
