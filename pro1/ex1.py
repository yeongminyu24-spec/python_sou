print("1~100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력")

su=1
hap=0
while su<100:


    if su%3==0 and su%2 !=0:
        print(su, end=' ')
        hap +=su
    su += 1    

print(' ')
print('합은', hap)