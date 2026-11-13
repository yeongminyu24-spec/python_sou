

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


pd.set_option('display.max_columns',None)

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/housing.data', sep=r'\s+', header=None)
df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
              'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head(2))
print(df.corr())


x=df[['LSTAT']].values
y=df['MEDV'].values
print(x[:3])
print(y[:3])

# 단항을 통한 단순선형회귀 모델
model = LinearRegression()

# 다항 특성(변수)
quad = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:3])
print(x_cubic[:3])

# 단순회귀
model.fit(x,y)
x_fit = np.arange(x.min(),x.max(),1)[:,np.newaxis]
y_lin_fit = model.predict(x_fit)  # 그래프에 표시용
# print('y_lin_fit : ', y_lin_fit)
model_r2 = r2_score(y,model.predict(x))
print('model_r2 : ',model_r2)

# 다항(2차)
model.fit(x_quad,y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y,model.predict(x_quad))
print('q_r2 : ', q_r2)

# 다항(3차)
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('c_r2 : ',c_r2)


# 시각화
plt.scatter(x, y, label='초기 데이터')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d=1), $R^2=%.2f$'%model_r2, lw=3, c='b')
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad fit(d=2), $R^2=%.2f$'%q_r2, lw=3, c='r')
plt.legend()
plt.show()
