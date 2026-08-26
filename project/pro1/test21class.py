kor = 100 # 모듈의 멤버 : 전역변수

def abc():   # 바깥쪽 일반함수 
    kor = 0 # 함수 내의 지역변수
    print('모듈의 멤버 함수')

class My:
    kor = 80  #My 클래스 멤버 변수(My type 객체 공유 자원)

    #def __init__(self):  초기화 작업이 없는 경우 생성자는 생략 가능 
    #   pass

    def abc(self):     # my class의 abc 메소드 
        print('My 클래스 멤버 메소드')

    def show(self):
        kor = 77   # 메소드 내의 지역변수
        print(kor)
        print(self.kor)
        abc()
        self.abc()


myObj = My()   # 생성자 호출
myObj.show()     # myobj안에 kot 있음?->없어서 my class에 있는 클래스 멤버 변수 80
print('-----------')

myObj2=My()
print(myObj2.kor)
myObj2.kor= 99
print(myObj2.kor)

print('~~~~')
myObj3 = My()
print(myObj3.kor)