# 서로독립인 세 집단의 평균 차이 검정
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로
# 실기시험을 실시. three_sample.csv
# 독립변수(범주형) : 요인은 한 개()

# 귀무 (영 가설) : 세 가지 교육방법에 따른 실기시험 평균 점수에 차이가 없다.
# 대립 (연구 가설) : 세 가지 교육방법에 따른 실기시험 평균 점수에 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols # 추정 및 검정, 회귀, 시계열 분석


data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/three_sample.csv")
print(data.head(3), ' ', len(data))
print(data.describe())

# 이상치(outlier) 시각화
import matplotlib.pyplot as plt
plt.boxplot(data.score)
plt.show()

# 이상치 값과 갯수 확인 - IQR 이용
q1 = data['score'].quantile(0.25)
q3 = data['score'].quantile(0.75)
iqr = q3-q1

# 이상치 기준
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1 : {q3}, Q3 : {q3}, IQR : {iqr}")
print("이상치 하한값 : ",lower)
print("이상치 상한값 : ",upper)
outlier = data[(data['score']<lower) | (data['score']>upper)]  
print('outlier : ', outlier)
# outlier :      no  method  survey  score
# 7    8       2       1    500
# 59  60       1       0    438
print('outlier 갯수 : ', len(outlier))

data = data.query("score <= 100")
print(len(data))
print(data.describe())


# 교육 방법별 만족 건수 - 교차표 -------
ctab = pd.crosstab(data['method'],data['survey'])
ctab.index = ['방법1','방법2','방법3']
ctab.columns = ['만족','불만족']
print(ctab)
# ============================

print('ANOVA 검정')
# F통계값을 얻기 위해 회귀분석 모델 사용
import statsmodels.api as sm
lin_model = ols("data['score'] ~ data['method']", data = data).fit() # 회귀분석모델 객체
result = sm.stats.anova_lm(lin_model, typ=1)
pd.set_option('display.max_columns',None)
print(result)


f_value = result.loc["data['method']","F"]
p_value = result.loc["data['method']","PR(>F)"]
print('f_value : ', f_value)
print('p_value : ', p_value)

print("\n교육방법별 평균 점수 : \n")
print(data.groupby('method')['score'].mean())

# ANOVA는 각 method별 1:1 평균비교는 알려 주지 않는다.
# 이 때 사후분석을 이용하면 어느 그룹과의 평균값이 의미가 있는지 없는지를 알 수 있다.
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog = data['score'], gruops = data['method'])
print(tukResult)

# tukeyhsd 시각화
import matplotlib.pyplot as plt
tukResult.plot_simulutaneous(xlabel='mean',ylabel='group')
plt.show()