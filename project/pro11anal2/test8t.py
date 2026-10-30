# 단일 모집단의 평균에 대한 가설검정(One Sample t-test)

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


# 실습예제1)
# A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리(국어점수 평균검정)
# 귀무 : 학생들의 국어 점수 평균은 80이다

data = pd.read_csv("")
print(data.head(3))
print(data.describe())
print(data["국어"].mean())
print(len(data))   # 20   30행이 넘으면 '중심극한정리'에 의해 정규성을 따른다고 가정




print(stats.shapiro(data["국어"]))


# # 정규성을 만족 못한 경우 대안: t-test
from scipy.stats import wilcoxon
wilcoxon_result =wilcoxon(data["국어"] - 80)
print('wilcoxon_result : ',wilcoxon_result)

# 정규성을 만족한 경우는 ttest_1samp() 수행
ttest_result = stats.ttest_1samp(data["국어"], popmean=80)
print("ttest_result : ", ttest_result)


print("============")
# 실습예제2
# 여아 신생아 몸무게의 평균검정 수행 babyboom.csv
data2 =pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/babyboom.csv")
print(data2.head(3))
pd.set_option("display.max_colums",None)
print(data2.describe())
print()
fdata = data2[data2.gender == 1]  # 1 : 여아, 2: 남아
print(fdata,' ',len(fdata))   # 18
print("여아 신생아 몸무게 평균:", np.mean(fdata.weight))  # 3132.44
# 평균 2800과 3132는 평균에 차이가 있는가?
print("여아 신생아 몸무게 표준편차:",np.std(fdata.weight))

# One sample t-test
result2 = stats.ttest_1samp(fdata['weight'],popmean=2800)
print("result2 : ", result2)
# 해석1 (p값 사용) : 유의수준 0.05> pvalue 이므로 귀무 기각
# 해석2 (t분포표 사용) :
# t값 : 
# t값이 cv값 오른쪽(귀무 기각)에 있으므로 귀무 기각

print("t-test 선행 조건으로 정규성 확인(n<30)")
