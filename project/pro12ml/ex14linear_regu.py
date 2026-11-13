# 과적합
# 선형 회귀 모델이 훈련 데이터(Training Data)에 너무 과하게 학습되어.
# 데이터에 포함된 노이즈나 지엽적인 특성까지 암기해 버리는 현상.
# 새로운 데이터가 들어왔을 때 예측 성능이 크게 떨어진다.

# Linear Regression에서 과적합을 해결하는 방법
# 특성 줄이기, 정규화 적용, 더 많은 데이터 취득하기

# 이 중에서 정규화 적용하기 진행 ---
# 회귀계수 값이 너무 커지지 않도록 비용 함수에 페널티를 부과
# Ridge 회귀 (L2 규제) : 가중치드르이 제곱합을 최소화하여 계수들을 0에 가깝게 작게 만든다.
# Lasso (L1 규제) : 가중치들의 절대값 합을 최소화하며, 중요하지 않은 특성의 계술르 아예 0으로 만든다.
# ElastucNet (Ridge + Lasso)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

iris = load_iris()
# print(iris)
print(iris.keys())

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df.head(2))


print(iris_df.shape)

# train(학습) / test(검증) 데이터로 분리
train_set, test_set = train_test_split(iris_df, test_size=0.3, random_state=12, shuffle=True)
print(train_set.shape, test_set.shape)
# print(train_set.head(3))
# print(test_set.head(3))

print(train_set.iloc[:,[2]])
print(train_set.iloc[:,[3]])

# 회귀분석 방법1 - LinearRegression
# 학습은 train dataset 사용
model_linear = LinearRegression().fit(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]])
print('slope : ', model_linear.coef_)
print('bias : ', model_linear.intercept_)

# 모델 평가는 test dataset으로 작업
pred = model_linear.predict(test_set.iloc[:, [2]])
print('예측값 : ', np.round(pred[:5].flatten(),1))
print('실제값 : ',test_set.iloc[:,[3]][:5].values.flatten())
# 예측값 :  [0.2 1.7 0.2 1.3 2.1]
# 실제값 :  [0.3 1.9 0.2 1.3 2.3]

print(f'r2_score(결정계수) : {r2_score(test_set.iloc[:,[3]], pred)}')

# 시각화
plt.scatter(train_set.iloc[:,[2]],train_set.iloc[:,[3]], color ='red')
plt.plot(np.array(test_set.iloc[:,[2]]))
plt.show()


