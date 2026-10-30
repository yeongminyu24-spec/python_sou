
# # 실습 ) 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화
# # 대응표본 t검정 가설
# # 귀무 : 수술 전후 평균 몸무게 차이는 0이다.
# # 대립 : 수술 전후 평균 몸무게 차이는 0이 아니다
# # 유의 수준(alpha) : 0.05
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns


# baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
# follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

# df = pd.DataFrame({
#     '수술전' : baseline,
#     '수술후' : follow_up,
# })

# df['감소량']=df['수술전']-df['수술후']

# print(df)
# print(df.describe())
# print(f"수술 전 평균 : {df['수술전'].mean():.2f}kg")
# print(f"수술 후 평균 : {df['수술후'].mean():.2f}kg") 


# # 대응 표본 t검정
# result = stats.ttest_rel(baseline, follow_up)
# print(f"t 통계량 : {result.statistic:.5f}")
# print(f"p-value : {result.pvalue:.5f}")

# # 해석
# alpha =0.05
# if result.pvalue < alpha:
#     print('귀무 기각 : 수술 전후 평균 몸무게에 통계적으로 유의한 차이가 있다')
# else:
#     print('귀무 채택 : 수술 전후 평균 몸무게에 차이가 있다는 근거가 부족하다')

# # 몸무게 차이값에 정규성 검정
# print('몸무게 감소량 정규성 : ', stats.shapiro(df['감소량']).pvalue)

# # q-q plot
# stats.probplot(df['감소량'],dist='norm',plot=plt)
# plt.grid()
# plt.show()

# # 몸무게 변화량을 시각화
# plt.figure(figsize=(8,5))
# for before, after in zip(baseline,follow_up):
#     plt.plot(['수술 전','수술 후'],[before,after],marker='o')
# plt.title('수술 전후 몸무게 변화')
# plt.ylabel('몸무게(kg)')
# plt.grid(axis='y',alpha=0.3)
# plt.show()


# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 수집된 자료 :  
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

midtest = np.array([80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80])
finaltest = np.array([90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95])


# 정규성 검정
df = finaltest-midtest
shapiro_test = stats.shapiro(df)
print(f"차이값의 정규성 검정 p-value: {shapiro_test.pvalue:.4f}")
# p 0.3011 > 0.05 정규성 만족

t_stat, p_val = stats.ttest_rel(midtest,finaltest)

# 대응 표본 t검정

print(f"t 통계량 : {t_stat:.5f}")
print(f"p-value : {p_val:.5f}")

# 해석
alpha =0.05
if p_val < alpha:
    print('귀무 기각 : 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있지 않다')
else:
    print('귀무 채택 : 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다')

# q-q plot
stats.probplot(df,dist='norm',plot=plt)
plt.grid()
plt.show()

# 성적 변화량을 시각화
plt.figure(figsize=(8,5))
for before, after in zip(midtest,finaltest):
    plt.plot(['중간','기말'],[before,after],marker='o')
plt.title('성적 변화')
plt.ylabel('점수')
plt.grid(axis='y',alpha=0.3)
plt.show()