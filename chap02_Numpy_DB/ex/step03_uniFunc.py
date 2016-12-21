'''
1. 유니버셜 함수 
   - numpy 객체에서 제공되는 수학/통계 함수 
2. 변수 -> FILE 저장 
3. 간단한 차트 그리기
'''

import numpy as np

# 1. 유니버셜 함수
arr = np.arange(20).reshape(5, 4)
print(arr)

# 기술통계량 함수 = 유니버설 함수 
print('평균 =', arr.mean())
print('합계 =', arr.sum())
print('최댓값 =', arr.max())
print('최솟값 =', arr.min())
print('분산 =', arr.var())
print('표준편차 =', arr.std())
print('누적합 =', arr.cumsum())


# 2. 변수 -> FILE 저장 
np.savetxt('data.txt', arr)  #현재 경로
np.savetxt('data.txt2', arr, delimiter = ',')
# 구분자 default : 공백, 현재 위치에 저장 

file = np.loadtxt('data.txt')
#file = np.loadtxt('data.txt', delimiter = ',')
print(file)

# 3. 간단한 차트 그리기
import matplotlib.pyplot as plt

#데이터 생성
dataset=np.arange(1,5) #1~4
print(dataset)

#격자행렬
x,y = np.meshgrid(dataset,dataset)

print(x)
print(y)

#x,y 변량 제곱 -> 합-> 제곱근
z = np.sqrt(x**2+y**2)
print(z)

#차트 생성
plt.plot(z) # 차트 생성
plt.show() # 차트 보이기

