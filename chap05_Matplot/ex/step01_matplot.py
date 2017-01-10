'''
Matplotlib API 사용
형식) plt.plot(data)
     plt.show()
  1. 기본 차트 그리기
  2. 산점도 그리기
  3. 차트 플롯으로 여러개 차트 그리기
  4. 차트 플롯으로 한 개 차트 그리기
'''

import matplotlib.pyplot as plt
import numpy as np

# 1. 기본 차트 그리기
data = np.arange(10) #0~9
#plt.plot(data,'r') #차트 생성
#plt.show() # 차트 보이기
help(plt.plot)

# 2. 산점도 그리기
vector_set =[]
for i in range(100) :
    x = np.random.normal(0,1) #(평균, 표준편차) 표준정규분포
    y = x*0.1 + 0.2 + np.random.normal(0,1)
    vector_set.append([x,y]) #[[x,y],[x,y], .....[x100,y100]]
print(vector_set[:5])

x_data = [ v[0] for v in vector_set] # v[0] = [x1,]
y_data = [ v[1] for v in vector_set] # v[1] = [ ,y1]

print(x_data[:5]); print(y_data[:5])

#plt.plot(x_data,y_data,'ro')
#plt.show()

# 3. 차트 플롯으로 여러개 차트 그리기
flg = plt.figure() # 차트 플롯 생성
x1 = flg.add_subplot(2,2,1) # 행,열,위치
x2 = flg.add_subplot(2,2,2) # 행,열,위치
x3 = flg.add_subplot(2,2,3) # 행,열,위치
x4 = flg.add_subplot(2,2,4) # 행,열,위치

#data 생성
data2 = np.random.randint(1,100,100) #start, end, size

#첫번째 영역
x1.hist(data2)

#두번째 영역
x2.scatter(x_data,y_data)

#세번째 영역
x3.plot(np.arange(50))

#네번째 영역
x4.plot(np.random.randn(100),'k--')
plt.show()

# 4. 차트 플롯으로 한 개 차트 그리기
flg2 = plt.figure() # 차트 플롯 생성
chart = flg2.add_subplot(1,1,1) #행,열,위치

# data 생성
data3 = np.random.randn(50) # 난수
data4 = np.random.randn(50).cumsum() #난수 -> 누적합

#계단형 차트
chart.plot(data3,color='r',label='step',drawstyle="steps")
#선스타일 차트
chart.plot(data4,color='g',label='line')
plt.title('multi chart draw')
plt.xlabel('stage')
plt.ylabel('random number')
plt.legend(loc='best')
plt.show()




