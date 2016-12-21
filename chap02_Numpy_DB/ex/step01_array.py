'''
Numpy 패키지
 - 선형대수(배열,행렬) 연산에 효과적인 함수 제공
 - list 자료구조 유사
 - list 보다 처리 속도 빠름
 - 주요 함수
   -> randn(r,c) :다차원 배열, 정규분포 난수 생성
   -> array([list]) :다차원 배열 데이터 생성
   -> arange(n) : 0~n-1 정수 생성
   
'''
import numpy as np #별칭

'''
C:\Anaconda3\Lib\site-packages\numpy
'''
# 1. randn(r,c) :다차원 배열, 정규분포 난수 생성

data = np.random.randn(3,4) #패키지.모듈.함수()

print(data)

#블럭연산
print(data+data) #2배
print(data-data) #0

# 2.array([list]) :다차원 배열 데이터 생성

#1) 단일 list
list1 = [3,5.6,5,8,9.5]
print(list1)

arr1 = np.array(list1) #list -> array 객체 생성
print(arr1)

print('평균:',arr1.mean())
print('합계:',arr1.sum())
print('최댓값:',arr1.max())
print('최소값:',arr1.min())
print('분산:',arr1.var())
print('표준편차:',arr1.std())

#2) 중첩 list
list2 = [[1,2,3,4,5],[6,7,8,9,10]]
print(list2)

arr2 = np.array(list2)
print(arr2)
'''2행5열
   0  1  2  3  4
[[ 1  2  3  4  5]  : 1행 -0
 [ 6  7  8  9 10]] : 2행 -1
'''

print(arr2[0,2]) #3

# 블럭연산
print(arr2 * 0.5)
print(arr2 ** 0.5) # arr2^0.5 = sqrt(arr2)
print(np.sqrt(arr2))

# 0으로 채워지는 행렬 데이터 생성
zarr=np.zeros((3,5))
print(zarr)

'''
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
 '''
cnt =0
for i in range(3): # 3회전 : 0~2
    for j in range(5): #5회전 : 0~4
        cnt+=1
        zarr[i][j]=cnt
         
print(zarr)
'''
[[  1.   2.   3.   4.   5.]
 [  6.   7.   8.   9.  10.]
 [ 11.  12.  13.  14.  15.]]
 '''
 
#3. arange(n) : 0 ~ n-1 정수 생성

cnt =0
for i in np.arange(3): # 3회전 : 0~2
    for j in np.arange(5): #5회전 : 0~4
        cnt+=1
        zarr[i][j]=cnt
         
print(zarr)

'''
1. list vs np 차이점
 - np 객체는 수학/통계 관련 함수를 사용 가능
 - np 객체는 블럭연산 가능
 - np 객체는 다차원 배열 객체를 생성해 준다.(행렬)
 
'''



