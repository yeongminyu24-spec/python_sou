# 웹 문서를 읽어 형태소 분석
# 단어 출현 횟수를 DataFrame에 저장

import requests
from bs4 import BeautifulSoup
import pandas as pd
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩

okt = Okt()

# url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0" # 이순신
para = "이순신"
url ="https://ko.wikipedia.org/wiki/" + para
# print(url)

headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url=url, headers=headers)

if response.status_code ==200:
    page = response.text
    # print(page,type(page))
    soup = BeautifulSoup(page, 'html.parser')

    wordlist=[]  # 형태소 분석을 통해 명사만 기억

    for item in soup.select("#mw-content-text p"):
        # print(item.string)
        if item.string !=None:
            wordlist += okt.nouns(item.string)

    print("wordlist : ", wordlist)
    print('단어 수 : ', len(wordlist))
    print('중복 제거 후 단어 수 : ', len(set(wordlist)))
    print()
    word_dict = {}  # 단어 발생횟수를 dict로 저장
    for i in wordlist:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    print('word_dict : ',word_dict)

    print('Series로 출력 ---')
    seri_list = pd.Series(wordlist)
    print(seri_list[:3])
    print(seri_list.value_counts()[:5])
    print()
    seri_dict = pd.Series(word_dict)
    print(seri_dict[:3])
    print(seri_dict.value_counts()[:5])

    print('\nDataFrame으로 출력---')
    