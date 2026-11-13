# *** 선형회귀분석의 기본 충족 조건 ***
# 선형성 : 독립변수의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
# 정규성 : 잔차항*(오차항)이 정규분포를 따라야 한다.
# 독립성 : 다중회귀 분석 시 독립변수의 값이 서로 관련되지 않아야 한다.
        # 예) 여성변수가 
# 등분산성 ; 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.







# 단순선형모델의 적절성 선행 조건 실습 - ols 사용
# 선형성, 정규성, 등분산성을 기본적으로 확인함.
import numpy as np
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import pandas as pd
import statsmodels.formula.api as smf


advdt = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv', usecols=[1,2,3,4])
print(advdt.head(3), advdt.shape)
print(advdt.info())
print(advdt.corr())  # 상관관계


print()
# 단순선형회귀모델 - ols 사용
lm = smf.ols(formula='sales ~ tv', data=advdt).fit()
print(f'coefficients: {lm.params}, p-value:{lm.pvalues}, r-squared:{lm.rsquared}')
print(lm.summary())  # 회귀분석 결과 요약
print(lm.summary().tables[1])  # 회귀분석 결과 요약 - 계수표만 출력
print()

# 예측
x_new = pd.DataFrame({'tv': advdt['tv'][:3]})
print('예측에 참여한 tv 값: ', x_new.values)
print('실제값 : ', advdt.sales[:3].values)
print('예측값 : ', lm.predict(x_new).values.round(1))
print()

# 경험하지 않은 tv 광고비에 따른 상품 판매량 예측하기
my_new = pd.DataFrame({'tv':[100, 350, 780]})
print('예측 상품 판매량 : ', lm.predict(my_new).values)

print('\n모델의 적절성 선행 조건 확인 : 선형성, 정규성, 등분산성')
# 잔차(Residual) : 실제 관측값과 모델이 예측한 값의 차이를 의미
#                : 모델이 데이터를 얼마나 잘 설명하는지를 보여주는 척도 
fitted = lm.predict(advdt)  # 예측값
residual = advdt.sales - fitted  # 잔차
print('실제값 : ', advdt.sales[:5].values)
print('예측값 : ', fitted[:5].values)
print('잔차 : ', residual[:5].values)
print('잔차의 평균값 : ', np.mean(residual))  # 잔차의 평균값

print('\n잔차의 정규성 : 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, pv = shapiro(residual)
print(f"통계량:{stat}, p값:{pv}")
print('정규성 만족' if pv >= 0.05 else '정규성 불만족')

# Q-Q plot으로 시각화
sm.qqplot(residual, line='s')
plt.title('Q-Q plot으로 정규성 확인')
plt.show()

print('선형성 검정 : 독립변수의 변화에 종속변수도 변화하나 특정한 패턴이 있으면 안됨')
# 독립변수와 종속변수 간에 선형형태로 적절하게 모델링 되었는지 검정
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print('reset_result 결과: ', reset_result.pvalue) 
print('선형성 만족' if reset_result.pvalue >= 0.05 else '선형성 불만족')

# 시각화
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0],'--', color='black')
plt.show()

print('\n등분산성 검정 : 독립변수의 값에 관계없이 오차항의 분산이 일정한지 확인')
# 회귀모델의 예측값이 달라져도 실제값과 예측값 사이의 오차가 비슷한 정도로 흩어지는지 확인
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(advdt['tv']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f'breuschpagan test 결과 : 통계량 : {bp_stat}, pvalue : {bp_pvalue}') # 통계량 : 48.037,  pvalue : 4.18
print('등분산성 만족' if bp_pvalue >= 0.05 else '등분산성 위배')

# 시각화
sns.scatterplot(x=advdt['tv'], y=residual)
plt.axhline(y=0, color='red', linestyle='--') # 잔차가 0인 기준선
plt.xlabel('tv 광고비')
plt.ylabel('잔차')
plt.show()
plt.grid(alpha=0.3)
plt.show()  # 부채꼴처럼 넓게 퍼지고 있어 좋지 않음 

print()
# 참고 : Cook's distance - 특정 데이터가 회귀모델에 얼마나 영향을 주는지 확인
# 영향력 있는 관측치(이상치, outlier)를 탐지하는 진단 방법
# 데이터가 적을 때, 이상치가 의심스러울 때, 모델 결과가 이상하게 나올 때 확인
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance

# 쿡 거리가 가장 큰 5개 확인
print(cd.sort_values(ascending=False).head())


# 쿡 거리가 가장 큰(이상치) 관측치 원본 확인
print(advdt.iloc[35, 178, 25, 175, 131])

# 시각화
fig = sm.graphics.influence_plot(lm, alpha=0.05, criterion="cooks")