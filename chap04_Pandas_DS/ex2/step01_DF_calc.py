'''
DataFrame 기본 연산 
'''

from pandas import DataFrame
import numpy as np

# DataFrame 생성 
frame1 = DataFrame(np.arange(0,9).reshape(3,3),
                   columns=list('abc'))
frame2 = DataFrame(np.arange(1,10).reshape(3,3),
                   columns=list('abc'))
print(frame1)

'''
   a  b  c
0  0  1  2
1  3  4  5
2  6  7  8
'''

print(frame2)

'''
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9
'''


# frame 덧셈
add = frame1.add(frame2)
print(add)

'''
    a   b   c
0   1   3   5
1   7   9  11
2  13  15  17
'''


# frame 뺄셈
sub = frame2.sub(frame1)
print(sub)

'''
   a  b  c
0  1  1  1
1  1  1  1
2  1  1  1
'''



# frame 나눗셈 div = frame2 / frame1
div = frame2.div(frame1)
print(div)

'''
          a         b      c
0       inf  2.000000  1.500
1  1.333333  1.250000  1.200
2  1.166667  1.142857  1.125

- inf : 분모가 0인 경우
'''



# frame 곱셈 
mul = frame1.mul(frame2)
print(mul)

'''
    a   b   c
0   0   2   6
1  12  20  30
2  42  56  72
'''



# 행/열 단위 합계/평균/최댓값/최솟값

sumr = mul.sum(axis = 1) # 행 단위
sumc = mul.sum(axis = 0) # 열 단위
print('행 단위 합계:\n',sumr)

'''
행 단위 합계:
 0      8
1     62
2    170
dtype: int64
'''

print('열 단위 합계:\n',sumc)

'''
열 단위 합계:
 a     54
b     78
c    108
dtype: int64
'''


avg1 = mul.mean(axis = 1) # 행 단위 평균
avg2 = mul.mean(axis = 0) # 열 단위 평균
print('행 단위 평균:\n',avg1)
print('열 단위 평균:\n',avg2)


mx = mul.max(axis = 0) # 열 단위 최댓값
mn = mul.min(axis = 0) # 열 단위 최솟값
print(mx)
print(mn)


# apply()함수 이용 외부함수 적용 
asum = mul.apply(sum)
print(asum)

'''
dtype: int32
a     54
b     78
c    108
dtype: int64
'''


# 요약통계량
des = mul.describe()
print(des)

'''
               a          b          c
count   3.000000   3.000000   3.000000
mean   18.000000  26.000000  36.000000
std    21.633308  27.495455  33.406586
min     0.000000   2.000000   6.000000
25%     6.000000  11.000000  18.000000
50%    12.000000  20.000000  30.000000
75%    27.000000  38.000000  51.000000
max    42.000000  56.000000  72.000000
'''












