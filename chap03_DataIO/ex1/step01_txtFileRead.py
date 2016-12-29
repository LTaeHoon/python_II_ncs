'''
기본 파일 입출력
1. read_csv()
2. read_table()
3. 파일 저장

'''

import pandas as pd # 별칭

#1. read_csv()
emp_df=pd.read_csv('data/emp.csv')
print(emp_df.info()) #파일 정보 확인
print(emp_df)

# 구분자가 있는 경우
emp_df=pd.read_csv('data/emp.csv',sep=',') #칼럼 구분자 : 콤마
print(emp_df)

#칼럼명이 없는 경우
student_df=pd.read_csv('data/student.csv',header = None)
print(student_df.info())
print(student_df)

#칼럼명 지정하여 파일 읽기
col_name =['학번','이름','키','몸무게']
student_df = pd.read_csv('data/student.csv',names=col_name)
print(student_df)

# 특정 행 읽기
line_skip = pd.read_csv('data/line_skip.csv',skiprows=[0,2,3])
print(line_skip)

#2.read_table()
'''
 - 데이터가 칼럼구조(행렬구조)
 - 구분자 : 탭, 공백, 특수문자(;)
'''
#1개 이상 공백 구분자
student_txt = pd.read_table('data/student.txt',sep="\s+")
print(student_txt)

student_txt2 = pd.read_table('data/student2.txt',sep="\s+")
print(student_txt2.info())
print(student_txt2)

h = student_txt2['키'] # 키 칼럼 추출
w = student_txt2['몸무게'] #몸무게 칼럼 추출
print(h)
print('키 합계 :',h.sum()) # 키 합계
print(w)
print('몸무게 합계:',w.sum()) # 몸무게 합계

# 특수문자 -> NaN 처리(NA) 
conv ={'키':['$','-'],'몸무게':'-'}
student_txt3 = pd.read_table('data/student2.txt',sep='\s+',
                             na_values = conv)
print(student_txt3)
h = student_txt3['키']
print(h)
print('키 합계:',h.sum())

# 3. 파일 저장
import sys

#파일 저장 전 미리보기
student_txt3.to_csv(sys.stdout, index=None, na_rep ='NaN') # 행번호제거

#파일 저장
student_txt3.to_csv('student_output.csv',index=None, na_rep ='NaN',
                    encoding = 'utf-8')
# 파일 읽기/ 콘솔 출력
st3_txt= pd.read_csv('student_output.csv')
print(st3_txt)










