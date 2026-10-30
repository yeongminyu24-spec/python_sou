# 연산 
from pandas import Series, DataFrame
import numpy as np

s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','c','d'])
print(s1)
print(s2)
print(s1+s1)  # 같은 인덱스끼리 연산
print(s1.add(s2))   # numpy 함수를 계승함 , 불일치시 NaN
print(s1.add(s2, fill_value=0))  # + 보다 add가 유연한 연산 가능

print()
print(s1.mul(s2)) # sub,div


print('--------')
df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), index=['서울','대전','부산'])
df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), index=['서울','대전','부산','광주'])
print(df1)
print(df2)
print()
print(df1+df2)
print(df1.add(df2, fill_value=0))  # NaN은 0으로 채움 
# sub, mul, div도 가능


print('NaN(결측값) 처리-----')
df = DataFrame([[1.4, np.nan],[7,-4.5],[np.nan,np.nan],[0.5, -1]], columns=['one','two'])
print(df)
print()
print(df.isnull())   # null 값 탐지
print(df.isna())
print(df.notnull())

print()
print(df.dropna())  # 결측치 포함된 항 싹 지워버리기
print(df.dropna(axis=0)) # 상동
print()
print(df.dropna(how='any')) # NaN이 하나라도 있으면 그 행은 삭제
print(df.dropna(how='all'))  # 한 행의 모든 값이 NaN일 때만 해당 행은 제외

print()  # 열 관련
print(df.dropna(axis=1))  # 결측치(NaN)가 포함된 열 제거
print()
print(df.dropna(subset=['one'])) # 특정 열에 NaN이 있는 행 삭제
print()
print(df.dropna(subset=['two'])) # 특정 열에 NaN이 있는 행 삭제
print()
print(df.dropna(axis='rows'))  # 행 기준 삭제
print()
print(df.dropna(axis='columns'))  # 열 기준 삭제
print()
print(df)
print()
imsi = df.dropna(axis='rows')  # 원본이 아니라 삭제된 복사본이 만들어 짐
print(imsi)
print()
print(df)
print()
# df.dropna(axis='rows',inplace=True)  # 원본 삭제
print(df)

print('\nNaN(결측값) 관련 연산 --------------------------')
print(df.sum())  # 열의 합 - NaN은 연산에서 제외된다.
print(df.sum(axis=0, skipna=True)) # 상동
print(df.sum(axis=1)) # 행별 합
# print(df)


print()
print(df.describe())  # 요약 통계량
print()
words= Series('봄','여름','가을','봄')
print(words.describe())