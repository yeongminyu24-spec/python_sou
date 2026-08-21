print('상품명','\t','수량','단가',' 금액')
print('--'*20)
# 새우깡 단가 450, 감자깡 단가 300, 양파깡 단가 350
datas=[
    "새우깡,15",
    "감자깡,20",
    "양파깡,10",
    "새우깡,30",
    "감자깡,25",
    "양파깡,40",
    "새우깡,40",
    "감자깡,10",
    "양파깡,35",
    "새우깡,50",
    "감자깡,60",
    "양파깡,20"
    ]



new_datas=[]  # datas에 있는 list 형식 문자열을 각각 나눌 것이다. 

for data in datas:
    name, price = data.split(",")  # 하나를 먼저 나누고 그거를 new_datas 리스트 형식에 담는다.
    new_datas.append([name, int(price)])  # ㅔ[]를 쓴 이유는 새우깡, 15를 하나의 리스트로 묶기 위해서이다. ,new_datas=[[새우깡, 15]]->[[새우깡, 15],[감자깡, 20]]....
# print(new_datas)

for data in new_datas:
    # if str(new_datas[0]) == "새우깡":   #여기서 맨날 하는 실수인데 반복 가능한 객체안에서 함수를 써야 그게 반복이 된다. 
    if data[0] == "새우깡":
        # data[-1]=450    # 이거는 -1자리에 있는거를 바꾸는 거고 추가를 해야한다. 
        data.append(450)

    elif data[0] == "감자깡":
        data.append(300)

    else:
        data.append(350)

    
# print(new_datas)   확인용

tot_money = lambda data:data[1]*data[2]   # lambda는 함수를 간단히 만드는 것
# 함수로 풀면
# def tot_money(data):
#     return data[1]*data[2]

for data in new_datas:
    data.append(tot_money(data))

# print(new_datas) 확인용 2

for data in new_datas:
    print(data)

print()
print("소계")
shrimp_count=0
shrimp_money=0
potato_count=0
potato_money=0
onion_count=0
onion_money=0


for data in new_datas:
    if data[0]=="새우깡":
        shrimp_count+=data[1]
        shrimp_money+=data[3]
        

    elif data[0]=="양파깡":
        onion_count+=data[1]
        onion_money+=data[3]

    else:
        potato_count+=data[1]
        potato_money+=data[3]

print("새우깡 : ", shrimp_count, "건    ", "소계액 : ",shrimp_money, "원") 
print("감자깡 : ", potato_count, "건    ", "소계액 : ",potato_money, "원") 
print("양파깡 : ", onion_count, "건    ", "소계액 : ",onion_money, "원") 
print("\n총계")
tot_count=shrimp_count+potato_count+onion_count
tot_money=shrimp_money+potato_money+onion_money
print("총 건수 : ", tot_count, "\n총 액 : ", tot_money,"원")
