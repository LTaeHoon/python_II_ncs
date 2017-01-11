'''
statistics 패키지 주요함수
  - 수학 통계관련 함수 제공
교차 테이블 작성  
'''

from statistics import mean, median, median_high, mode, pstdev, pvariance 
from numpy import sqrt
import pandas as pd

###################################
### 1. 수학 통계관련 함수 - statistics
###################################

x = [1, 3.3, 5, 7.5, 9]
print(mean(x)) # 평균 - 5.16
print(median(x)) # 중위수 - 5

x = [1, 3.3, 5, 6, 7.5, 9]
print(median_high(x)) # 높은 중위수 - 6

x = [1, 3.3, 5, 7.5, 9, 3.3]
print(mode(x)) # 최빈수 - 3.3

x = [1,2,3,4,5]
# 분산(x) : 평균(3) -> 변량의 편차 : -2,-1,0,1,2 -> 편차제곱: 4,1,0,1,4 -> 평균:2(분산)
# 표준편차(x) : 분산에 sqrt 적용 -> 1.414..

print(pvariance(x)) # 분산 - 2.0
var = pvariance(x)

print(sqrt(var)) # numpy 패키지 함수
print(pstdev(x)) # 표준편차 - 1.4142135623730951


###############################
### 2. 교차테이블 작성 - pandas
###############################

des = pd.read_csv('descriptive.csv') # 인구통계적 데이터 셋 
print(des.info())

# 5개 칼럼만 선택하여 data frame 생성 
data = des[['resident','gender','age','level','pass']]

print(data[:10])

# 지역과 성별 칼럼 교차테이블 
table = pd.crosstab(data.resident, data.gender, margins=True)
# margins=True : All       175  125  300
'''
gender      1    2  All
resident               
           15    6   21 <- resident nan 21개수
1          78   54  132
2          29   26   55
3          21   10   31
4           7   10   17
5          25   19   44
All       175  125  300
'''
print(table)

# 지역과 성별 칼럼 기준 학력수준 교차테이블 
# 지역과 성별 칼럼으로 교차테이블 -> 학력수준 칼럼으로 교차 테이블 
table = pd.crosstab([data.resident, data.gender], data.level, margins=True)
print(table)
'''
level                        1    2   3  All
resident gender                             
         1              0    3   10   2   15 <- 지역의 NaN
         2              0    0    5   1    6 <- 지역의 NaN
1        1              5   44   13  16   78 <- 서울 지역의 남자는 고졸 44, 대졸 13, 대학원졸 16
         2              2   23   19  10   54 <- 서울 지역의 여자는 고졸 23, 대졸 19, 대학원졸 10
2        1              0    9   16   4   29
         2              0   13    7   6   26
'''