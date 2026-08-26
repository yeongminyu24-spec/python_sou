def fileopen():

    with open(r'sales.txt',mode='r',encoding='utf-8') as f:
        line = f.readline()


        print("날짜\t\t","이름\t","상품명\t","갯수\t","판매금액\t")
        while line:
            lines = line.split(',')
            total=int(lines[3])*int(lines[4])

            line=f.readline()
            
            print(f"{lines[0]}\t{lines[1]}\t{lines[2]}\t{lines[3]}개\t{total}원")

            person_total={}   # 이름별로 누적될 합이 들어갈 곳을 {}로 설정

        print("전체 판매 금액: ",)

print("전체 판매 금액")
if __name__ =='__main__':
    fileopen()
