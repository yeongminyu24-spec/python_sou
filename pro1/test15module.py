# 현재 모듈은 다른 package에 있는 모듈의 멤버를 사용해
# 실행을 통해 어떤 결과를 확인할 수 있는 실행파일!!
# 실행파일은 > python 파일명.py     <== 이 파일은 main module

print('사용자 정의 모듈 후 호출 연습---')
imsi=100 # 뭔가를 하다가...

print('\n경로 지정 방법1 : import 모듈명')
import pack1.mymod1  # pack1 패키지 안에 있는 모듈을 불러오고 
print(dir(pack1.mymod1))   # dir()은 파이썬의 내장 함수로, 어떤 객체가 가지고 있는 이름들을 목록으로 보여주는 함수야.  -> mymod1 안에 들어있는 것들의 이름을 전부 출력
print(pack1.mymod1.__file__)   # 경로명 및 파일명  
print(pack1.mymod1.__name__)   # 모듈명


list1 = [1,2]
list2 = [3, 4, 5]
pack1.mymod1.listHap(list1,list2)  # ([1, 2], [3, 4, 5]) # 다른 사람이 만든 모듈도 쓸 수 있다는 거를 실습하는 중 
if __name__ == '__main__':    # 이게 test15에서 다른 모듈 mymod에서 꺼내 쓸때는 main module인 mymod가 아니였기 때문에 해당 메세지가 뜨지 않았지만
        # if문을 test15로 끌고 오니깐 해당 모듈이 mainmodule이 되어서 print 문이 출력되었다. 
        print('나는 메인 모듈이야') 


print('\n경로 지정 방법2 : from 모듈명 improt 모듈멤버')
from pack1.mymod1 import kbsFunc
kbsFunc()
from pack1.mymod1 import mbcFunc, tot
mbcFunc()
print('tot : ', tot)

from pack1.mymod1 import * # 메모리 낭비가 심하므로 비권장

from pack1.mymod1 import kbsFunc as 케이비에스별명  # 쓰기 귀찮으면 별명을 지어줘도 됨 
케이비에스별명()   # 대한민국 대표 방송

import pack1.subpack.sbs  # 모듈 sbs, 
pack1.subpack.sbs.sbsMansae()
import pack1.subpack.sbs as 난별명
난별명.sbsMansae

print()
from pack1_other import mymod2
imsi = mymod2.Hap(3,4) # 모듈내 함수에서 return만 하므로 해당 값을 새로 변수를 만들어 넣어주고 print해준다. 
print(imsi)

from pack1_other.mymod2 import Cha as 차차차
print(차차차(5,2))

print('\n 경로 지정 방법4 : path 설정이 된 폴더에 모듈이 저장된 경우')
# 예 C:\Users\acorn\anaconda3\envs\myproject\Lib에 mymod3을 넣었을 떄
import mymod3
print(mymod3.Gop(4,5))
# 예 C:\Users\acorn\anaconda3\envs\myproject\Lib\site-packages\numpy\__init__.py
import numpy
print(numpy.mean([3,5,7]))