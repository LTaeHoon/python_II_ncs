'''
Set 특징 
 - 순서없음, 중복 허용 불가 
 - index 사용 불가 
 형식) 참조변수 = {값1, 값2, ...}
 - 집합 개념 
'''

s = {3,2,14,5,10}
print(s) # {3, 10, 2, 5, 14}
print(len(s)) # 5
# print(s[2])

gender = ['남', '여', '남', '여']
sgender = set(gender) # 중복 제거 : list -> set
lgender = list(sgender) # set -> list
print(lgender) # ['여', '남']

# 원소 추가/삭제 
s.add(5); print(s) # {3, 10, 2, 5, 14}
s.discard(14); print(s) # {3, 10, 2, 5}









