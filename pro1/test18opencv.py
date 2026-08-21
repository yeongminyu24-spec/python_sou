# Computer Vision(opencv:Open Source Computer Vision) 라이브러리 사용


# pip install opencv-python (밑에 터미널에 입력)
# 만약 위에게 안되면 conda install opencv-python라 치기 
import cv2 # 없어서 이것도 설치해야함 
print(cv2.__version__)

img1=cv2.imread('test18ani.jpeg')
print(type(img1))  # 5.0.0 ->opencv 버전은 5.0 이라는거  # <class 'numpy.ndarray'>

cv2.imshow('image test',img1)
cv2.waitKey()
cv2.destroyAllWindows()
# print('end')    # 창을 닫으면 end가 뜸 


#다른 이름으로 저장
cv2.imwrite('test18ani2.jpg',img1)                                     
cv2.imwrite('test18ani3.jpg',img1, [cv2.IMWRITE_JPEG_QUALITY, 10])   # 퀄리티 낮게함(10이 낮은거 100이 높은거 50이 중간)


# 이미지 크기 조정
img2 = cv2.resize(img1, (300, 100),interpolation=cv2.INTER_AREA)  # 대문자들은 특별한 의미를 가지고 있는 상수라 생각하기 
cv2.imwrite('test18ani4.jpg', img2)    # 크기 작게했음


# 밝기, 상하좌우 회전, 자르기 ..... 지원 