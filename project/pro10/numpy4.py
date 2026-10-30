# * numpy의 array() 관련 연습문제 *
# 1) step1 : array 관련 문제
#  정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
# < 출력 결과 예시>

# 1행 합계   : 0.8621332497162859
# 1행 최댓값 : 0.3422690004932227
# 2행 합계   : -1.5039264306910727
# 2행 최댓값 : 0.44626169669315
# 3행 합계   : 2.2852559938172514
# 3행 최댓값 : 1.5507574553572447

import numpy as np


np.random.seed(42)
data = np.random.randn(5,4)
print(data)


i=1
for row in data:
    print('행 합계 : ', np.sum(row))  # row.sum()
    print('행 합계 : ', np.sum(row))
    i += 1

print()


# 2) step2 : indexing 관련문제
#  문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
#    조건1> 36개의 셀에 1~36까지 정수 채우기
#    조건2> 2번째 행 전체 원소 출력하기 
#               출력 결과 : [ 7.   8.   9.  10.  11.  12.]
#    조건3> 5번째 열 전체 원소 출력하기
#               출력결과 : [ 5. 11. 17. 23. 29. 35.]
#    조건4> 15~29 까지 아래 처럼 출력하기
#               출력결과 : 
#               [[15.  16.  17.]
#               [21.  22.  23]
#               [27.  28.  29.]]
zarr = np.zeros((6,6))
print(zarr)
cnt = 0
for i in range(6):
    for j in range(6):
        cnt += 1
        zarr[i, j] = cnt

print(zarr)


print(zarr[1,:])  # zarr[1]
print(zarr[:,4])  
print(zarr[2:5, 2:5])



# 3. zero 다차원 배열에 난수 정수 초기화 결과. 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# [[  90.   91.   92.   93.]
#  [  40.   41.   42.   43.]
#  [ 100.  101.  102.  103.]
#  [  22.   23.   24.   25.]
#  [  52.   53.   54.   55.]
#  [  71.   72.   73.   74.]]

# 4. 첫 번째 행에 1000, 마지막 행에 6000으로 수정

#  [[ 1000.  1000.  1000.  1000.]
#   [   40.    41.    42.    43.]
#   [  100.   101.   102.   103.]
#   [   22.    23.    24.    25.]
#   [   52.    53.    54.    55.]
#   [ 6000.  6000.  6000.  6000.]]

zarr2 = np.zeros((6,4))
print(zarr2)

ran = np.random.randint(20,100,6)
print('ran : ', ran)
ran = list(ran)

for row in range(len(zarr2)):
    num = ran.pop(0)
    for col in range(len(zarr2[0])):
        zarr2[row,col] = num
        num +=1

print(zarr2)

zarr2[0][:] = 1000
zarr2[-1][:] = 6000
print(zarr2)

# 3) step3 : unifunc 관련문제
#   표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
#   아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
#   배열 요소의 누적합을 출력하시오.
# <<출력 예시>>
# ~ 4행 5열 다차원 배열 ~
# [[ 0.56886895  2.27871787 -0.20665035 -1.67593523 -0.54286047]
#            ...
#  [ 0.05807754  0.63466469 -0.90317403  0.11848534  1.26334224]]


arr3 = np.random.randn(4,5)
print(arr3)
print("기술 통계량")
print("평균 : ", np.mean(arr3))
print("합계 : ", np.sum(arr3))
print("표준편차 : ", np.std(arr3))
print("분산 : ", np.var(arr3))
print("최대값 : ", np.max(arr3))
print("최솟값 : ", np.min(arr3))

print("1사분위수 : ", np.percentile(arr3,25))
print("2사분위수 : ", np.percentile(arr3,50))
print("3사분위수 : ", np.percentile(arr3,75))
print("누적합 : ", np.cumsum(arr3))

# numpy 문제 추가~~~~

# q1) 브로드캐스팅과 조건 연산
# 다음 두 배열이 있을 때,
a=np.array([[1],[2],[3]])  # 3행 1열
b=np.array([10,20,30])  # 1행
print(a) 
print(b)
# 두 배열을 브로드캐스팅하여 곱한 결과를 출력하시오.
# 그 결과에서 값이 30이상인 요소만 골라 출력하시오.
result = a*b
print('result : \n', result)
print(result[result >=30])   # [30 40 60 30 60 90]

