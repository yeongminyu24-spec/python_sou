# 외국인(미국, 일본, 중국)이 국내 관광지(5개) 방문 관련자료 사용
# 나라별 관광지 상관관계 확인하기

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 산점도 그리기
def setScatterGraph(tour_table, all_table, tourPoint):
    
    # print('tour_table 크기 : ', tour_table.shape)
    # print('all_table 크기 : ', all_table.shape)

    # 현재 관광지 데이터만 추출
    print('관광지명 : ', tourPoint)
    tour = tour_table[tour_table['resNm'] == tourPoint]
    
    # print('관광지별 외국인 방문 데이터 건수 : ', len(tour)) 
    # # print('외국인 방문 데이터 건수 : ', len(all_table)) 
    print(tour)  

    merge_table = pd.merge(tour_table,all_table,tourPoint)


    # 시각화 - 상관계수
    fig = plt.figure()
    fig.suptitle(tourPoint + '상관관계 분석')

    plt.subplot(1,3,1)
    plt.xlabel('중국인 방문 수')
    plt.ylabel('외국인 방문')
    lamb1 = lambda p:merge_table['china'].corr[merge_table['ForNum']]
    r1 = lamb1(merge_table)
    print('r1 : ', r1)
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'],merge_table['ForNum'],alpha=0.7,s=6, c='red')

    plt.tight_layout()
    plt.show()

def processFunc():
    # 서울시 관광지 정보 파일 읽기
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, mode='r', encoding='utf-8').read())
    # print(jsonTP)
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm','resNm','ForNum'))
    tour_table = tour_table.set_index('yyyymm')
    # print(tour_table.head())
    resNm = tour_table.resNm.unique()
    # print(resNm)

    # 중국인 관광지 정보 파일 읽기
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, mode='r',encoding='utf-8').read())
    china_table = pd.DataFrame(jdata,columns=('yyyymm','visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])

    # 일본인 관광지 정보 파일 읽기
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, mode='r',encoding='utf-8').read())
    japan_table = pd.DataFrame(jdata,columns=('yyyymm','visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])

    # 미국인 관광지 정보 파일 읽기
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, mode='r',encoding='utf-8').read())
    usa_table = pd.DataFrame(jdata,columns=('yyyymm','visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2])

    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)


    r_list = []
    for tourPoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint))

    print('r_list:',r_list)  

    r_df = pd.DataFrame(r_list, columns=('고궁명','중국','일본','미국'))
    r_df = r_df.set_index('고궁명')
    print(r_df)


    r_df.plot(kind='bar', rot=50)
    plt.show()

if __name__ == "__main__":
    processFunc()