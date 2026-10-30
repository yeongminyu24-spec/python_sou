import numpy as np
import pandas as pd
import scipy.stats as stats


# 문제 : 새로 개발된 백열전구의 수명은 300 시간인지 검정
# 귀무 : 한국 연구소에서 개발한 백열전구의 평균 수명은 300시간이다.
# 대립 : 한국 연구소에서 개발한 백열전구의 평균 수명은 300시간이 아니다.

# data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
# print("표본 평균 수명 : ", np.mean(data))
# print("표본 크기 : ", len(data))

# # 정규성 검정
# result = stats.shapiro(data)
# print("shapiro result : ", result)

# t_result = stats.ttest_1samp(data, popmean=300)
# print("t_result : ", t_result)
# # 해석 : pvalue=0.143606 > 0.05 귀무 채택
# # 한국 연구소에서 개발한 백열 전구의 평균 수명은 300시간이다.

# print("===========")
# # 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2시간으로 파악되었다.
# # A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서


# data2 = pd.read_csv("")
# print(data2.head(3))

# # 전처리
# data2['time'] = data2['time'].replate("     ","").str.strip()
# data2['time'] = pd.to_numeric(data2['time'], errors='coerce')  # str을 숫자로 변경
# data2 = data2.dropna(subset=['time'])

# print("표본 평균 사용 시간: ", data2['time'].mean())
# print("표본 크기 : ", len(data2))

# # 정규성 검정
# result2 = stats.shapiro(data2['time'])
# print('time에 대한 shapiro result : ', result2)


# # One sample t-test
# t_result2 = stats.ttest_1samp(data2['time'], popmean=5.2)
# print("t_result2:", t_result2)


# print('------------')

# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)


data3 = pd.read_excel(r'C:\Users\acorn\Downloads\개인서비스지역별_동향.xls')
print(data3.head(3))

# 어떤 게 있는지 체크
print(data3.to_string(index=False))
print('--------------------------')
print(data3.columns)

prices = data3["2026년 9월"]

prices = prices.astype(str).str.replace(",","",regex=False)
prices = pd.to_numeric(prices,errors="coerce")

print("지역 수 : ", len(prices))
print("평균 미용 요금: ",prices.mean())