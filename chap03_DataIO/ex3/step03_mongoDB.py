'''
MongoDB + dict(json)
준비 : mongod 데몬 실행
'''
import pymongo
import requests

# 1. db 연결 객체 생성
conn = pymongo.MongoClient('127.0.0.1')

# 2. db.collection   
labels = conn.db.labels  #conn.db명.collection명
#labels.insert(dict 형식)

# 3. json -> dict
url = "http://192.168.0.145:8282/Data_Server/data/labels.json"
url_result = requests.get(url)
data = url_result.json()

# 4.DB 저장 : dict -> insert
for d in data :
    labels.insert(d)
    #관측치를 대상으로 문서 저장
    
# 5. 컬렉션에 저장된 데이터 검색
labels_all =labels.find()
print(labels_all) # Cursor

# 6. dict -> DF
import pandas as pd
names = ['name','url','color']
labels_df = pd.DataFrame(list(labels_all),columns = names)
print(labels_df)

'''
정규표현식으로 조건 검색
'^xxx' : xxx로 시작한 문자열 검색
'xxx' : xxx 포함 문자열 검색
'xxx$' : xxx로 끝나는 문자열 검색
'''

# name이 Time으로 시작하는 문자열 검색
find_time = labels.find({'name':{'$regex':'^Time'}})
names = ['name','url','color']
find_time_df = pd.DataFrame(list(find_time),columns = names)
print(find_time_df)

# name이 es로 끝나는 문자열 검색
find_es = labels.find({'name':{'$regex':'es$'}})
names = ['name','color']
find_es_df = pd.DataFrame(list(find_es),columns = names)
print(find_es_df)


# 컬렉션 제거
labels.drop()