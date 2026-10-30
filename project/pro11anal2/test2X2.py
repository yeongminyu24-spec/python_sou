# 교차 분석(카이제곱, 카이스퀘어) 가설 검정
# 범주형 자료(변수)를 대상으로 교차빈도에 대한 기술 통계량을 사용
# 교차빈도에 대한 통계적 유의성을 검증해 주는 분석 기법

# 분산이 퍼져 있는 모습을 분포로 만든 것이 카이제곱 분포
# 


# 독립성, 적합도 검정, 분산에 대한 검정, 회귀 분석의 잔체제곱합(SSE) 분석
# 특징 : 항상 양수, 비대칭적 분포(자유도에 따라 모양이 바뀜)

# 실습 - 적합도 검정 (일원카이제곱 검정)

# 가설을 채택하는 두 가지 방법 연습
import pandas as pd

data = pd.read_csv("pass_cross.csv",encoding="euc-kr")
print(data.head())
print(data.shape)   # (50,4)
print()

# 귀무가설(HO) : 벼락치기 공부하는 것과 합격 여부는 관계가 없다. 
# 대립가설(H1) : 벼락치기 공부하는 것과 합격 여부는 관계가 있다. 

print(data[(data['공부함'] ==1)& (data['합격']==1)].shape[0])
print(data[(data['공부함'] ==1)& (data['불합격']==1)].shape[0]) 
print('빈도표 ---')
ctab = pd.crosstab(index=data['공부안함'],columns=data['불합격'], margins=True)
ctab.columns = ['합격','불합격','행합']
ctab.index =['공부함','공부안함','열합']
print(ctab)  # 관찰값(빈도)
# 기대돗수 = (각행의 주변합) * (각열의 주변합) / 총합(전체 표본수)
chi2 = ((18-15) ** 2 / 15 + (7-10) ** 2 / 10 + (12-15) ** 2 / 15 + (13-10) ** 2 / 10)
print("검정 통계량 chi2  : ", chi2)  # 3.0
# df = 2-1 = 1
# 유의수준 : 0.05
# 임계값 - H0을 기각할 지 결정하는 경계값 : 3.84 (카이제곱 분포표 기준)
# 판정 : 검정 통계량 chi2이 3.0< 임계값 3.84 이므로 
# 그러므로 벼락치기 공부하는 것과 합격 여부는 관계가 없다가 의견 유지됨

print('\n방법2 : p-valuer 사용 --- ')
import scipy.stats as stats
chi2, p, _, _ = stats.chi2_contingency(ctab)
print('검정 통계량 : ', chi2)  # 3.0
print('유의 확률(p값) : ',p) 
# 