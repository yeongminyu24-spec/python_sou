# 냉장고 객체에 음식 객체 넣기 


class FoodData:    # 음식 객체 (냉장고에 보관될 클래스)
    def __init__(self, name, expiry_date):
        self.name=name
        self.expiry_date=expiry_date

class Fridge:   
    isOPened=False
    foods = []

    # 생성자는 생략한다고 하심 
    def open(self):
        self.isOPened=True
        print('냉장고 문이 열림')

    def close(self):
        self.isOPened = False
        print("냉장고 문이 닫힘 ")

    def foodList(self): # 냉장고 문이 열린 경우 음식물 확인 메소드
        for f in self.foods:
            print(f" -{f.name}{f.expiry_date}")
        print()

    def put(self, thing):
        if self.isOPened:
            self.foods.append(thing)
            print(f"냉장고에 {thing.name}넣음")
            self.foodList()
        else:
            print("냉장고 문이 닫혀 있음")


fobj = Fridge()

apple = FoodData("사과", "2026-9-6")
fobj.put(apple)   # 냉장고 문이 닫혀 있음
fobj.open()   # 냉장고 문이 열림
fobj.put(apple)  #  냉장고에 사과넣음   -사과2026-9-6
fobj.close()    #  냉장고 문이 닫힘 
print()
cola = FoodData("콜라", "2027-9-6")
fobj.open() 
fobj.put(cola)   # 냉장고 문이 닫혀 있음
fobj.close()
