


























# print(int(data), type(int(data)))
# print(int(data)+5)


# jumsu = int(input('점수입력:'))


jamsu = 88
print(jamsu)
if jamsu >= 90:
    print('우수')
elif jamsu >= 80:  #elseif를 줄여서 elif라고 쓸 수 있음 
    print('보통')
else:
    print("저조")

jum=80
if 90 <= jum <=100:
    print('A')
elif 70 <= jum < 90:
    print('B')

else:
    print('C')

print('---------')
names = ['홍길동','신기해','이기자']  # 집합형 자리
if '홍길동' in names:
    print('친구 이름이야')
else:
    print('누구야')


if (count := len(names) >=3):   # :=  대입 표현식
    print(f"인원수가 {count}명 이므로 단체 할인 적용")
else:
    print("ㅜㅜ")

scores = [95, 88, 76, 92, 81]

if(avg := sum(scores) / len(scores)) >= 80:
    print(f"우수반 평균 점수 : {avg}")

print('삼항 연산')


a = 'kbs'
#if a== 'kbs':
#    b=9
#else:
#    b=11    
b = 9 if a=='kbs' else 11  #위에 4줄을 한줄로 나타낸거
print('b : ', b)

a=11
b='mbc'if a==9 else 'kbs'
print('b:',b)

a=9
print(0 if a<5 else 1 if a<10 else 2 )  # 이정도 줄이는 건 권장하지 않는다 

print("끝")

