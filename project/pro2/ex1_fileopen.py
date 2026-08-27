def fileopen():

    # 전체 판매 금액
    all_total=0

    # 직원별 판매금액 저장
    person_total={}

    with open(r'sales.txt',mode='r',encoding='utf-8') as f:
        line = f.readline()


        print("날짜\t\t","이름\t","상품명\t","갯수\t","판매금액\t")
        while line:    # line이 있을때동안은 while문 계속 돌아감
            lines = line.split(',')                 # ,를 기준으로 데이터를 나눔 
            total=int(lines[3])*int(lines[4])      # 나눠진 lines는 문자열이므로 숫자(정수)로 바꿔주기 위해 int 사용 

            # 전체 판매 금액 누적
            all_total+=total                    

            # 직원 이름 설정->이름에 금액을 배정하기 위해 
            name=lines[1]

            if name in person_total:
                person_total[name]+=total              # 이름이 같을 경우->홍길동 : 홍길동의 누적금액 
            else: 
                person_total[name]=total               # 홍길동 : 홍길동의 금액 (신규 생성)

            
            
            print(f"{lines[0]}\t{lines[1]}\t{lines[2]}\t{lines[3]}개\t{total}원")

            # 다음줄 읽기 
            line=f.readline()

    # 전체 판매 금액과 판매왕 찾기 
    print(f"전체 판매 금액: {all_total:,}원")
    best_person=max(person_total,key=person_total.get)    # person_total에 담긴 딕셔너리중에서 가장 큰 값을 가진 ket를 찾아라 
    print("판매왕 : ", best_person)

    # 직원별 판매실적 정리 
    print("직원별 판매실적 ")
    for name in person_total:
        print(f"{name}: {person_total[name]:,}원")     # :,은 천단위의 쉼표를 찍어준다.


    with open('sales_report.txt',mode='w',encoding='utf-8') as report:   #w는 write라서 

        report.write("직원별 판매실적\n\n")

        for name in person_total:
            report.write(f"{name}: {person_total[name]:,}원\n")

        report.write(f"전체 판매 금액: {all_total:,}원\n")
        report.write(f"판매왕 :  {best_person} ({person_total[best_person]:,})원")


if __name__ =='__main__':
    fileopen()