print()
# q2) 다차원 배열 슬라이싱 및 재배열
# - 3x4 크기의 배열을 만들고 (reshape사용)
# - 2번째 행 전체 출력
# - 1번째 행 전체 출력
# - 배열을 (4,3) 형태로 reshape
# - reshape한 배열을 flatten() 함수를 사용하여 1차원 배열로 만들기
arr=np.arange(1,13).reshape(3,4)
print(arr)
print(arr[1])
print(arr[:,0])
resh=arr.reshape(4,3)
print(resh)
# flat = resh.flatten()
flat = resh.ravel()  # 차원을 떨어뜨림
print(flat)


# q3) 1부터 100까지의 수로 구성된 배열에서 3의 배수이면서 5의 배수가 아닌 값들
# 그런값들을 모두 제곱한 배열을 만들고 출력하시오.
arr= np.arange(1,101)
imsi=(arr%3==0) & (arr%5 !=0)
# print(imsi)
filtered = arr[imsi]
print(filtered)
squ = filtered **2
print(squ)


# q4) 다음과 같은 배열이 있다고 할 때,
arr = np.array([15,22,8,19,31,4])
# 값이 10이상이면 high, 그렇지 않으면 low라는 문자열 배열로 변환하시오.
# 값이 20이상인 요소만 -1로 바꾼 새로운 배열을 만들어 출력하시오,
# 힌트 : np.where(), np.copy()
labels = np.where(arr >= 10, 'high','low')
print(labels)

new_arr = np.copy(arr)
new_arr[new_arr >= 20] = -1
print(new_arr)

print()
# Q5) 정규분포(평균 50, 표준편차 10)를 따르는 난수 1000개를 만들고, 상위 5% 값만 출력하세요.
# 힌트 :  np.random.normal(), np.percentile()
data=np.random.normal(loc=50, scale=10, size=1000)


# 편차가 큰 데이터에 대한 로그 변환
# 큰 값을 압축해서 데이터 간 격차를 줄이는 변환이 가능! 

# ML에서 데이터 분석 시 log를 사용하면?
# 1) 스케일 차이를 축소해 준다. log(10)=1
# 2) 로그 변환하면 치우친 데이터를 정규분포에 가깝게 변경 가능
# 3) 모델링에서 지수 관계를 선형 관계로 바꿔준다

import numpy as np
np.set_printoptions(suppress=True,precision=6)

def test():
    values=np.array([345,34.5,3.45,0.345,0.01,0.1,10,100])
    print(np.log2(3.45),' ',np.log10(3.45),' ',np.log(3.45))

    print('원본 값 : ', values)
    log_values=np.log10(values)
    print('log_values : ', log_values) # 상용 로그
    ln_values = np.log(values)
    print('ln_values :', ln_values) # 자연 로그(밑이 e) : ML에서 주로 자연로그 사용


    # 데이터 분석과 ML에서 Normalization / Min-Max Scaling와 Standardization는
    # 서로 다른 스케일을 가진 특성들을 일정한 기준으로 맞춰주는 Feature Scaling
    
    # 정규화 : 모든 데이터를 0~1 사이 범위 내에 출력
    min_val=np.min(values)
    max_val=np.max(values)
    normalized = (values-min_val) / (max_val-min_val)
    print('정규화 결과 : ', normalized)


    # 표준화 : (데이터-평균) / (표준편차)
    # 데이터의 평균을 0, 표준편차를 1이 되도록 변환하는 방식
    mymean = np.mean(values)
    mystd = np.std(values)
    standardized = (values-mymean) / mystd
    print('표준화 결과 : ', standardized)


class LogTrans:
    # 편차가 큰 데이터를 로그 스케일 변환하고 그 역변환을 제공하는 클래스
    def __init__(self, offset:float=1.0):
        self.offset = offset

    # 로그 변환 메소드
    def transform(self, x:np.ndarray) -> np.ndarray: # 입력, 출력 모두 ndarray
        return np.log(x+self.offset)

    # 역 변환 메소드
    def inverse_transform(self, x_log:np.ndarray) -> np.ndarray:
        return np.exp(x_log) - self.offset


test()
print('-------------')
data=np.array([0.001,0.01,0.1,1,10,100,1000,10000], dtype=float)
logObj = LogTrans()

data_log_scaled = logObj.transform(data)
reversed_data = logObj.inverse_transform(data_log_scaled) # 역변환

print('원본 자료 : ', data)
print('로그 변환 : ', data_log_scaled)
print('역 변환 : ', reversed_data)
