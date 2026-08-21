# 모듈 : 파이썬 파일(.py) 하나에 정의된 함수, 클래스, 변수 등을 모아둔 것입니다. 즉, 관련된 코드들을 하나의 파일로 정리한 것이 모듈입니다.
# 표준 모듈, 사용자 작성 모듈, 제3자 모듈(third party)로 구분 할 수 있다. 

# 패키지(폴더 느낌) : 여러 모듈을 디렉토리 구조로 묶어 관리하는 것입니다. 즉, 관련된 모듈들을 한데 모아 체계적으로 관리하기 위한 구조입니다. 
# 패키지의 디렉토리에는 init.py 파일이 포함되어 있어야 패키지로 인식됩니다.(파이썬 인터프리터는 init.py 파일이 포함되어 있어야 폴더를 패키지로 인식한다. 
# 이때 init.py에는 아무것도 안들어 있어도 됨) 

print(print.__module__)   # builtins(내장 모듈)

print('뭔 작업을 하다가 ... 외부 모듈 사용하기')
import sys
print(sys.path)   # sys 표준 라이브러리 모듈을 불러오는 명령 
# 모듈 경로 확인  ->['C:\\works\\project\\pro1', 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\python314.zip', 
# 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\DLLs', 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib', 
# 'C:\\Users\\acorn\\anaconda3\\envs\\myproject', 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib\\site-packages', 
# 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib\\site-packages\\win32', 'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib\\site-packages\\win32\\lib',
#  'C:\\Users\\acorn\\anaconda3\\envs\\myproject\\Lib\\site-packages\\pythonwin']
q = 'n'
if q=='y':
    sys.exit()   # 실행 중인 프로그램의 종료 

# 수학 관련 모듈 읽기 
import math
print(math.pi)
print(math.sin(math.radians(30)))

# 달력 출력
import calendar
print(calendar.JULY)
calendar.setfirstweekday
calendar.prmonth(2026,8)
del calendar   # 다써서 메모리에서 지우기  

# import time
# print('시작')
# time.sleep(3)
# print('계속')


# 난수 출력
import random                             # 모듈 호출 후 필요한 거 random. 찍고 불러오기 
print(random.random())
print(random.randrange(1,10))   # 1~10까지의 숫자중에서 랜덤으로 하나 뽑기 

from random import random
print(random())

from random import randint, randrange, choice   # 일부 멤버만 로딩
# 일부 멤버를 바로 가져오면 random.을 안써도 됨 가장 편한 방법으로 써주면 된다 
print(randrange(1,5))
print(randint(1,5))


from random import *  # 전체 멤버 로딩(비권장)->메모리 소모가 많기 때문에 

print('종료')