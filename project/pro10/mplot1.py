# matplotlib : 프로팅 라이브러리. 그래프 작성을 위한 다양한 함수를 지원함

# 시각화의 중요성 ......

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')   # AppleGothic  한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수가 깨지는 걸 방지하기 위해서
import koreanize_matplotlib # 예를 이용하면 위 두줄을 대체 가능

x = ['서울','인천','수원']  # 그래프의 x축에 값은 인덱스(수치)
y = [5, 3, 7]  # list
# y = (5,3,7)    # tiple
# y = {5,3,7}    # set X

plt.xlabel('지역명')
plt.ylabel('투자액')
plt.xlim([-1, 3])
plt.ylim([0, 10])
plt.yticks(list(range(0,11,3))) # y축의 라벨을 인위적으로 변경
plt.plot(x,y)
plt.show()


data = np.arange(1,11,2)
plt.plot(data)   # x축의 구간은 자동 설정
x = [0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(x=a, y=b, s=str(b))
plt.show()

x=np.arange(10)
y=np.sin(x)
print(x,y)
# plt.plot(x, y)
plt.plot(x,y,'bo') # color, marker
plt.plot(x, y, 'go--', linewidth = 2, markersize =12)   # option 부여
plt.show()

# hold : 복수의 plot으로 여러 개의 차트를 겹쳐 그림
x = np.arange(0, np.pi*3 ,0.1)
print(x)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.figure(figsize=(10, 5))   # 그래프 전체 크기 지정(w, h)
plt.plot(x, y_sin, 'r')  # 선
plt.scatter(x, y_cos)  # 산점도
plt.legend(['사인','코사인'])   # 범례
plt.show()

print()
# subplot : 하나의 Figure을 여러 개의 Axes(plot)으로 나누기
plt.subplot(2, 1, 1)  # 1행
plt.plot(x,y_sin)
plt.title('sine')
plt.subplot(2, 1, 2)  # 2행
plt.plot(x,y_cos)
plt.title('cosine')
plt.show()


print()
irum=['a','b','c','d','e']
kor = [80,50,70,70,90]
eng = [60,70,80,80,100]
plt.plot(irum, kor, 'ro--')
plt.plot(irum, eng, 'bo--')
plt.ylim([50,100])
plt.title('시험 점수')
plt.legend(['국어','영어'],loc='best')  # loc=1 ~ 4
plt.grid(True)
plt.show()

# 그래프를 이미지 파일로 저장
fig = plt.gcf()
plt.show()
fig.savefig('mplot1.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('mplot1.png')
plt.imshow(img)
plt.show()