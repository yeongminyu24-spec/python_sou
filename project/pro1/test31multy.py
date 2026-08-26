# 클래스의 다중 상속 - 부모 클래스가 복수 (순서에 유의)


class Tiger:
    data = "호랑이 세상"

    def cry(self):
        print("호랑이 : 어흥")

    def eat(self):
        print("맹수는 고기를 좋아함")
        print("아침에 닭고기, 낮에 소고기, 저녁에 양고기")


class Lion:
    def cry(self):
        print("사자 : 으르렁")

    def hobby(self):
        print("백수의 왕은 낮잠이 취미")


class Liger1(Tiger,Lion):    # 2개의 클래스를 상속 받은거임 
    pass

a1= Liger1()
print(a1.data)   # 호랑이 세상
a1.eat()       # 맹수는 고기를 좋아함 아침에 닭고기, 낮에 소고기, 저녁에 양고기
a1.hobby()
a1.cry()   # 호랑이 : 어흥   -> 동일 멤버일 경우 첫번째 클래스인 Tiger의 멤버를 취함. 



print('-'*30)

def hobby():
        print("모듈의 멤버 : 일반 함수")
class Liger2(Lion,Tiger): 
    data="라이거 만세"
    
    def play(self):
        print("라이거 고유 메소드")

    def hobby(self):     # 메소드 오버라이딩 : 부모인 사자와 호랑이의 메소드를 재정의
        print("라이거는 공원 산책을 좋아함 - 오버라이딩")

    def showData(self):
        self.hobby()   # 현재 클래스에서 호출하고 없으면 부모에서 찾음 
        super().hobby()   # 부모에서 호출 
        hobby()           # 클래스 밖 : 모듈에서 호출 

        self.eat
        super().eat()

        print(f"data : {self.data}, {super().data}")

a2=Liger2()
a2.cry()
a2.showData()
        