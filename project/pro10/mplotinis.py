# iris dataset : 150행


import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/blob/master/testdata_utf8/iris.csv")
print(iris_data.info())
print(iris_data.head(3))
print(iris_data.tail(3))


# 산점도 파트
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃잎 길이')
plt.title('붓꽃 길이')
plt.show()

# 꽃의 종류에 따라 다른색(3가지)으로 출력
print()
print(iris_data['Species'].unique())  

cols = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa':choice=1
    elif s== 'versicolor':choice=2
    elif s== 'virginlar':choice =3
    cols.append(choice)

plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃잎 길이')
plt.title('붓꽃 길이')
plt.show()

# pandas의 시각화 기능
from pandas.plotting import scatter_matrix
iris_col = iris_data.loc