# 이원카이제곱
# 동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다.
# 두 집단 이상에서 각 범주(집단) 간의 비율이 서로 동일한가를 검정하게 된다. 
# 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다. 

# 동질성 검정 실습1) 교육 방법에 따른 교육생들의 만족도 분석 - 동질성 검정

# 귀무 : 교육 방법에 따른 교육생들의 만족도에 차이가 없다 
# 대립 : 

import pandas as pd
import scipy.stats as stats

# 만족도에 대한 설문조사 수집 자료
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/survey_method.csv")
print(data.head(3))
print(data['method'].unique())  # [1 2 3]
print(data['survey'].unique())  # [1 2 3 4 5]

ctab = pd.crosstab(index=data['method'], columns=data['survey'])
ctab.index = ["방법1","방법2","방법3"]
ctab.columns = ["매우만족3","만족","보통","불만족","매우불만족"]
print(ctab)

chi2, pv, dof, expected = stats.chi2_contingency(ctab)
print(f"chi2:{chi2},pv:{pv},dof:{dof}")
print("expected : \n", expected)  # 예측 비율

# 해석 : 유의 수준 0.05보다 < pv : 0.5864574374 이므로 새로운 의견을 받아들일 수 없다 (귀무 채택)

print("----------")
# 동질성검정실습2)연령대별sns이용률의 동질성 검정
data2 = pd.read_csv("")
print(data2.head(3))

print(data2['age'].unique())
ctab2=pd.crosstab(index=data2['age'],columns=data2['service'])

ctab2.index = ["20대","30대","40대"]
ctab2.columns = []

chi2, pv, dof, expected = stats.chi2_contingency(ctab2)
print(f"chi2:{chi2},pv:{pv},dof:{dof}")

print("\n위 자료는 샘플 자료이지만 모집단 자료라 가정하고 샘플링 후 검정하기--")
print("전체 건수 : ",len(data2))

samp_data = data2.sample(n=500, replace=True, random_state=1) \
                        .reset_index(drop=True)  # 인덱스를 새로 부여
print("샘플 건수:", len(samp_data))

ctab3 = pd.crosstab(index=samp_data['age'],columns=samp_data)
print(ctab3)

ctab3.index = ["20대","30대","40대"]
ctab3.columns = ["F","T","K","C","E"]

chi2, pv, dof, expected = stats.chi2_contingency(ctab3)
print(f"chi2:{chi2},pv:{pv},dof:{dof}")