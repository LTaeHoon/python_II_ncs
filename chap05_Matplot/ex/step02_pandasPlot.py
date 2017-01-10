'''
Pandas 객체를 이용한 시각화
형식) pandas 객체.plot(data)
    plt.show()
'''

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Series 객체 시각화
ser = Series(np.random.randn(10),
             index = np.arange(0,100,10)) # 0~100, 10개
print(ser)

#ser.plot(color='g')
#plt.show()

# 2. DataFrame 객체 시각화
df = DataFrame(np.random.randn(10,4),
               columns=['one','two','three','four'])
print(df)

#기본 차트
#df.plot()
#plt.show()

#막대차트(세로막대)
#df.plot(kind='bar',title='bar chart plotting')
#plt.show()

#막대차트(가로막대)
#df.plot(kind='barh',title='bar chart plotting')
#plt.show()
#누적막대차트
#df.plot(kind='barh',title='bar chart plotting',stacked=True)
#plt.show()
#밀도분포곡선 : 히스토그램(밀도) -> 곡선
#df.plot(kind='kde',title='kde chart plotting')
#plt.show()

'''
tips.csv
 - 파티 행사에서 총지불금액 vs 팁의 비율 데이터 셋
'''

tips=pd.read_csv('tips.csv')
print(tips.info())
print(tips.head())

# 요일(day)과 파티규모(size) 범주 확인
print(tips['day'].unique()) #['Sun' 'Sat' 'Thur' 'Fri']
print(tips['size'].unique()) #[2 3 4 1 6 5]

# 요일(day)과 파티규모(size)의 교차테이블
party_table = pd.crosstab(tips['day'],tips['size']) # 행,열
print(party_table)

'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''

party_result = party_table.ix[:,2:5] # [row,col]
print(party_result)

#party_result.plot(kind='barh',stacked=True,
#                  title = 'day and size plotting')
#plt.show()

'''
dataset.csv
-특정 컬럼으로 산점도 시각화
'''

dataset = pd.read_csv('dataset.csv')
print(dataset.info())
print(dataset.head())
print(dataset.tail())

data_col = dataset[['resident','gender','age','price']]
print(data_col)

# 산점도 시각화
#plt.scatter(data_col['age'],data_col['price'])
#plt.show()

'''
data.csv
 - 산점도 matrix 시각화 
'''

data = pd.read_csv('data.csv')
print(data.info())
print(data.head())

data_result = data[['E','C','A']]
print(data_result)

# 산점도 matrix 시각화
pd.scatter_matrix(data_result,diagonal='kde')
#diagonal(대각선) : 밀도분포곡선 시각화
plt.show()