# 어느 음식점의 매출과 날씨 자료를 이용해 강수 여부에 따른 매출액 평균의 차이 검정
# 어느 음식점의 매출 데이터와 기상청이 제공한 날씨 데이터를 활용하여
# 강수 여부에 따른 매출액에 차이가 있는지 검정.
# 두 집단 : 강수량이 있을 때, 맑을 때
# 매출 데이터 : tsales.csv
# 날씨 데이터 : tweather.csv

# 귀무 : 강수 여부에 따라 매출액의 평균에 차이가 없다.
# 대립 : 강수 여부에 따라 매출액의 평균에 차이가 있다. 

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

pd.set_option('display.max_columns', None)

# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv",dtype={'YMD':'object'})
print(sales_data.head(2))
print(sales_data.info())

# 날씨 데이터 읽기
wt_data=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(2))
print(wt_data.info())

data = frame.iloc[:, [0,1,7,8]]
print(data.head())
print('결측치 확인 : ', data.isnull().sum())


# 데이터 분석 box plot으로 시각화
sp = np.array(data.iloc[:,[1,4]])
print(sp)

tg1 = sp[sp[:,1]==0,0]
tg2 = sp[sp[:,1]==1,0]
print(tg1[:3])
print(tg2[:3])
print('tg1 : 강수 없을 때 매출액 평균 : ', np.mean(tg1))
print('tg2 : 강수 있을 때 매출액 평균 : ',np.mean(tg2))

plt.boxplot([tg1,tg2],meanline=True, showmeans=True, notch=True)
plt.show()