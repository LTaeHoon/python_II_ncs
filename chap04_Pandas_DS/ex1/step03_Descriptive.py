'''
DataFrame의 요약 통계량 
'''
import pandas as pd

name = ['hong', 'lee', 'kang']
bonus = [50,150,100]
pay = [250,350,450]
su = [40, 40, 30]

frame = pd.DataFrame({'name':name, 'bonus':bonus,         
                      'pay':pay, 'su' : su},
                      columns = ['name','bonus','pay','su'])
print(frame)

# 기술통계량 구하기 
sum1 = frame.sum() # default : 칼럼 단위 합계 
print(sum1)

sum2 = frame.sum(axis = 1) # 사원 단위 : 행 단 단위 합계 
print(sum2)

# axis = 0
print(frame.mean())
print(frame.var())

# summary() = 요약통계량 
print(frame.describe())

# str() = 구조 보기 
print(frame.info()) 

# DF 정렬 
frame_sort = frame.sort_values('pay') # 오름차순 
print(frame_sort)

frame_sort = frame.sort_values('pay', ascending=False) # 내림차순 
print(frame_sort)

# 2개 이상 칼럼으로 정렬 
frame_sort = frame.sort_values(['su', 'bonus'], ascending=False) # 내림차순 
print(frame_sort)

product = pd.read_csv("product.csv")
print(product.info())
print(product.head())
print(product.tail())

# 칼럼의 빈도수
a_cnt = product['a'].value_counts();
print(a_cnt)

# 칼럼의 유일한 값 확인
result = product['b'].unique();
print(result) #[4 3 2 5 1]

b_cnt = product['b'].value_counts();
print(b_cnt)


