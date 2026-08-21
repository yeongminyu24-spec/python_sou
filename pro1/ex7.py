print('구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음단으로 이동')



i=2
all=0
while i<=9:
    j=1
    print(' ')
    print('구구단'+str(i))
    while j<=9:
        all=i*j
        if all>30: break
        print(all, end=' ')
        j+=1
        

    i+=1
