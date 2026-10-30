# 집단간 차이분석 : 평균 또는 비율 차이를 분석



import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 실습 1번 : 어느 남성 집단의 평균 키 검정
# 귀무 : 해당 집단의 평균 키가 177이다. (모수)
# 대립 : 해당 집단의 평균 키가 177이 아니다 (양측 검정)
# 대립 : 해당 집단의 평균 키가 177보다 크다 (단측 검정)
one_sample = [167.0, 182.7, 169.7, 176.8, 185.0]
print(np.array(one_sample).mean())   # 175.24


# 단일 표본 t-검정

result = stats.ttest_1samp(one_sample, popmean=177.0)
print(result)


print()
result2 = stats.ttest_1samp(one_sample, popmean=170.0)
print(result2)
# statistic=1.74991675, pvalue=0.15503128, df=4

sns.displot(one_sample,bins=10,kde=False, color='skyblue',edgecolor='blue')
plt.axvline(np.mean(one_sample),color='green',linestyle='-',label='표본평균')
plt.axvline(177,color='red',linestyle='-',label='키')