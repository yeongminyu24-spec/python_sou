print('1~100사이의 숫자 중 각 자리 수의 합이 10이상인 수만 출력 ')

su=10
suten=0
suone=0
suall=0

# su=su//3
# print(su)

while su<100:
    suten=su//10
    suone=su-suten*10
    suall=suten+suone
    if suall>=10:
        print(su, end=' ')

    su+=1        
