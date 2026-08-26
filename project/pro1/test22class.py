# 클래스는 새로운 타입을 만들어 자원 공유가 목적
# 데이터와 기능(메소드)을 하나의 단위로 묶어 새로운 정의 타입을 만들고, 
# 객체마다 상태를 가지게 하거나 경우에 따라 공통 자원을 공유할 수 있다.
"""
class Singer: 
    title_song = "아 대한민국"   # class 변수 

    def sing(self):        # self는 현재 이 기능(메소드)를 실행하고 있는 객체(bts나 ive)
        msg = "노래는"
        print(msg, self.title_song)    # 현재 객체 안에 title_song이 있는가?->있으면 그것 사용 없으면->Singer 클래스에서 찾음
"""

# import test22singer    # test22singer의 모듈 전체를 가져와라 
# bts = test22singer.Singer()

from test22singer import Singer   # 위에 두줄이랑 똑같은 내용 : 외부 모듈의 멤버 로딩 

bts = Singer()   # Singer 설계도 -> 객체 bts 생성
bts.sing()    # 변경 전   #bts 객체안에서 sing의 기능인 title_song 찾음->없어서 Class Singer에서 찾음
print(type(bts))   # 객체의 type이 뭐니? -?bts는 Singer라는 클래스로부터 만들어진 객체이다.
bts.title_song = "Stay for a night"  # Class Singer과는 다르게 title_song이 없어서 만들어줌
bts.co = '빅히트 엔터테인먼트'   # 객체 내에 인스턴스 변수 새로 설정->ive나 Class에 변수를 만드는 것 X
bts.sing()    # 변경 후 -> "노래는 Stay for a night"    즉 인스턴스 변수를 설정해줌으로써 클래스 변수를 가린다. 
print('bts 소속사 :' , bts.co)


print('-----')
ive=Singer()   # ive 객체 생성 
ive.sing()
print(type(ive))
# print('ive 소속사 : ', ive.co)   # AttributeError : 'Singer' object

print()
Singer.title_song = '긴 여름은 가고~'   # 클래스 자체의 변수 변경
ive.sing()  # 노래는 긴 여름은 가고~      ->title song 없어서 class 변수 사용
bts.sing()   # 노래는 Stay for a night    ->객체 내의 변수가 있어서 클래스까지 갈 필요가 없음 

niceGroup = ive   # ive가 가리키고 있는 Singer Class를 niceGroup도 가리켜라 
niceGroup.sing()    # 사실상 ive.sing()이랑 같음 ->노래는 긴 여름은 가고~

print(ive is niceGroup)    # True = 두 변수가 같은 객체를 가리키고 있는가? 