'''
조건문
'''

# 파이썬은 elif를 씁니다. 크음...
num = 75
if num > 80:
  print("A")
elif num > 70:
  print("B")
else:
  print("F")

# pass됩니다.
num = 80
if num >= 80:
 pass

# 한 줄에 if/else를 작성할 수 있습니다.
# annotation이 조금 괴랄하긴 합니다.
# JS의 삼항 연산자가 그리워지는군요...
num = 90
result = "A" if num >= 90 else "F"
print(result)


'''
while 반복문
'''
i = 1
result = 0

while i <= 9:
  result += i
  i+= 1

print(result)


'''
for 반복문
'''
for i in [1, 3, 5]:
  print(i, end=", ")

print(" ")

# range이용, step까지.
for j in range(1, 100, 5):
  print(j, end=", ")

print(" ")

# list와 for의 결합
scores = [50, 76, 80, 90, 30]
for i in range(len(scores)):
  if scores[i] > 70:
    print(f"{i + 1}번 째 점수는 {scores[i]} 합격")
  else:
    print(f"{i + 1}번 째 점수는 {scores[i]} 불합격")


'''
함수
'''
def add(a, b):
  return a + b

print(add(a=2, b=3), end = " ") # 직접 매핑도 가능

# *args, **kwargs
def plus(a, b, *args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

plus(1, 3, 5, 3, 3, 4, hello="test", age=25)

# python은 여러 값을 return할 수 있습니다.
def operators(a, b):
  return a +b, a- b, a /b , a * b

print(type(operators(3, 5)))
print(operators(3, 5))


'''
람다 (일회용, 함수형 프로그래밍을 위함)
'''

print((lambda a, b: a + b)(3, 5))

# sorted에 람다 활용
arr = [("martin", 35), ("darren", 25), ("holster", 55)]

print(sorted(arr, key=lambda x: x[1]))

# map에 람다 활용
list1 = [1, 2, 3, 4 ,5]
list2 = [6, 7, 8, 9, 10]

result = list(map(lambda a, b: a + b, list1, list2))
print(result)



'''
유용한 표준 라이브러리
'''

"""
내장 함수 : 당연히 써야 함
itertools : 순열, 조합
heapq : 힙 기능을 제공하는 라이브러리
bisect : 이진 탐색 기능 제공
collections : 덱, 카운터 등 유용한 자료구조
"""

# 내장 함수
result = sum([1, 3, 5])
print(result)

min = min(1, 3, 5)
max = max(1, 3, 5)
print(min, max)

eval_result = eval("1+3+5")
print(eval_result)


'''순열'''
# 순열 : 서로 다른 n개에서 r개 선택(순서 중요)
# nPr = n(n-1)...(n-r+1)

from itertools import permutations

data = ["A", "B", "C"]

res = list(permutations(data, 2))
print("순열 : ", res)

# 중복 순열
from itertools import product

data = ["A", "B", "C"]
res = list(product(data, repeat=2))
print("중복 순열 : ", res)


'''조합'''
# 조합 : 서로 다른 n개에서 r개 선택(순서 상관 X)
# nCr = nPr / r!

# 조합 (중복 허용)
from itertools import combinations_with_replacement

data = ["A", "B", "C"]
res = list(combinations_with_replacement(data, 2))
print("조합 : ", res)
