# 회귀분석 문제 4) 
# 원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
# Django 또는 Flask로 작성한 웹에서 근무년수를 입력하면 예상 연봉이 나올 수 있도록 프로그래밍 하시오.
# LinearRegression 사용. Ajax 처리!!!      참고: Ajax 처리가 힘들면 그냥 submit()을 해도 됩니다.


# 회귀분석 문제 5) 
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# testdata 폴더 : Consumo_cerveja.csv
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
# Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오
# 조건 : NaN이 있는 경우 삭제!


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Consumo_cerveja.csv')

print(df.head(3))
print(df.info())


columns = [
    'Temperatura Media (C)',
    'Final de Semana',
    'Consumo de cerveja (litros)'
]

# 문제 조건 : Nan이 있는 경우 삭제 
df = df.dropna().copy()

for col in columns:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(',','.',regex=False),
        errors='coerce'   
    )

X=df[['Temperatura Media (C)', 'Final de Semana(mm)']]
y=df['Consumo de cerveja (litros)']

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

print('회귀계수:', model.coef_)
print('절편:', model.intercept_)

# 예측과 실제값과 비교 
pred = model.predict(X)

print('실제값:',y.head(5).values)
print('예측값:',pred[:5])

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

print('MSE:', mean_squared_error(y, pred))
print('RMSE:', np.sqrt(mean_squared_error(y, pred)))
print('R²:', r2_score(y, pred))










