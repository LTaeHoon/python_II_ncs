'''
Data Frame의 모양 변경
'''

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df = DataFrame(1000 + np.arange(6).reshape(2,3),
        index = ['대전시', '서울시'],
        columns = ['2015','2016','2017'] )
print(df)

print()

# 1. 칼럼 -> 행으로 변경
df_row = df.stack()
print(df_row)

# 2. 행 -> 칼럼 변경 
df_col = df_row.unstack()
print(df_col)
print("--------------------------------")

# 3. 중복데이터 제거 
data = {'data1' : ['a']*4, 'data2' : [1,1,2,2]}
df2 = DataFrame(data)
print(df2)
'''
  data1  data2
0     a      1  <- 중복1
1     a      1
2     a      2  <- 중복2
3     a      2
'''

result = df2.drop_duplicates()
print(result)
'''
  data1  data2
0     a      1
2     a      2
'''

counter = result['data1'].value_counts() # 빈도수 
print(counter)
# a    2

counter2 = result['data2'].value_counts() # 빈도수 
print(counter2)

'''
2    1
1    1
Name: data2, dtype: int64
'''
print("--------------------------------")

# 4. data 범주화 : 연속형 -> 범주형 
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]

result_cut = pd.cut(price, cut)
print(result_cut)
#   10.3      5.5     7.8     3.6
# [(9, 11], (3, 7], (7, 9], (3, 7]]

counter = pd.value_counts(result_cut)
print(counter)
'''
(3, 7]     2
(9, 11]    1
(7, 9]     1
'''

print("--------------------------------")

# 1 ~ 1000 대상으로 3개 영역 범주화 
data_df = Series( np.arange(1, 1001))
print(data_df)

print()

result_qcut = pd.qcut(data_df, 3)
print(result_qcut)

print()

result_cnt = pd.value_counts(result_qcut)
print(result_cnt)
'''
[1, 334]       334
(667, 1000]    333
(334, 667]     333
'''










