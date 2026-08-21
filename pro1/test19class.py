# oop : 객체지향(중심)적인 프로그래밍 가능. 상속, 포함, 다형성
# class : 멤버변수(필드), 멤버 메소드로 구성
# 인스턴스에 의해 새로운 이름공간을 갖는다. 


import math   # 모듈

a=2    # 전역 변수
print(a)   # statement

def func():     # 함수, function
    print('ok')

class TestClass:    # Class의 헤더
    aa=1 # 멤버 변수

    def __init__(self):    # Method의 첫 인자는 반드시 self
        print('생성자')

    def __del__(self):
        print('소멸자')

    def showMessage(self):
        name = '한국인'
        print(name)
        print(self.aa)  # self는 키워드이다. 
        

print(TestClass)   # <class '__main__a.TestClass'>
print('클래스 멤버 a : ', TestClass.aa) # 클래스 멤버 a :
# TestClass.showMessage()   # TypeError : ...


# 클래스 생성자를 이용해 객체 생성 후 해당 개체의 주소를 객체변수에 치환
test =TestClass()    # 생성자 호출, instance를 함. ->object(객체, 개체)이 생성됨 
print('클래스 멤버 a : ', test.aa)
print()

# 1. Bound Method call
test.showMessage()  # 자동으로 객체 변수 test가 메소드의 인수로 담겨 호출됨

# 2. UnBound Method call
TestClass.showMessage(test) 

print()
print(type(1))   # <class 'int'>
print(type(1.0))
print(type('ok'))
print(type(test))   # <class '__main__.TestClass'>

print(id(test))                    # 2599641697984
print(id(TestClass))               # 2599643841264
test2=TestClass()  # 객체 한개 더 생성
print(id(test2))                    # 2599641615888