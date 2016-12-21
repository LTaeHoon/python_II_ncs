'''
tuple 특징 
 - list 자료구조와 유사함 : index 사용 
 형식) 참조변수 = (값1, 값2, ...)
 - 수정 불가능, list 보다 속도 빠름
'''

t = (1,2,3,4)
print(t) # (1, 2, 3, 4)

# index : 0
print(t[1:3]) # (2, 3) 
print(t[-1]) # 4

# 수정 불가 
#t[1] = 'two' # Error 

# tuple type 반환 함수 

z = zip([1,2,3], [4,5,6])
print(z) # object 형태
print(list(z)) # [(1, 4), (2, 5), (3, 6)]

# 2개 원소로 묶기 
sel = [1,2]
z = zip(sel, [1,2,3], [4,5,6])
print(list(z)) # [(1, 1, 4), (2, 2, 5)]

# 3개 원소로 묶기 
sel = [4,2,6]
z = zip(sel, [1,2,3], [4,5,6])
print(list(z)) # [(4, 1, 4), (2, 2, 5), (6, 3, 6)]














