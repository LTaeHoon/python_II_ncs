'''
step02_specialFile 과제 
문제) 다음과 같은 웹 주소에서 파일을 직접 읽어서 조건에 맞게 처리하시오.
    http://databank.worldbank.org/data/download/GDP.csv
    조건1> 데이터 전처리 : step02_specialFile 참고 
    조건2> 'Code','Ranking','Nation','GDP' 칼럼명을 지정하여 상위 20개국 데이터만 읽기 
    조건3> 상위 20위 국가의 GDP 칼럼을 대상으로 차트 그리기(GDP 시각화 참고)  
'''


import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "http://databank.worldbank.org/data/download/GDP.csv"

names =['Code','Ranking','3','Nation','GDP','6','7','8','9','10']

#불필요한 행제외, 읽어올 행수 지정, 컬럼명 지정
GDP = pd.read_csv(url,skiprows=[0,1,2,3,4],nrows=50,
                   names=names)

#print(GDP)

GDP.to_csv('GDP.csv',index=None, na_rep='NaN',
            columns =['Code','Ranking','Nation','GDP'])

GDP2 = pd.read_csv('GDP.csv',nrows=20)
#print(GDP2)

GDP2_df = pd.DataFrame(GDP2)
#GDP 데이터만 추출
str_gdp_data = GDP2_df.loc[:,'GDP']
print(type(str_gdp_data))
#GDP 데이터 int 형 변환(그림 그리려면)
GDP_data = [int(g.replace(',','')) for g in str_gdp_data]

print(GDP_data)
plt.plot(GDP_data)
plt.title("GDP Ranking Top 20")
plt.show()

