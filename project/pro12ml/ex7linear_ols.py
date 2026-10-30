# 단순선형회귀 : ols를 이용한 결과 이해
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.formula.api as smf

# 음료 : 친밀도 적절성 만족도 데이터 이용
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(df.head(3))
print(df.corr())  # 상관계수


# #      친밀도       적절성       만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000

# 음료 적절성과 만족도는 양의 상관관계가 매우 강함.
# 음료 적절성이 만족도에 영향을 준다. 즉, 적절성과 만족도는 원인과 결과의 관계(인과관계)
# 귀무 : 적절성과 만족도는 원인과 결과의 관계가 없다.
# 대립 : 적절성과 만족도는 원인과 결과의 관계가 있다.

model = smf.ols(formula = '만족도~ 적절성',data=df ).fit()
print(model.summary())
print('parameters. : ', model.params)
print('R-squared : ', model.requared)
print('p-value : ',model.pvalues)
print('예측값:', model.predict()[:5])
print('실제값:', df.만족도[:5].values)

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, slope * df.적절성 + intercept, c='b')
plt.show()

print('\n실제값과 예측값 비교')
result_df = pd.DataFrame({
    '실제값':df['만족도'], 
})
print(result_df.head(10).round(3))

# 회귀모델 평가지표 : 결정계수(설명력), 예측오차(MAE, MSE, RMSE), p-value
# 모델 오차로 평가
print(f'RSS : {model.ssr:.4f}')
print(f'MSE : {np.mean(model.resid ** 2):.4f}')
print(f'RMSE : {np.sqrt(np.mean(model.resid ** 2)):.4f}')
# RSS는 오차를 제곱해서 전부 더한 값, MSE는 그것을 평균 낸 값, RMSE는 다시 원래 단위로 바꾼 값
# 세 지표 모두 작을수록 예측 오차가 작지만, 실제 모델의 오차 규모를 이해하기에는 RMSE가 가장 직관적
# LinearRegression과 OLD는 RSS가 최소가 되는 회귀직선을 구한다.
# 그리고 완성된 모델이 얼마나 정확하게 예측하는지는 MES, RMES 등의 지표로 평가한다. 

# 생성된 모델로 새로운 x값에 대한 예측 결과를 출력 (정량적 분석)
new_data = pd.DataFrame({'적절성' : [3.123, 4.123, 5.123]})
new_pred = model.predict(new_data)
print(pd.DataFrame({'적절성' : new_data['적절성'], '예측만족도':new_data['만족도']}))