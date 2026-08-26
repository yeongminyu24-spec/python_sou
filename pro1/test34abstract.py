# 추상 클래스

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,irum,nai):
        self.irum=irum
        self.nai=nai

    @abstractmethod
    def pay(self): #자식 클래스가 반드시 구현해야 하는 메소드
        pass

    @abstractmethod
    def data_print(self):
        pass

    def irummai_print(self):
        print("이름: ",self.irum)
        print("나이: ",self.nai, "살")    # 클래스에 따라 다른 결과 

# 임시직원
class Temporary(Employee):

    def __init__(self,irum,nai,ilsu,ildang):
        super().__init__(irum,nai)   # 부모 생성자에서 받아오는 거는 한꺼번에 받아와야함 super().
        self.ilsu = ilsu
        self.ildang = ildang



    def pay(self):
        self.total=self.ilsu*self.ildang
        return self.total

    def data_print(self): 
        self.total=self.ilsu*self.ildang
        print("이름: ",self.irum,",나이 :",self.nai,"월급 :", self.total)


# Regular

class Regular(Employee):

    def __init__(self,irum,nai,salary):
        super().__init__(irum,nai)
        self.salary = salary

    def pay(self):
        return self.salary

    def data_print(self):
        print("이름: ",self.irum,",나이 :",self.nai,"급여 :", self.salary)


# SalesMan
class SalesMan(Regular):

    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum,nai,salary)
        self.sales = sales
        self.commission = commission

    def pay(self):
        self.susuryo=self.sales*self.commission
        self.sureng=self.salary+self.susuryo
        return self.sureng
        

    def data_print(self):
        self.susuryo=self.sales*self.commission
        self.sureng=self.salary+self.susuryo
        print("이름: ",self.irum,",나이 :",self.nai,"수령액 :", int(self.sureng))


t=Temporary("홍길동",25,20,15000)
r=Regular("한국인",27,3500000)
s=SalesMan("손오공",29,1200000,5000000,0.25)

t.data_print()
print()
r.data_print()
print()
s.data_print()


