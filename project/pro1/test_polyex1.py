# 클래스의 상속관계 연습문제 - 다형성

class ElecProduct: # 부모 클래스 (tv와 라디오의)
    volume=0
    def volumeControl(self,volume):
        print(f"야간시간 가전 제품의 볼륨은 {volume}으로 만드는 것이 좋다")


class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        print("ElecTv에서 volumeControl 함수 오버라이딩")
        print(f"ElecTV에서 볼륨조절 재정의, 권장 볼륨 : {volume}")


class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print("ElecRadio에서 volumeControl 함수 오버라이딩")
        print(f"ElecRadio에서 볼륨조절 재정의, 권장 볼륨 : {volume} ")


def process_Elec(elecpr : ElecProduct, volume : int) ->None:
    elecpr.volumeControl(volume)

if __name__=="__main__":
    E1=ElecTv()
    E2=ElecRadio()

    process_Elec(E1,40)
    print()
    process_Elec(E2,30)