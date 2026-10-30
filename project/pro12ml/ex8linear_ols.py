# 단순선형회귀 - iris dataset 사용
# 상관관계가 약한 경우와 강한 경우로 회귀모델을

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')
print(iris.head(3), type(iris))
print(iris.iloc[:,0:4].corr())

print('\n연습2 : 상관관계가 약한 변수를 사용 : -0.117570')
result2 = smf.ols(formula = 'sepal_length ~ sepal_width', data=iris).fit()
print(result2.summary())
print('R squared : ', result2.rsquared)
print('P-value : ', result2.pvalues.iloc[1])

# 시각화
plt.scatter(iris.sepal_width, iris.sepal_length)
plt.plot(iris.sepal_width, result2.predict(),color='r')
plt.show()

print('\n모델 예측값 확인')
print('실제값 : ', iris.sepal_length[:10].values.round(1))
print('예측값 : ', result2.predict()[:10].round(1))

print('\n새로운 petal_length로 sepal_length를 예측')
new_data = pd.DataFrame({'petal_length' : [1.1, 0.5, 6.0]})
y_pred = result2.predict(new_data)
print('예측된 꽃받침의 길이 : ', y_pred.values.round(5))


print('\n독립변수가 복수인 경우 - 다중선형회귀')

column_select = "+".join(iris.columns.difference(['sepal_length','sepal_width','special_length']))
print(column_select)
result3 = smf.ols(formula ='sepal_length ~ ' + column_select, data=iris).fit()
print(result3.summary())