'''
DataFrame 객체 특징 
 - DB의 table 구조와 유사 
 - 칼럼단위 상이한 값을 갖는다.
 - DF의 칼럼 구성요소 : numpy, Series, list, dict 
 - 2차원 행렬구조 
'''

import pandas as pd

# 1. 기본자료구조 -> DF 생성 
name = ['hong', 'lee', 'kang']
age = [35,45,55]
pay = [250,350,450]
address = ['seoul', 'busan', 'inchon']

frame = pd.DataFrame({'name':name, 'age':age,         
                      'pay':pay, 'address' : address},
                      columns = ['name','age','pay','address'])
print(frame)

d = {'name':name, 'age':age, 'pay':pay, 'address' : address}
frame2 = pd.DataFrame(d, index = ['a', 'b', 'c'],
                      columns = ['name','age','pay','address'])
print(frame2)


# 2. Series 객체 -> DF 생성 
# Series 객체로 새로운 컬럼 추가
gender = pd.Series(['M', 'M', 'F'] , index = ['a', 'b', 'c'] ) 
frame2['gender'] = gender
print(frame2)


# 3. numpy 객체 -> DF 생성 
import numpy as np

frame3 = pd.DataFrame(np.arange(12).reshape( (3,4) ),
                      columns = ['a','b','c','d'])
print(frame3)

# 원소 참조 예
print(frame3.a)  #DF.컬럼명
print(frame3['a']) #DF['컬럼명']
print(frame3['a'][2])  

# 조건식(부울리언 식) 검색
result = frame3[frame3 > 5]
print(result) # 5미만 NaN 처리 


# 4. DF 행렬 검색 

# 1) ix 속성 이용 : 단일행,열 참조 
print(frame3.ix[1]) # 1행 
print(frame3.ix[1,2]) # 2행3열 - 6

# ix 속성 이용 : 복수 행과열 참조 
print(frame3.ix[ [0,1], [1,2] ]) # [[행], [열]]

# 2) 이름으로 참조
print(frame3['a']) # a칼럼 : 단일칼럼 
col_name = ['a', 'c']
print(frame3[col_name]) # a, c 칼럼 : 복수칼럼  
print(frame3[col_name][:2]) # 복수칼럼의 특정 행 조회 


# 5. DF 행렬 삭제 
print(frame3)
#axis =0 이면 행, axis = 1이면 열
frame4 = frame3.drop(0, axis = 0) # axis = 0 : 1행 삭제  
print(frame4)

frame5 = frame3.drop('a', axis = 1) # axis = 1 : a열 삭제  
print(frame5)






