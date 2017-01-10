'''
문) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
  <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기  
  <조건2> 첫번째 칼럼과 세번째 칼럼을 대상으로 산점도 그래프 그리기(제목과 x,y축이름 표시) 
  <조건3> Species 칼럼을 제외한 나머지 4개 칼럼으로  분포곡선과 산점도 matrix 그리기 
  <조건4> Species 칼럼을 제외한 나머지 4개 칼럼의 평균을 계산하여 막대차트 그리기
'''

import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
from matplotlib.pyplot import ylabel
from docutils.nodes import title

#<조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기  
iris = pd.read_csv('iris.csv')

print(iris.info())
print(iris.head())
print(iris.tail())

#<조건2> 첫번째 칼럼과 세번째 칼럼을 대상으로 산점도 그래프 그리기(제목과 x,y축이름 표시) 

x_data = iris['Sepal.Length'] 
y_data = iris['Petal.Length']

#plt.scatter(x_data,y_data)
#plt.xlabel('Length of Sepal')
#plt.ylabel('Length of Petal')
#plt.title('Scatter plotting')
#plt.show()

#<조건3> Species 칼럼을 제외한 나머지 4개 칼럼으로  분포곡선과 산점도 matrix 그리기 
data_result = iris.ix[:,0:4]
print(data_result)
data_result.plot(kind='kde',title='kde chart plotting')
plt.show()

pd.scatter_matrix(data_result,diagonal='kde')
plt.show()

#<조건4> Species 칼럼을 제외한 나머지 4개 칼럼의 평균을 계산하여 막대차트 그리기
mean=data_result.mean(axis=0)
print(mean)
mean.plot(kind='bar',title='Average of four colimn except Species', color='g')
plt.show()