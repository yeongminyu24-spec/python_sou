print('1~1000사이의 소수와 그 갯수를 출력')

su=2
i=1
j=1
while su<1000:
    while j<su:
        if su%j==0 :
            print(su)
        j+=1
        i+=1
su+=1
        

