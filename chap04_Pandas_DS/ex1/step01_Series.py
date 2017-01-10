'''
Series 객체 특징 
  - 1차원 자료구조
  - pandas에서 제공 
  - DataFrame에 특정 칼럼 추출(Series)
    -> DF 칼럼 구성   
  - numpy와 공통점
    -> 유니버셜 함수
    -> 법위 수정, 블럭 연산
    -> index/slicing 기능
    -> DF 칼럼 구성
  - numpy와 차이점
    -> 1차원(series) vs 다차원(numpy)
'''
#from pandas import Series #Series()
import pandas as pd # pd.Series()
import numpy as np

# list vs Series 객체 생성 
print([4,5.4, 8, 9, 10.5])
ser = pd.Series([4, 5.4, 8, 9, 10.5])
print(ser)

# Series
print(ser[1:4])
print(ser[:4])
print(ser[2:])

# numpy vs series 공통점
# 범위 수정 = numpy 
ser[1:4] = 100
print(ser)

# 블럭연산 : 원소 단위 연산 
ser2 = ser * 0.5
print(ser2)

# 유니버설 함수 
print(np.sum(ser2))
print(np.mean(ser2))
print(np.std(ser2))


# Series 객체 생성  

# (1) list
name = ['hong', 'lee', 'kang'] # index
pay = [250, 350, 450] # value

ser3 = pd.Series(pay, index= name)
print(ser3)

name2 = ['park', 'lee', 'kang'] # index
bonus = [50, 100, 150] # value

ser4 = pd.Series(bonus, index= name2)
print(ser4)

ser5 = ser3 + ser4
print(ser5)
'''
hong      NaN
kang    600.0
lee     450.0
park      NaN
'''

#NaN 처리 방법 : 0으로 대체, 평균으로 대체

ser6=ser5.fillna(ser5.mean())
print(ser6)

'''
hong    525.0
kang    600.0
lee     450.0
park    525.0
'''
# (2) dict
d = {'name':'hong', 'age' : 35, 'pay': 350} # key-> index, value -> value
ser6 = pd.Series(d) 
print(ser6)













