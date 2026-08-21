print('1~100 사이의 정수 중 "짝수는 더하고, 홀수는 뺴서" 최종결과 출력')

jaksu =0
halsu =0
jakhap=0
halhap=0
while jaksu<100:
    if jaksu %2==0:
        jakhap+=jaksu
    jaksu+=1    

print('짝수끼리 더한 것의 합은',jakhap)

while halsu<100:
    if halsu %2 !=0:
        halhap+=halsu
    halsu+=1

print('홀수끼리 더한 것의 합은',halhap)    
