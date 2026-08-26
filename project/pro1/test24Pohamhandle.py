# 어딘 가에서 필요한 부품으로 핸들 클래스 작성
class Pohamhandle:
    quantity = 0 # 핸들 회전량 

    def leftTurn(self, quantity):
        self.quantity = quantity
        return "좌회전"

    def RightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"