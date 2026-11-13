# 다항회귀분석 문제) 

# 데이터 로드 (Servo, UCI) : "https://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data"

# 제어 시스템(servo system), 특히 서보 제어기의 응답 속도(response time) 를 예측하기 위해 수집된 고전 데이터.
# 당시 뉴럴 네트워크와 회귀 분석 연구에 자주 쓰임.

# cols = ["motor", "screw", "pgain", "vgain", "class"]  # 모터 위치, 스크류 위치, P게인(비례 이득), V게인(속도 이득), 응답 시간(타깃)

#  - 타깃/피처 (숫자만 사용: pgain, vgain)
#    x = df[["pgain", "vgain"]].astype(float)   
#    y = df["class"].values
#  - 학습/테스트 분할 ( 8:2 )
#  - 스케일링 (StandardScaler)
#  - 다항 특성 (degree=2) + LinearRegression 또는 Ridge 학습
#  - 성능 평가 
#  - 시각화
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/servo/servo.data', header=None)
cols = ["motor", "screw", "pgain", "vgain", "class"]

print(df.head())
print(df.info())

x = df[["pgain", "vgain"]].astype(float)   
y = df["class"].values

print('입력 데이터 크기 :', x.shape)
print('정답 데이터 크기 : ', y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42) 

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print('스케일링 결과 : ')
print(x_train_scaled[:3])