# 함수 장식자(데오레이터, Decorator )는 기존의 함수 코드를 수정하지 않고도 앞뒤에 새로운 기능을 더해 포장(wrapping)해 주는 파이썬의 특별한 기능
# 함수 위에 @장식자 이름 기호를 붙여서 간단하게 사용. 
# 장식자의 주요
# - 특정기능 추가 : 원래 함수를 바꾸지 않고 실행 전후로 로그 기록, 시간 측정, 권한 확인
# - 코드 중복 줄이기 : 여러 함수에서 공통으로 쓰는 기능을 하나로 묶어 재사용성을 높임.
# 가독성 향상 : @ 기호를 사용해 코드를 깔끔하고 직관적으로 유지한다. 
# 기본 작동원리
#  : 장식자는 함수로 인자로 받아 내부에서 새로운 함수(보통 wrapper)를 감싸서 반환


# 함수 장식자 

def make2(fn):
    return lambda: "안녕" + fn()

def make1(fn):
    return lambda : "반가워" + fn()

def helloFunc():
    return "홍길동"

hi=make2(make1(helloFunc))  # Decorator 없이 실행 # 처음에 make2를 부름->함수(fn)를 달라고 함->make1을 줌->make1도 함수를 달라고 함->helloFunc의 주소를 받음 
print(hi())


@make2   # decorator, 위에 있는게 가장 바깥쪽에서 감싸는 거 
@make1
def helloFunc2():
    return "고길동"

print(helloFunc2())

print('--------')
def traceFunc(func):
    def wrapperFunc(a,b):
        r=func(a,b)
        print(f'함수명 : {func.__name__} (a={a},b={b}->{r})')  # __name__은 내장 명령어 
        return r
    return wrapperFunc # 함수의 주소를 반환 ->closure가 되는거임 


@traceFunc
def addFunc(a,b):
    return a+b

print(addFunc(10,20))  # 함수명 : addFunc (a=10,b=20->30)
