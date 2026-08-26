# datas=int(input(('[사번, 이름, 기본급, 입사년도]')))

# def inputFunc(num:int,name:str,basepay:int,joiningyear:int):
datas = [[1,"강나루",1500000,2010], 
        [2,"이바다",2200000, 2018],
        [3, "박하늘", 3200000,2005]
        ]

    # return datas


for data in datas:
    emp_no, name, base_pay, hire_year = data


print("출력 결과 : ")
print()
print('사번','\t','이름','\t\t','기본급','\t','근무년수','\t','근속수당','\t\t','공제액','\t\t','수령액')

print('--'*60)


for data in datas:
    a=(data[-1])
    b=2026-a
    data.append(b)   # 리스트에 추가할 때는 extend를 써야함 


for data in datas:
    if 0<data[-1]<=3:
        data.append(150000)
    elif 4<=data[-1]<=8:
        data.append(450000)
    else:
        data.append(1000000)

# print(datas)
for data in datas:
    if 0<data[-1]+data[2]<2000000:
        data.append(0.15*(data[-1]+data[2]))
    elif 2000000<=data[-1]+data[2]<3000000:
        data.append(0.3*(data[-1]+data[2]))
    elif 3000000<=data[-1]+data[2]:
        data.append(0.5*(data[-1]+data[2]))
# print(datas)

for data in datas:
    c=data[2]+data[5]-data[-1]
    data.append(c)

for data in datas:
    data.pop(3)
# print(datas)
for data in datas:
    print(data[0],"\t",data[1],"\t",data[2],"\t",data[3],"\t\t",data[4],"\t\t",int(data[5]),"\t\t",int(data[6]))






    

# print(list(filter(inputFunc(4):)))
