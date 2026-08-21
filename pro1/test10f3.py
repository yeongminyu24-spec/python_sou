# 매겨변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우


def showGugu(start,end=5):   #매개변수 이름은 start랑 end->기본값을 넣어버림
    for dan in range(start, end+1, 1):  # start에서 end+1까지 차이 1로 등차수열 만들어줌       # 여기서 dan은 앞에서 초기값 안줘도 되는건가???
        print(str(dan)+'단 출력')   # 여기서 str은 숫자를 문자열로 만들어줌
        for i in range(1,10):
            print(f'{dan}*{i}={dan*i}', end=' ')
        print()

showGugu(2,3)
print()
showGugu(2)  #여기서 end값을 안줬으니 3번째 줄처럼 기본값을 사용한다. 
print()
showGugu(start=7,end=9)   # 이름으로 매핑해도 됨 
print()
showGugu(end=9, start=7)   # 순서를 바꿔도 이름으로 매핑되는 거기 때문에 상관없다 
# showGugu(start=7, 9)   # 위치변수는 키워드 변수 뒤에 오지 못한다. 매핑할거면 둘 다 매핑해줘야 함 (syntaxError)
# showGugu(end=9, 7)    # 위랑 마찬가지로 syntaxerror : positional argument 

print('가변 매개변수 ---')
def func1(*ar):   # * : 여러 개의 인자를 tuple로 묶어서 받겠다는 의미->원래 *없으면 밑에 인자 2개라서 오류 남 
    print(ar)
    for i in ar:
        print('밥 : '+ i)

func1('김밥',)    # ('김밥',)->tuple로 받기 때문에 뒤에 ,가 온다 !!!!!!!!꼭 기억할 것!!!!!!!!
func1('김밥','비빔밥')   # ('김밥','비빔밥')
func1('김밥','비빔밥','공기밥','주먹밥')

print()
def func2(a, *ar):  # ar은 튜플로 받음 
# def func2(*ar, a):  # func2() missing 1 required keyword-only argument: 'a'
    print(a)
    print(ar)
func2('김밥')
func2('김밥','비빔밥','공기밥','주먹밥')

print()
def func3(w, h, **other):
    print(f'몸무게:{w}, 키 : {h}')
    print(f'기타: {other}')

func3(80,180, irum ='신기해', nai=33)
# 몸무게 : 80, 키: 180
# 기타 : {'irum': '신기해', 'nai' : 33}
# func3(80, 180, {'irum':'신기해', 'nai':33})  # err : dict형식으로 넣으면 안된다, dict 형식은 {}임 -> func3() takes 2 positional arguments but 3 were given
# dict 형식으로 출력은 되지만 인자는 그렇게 넣으면 안됨
print()
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)

func4(1,2)
func4(1,2,3,4,5)
func4(1,2,3,4,5,kbs=9, mbc=11)

print()
# type hint : 함수의 인자와 반환 값에 type을 적어 가독성 향상  -> !!이걸 쓰는 사람이 꽤 많아서 기억해둘것!!
def typeFunc(num:int, data:list[str]) -> dict[str, int]:   # num:int(숫자, 정수)라 준거는 type hint를 준거임, 가독성을 위해  list안에 변수는 str(문자) 였으면 좋겠어(권장 느낌)
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start=1):  # 몇번째 반복문인지 확인할 필요가 있을 때 enumerate 함수를 사용한다., 
        print(f'idx:{idx}, item :{item}')
        result[item]  =idx 
    return result

rdata = typeFunc('ok', ['일', '이', '삼'] )  # [] : 리스트 형식
print(rdata)
print()
rdata = typeFunc('한개', [10,20,30])
print(rdata)