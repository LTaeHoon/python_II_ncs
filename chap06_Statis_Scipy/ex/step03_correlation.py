'''
# 상관관계분석 : 피어슨의 상관계수 
  - pd객체.corr()
'''

# 패키지에 대한 별칭 지정 
import pandas as pd 

# csv 파일 가져오기 
print('\ncsv 파일 가져오기')
product = pd.read_csv('product.csv')
'''
product.csv
 - 친밀도, 적절성, 만족도 칼럼
 - 제품에 대해서 친밀도, 적절성, 만족도를 5점 척도로 조사한 data set
'''

print(product.head()) # 앞부분 5줄 보기
# a(친밀도)  b(적절성)  c(만족도)

print('\n상관계수')
re = product.corr(method='pearson')
print(re) # b와 c가 상관계수가 가장높다.
# 피어슨 상관계수 : 0.766853

#          a         b         c
#a  1.000000  0.499209  0.467145
#b  0.499209  1.000000  0.766853 <- 가장 높은 상관계수
#c  0.467145  0.766853  1.000000

# 친밀도와 만족도 칼럼 간의 상관관계 
corr = lambda p : p['a'].corr(p['c'])
re = corr(product)
print('친밀도와 만족도 상관관계:', re) # 피어슨 상관계수 = 0.467144983601
# 다소 높은 양의 상관관계

# 적절성과 만족도 칼럼 간의 상관관계
corr = lambda p : p['b'].corr(p['c'])
re = corr(product)
print('적절성과 만족도 상관관계:',re) # 피어슨 상관계수 = 0.766852699641
# 높은 양의 상관관계

