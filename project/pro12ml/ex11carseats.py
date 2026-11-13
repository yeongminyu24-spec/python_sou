# 다중선형모델의 적절성 선행 조건 실습 - ols 사용

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/Carseats.csv')
print(df.head(3), df.shape)
print(df.info())
df = df.drop([df.columns[6], df.columns[9],df.columns[10]], axis=1)
print(df.corr())

lm = smf.ols(formula='Sales ~ Income + Advertising', data=df).fit()
print(lm.summary())  # 4개의 독립변수가 모두 p값이 0.05작아 유의한 변수
# Skew(왜도 - 0이면 좌우대칭):0.218(대체로 대칭적 분포임)
# Kurtosis(첨도):2.903 (3에 근사하므로 정규분포와 유사함)
print(f'수정된 결정계수는 {lm.rsquared_adj:.4f}이므로 양호')

print("\n선형회귀 모델의 적절성 조건 체크 후 모델 사용")
print(df.columns)

# 잔차항 구하기
df_lm = df.iloc[:, [0,2,3,5,6]]
print(df_lm.head(2))
fitted = lm.predict(df_lm)
residual = df_lm["Sales"] - fitted
print('잔차 : ', residual[:5])
print('잔차 평균 : ', np.mean(residual))

print('1) 잔차의 정규성 : 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, pv = shapiro(residual)
print(f'통계량 : {stat:.5f}, p값 : {pv:.5f}')
print('정규성 만족' if pv >=0.05 else '정규성 위배')

# q-q plot
sm.qqplot(residual, line='s')
plt.title('q-q plot으로 정규성 확인')
plt.show()

# 선형성 확인
print('2) 선형성 검정')
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print(f'RESET p값 : {reset_result.pvalue:.5f}')
print('선형성 기각 못함' if reset_result.pvalue >= 0.05 else '모형 형태 재검토 필요')


# plot
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0],'--',color='grey')
plt.show()

print('3) 등분산성 검정')
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, lm.model.exog)
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f'p-value : {bp_pvalue}')
print('등분산성 만족' if bp_pvalue >= 0.05 else '등분산성 위배')

# 시각화는 선형성

print('4) 독립성 검정 : 독립변수들 간에 값이 서로 관련되지 않아야 한다.')
# 잔차가 자기상관(인접 관측치의 오차가 관련됨)이 있는지 확인
# Durbin-Watson : 잔차의 자기상관 검정 지표
# 값의 범위는 0 ~ 4이고 2이면 정상(자기상관 없음). <2이면 양의, >2이면 음의 자기상관이 있다.
# Income,Advertising,Price, Age 간에 서로 관련이 없다.

import statsmodels.api as sm
print('Durbin-Watson :',sm.stats.stattools.durbin_watson(residual))

# plot
plt.plot(np.arange(len(residual)), residual, marker='o', linestyle='-')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('관측순서')
plt.ylabel('잔차')
plt.title('독립성확인 : 잔차 순서 그래프')
plt.grid(alpha=0.3)
plt.show()

print('5) 가중공선성 검정 : 독립변수들 간에 값이 서로 관련되지 않아야 한다.')
# VIF(variance_inflation_factor, 분산 인플레 요인, 분산 팽창 지수)
from statsmodels.stats.outliers_influence import variance_inflation_factor
df_ind = df[['Income', 'Advertising']] # 현재 모델에 사용한 독립변수
vif_exog = sm.add_constant(df_ind)
vifdf = pd.DataFrame()
vifdf['변수'] = df_ind.columns
vifdf['vif_value'] = [variance_inflation_factor(vif_exog.values, i + 1)
                for i in range(df_ind.shape[1])]

print(vifdf) # 10을 초과하지 않으면 다중공선성 문제 없음


sns.barplot(x='변수',y='vif_value',data=vifdf)
plt.axhline(10, color='red',linestyle='--')
plt.title('다중공선성 검정')
plt.ylabel('vif')
plt.show()

print('=========')

import pickle
with open('carseat.pickle', 'wb') as obj:
    pickle.dump(lm, obj)
with open('carseat.pickle','rb') as obj: 
    mymodel = pickle.load(obj)

print(mymodel.summary())

print('새로운 값으로 예측')
new_df = pd.DataFrame({'Income' : [35, 62], 'Advertising':[6,3], \
                        'Price' : [105,88], 'Age':[32,55]})
new_pred =mymodel.predict(new_df)
print('Sales 예측 결과 : ',new_pred.values)