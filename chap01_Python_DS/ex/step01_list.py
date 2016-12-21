'''
list 특징 
 - 1차원 배열 구조 
 형식) 참조변수 = [값1, 값2, ...]
 - 다양한 data type 저장 가능 
 - index 사용, 값 수정
 형식) 참조변수[index] 
'''

# list 생성 
a = ['a', 'b', 'c']
print(a)

# 중첩 list 생성 
b = [10, 20, a, 5, True, "String"]
print(b) # [10, 20, ['a', 'b', 'c'], 5, True, 'String']

# 자료구조 확인 
print(type(a), type(b)) # <class 'list'> <class 'list'>
# 주소 확인 
print(id(a), id(b)) # 12538824 12538568

# 추가,삽입,삭제,수정 
num = ['one', 'two', 'three', 'fore', 'five']
print(num) # ['one', 'two', 'three', 'fore', 'five']

# 원소 추가  
num.append('육'); print(num)
# 원소 삭제 
num.remove('five'); print(num)
# 원소 삽입 
num.insert(0, 'zero'); print(num)
# 원소 수정 
num[2] = '2' ; print(num)

# list 연결, 확장 
list1 = [2.5, 3.6]
list2 = [5.6, 9.3]
list3 = list1 + list2 # list 연결 
print(list3) # [2.5, 3.6, 5.6, 9.3]
list1.append(list2) # list 확장 
print(list1) # [2.5, 3.6, [5.6, 9.3]]

# list 정렬 
list3.sort(reverse=True) # 내림차순 
print(list3) # [9.3, 5.6, 3.6, 2.5]

# 문자열 분리 
word = []
doc = "나는 홍길동 입니다."

for w in doc.split(sep=' ') :
    word.append(w)

print(word) # ['나는', '홍길동', '입니다.']

# 성적처리 : 국어, 영어, 수학 
hong = [85, 75, 90]; yoo = [75, 64, 90]; lee = [65, 74, 64]
student = [hong, yoo, lee]
print(student) # [[85, 75, 90], [75, 64, 90], [65, 74, 64]]
name = ['홍길동', '유관순', '이순신']
print("이름\t국어\t영어\t수학\t총점\t평균")
print('-'*45)
idx = 0
for s in student :
    tot = s[0] + s[1] + s[2]
    avg = tot / 3
    print('{0}    {1}     {2}      {3}     {4}     {5}'\
          .format(name[idx], s[0], s[1], s[2], tot, round(avg,2) ) )
    idx += 1 
    
print('-'*45)    
'''
이름    국어    영어    수학    총점    평균
---------------------------------------------
홍길동    85     75      90     250     83.33
유관순    75     64      90     229     76.33
이순신    65     74      64     203     67.67
---------------------------------------------
'''    
    
'''
list 내포 : list + for
형식) 변수 = [ 실행문   for 변수 in 자료구조 ]
'''

# 정수 -> 실수 
data = [2, 4, 1, 5]
fdata = [] # 빈 list   

for d in data :
    f = float(d) # 정수 -> 실수 
    fdata.append(f)
print(fdata)  # [2.0, 4.0, 1.0, 5.0]  
    
# list + for
result = [ float(d) for d in data ]
print(result) # [2.0, 4.0, 1.0, 5.0]  




