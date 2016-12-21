'''
numpy 객체의 indexing/slicing
'''

import numpy as np

# 1. indexing

# list 객체 
ldata = [0,1,2,3,4,5]
print(ldata[3]) # 4번째 원소 - 3
print(ldata[:]) # 전체 원소 - [0, 1, 2, 3, 4, 5]
print(ldata[:3]) # 0 ~ n-1까지 - [0, 1, 2]

# np 객체 
arr= np.arange(10) # 0 ~ 9
print(arr[3]) # 3
print(arr[:]) # [0 1 2 3 4 5 6 7 8 9]
print(arr[:3]) # [0 1 2]

'''
2. list vs np 공통점
    - index 사용은 동일함(단, 1차원 배열 경우만)
    - 결과는 list 로 반환
'''



# 2. slicing

# list
li_sclicing = ldata[1:4] # ldata = [0,1,2,3,4,5]
print(li_sclicing) # [1, 2, 3]
li_sclicing[2] = 300 # 수정 
print(li_sclicing) # [1, 2, 300]

# li_sclicing[:] = 500 # 전체 수정 불가  
print(ldata) # 원본 수정 안됨 

# np
arr_sclicing = arr[5:8] # arr = [0 1 2 3 4 5 6 7 8 9]
print(arr_sclicing) # [5 6 7]
arr_sclicing[:] = 500 # 전체 수정 
print(arr_sclicing) # [500 500 500]
print(arr) # 원본 수정 - [  0   1   2   3   4 500 500 500   8   9]

'''
3. list vs np 차이점
 - np 객체는 전체 수정이 가능
 - np 객체는 사본 수정 시 원본도 수정됨
'''


# 3. 3차원 배열 구조
arr2d = np.array([ [1,2,3], [4,5,6], [7,8,9] ]) #중첩list(2)
print(arr2d) # 3행3열 

arr3d = np.array([ [[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]] ]) #중첩list(3)
print(arr3d) # 2면2행3열


# 면 접근 
print(arr3d[0]) # default : 면 
# 면,행 접근 
print(arr3d[0,1]) # [4 5 6]
# 면,행,열 접근 
print(arr3d[0,1,1]) # 5


# 4. view & copy 
# 객체 복사 

# (1) view
print('(1) view ')
arr_view = arr3d[1] # 2면 복제(new object) 
print(arr_view) 
print(id(arr_view), id(arr3d)) # 주소 다름 

arr_view[:] = 1000 # 전체 수정 
print(arr_view) # 사본 수정 
print(arr3d) # 원본 수정

# (2) copy 
print('(2) copy ')
arr_copy = arr3d[1].copy() # 2면 복사(new object) 
print(arr_copy) 

arr_copy[:] = 1000 # 전체 수정 
print(arr_copy) 
print(arr3d) # 원본 : copy는 원본 수정 안됨 


# 5. 부울리언 색인 : data[조건식]

data = np.random.randn(3, 4) # 12개 
print(data)

# 부울리언 색인 
print(data[np.logical_and(data > 0.5,data<0.8)]) # list 반환 



