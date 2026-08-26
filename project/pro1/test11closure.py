# Closure : Scope에 제약을 받지 않는 변수들을 포함하고 잇는 코드블럭이다. 
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내에 멤버를 참조하기

def funcTimes(a,b):
    c=a*b
    return c

print(funcTimes(2,3))
# print('c: ', c)  # nameerror 너가 c를 선언한 적이 없는데 어디서 가져오라는거니

kbs=funcTimes(2,3)   # 함수 실행 결과를 치환한거다 kbs로
print(kbs)           # 
kbs=funcTimes   # 함수 주소를 치환(별명이 하나 생김) 
print(kbs)      # 그래서 주소를 반환
print(kbs(2,3)) # 여기는 값을 반환 
print(id(funcTimes),id(kbs))    # 둘의 주소가 같음 1961838770160 1961838770160

mbc=sbs=kbs
del funcTimes   # funcTimes 함수명 삭제(기존에 참조하던 참조 변수를 삭제)
# aa= funcTimes(2,3)  # error : name 'funcTimes' is not defined
print(kbs(3,4))
print(sbs(3,4))
print(mbc(3,4))

print('\n--- 클러저를 사용하지 않은 경우 -----')
def out():
    count=0         # count는 out 수준이다. 
    def inn():
        nonlocal count  # out에서 만든 count 변수를 out 안에 새로운 함수인 inn에서 가져와서 수정하겠다 라는 뜻 
        count +=1
        return count
    print(inn())

# print(count)  # err
out()


print('\n--- 클러저를 사용한 경우 -----')
def outer():
    count=0         # count는 out 수준이다. 
    def inner():
        nonlocal count  # out에서 만든 count 변수를 out 안에 새로운 함수인 inn에서 가져와서 수정하겠다 라는 뜻 
        count +=1
        return count
    return inner    # 요것이 클로저 : 내부 함수의 객체의 주소를 반환함

var1 = outer()   
print('var1 주소 : ',var1)  # <function outer.<locals>.inner at 0x0000028AD8883480>
print('count : ', var1())
print('count : ', var1())
# print(var1.count)    #외부에서 직접적인 접근은 안됨 
print('클로저 내부 확인 : ' , var1.__closure__)      #  (<cell at 0x000001A79FD7BA90: int object at 0x00007FF90931E498>,)
myvar = var1()
print(myvar)
var2 = outer()   # 새로운 객체(inner 함수) 생성 
print(var2())
print(var2())

print('\n 수량 * 단가 * 세금한 결과를 출력하기 ---')
def outer2(tax):   # 여기서 tax는 지역변수 
    def inner2(su, dan):   # su, dan은 inner2안에서의 지역변수다. 
        amount= su*dan*tax
        return amount
    return inner2 

# 1분기에는 금액 : su*dan에 대한 tax는 0.1 부과
q1=outer2(0.1)   # q1은 inner2의 주소를 받음
result1=q1(5,50000)
print('result1 : ', result1)   
result2=q1(2,10000)
print('result2 : ',result2)

# 2분기에는 금액 : su*dan에 대한 tax는 0.05 부과
q2=outer2(0.05)   # inner2의 주소를 기억함 
result3=q2(5,50000)
print('result3 : ', result3)   
result4=q2(2,10000)
print('result4 : ',result4)


# 일급함수 , 일급객체
print('\n\n일급함수(객체) : 함수를 변수나 상수에 저장, 함수 안에 함수, 인자로 함수 전달, 반환 값이 함수')
def func1(a,b):
    return a+b
func2 = func1   # 함수를 변수나 상수에 저장 
print(func1(3,4))  # 모든 변수는 주소를 기억하고 있는 것 
print(func2(3,4))

print()
def func3(fu):   # 인자로 함수 전달
    def func4():
        print('나는 내부 함수야 ~~~')
    func4()
    return fu   # 반환값이 함수

mbc=func3(func1)    # 인자로 함수 전달함
print(mbc(6,7))

print('\n축약함수(Lambda Function) : 여러 줄의 함수 정의를 한 줄로 간단하게 줄여서 쓰는 익명 함수')
# 형식 -- lambda 매개변수 : 표현식  ->활용도가 매우 높다

def hapFunc(x,y):
    return x+y 

print(hapFunc(1,2))
# 람다로 표현하면
print((lambda x, y:x+y)(1,2))  # 단발성(휘발성) - 실행과 동시에 메모리 사라짐

gg=lambda x,y: x+y
print(gg)   # <function <lambda> at 0x00000255BEC93A00>
print(gg(1,2))

gg2 = lambda x, y:x+y
print(id(gg), id(gg2))
# print((lambda x, y:x+y)) is (lambda x, y:x+y))   #False

print()
kbs=lambda a, su=10: a+su
print(kbs(5))
print(kbs(5,6))

print()
sbs=lambda a, *tu, **di : print(a,tu,di)
sbs(1,2,3,var1=4,var2=5)  # 결과 값 : 1 (2, 3) {'var1': 4, 'var2': 5}

print('\n임의의 함수에서 람다 사용하기')
# filter() : 반복 가능한 객체(리스트 등)에서 특정 조건에 맞는 요소만 골라낼 때 사용
# 기본 구조는 filter(함수, 반복가능한 객체)
print(list(filter(lambda a:a<5, range(10)))) # 5보다 작은 것만 추려내겠다 , range를 사용한 이유는 0부터 10까지의 수를 반환, 근데 그값을 list로 찍어내라!!
print(list(filter(lambda a:a%2, range(10)))) # a%2의 나머지가 1이면 참이니깐 즉 홀수만 골라내겠다. 
print(bool(0),bool(1))  #false는 0, true는 1

# filter를 이용해 1~100사이의 정수 중 5의 배수이거나 7의 배수만 출력(리스트 형식)
print(list(filter(lambda a:a%5==0 or a%7==0 , range(1,101))))  #1부터 101 사이의 정수 중에서 5의 배수이거나 (True) 7의배수(True)를 출력


