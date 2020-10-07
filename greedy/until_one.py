n, k = map(int, input().split())
counter = 0

while True:
  if (n % k == 0):
    n = n // k
    counter = counter + 1
    if (n == 0): break
  else:
    n = n -1
    counter = counter + 1
    if n == 1: break

print(counter)