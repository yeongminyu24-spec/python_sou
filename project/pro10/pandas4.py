# DataFrame의 재구조화 (열을 행으로, 행을 열로 ...)
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(6).reshape(2,3), 
                index=['대전','서울'], columns=['2023','2024','2025'])
print(df)

print()
# stack, unstack
df_row = df.stack() # 열을 아래로 내려서 행 인덱스 쪽으로 쌓기 (가로로 펼쳐진 열을 세로로 쌓기)
print(df_row)
print()
df_col = df_row.unstack()  # 행 인덱스를 다시 열쪽으로 펼치기 (세로로 쌓인 인덱스를 다시 가로로 펼치기)
print(df_col)

print('\n범주화 ---------')
price = [10.3, 5.5, 7.8, 3.6]
cut= [3,7,9,11]  # 구간 기준 값
result_cut=pd.cut(price, cut)  # 연속형 자료가 범주형으로 바뀜
print(result_cut)   
print(pd.Series(result_cut).value_counts())

print('----')
datas=pd.Series(np.arange(1,1001))
# print(datas)
print(datas[:5])
print(datas.head())  # 상
print(datas.head(2))

print(datas[-2:])
print(datas.tail(2)) # 상동

print('\nagg 함수 : 범주의 그룹별 연산')
datas = pd.DataFrame({
    '부서':['개발','개발','영업','영업','인사','개발'],
    '이름':['길동','철수','영희','민수','유리','찬우'],
    '연봉':[4500,4200,4000,4600,3500,3900],
    '성과점수':[90,85,70,75,88,95]
})
print(datas)
print()
print(datas.groupby('부서')['연봉'].mean())
print(datas.groupby('부서')['이름'].count())
print(datas.groupby('부서')[['연봉','성과점수']].mean())

pd.set_option('display.max_columns', None)
print(datas.groupby('부서')[['연봉','성과점수']].agg(['sum','mean','count']))  # 여러 집계함수

print()
# agg 대신 사용자 함수를 작성
def summaryFunc(gr):
    return {
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
    }

print(datas.apply(summaryFunc))  # apply : 함수 실행용 함수