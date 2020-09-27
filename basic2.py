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

def isLargerThanThree(a):
  if (a > 3):
    return true
  elseL
    return false

print(add(2, 3))
print(isLargerThanThree(5))


'''
람다
'''
