# 메소드 오버라이딩(메소드 재정의)
# 부모 클래스에서 정의된 메소드를 자식이 동일명의 메소드로 내용만 변경해 사용
# 부모 메소드의 기능을 대체하는 새로운 기능을 구현 가능
# 동작의 구체화(공동 들은 부모가, 실제 행동은 자식) 실현
# polymorphism(다형성) - 같은 메소드이나 객체에 따라 다른 기능을 수행
# 확장, 유지보수에 도움 - 부모 코드는 유치한 채 자식 코드만 변경

class parent:               # 용도 : 부모 클래스
    def printdata(self):    # 내용이 없는 메소드 - 의도는 자식 클래스에서 오버라이딩을 기대
        pass

class child1(parent):
    def abc():
        print('child1 클래스의 고유 메소드')

    def printdata(self):    # 메소드 오버라이딩(method overriding)
        su = 6
        a = 5 + su
        # 뭔가를 ...
        print('child1에서 printdata 오버라이딩')

class child2(parent):
    good = 'ok'

    def printdata(self):       # 메소드 오버라이딩(method overriding)
        print('child2에서 printdata 재정의함')
        msg = '부모와 동일 메소드명이나 내용은 다름'
        print(msg)

c1 = child1()
c1.printdata()
print()
c2 = child2()
c2.printdata()

print('\n다형성 구현 ----')
par = parent()
par = c1
par.printdata()
print()
par = c2
par.printdata()
print('-'*30)
imsi = c1
imsi.printdata()
print()
imsi = c2
imsi.printdata()
