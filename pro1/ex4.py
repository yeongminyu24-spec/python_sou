print('-1,3,-5,7,-9,11~ -99까지의 모두에 대한 합을 출력')

suminus=-1
suplus=3
minushap=0
plushap=0
all=0
while suminus>=-99:
    suminus-=4
    minushap+=suminus

print('음수끼리의 합은',minushap)

while suplus<=97:
    suplus+=4
    plushap+=suplus

print('양수끼리의 합은',plushap)
all=minushap+plushap
print('전체의 합은',all)