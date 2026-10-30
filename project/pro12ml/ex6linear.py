from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# IQ에 따른 시험 점수 예측
score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/score_iq.csv")
print(score_iq.head(3))
print(score_iq.info())
x=score_iq.iq
y=score_iq.score
print(x[:3])
print(y[:3])

print('상관 계수 : ', np.corrcoef(x,y)[0,1])
print(score_iq[['iq','score']].corr())


# 단순선형회귀분석 모델 생성 - 인과관계가 있다는 가정 하에 진행
model = stats.linregress(x,y)
print(model)

print('가중치 : ',model.slone)
print('편향 : ', model.intercept)
print('p값 : ', model.pvalue)

plt.scatter(x,y)
plt.plot(x, model.slope * x + model.intercept, c='r')
plt.show()


newdf = pd.DataFrame({'iq' : [55,66,77,88,99]})
print('점수 예측 : \n', np.polyval([model.slope, model.intercept],newdf).ravel().round())

