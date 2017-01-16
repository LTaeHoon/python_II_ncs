'''
1. web 문서(html) 가져오기
    - www.google.com/finance
    - 기업정보 : samsung 전자
2. html의 태크 가져오기
3. 태그 내용 가져오기
'''
import requests # url 요청 모듈
from lxml.html import parse #html 양식으로 파싱
from io import StringIO #문자열 입출력 모듈

# 1. web 문서를 source(text문서)로 가져오기
#url = "http://www.google.com/finance/historical?q=KRX%3A005930&ei=7XJ8WKmBF9WN0ATsrKLIAw&output=csv"
url ="https://www.google.com/finance/historical?q=KRX%3A005930&ei=7XJ8WKmBF9WN0ATsrKLIAw"
# html source 가져오기
text = requests.get(url).text
print(text)

# html 문서로 파싱(처리)
text_source = StringIO(text)
parsed = parse(text_source)
print(parsed) #source -> html
#<lxml.etree._ElementTree object at 0x00000000031366C8>

#root node 찾기
doc = parsed.getroot();

# 2.html의 <a> 태그 가져오기
# 형식) <a href="http://www.naver.com">네이버</a>
#links = doc.findall(.//태그)

links = doc.findall(".//a")
print('링크수 : ',len(links)) #링크수 : 35

# 3. href 속성 가져오기
# 형식) obj.get('href')
link_url =[] # href 값을 저장
cnt=1
for link in links:
    print(cnt, '->',link.get('href'))
    link_url.append(link.get('href'))
    cnt+=1

for lin in link_url:
    print(lin)   
    
'''
4. html의  <table>태그 가져오기  -> <tr> -> <th> or <td> 
'''     
  
# 1) <table> 태그     
tables = doc.findall('.//table')
print('테이블 길이:',len(tables)) # 4

table = tables[3] # 주식정보 : 4번째 테이블 

# 2) <tr> 태그 
rows = table.findall('.//tr')
print('행 길이:', len(rows)) # 행 길이: 31

# 3) 내용 추출 함수 정의 : <th>/<td> 태그  
def col_content(rows, kind = 'td'): #(<tr>, <th>/<td>)
    centents = [] # 내용 저장 list
    col = rows.findall('.//%s'%kind) # th/td
    for val in col :
        centents.append(val.text_content().strip())
        # val.text_content() : 내용을 텍스트 변경(생략하면 object 정보 출력) 
        # strip() : 앞/뒤 공백 제거(생략하면 \n 표시됨)
    return centents # 1행 list 반환    
    
# 표의 제목줄 표시 : <th> : 0행 
th = col_content(rows[0], kind='th') # 1행 - th
print(th) # ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

# 표의 내용 : <td> : 2행 ~ 31행
idx = range(1, len(rows)) # 1 ~ 30
cnt = 1
for i in idx :
    td = col_content(rows[i]) # 행 단위 결과 반환 
    print('[',cnt,']', td)
    cnt += 1


# DataFrame 생성(Date,Open,High) 
import pandas as pd

idx = range(1, len(rows))
def parse_DF():
    Date = []; Open = []; High = []
    
    for i in idx :
        td = col_content(rows[i])
        Date.append(td[0])
        Open.append(td[1])
        High.append(td[2])    
    return pd.DataFrame({'Date':Date,'Open':Open, 'High':High},
                       columns=['Date','Open', 'High'])
print(parse_DF())    










