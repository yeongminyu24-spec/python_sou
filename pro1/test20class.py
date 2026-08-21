class Car:
    handle = 1   # handle, speed는 속성이다.
    speed = 0


    def __init__(self, name, speed):    # name, speed는 지역변수  # self.name,speed는 객체이다.
        self.name = name       # 현재 객체의 name에게 name(지역변수) 인자값 치환
        self.speed = speed

    def showData(self):
        km = "킬로미터"
        msg = "속도:" + str(self.speed) + km   # 문자열을 맞춰주기 위해 str로
        return msg

    def printHandle(self):
        return self.handle      # Class의 handle을 찍어라 

print(Car.handle)    # 원형(prototype) 클래스의 멤버 호출
print()
