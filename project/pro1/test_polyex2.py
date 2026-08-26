# 3번 다중 상속 연습 문제

class Animal:   # 동물들의 부모 클래스

    def move(self):
        print("동물들은 움직인다")


class Dog(Animal):
    name="개"
    def move(self):
        print("강아지는 헐레벌떡 움직인다")


class Cat(Animal):
    name="고양이"
    def move(self):
        print("고양이는 살금살금 움직인다")

class Wolf(Cat,Dog):

    def look(self):
        print("늑대는 멋있게 생겼다")


class Fox(Dog,Cat):   # 강아지, 고양이 2개의 클래스를 상속 받은것이다.

    def move(self):
        print("여우는 빠르게 움직인다")

    def foxMethod(self):
        print("여우는 사냥할 떄 재빠르다")

w1=Wolf()
w1.move()     #  고양이는 살금살금 움직인다
w1.look()     #    늑대는 멋있게 생겼다s

print("----------------------------------------")
w2=Fox()
w2.move()     # 여우는 빠르게 움직인다
w2.foxMethod()    #     여우는 사냥할 떄 재빠르다
print("----------------------------------------")
