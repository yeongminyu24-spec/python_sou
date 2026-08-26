# 재귀함수 : 함수가 자기 자신을 호출-반복 처리 가능

def countDown(n):
    if n==0:
        print("완료")
        return       # 함수가 빠져 나오게 하는건 return
    else:
        print(n, end=' ')
        countDown(n-1)  # 재귀(recursion)

countDown(5)


print('\n---1부터 n까지의 정수의 합 구하기 ---')
def totFunc(n):
    if n==1:
        print("완료")
        return 1       # 함수가 빠져 나오게 하는건 return


    return n + totFunc(n-1)  # 재귀함수 -> 5을 넣으면 return 5하고 totFunc(4)를 다시한다->쭉 가다가 1이 되면 return 1에서 함수에서 빠져나온다 그러면 5+4+3+2+1의 값이 result 값에 저장이 된다.

# 호출하는 동안은 함수가 계산안함 호출이 다 끝나고 함수를 빠져나올 때 연산을 해준다.  
result=totFunc(5)
print('result : ',result)


print('\n-- factorial 계산 ---')
# 팩토리얼 : 1부터 어떤 자연수 n까지 차례대로 곱하는 것이다

def factFunc(n):
    if n==1: return 1
    print(n)
    return n * factFunc(n-1)


result2=factFunc(5)
print('result2 : ', result2)
