# 광고비(tv, radio, newspaper)와 판매량(sales)의 상관관계
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv")
print(data.head())
print(data.describe())

# 필요한 열 선택 (번호 제외)
attr = ['tv', 'radio', 'newspaper', 'sales']
data = data[attr]

print('\n광고 매체 간 상관관계')
print(data[['tv', 'radio', 'newspaper']].corr())


print('\nsales와 다른 특성 사이의 상관관계 (내림차순)')
co_re = data.corr()
sales_corr= co_re['sales'].drop('sales')
sales_corr= co_re['sales'].sort_values(ascending=False)
print(sales_corr.round(3))

# 히트맵
sns.heatmap(co_re, annot=True)
plt.title('광고비와 판매량의 상관관계')
plt.show()
plt.close()
