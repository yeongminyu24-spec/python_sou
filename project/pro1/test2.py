# 연산자
# 치환 연산자

vl = 3
v1 = v2 = v3 = 5
print(v1, v2, v3)

v1 = 10,20,30   # 치환 연산자를 씀 
print('v1 = ',v1)  # v1 = (10, 20, 30)  # 튜플로 묶여서 출력됨


v1, v2 = 10, 20
print(v1,v2)   # 하나씩 매핑 함
v1, v2 = v2, v1   # 기억 장소의 값 서로 바꾸기
print(v1,v2)  


print('값 할당 packing')
v1, *v2 = 1,2,3,4,5    # *를 주는 이유는 v1에 1을 할당하고 나머지 값들을 v2에 할당하기 위해서임
print(v1,v2)  # 1 [2, 3, 4, 5]
*v1, v2 = 1,2,3,4,5 # *를 주는 이유는 v2에 5를 할당하고 나머지 값들을 v1에 할당하기 위해서임
print(v1,v2) # [1, 2, 3, 4] 5
*v1,v2,v3 = 1,2,3,4,5
print(v1,v2,v3)  # [1, 2, 3] 4 5
v1, *v2, v3 = 1,2,3,4,5
print(v1,v2,v3)  # 1 [2, 3, 4] 5

name = "마우스"; # ;를 쓰는 이유는 한 줄에 명령어를 여러개 쓰기 위해서임
price = 5000;   
print(f"이름:{name}, 가격:{price}") 
print('abc')
print('def')
print('abc', end=' ')  # end=''를 쓰는 이유는 다음줄로 넘어가지 않고 이어서 출력하기 위해서임
print('def')  # end=''를 쓰지 않으면 다음줄로 넘어가서 출력됨
print('\n\n연산자 연습 계속')
print(5+3,5-3,5*3,5/3,5//3,5%3,5**3)  # //는 몫을 구하는 연산자임  % 는 나머지를 구하는 연산자임  ** 는 거듭제곱을 구하는 연산자임
print(123456789**12)  # 파이썬은 정수형의 범위가 무한대임
print(divmod(5,3))  # divmod()는 몫과 나머지를 동시에 구하는 함수임  (1,2) 1은 몫, 2는 나머지
print(3+4*5, (3+4)*5)  # 연산자 우선순위에 따라 계산됨  *가 +보다 우선순위가 높음
# 연산자 우선순위 : 왼쪽이 우선순위이고, ()->**-> *,/ -> +,- -> 비교 -> not -> and -> or -> = 순서임
print(5>3, 5==3, 5 != 3) # != 는 같지 않다라는 의미임  True, False, True

print('논리 연산자')
print(5>4 and 4<3, 5>4 or 4<3, not(5>4))  # and는 둘 다 참이어야 참, or는 둘 중 하나만 참이어도 참, not은 반대로 바꿈

print('문자열 더하기')
print('한'+'국'+"만세")
print('한국 '*5)

print('누적')
a= 10
a=a+1
a+=1  # a=a+1과 같은 의미임
print('a는', a)
print(f'a는 {a}')  # f-string을 사용하면 변수 값을 문자열 안에 바로 넣을 수 있음
print('부호 변경 : ', a,a*-1, -a,--a,---a)


print('boolean 처리 : ', bool(123), bool(1), bool(-3.5), bool(True))  # 파이썬은 0 이외에 다른 값이 들어가 있으면 True로 처리함
print('boolean 처리 : ', bool(0), bool(0.0), bool(False), bool(None)) # 파이썬은 0, 0.0, False, None은 False로 처리함
print('boolean 처리 : ', bool([]), bool({}), bool(set())) # 파이썬은 빈 리스트, 빈 딕셔너리, 빈 집합은 False로 처리함

print('이스케이프 문자')  # 이스케이프 문자 - Escape character : 특수한 의미를 포현하기 위한 문자 
print('aa\tbb')   # aa치고 tab키를 눌러서 bb를 출력함
print(r'aa\tbb')  # r을 붙이면 raw string으로 처리되어 이스케이프 문자가 적용되지 않음
print('aa\bbb')  # \b는 백스페이스(backspace)로, 커서를 한 칸 뒤로 이동시키는 역할을 함   
print(r'aa\bbb')  
print('aa\nbb')  # \n은 줄바꿈(new line)으로, 커서를 다음 줄로 이동시키는 역할을 함
print(r'aa\nbb')
print('c:\a\abc.txt')  # \a는 경고음(bell)으로, 경고음을 발생시키는 역할을 함
print('c:\n\abc.txt') # \n은 줄바꿈(new line)으로, 커서를 다음 줄로 이동시키는 역할을 함  이것만 잘 알아두면 됨!! 