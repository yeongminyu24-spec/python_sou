class Singer: 
    title_song = "아 대한민국"

    def sing(self):                       # Singer 객체가 사용할 수 있는 기능 
        msg = "노래는"                     # self는 현재 이 메소드를 실행하고 있는 객체
        print(msg, self.title_song)

class Etc:
    pass

# 여러 개의 클래스나 함수 등을 선언하고 다른 파일에서 공유하도록 설정함