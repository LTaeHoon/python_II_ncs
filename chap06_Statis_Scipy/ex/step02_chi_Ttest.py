'''
  scipy 패키지의 stats 모듈의 함수 이용 
   1) 카이제곱 검정
   2) 집단 간 평균차이 검정
'''

import pandas as pd
from scipy import stats
from numpy import mean

############################
### 1. 카이제곱 검정
############################
data1 = [4,6,17,16,8,9] #관측치
data2 = [10,10,10,10,10,10] #기대치
chis = stats.chisquare(data1, data2)
print('statistic = %.3f, pvalue = %.3f'%(chis))
#  statistic = 14.200, pvalue = 0.014
#  pvalue >=0.05 : 귀무가설 채택(부정적 진술: 차이가 없다) 
#  pvalue <0.05 : 귀무가설 기각 대립가설 채택(긍정적 진술: 차이가 있다)
############################
### 2. 집단 간 평균 차이 검정
############################

# 1) 한 집단 평균 검정
one_sample = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]
print(len(one_sample)) # 10
one_sample_result = stats.ttest_1samp(one_sample, 175.3)
print(one_sample_result)
print('t검정 통계량 = %.3f, pvalue = %.3f'%(one_sample_result))
# t검정 통계량 = 2.296, pvalue = 0.047
print(mean(one_sample))

# 2) 두 집단 평균 검정 
female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]
two_sample = stats.ttest_ind(male, female)
print(two_sample)
print('t검정 통계량 = %.3f, pvalue = %.3f'%(two_sample))\
# t검정 통계량 = 3.588, pvalue = 0.003

# file 데이터 이용 두집단 평균 검정 
two_sample = pd.read_csv('two_sample.csv')
print(two_sample.info())

# 2개 칼럼만 추출
result = two_sample[['method', 'score']]


# 데이터 분리
# (1) 교육방법 별로 분리(부울식 이용)
m1 = result[result['method'] == 1] # 방법1 
m2 = result[result['method'] == 2] # 방법2 

# (2) 교육방법에서 점수 추출
score1 = m1['score'] # 방법1 -> 점수 
score2 = m2['score'] # 방법2 -> 점수 

# NaN 제거 -> 0 대체 
rms1 = score1.fillna(0)
rms2 = score2.fillna(0)

# rms1과 rms2에 NA가 있으면 Error 발생 
result = stats.ttest_ind(rms1, rms2) # tuple 타입 리턴 
print(result)
print('t검정 통계량 = %.3f, pvalue = %.3f'%result)
# t검정 통계량 = -0.783, pvalue = 0.434

# 3) 대응 두 집단 : 복부 수술전 9명의 몸무게와 복부 수술후 몸무게 변화 
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
paired_sample = stats.ttest_rel(baseline, follow_up)
print(paired_sample)
print('t검정 통계량 = %.3f, pvalue = %.3f'%paired_sample)
#t검정 통계량 = 3.668, pvalue = 0.006 <0.05
print(mean(baseline), mean(follow_up))
#78.4111111111 71.5
print(78.4111111111 - 71.5)








