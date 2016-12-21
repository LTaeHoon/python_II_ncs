'''
dist 특징 
 - set과 유사함 
 형식) 참조변수 = {'key' : 'value'}
 - json 데이터 처리 시 유용 
 - index 사용불가(순서 없음)
 - 원소는 key로 접근
 형식) 참조변수[key] -> value 반환 
'''

person = {'name' : '홍길동', 'age' : 35, 'address' : '서울시'}
print(person)
print(type(person)) # <class 'dict'>

# 원소 조회 : key
print(person['name']) # 홍길동

# 원소 수정 
person['name'] = "이순신"
print(person) # {'address': '서울시', 'name': '이순신', 'age': 35}

# 원소 삭제 
del person['address']; print(person) # {'age': 35, 'name': '이순신'}

# 원소 추가 
person['pay'] = 5000; print(person) # {'name': '이순신', 'pay': 5000, 'age': 35}

# for문 이용 
for p in person.keys() : 
    print(p, person[p]) # key, value
'''
pay 5000
name 이순신
age 35
'''

# 문자 빈도수 구하기 
result = {} # 빈 set 
str_key = ['a', 'b', 'c', 'a', 'a', 'c']
# a : 3, b : 1, c : 2

for k in str_key : 
    result[k] = result.get(k, 0) + 1 # {'a' : 3}

print(result) # {'a': 3, 'c': 2, 'b': 1}










