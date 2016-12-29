'''
1. DataFrame 객체 생성
2. json 데이터 처리
3. excel 파일 처리
4. web에서 주식 데이터 읽기
5. web의 upload된 파일 읽기
'''

import pandas as pd
from pandas import DataFrame # class 임포트
from pandas.io.tests import test_excel
from pandas.io.tests.parser import skiprows


# 1. DataFrame 객체 생성

# dict -> DataFrame
# 형식) {'key':['value1','value2']} -> DataFrame(column,내용)

data = {'name':['홍길동','이순신'],'age':[35,45],
        'address':['한양시','해남시']}
print(data)

# DataFrame 객체 생성
data_df = DataFrame(data,columns=['name','age','address'])
print(data_df)
# 특정 칼럼 보기
print(data_df['name'])
print(data_df[['name','address']])
'''  
    name address
0  홍길동     한양시
1  이순신     해남시
'''

# 2. json 데이터 처리

# 1) 간단한 json 데이터 처리
obj ="""
{
    "name":["홍길동","유관순"],
    "age":[35,25],
    "gender":["남자","여자"],
    "address":["서울시","충남시"]
}
"""
import json #json 데이터 -> dict 객체

#(1)json -> dict 
result = json.loads(obj)
print(result)

#(2) dict-> DataFrame
result_df = DataFrame(result,columns=['name','age','gender','address'])
print(result_df)

print(result_df['name'])
#순서 , 개수 변경 가능
print(result_df[['name','gender','age']])

# 2) json 데이터 파일 처리

#json 파일 읽기 -> dict 변환
file = open("data/usagov_bitly.txt", mode ="r", encoding ="utf-8")

# 줄 단위 읽어서 -> dict 변환
recode = [json.loads(data)   for data  in file]
print(recode) #dict 결과 확인

# dict -> DataFrame 변환
recode_df = DataFrame(recode)
print(recode_df.info())
'''
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
'''
print(recode_df[:10])#0~9행

'''
DataFrame 내용보기
 - 칼럼 보기 :DF['칼럼명'] , DF[['칼럼명1','칼럼명2']]
 - 행 보기 : DF[행index]
'''

'''
json vs DataFrame
 - json : 자바스크립트 표준객체 = dict
 - DataFrame : 행렬 구조 객체 - 데이터처리가 용이
'''
# 3. excel 파일 처리
st_excel=pd.ExcelFile('data/student.xlsx')
print(st_excel) #ExcelFile

# 시트 이름을 파싱
st_result = st_excel.parse('student') #탭 이름
print(st_result)

#4. web에서 주식 데이터 읽기
'''
pandas에서 주식정보 읽기 함수 : DataReader() 함수 제공
 - 야후, 구글 사이트
 1.www.yahoo.com
 2.기업정보 입력
 3.주식코드(005930.kr)
 
'''

from pandas.io import data
import datetime #날짜/시간

#야후에서 주식정보 가져오기
'''
 - 야후 사이트
 1. https://finance.yahoo.com/quote/005930.KS/history?p=005930.KS
 2. 기업정보 입력
 3. 주식코드(005930.KS)
 '''
start = datetime.datetime(2016,9,1) #시작일
end = datetime.datetime(2016,12,23) #종료일

samsung=data.DataReader('005930.ks','yahoo',start,end)
print(samsung)

#구글에서 주식정보 가져오기
'''
 - 구글 사이트
 1. https://www.google.com/finance
 2. 기업정보 입력
 3. 주식코드(KRX:005930)
 
 '''
samsung1 = data.DataReader('KRX:005930','google',start, end)
print(samsung1)


#5. web의 upload 된 파일 읽기

import requests
# (1) json 파일 읽기
url = "http://192.168.0.145:8282/Data_Server/data/labels.json"
url_result = requests.get(url)
print(url_result) #[200]

#json -> dict
data = url_result.json()
print(data)

#dict -> data frame
data_df = pd.DataFrame(data)
print(data_df.info())
print(data_df)

# (2) csv 파일 읽기
url2 = "http://databank.worldbank.org/data/download/GDP.csv"
GDP = pd.read_csv(url2)
print(GDP)

# 칼럼명
names =['Code','Ranking','3','Nation','GDP','6','7','8','9','10']


#불필요한 행제외, 읽어올 행수 지정, 컬럼명 지정
GDP2 = pd.read_csv(url2,skiprows=[0,1,2,3,4],nrows=50,
                   names=names) #skiprows 특정행 제거, nrows: 앞에 50개 행을 가져오겠다.names : 컬럼명
print(GDP2)

# 4개 컬럼만 지정하여 파일 저장 index : 행번호 없이 저장
GDP2.to_csv('GDP.csv',index=None, na_rep='NaN',
            columns =['Code','Ranking','3','Nation','GDP'])

#파일 읽기
GDP_result = pd.read_csv('GDP.csv')
print(GDP_result)
