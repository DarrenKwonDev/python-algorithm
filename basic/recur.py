# # sum 재귀함수

# def func(n):
#   if n <= 1:
#     return 1
#   else:
#     return n + func(n-1)

# print(func(100))


# # 곱 재귀함수(팩토리얼)
# def func(n):
#   if n <= 1:
#     return 1
#   else:
#     return n * func(n-1)

# print(func(5))

# # 문자 뒤집기
# string = input("뒤집을 문자열 입력 :")
# def upside_down(string):
#   if string == "":
#     return None
#   else:
#     upside_down(string[1:])
#     return print(string[0])

# upside_down(string)

# 피보나치 수열
a = 0
b = 1
print(a)
for i in range(10):
  print(b)
  a, b = b, a + b
