# 상속

class Person:
    say = '난 사람이야~~'     # 접근 권한: public
    nai = '20'
    __msg = 'good : private 멤버 - 현재 클래스에서만 유효'

    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai

    def printInfo(self):     # 접근권한 : public
        print(f'나이 : {self.nai}, 이야기 : {self.say}')

    def helloMethod(self):
        print('안녕')
        print('hello : ', self.say, self.nai, self.__msg)
        

print(Person.say, Person.nai)    # 원형 클래스로 멤버 호출(비권장)
# 설계도.상품~은 좋지가 않다. 객체 지향 프로그램이기 떄문에 
# Person.printInfo()   #type error ->printinfo함수는 self, 즉 객체를 줘야하는데 원형 클래스를 줬으므로 타입 에러
per = Person('25')         # 객체 변수로 멤버 호출(권장)
per.printInfo()      
per.helloMethod()

print('-'*40)
class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'    # hiding(shadowing)

    def __init__(self):
        print('employee 생성자')

    def printInfo(self):   # 메소드오버라이딩 : 부모와 똑같은 메소드를 자식이 가지고 있음
        print('employee 클래스의 printInfo() 호출됨')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai)
        # print(self.__msg)     # 부모 클래스의 private 호출->호출 시 error(private이니깐)
        self.helloMethod()   # 여기는 부모 메소드를 부른다음에 private를 호출했으므로 윗줄과 다르게 호출이 된다.
        self.printInfo()   # 현재 클래스에서 검색 후 없으면 부모 메소드 호출 
        super().printInfo()  # 바로 부모 클래스로 가버림 
        print(self.say, super().say)   

emp = Employee()
print(emp.subject,emp.nai,emp.say)       # say가 없어서 부모인 person한테로 가서 say를 찾아옴
# 만약 둘다 say가 있으면 지역 즉 자식거를 우선적으로
emp.printInfo()
emp.ePrintInfo()

print('---'*5)

class Worker(Person):
    # def __init__(self, nai):
    #     pass

    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)    # 부모 클래스의 생성자 호출 ->Person 생성자, 30을 부모의 클래스 생성자 nai에 저장

    def wPrintInfo(self):
        print('Worker - wPrintInfo() 처리')
        self.printInfo()
        super().printInfo()

wor =  Worker('30')   # 30을 줬지만 30을 아무한테도 안 줬기 때문에 날라간다 
print(wor.say,wor.nai) # 난 사람이야~~ 20
wor.wPrintInfo()

print('==='*5)
class Programmer(Worker):
    def __init__(self,nai):
        print('Programmer 생성자')
    #    super().__init__(nai)   # Bound Method call
        Worker.__init__(self, nai)    # Unbounded Method call     # 그냥 nai만 하면안됨 직접 불러주는 경우에는 오류 뜬다 

    def pPrintInfo(self):
        print('Programmer - pPrintInfo() 처리함')


pro = Programmer(35)
print(pro.say, pro.nai)
pro.wPrintInfo()
pro.printInfo()

print('\n 클래스 타입 확인 ------') 
a=3; print(type(a))   # <class 'int'>
print(type(pro))   # <class '__main__.Programmer'>
print(type(wor))   #   <class '__main__.Worker'>

print(Person.__bases__)   # (<class 'object'>,)
print(Employee.__bases__)  # (<class '__main__.Person'>,)
print(Worker.__bases__)    # (<class '__main__.Person'>,)
print(Programmer.__bases__)  # (<class '__main__.Worker'>,)






