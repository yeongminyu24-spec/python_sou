# 최소 제곱 문제를 행렬방정식으로 표현하고, 
# 수치 선형대수 연산을 통해 

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.5,2.1])

# plt.scatter(x,y)
# plt.grid(True)
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)


# 본래 데이터를 직선으로 표현하기 위해 선형대수학 이용
import numpy.linalg as lin
weight, bias = lin.lstsq(A,y)[0]
print(weight,' ',bias)
print() 
# 회귀식
print(0.96 * 0 + -0.9899999999999998)  # 실제값 -1, 예측값 -0.9899999999999998
print(0.96 * 1 + -0.9899999999999998) #  -0.029999999999999805
print(0.96 * 2 + -0.9899999999999998) # 0.9300000000000002
print(0.96 * 3 + -0.9899999999999998) #  1.8900000000000001


plt.scatter(x,y, marker='o', label ='실제값')
plt.plot(x,weight*x + bias, 'r',label='최적화된 선형직선')
plt.grid(True)
plt.show()

# 경험하지 못한 x값에 대한 예측값 y는?
new_x = 7.5
yhat = weight * new_x  + bias
print('예측 결과 : ', yhat) # 신빙성있는 추론된 결과로 어떤 작업을 참고값으로 사용 가능하다

print()
new_x = 1.2345678
yhat = weight * new_x  + bias
print('예측 결과 : ', yhat)

print('--------------------------------------')
# 선형 회귀 모델 추세식 계산(최소제곱법) 클래스
class MySimpleLinearRegression:
    def __init__(self):
        self.w =None
        self.b = None

    def fit(self, x:np.ndarray, y:np.ndarray):
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        # 최소 제곱법 공식 적용
        bunja = np.sum((x - x_mean)  * (y-y_mean))
        bunmo = np.sum((x - x_mean)  ** 2 )
        self.w = bunja / bunmo

        self.b =  y_mean - (self.w * x_mean)

    def predict(self, new_x:np.ndarray):
        return self.w * new_x + self.b

# 실행 - 임의의 성인 50
np.random.seed(42)  # 난수를 42로 정함
x_height = np.random.normal(175, 5, 50) # 키 (평균키, 표준편차, 갯수)
y_weight = np.random.normal(70, 10, 50) # 몸무게
print(x_height)
print(y_weight)

# 모델 생성
model = MySimpleLinearRegression()
model.fit(x_height,y_weight)  # 기존 데이터를 이용해 회귀계수 w,b를 학습

print('추정된 w(기울기) : ', model.w)
print('추정된 b(절편) : ', model.b)
# yhat =
print()
y_pred = model.predict(x_height)

for i in range(len(x_height)):
    print(f"키:{x_height[i]:.2f}cm의 실제 몸무게:{y_weight[i]:.2f}kg, 예측몸무게:{y_pred[i]:.2f}kg")

print()
# 새로운 키에 대한 몸무게 예측
new_height = np.array([198])
new_weight = model.predict(new_height)
print(f'키 {new_height}cm인 경우 몸무게는 대략 {new_weight}kg')

# 시각화
plt.figure(figsize=(9,6))
plt.scatter(x_height, y_weight, color ='blue', label='실제 데이터')
x_line = np.linspace(x_height.min(),x_height.max(),100)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red',linewidth=2,label='회귀직선')
plt.xlabel('키(cm)')
plt.ylabel('몸무게(kg)')
plt.title('키에 따른 몸무게 선형회귀 분석')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()