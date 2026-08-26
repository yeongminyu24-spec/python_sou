print('1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력')

# while 작업 사용

su=1
suhap=0
while suhap<=1000:
    suhap+=su
    su+=1
    
    if suhap >1000:
        break
        
print('누적합이 처음으로 1000을 넘는 순간 숫자',su)
print('누적합이 처음으로 1000을 넘는 순간 숫자',suhap)

