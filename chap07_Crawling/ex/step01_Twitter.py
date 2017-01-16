'''
twitter data crawling 절차 
1.트위터 앱 생성 - https://apps.twitter.com(기존 app 사용 가능)
2.트위터 앱의 Keys and Access Tokens 탭에서
  - Consumer Key,Consumer Secret,Access Token,Access Token Secret 이용 인증 요청
3. tweepy 패키지 설치 
  c:\> pip install tweepy 
4. tweepy 관련 폴더 복사(11개 - 날짜/시간 구분)   
  C:\Anaconda3\Lib\site-packages
'''
import tweepy
from tweepy.auth import OAuthHandler,AppAuthHandler  

# 트위터 앱의 Keys and Access Tokens 탭 참조
consumer_key = "YBLhLum2yOLULXRKHhKWLEBrM"
consumer_secret = "AfY6gRtlTBLXWHkYAjLfEwIqCltZBz51Uey2X9a0cMuHkPmn5c"

# 1. 인증요청(1차) : 개인 앱 정보 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "195631864-l8IxAIZ1JdjYx8lrklgNXlRSJEM37LsUauuC6av2"
access_token_secret="5IUPuU5pKu84Yw2SfYbrNVM0p6hXB1KAVYy0Wvyf9AOIF"

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용 
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성  
api = tweepy.API(auth) # API 객체 얻기 
print('api:', api)

keyword ='데이터 분석' # 검색 키워드  

search = [] # 크롤링 결과 저장   

cnt = 1
while(cnt <= 10): # 10 page 대상 크롤링 
    tweets = api.search(keyword)
    for tweet in tweets:
        search.append(tweet)
    cnt = cnt + 1

print(len(search)) # 문서 길이 

print(search[0]) # 첫번째 text 보기 

################
# 전체 문서보기
################

data = {} #전체 문서 추가
i =0

for tweet in search :
    data['text'] = tweet.text #text키에 text 문서 저장    
    print(i," : ",data) #문서번호 : 문서 내용
    i+=1

#####################
# 전체 문서보기 파일 저장
#####################

import os
import codecs

wfile = codecs.open(os.getcwd()+'/twitter.txt', 'w','UTF-8')

data = {} #전체 문서 추가
i =0

for tweet in search :
    data['text'] = tweet.text #text키에 text 문서 저장    
    wfile.write(data['text']+'\n') # 파일 출력
    i+=1
    
wfile.close()  

#파일 읽기
rfile = codecs.open(os.getcwd()+'/twitter.txt','r','UTF-8')
r= rfile.read()
print(r)

rfile.close()