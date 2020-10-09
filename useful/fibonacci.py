# 피보나치 수열
a = 0
b = 1
print(a)
for i in range(4):
  print(b)
  a, b = b, a + b

# 피보나치 재귀 f(n)을 구하는 재귀식
# f(n) = f(n-1) + (n-2)
def fibo(num):
  if (num == 0 or num == 1):
    return 1
  return fibo(num - 1) + fibo(num -2)

print(fibo(5))