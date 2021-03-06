'''
 step02_indexing 관련문제
 문) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 처리하시오.
     조건1> 20~100 사이의 난수 정수를 발생하여 각 행의 시작열에 난수 정수를 저장하고,
            두번째 열 부터는 1씩 증가시켜 원소 저장
     조건2> 첫번째 행과 마지막 행의 복사본 생성 후,첫번째 행에 1000,마지막 행에 6000으로 수정 

<<출력 예시>>
1. zero 다차원 배열 객체 
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
 
2. 난수 정수 발생 
random.randint(20, 100, 6)
90
40
100
22
52
71

3. zero 다차원 배열에 난수 정수 초기화 결과 
[[  90.   91.   92.   93.]
 [  40.   41.   42.   43.]
 [ 100.  101.  102.  103.]
 [  22.   23.   24.   25.]
 [  52.   53.   54.   55.]
 [  71.   72.   73.   74.]] 

4. 첫번째 행에 1000,마지막 행에 6000으로 수정
 [[ 1000.  1000.  1000.  1000.]
  [   40.    41.    42.    43.]
  [  100.   101.   102.   103.]
  [   22.    23.    24.    25.]
  [   52.    53.    54.    55.]
 [ 6000.  6000.  6000.  6000.]] 
'''

import numpy as np

rd = np.random.randint(20,100,6)
zarr = np.zeros((6,4))
print(zarr)
print(rd)
for i in range(6):
    for j in range(4):
        if j==0:
            zarr[i][j] = rd[i]
            
print(zarr)

for i in range(6):
    for j in range(4):
        if j>0:
            zarr[i][j] =zarr[i][j-1]+1; 
 

print(zarr)

zarrF = zarr[0]
zarrL = zarr[5]
zarrF[:]=1000
zarrL[:]=6000

print(zarr)





