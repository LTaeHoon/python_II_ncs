'''
날씨 데이터 처리와 시각화

'''

import pandas as pd

#날씨 데이터 가져오기
weather = pd.read_csv('weatherAUS.csv')
print(weather.info())
print(weather.head())
print(weather.tail())

# 특정 행 보기
print(weather.ix[0])

# 특정 컬럼 보기
print(weather['MaxTemp'][:10])
print(weather['Rainfall'][:20])
print(weather['RainTomorrow'][:20])

# 3개 컬럼 보기
col = ['MaxTemp','Rainfall','WindDir3pm']
print(weather[col][:20])

# 오후3시 돌풍(WindDir3pm)에 방향 빈도수
WindDir3pm_count = weather['WindDir3pm'].value_counts()
print(WindDir3pm_count)

import matplotlib.pyplot as plt

WindDir3pm_count.plot(kind='bar',rot=45,title='WindDir3pm_counts')
plt.show()

# DF -> 칼럼 추출
rain = weather['RainTomorrow'] # yes,no,nan
print(type(rain))
#<class 'pandas.core.series.Series'>

rain_tomorrow = []
for r in rain :
    rain_tomorrow.append(r)
    
print(rain_tomorrow[:10])
#['No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No']

yes =no = nan = 0
for r in rain_tomorrow :
    if r == 'No':
        no +=1;
    elif r == 'Yes':
        yes +=1;
    else :
        nan +=1;

print(yes,no,nan) #8529 27732 620
print(8529+27732+620) #36881

# dict 형식 빈도수
{'Yes':8529,'No':27732,'Nan' : 620 }

counts = {} # 빈 set(dict)
for rain in rain_tomorrow :
    counts[rain] = counts.get(rain,0) +1
print(counts)
#{nan: 620, 'No': 27732, 'Yes': 8529}
'''
문) 돌풍의 방향(WindGustDir) 칼럼을 이용하여 바람의 방향별로 빈도수를 구하시오.
    <조건1> 빈도수 출력
    <조건2> 가로막대차트 시각화
    힌트 : value_counts(), plot() 이용
'''

WindGustDir = weather['WindGustDir']

WindGustDir_count = WindGustDir.value_counts()

WindGustDir_count.plot(kind='barh',title='WindGustDir_counts')
plt.show()

# 특정 칼럼으로 그룹화
# 형식) DF.groupby(['그룹칼럼','그룹대상칼럼'])

# 돌풍방향에 따른 내일 비 유무 빈도수
groupby = weather.groupby(['WindGustDir','RainTomorrow'])

print(groupby) #<pandas.core.groupby.DataFrameGroupBy>
print(groupby.size())
'''
E            No              1810
             Yes              382
'''
'''
E   1810     382
'''
#칼럼 -> 행
result = groupby.size().unstack()
print(result)
