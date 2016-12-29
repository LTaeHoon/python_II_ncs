'''
step01_array 관련 문제 
 문제) 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고,
       각 행 단위로 합계, 최댓값, 최솟값를 구하시오.

  << 출력 결과 예시>>
1행 합계     :0.8621332497162859
1행 최댓값  :0.3422690004932227
2행 합계     :-1.5039264306910727
2행 최댓값  :0.44626169669315
3행 합계     :2.2852559938172514
3행 최댓값  :1.5507574553572447
4행 합계     :2.772839514775817
4행 최댓값  :2.1615213303400487
5행 합계     :-1.627854878665837
5행 최댓값  :0.528074866336766
'''    

import numpy as np

data = np.random.randn(5,4) #패키지.모듈.함수()
print(data)
print('1행의 합계',data[0].sum())
print('1행의 최댓값',data[0].max())
print('1행의 최소값',data[0].min())
print('2행의 합계',data[1].sum())
print('2행의 최댓값',data[1].max())
print('2행의 최소값',data[1].min())
print('3행의 합계',data[2].sum())
print('3행의 최댓값',data[2].max())
print('3행의 최소값',data[1].min())
print('4행의 합계',data[3].sum())
print('4행의 최댓값',data[3].max())
print('4행의 최소값',data[1].min())
print('5행의 합계',data[4].sum())
print('5행의 최댓값',data[4].max())
print('5행의 최소값',data[4].min())


