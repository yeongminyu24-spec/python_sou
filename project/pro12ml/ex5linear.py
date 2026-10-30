# 전통적 방법의 선형회귀(기계학습 중 지도학습)
# 각 데이터에 대한 잔차제곱합이 최소가 되는 추세선(회귀선)을 만들고, 
# 이를 통해 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계를 분석,
# 독립변수 : 연속형, 종속변수 : 연속형 - 두 변수는 상관관계 및 인과관계가 있어야 함
# 정량적인 모델을 생성

import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(12)

# 공부 시간과 시험 점수 데이터
# 독립변수(x, feature) : 공부 시간(1~10)
x=np.linspace(1, 10, 5).reshape(-1, 1)  # 2차원(독립변수는 일관성을 주기위해 2차원으로->파이썬이 그렇게 만들어 둠)
print(x)
# 종속변수(y, label, class)
y = 5*x.ravel() + 40 + np.random.normal(0, 3, 5)
print(y)

r=np.corrcoef(x.ravel(),y)[0,1]
print(f'상관계수 : {r:.4f}')

print('\n모델 작성 방법 1 : LinearRegression 사용 - 모델 생성')

model = LinearRegression()
fit_model = model.fit(x,y) # 내부에서 아래와 같은 작업 진행
# 1) 독립변수 (x)와 종속변수(y)를 입력 받음
# 2) 예측값과 실제값 사이의 오차제곱합이 최소가 되도록 계산
# 3) 최적의 회귀계수(기울기, 절편)을 구함
# 4) 계산된 계수를 모델에 저장
# 단순선형회귀 모델에서는 y=wx+b와 같은 단순한 형태의 수식을
# 참고 : LinearRegression은 신경망처럼 반복학습을 통해 가중치를 

# 예측값 확인
y_newpred = fit_model.predict(x[[0]])
print('예측값1 : ',y_newpred)

# 여러 개의 예측값 확인
new_x = np.array([[2.34], [6.21], [8.123]])
y_newpreds = fit_model.predict(new_x)
for hour, score in zip(new_x.ravel(),y_newpreds):
    print(f"공부시간:{hour:.0f}시간 -> 예상 점수:{score:.2f}점")


print('\n모델 작성 방법 2 : os(Oridinary Least Squares) 사용 - 모델 생성')
# 잔차제곱합(RSS)을 최소화하는 가중치 벡터를 행렬 미분으로 구하는 방법
# 실제 계산은 수치 선형대수 알고리즘을 사용
import statsmodels.formula.api as smf
import pandas as pd

data = np.array([x.ravel(), y])
df = pd.DataFrame(data)
df.columns=['x','y']
print(df.head(3))

model2 = smf.ols(formula ='y~x', data=df)
print(model2.summary())  # OLS Regression Results 제공
print('가중치:',model2.params['x'])
print('편향:', model2.params['Intercept'])

# 예측값 확인
new_df = pd.DataFrame({'x':[2.34,6.21,8.123]})
print('예측 점수 : ', model2.predict(new_df))



# x, y, _= make_regression(n_samples=50,n_features=1, bias=50, coef=True, noise=40)
# print(x)
# print(y)
# r = np.corrcoef(x.ravel(),y)[0,1]
# print(f'상관계수 : {r:.4f}')  

# print('\n모델 작성 방법 1: LinearRegression 사용 - 모델 생성')
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# fit_model = model.fit(x,y)  # 내부에서 아래와 같은 작업 진행
# # 1) 독립변수(x)와 종속변수(y)를 입력 받음
# # 2) 예측값과 실제값 사이의 오차제곱합이 최소가 되도록 계산 
# # 3) 최적의 회귀계수(기울기, 절편)을 구함
# # 4) 계산된 계수를 모델에 저장
# # 단순선형회귀 모델에서는 y=wx + b와 같은 단순한 형태의 수식을 가진 모델이 만들어진다.
# # 참고 : LinearRegression은 신경망처럼 반복학습을 통해 가중치를 갱신하는 것이 아님
# print('기울기(가중치,weight, slope):',fit_model.coef_)
# print('절편(편향,bias):', fit_model.intercept_)

