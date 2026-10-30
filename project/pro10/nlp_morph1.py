# 형태소 분석 ---------------


# 토큰이란 컴퓨터가 텍스트를 이해하고 연산할 수 있도록 문장, 단어, 형태소,
# 한글자의 조각처럼 의미를 가진 최소 단위로 쪼갠 결과물을 뜻한다. 

import nltk
from nltk.tokenize import word_tokenize

# 최초 실행 시 필요한 데이터 다운로드
# nltk.download("punkt")


text = "I am studying Python with my friends at room"

# 1. 토큰화
tokens = word_tokenize(text) # ['I', 'am', 'studying', 'Python', 'with', 'my', 'friends', 'at', 'room']
print(tokens)
print()
# 품사 태깅
pos_tags = nltk.pos_tag(tokens)  
print(pos_tags) # [('I', 'PRP'), ('am', 'VBP'), ('studying', 'VBG'), ('Python', 'NNP'), ('with', 'IN'), ('my', 'PRP$'), ('friends', 'NNS'), ('at', 'IN'), ('room', 'NN')]

print('\n\n한국어 토큰(Token)화----------')
# 대표적인 한글 형태소 분석 라이브러리
from konlpy.tag import Okt, Kkma, Komoran

text = "나는 오늘 아침에 학교에 갔다. 가는 길에 국화가 피어 너무 아름다웠다."

print("Okt ---------")
okt = Okt()
print('형태소 : ', okt.morphs(text))
print('품사 태깅 : ',okt.pos(text))
print('품사 태깅 (어간 포함) : ', okt.pos(text, stem=True))
print('명사 추출 : ', okt.nouns(text))


print('Kkma ----------')
kkma =Kkma()
print('형태소 : ', kkma.morphs(text))
print('품사 태깅 : ', kkma.pos(text))
print('명사 추출 : ', kkma.nouns(text))

