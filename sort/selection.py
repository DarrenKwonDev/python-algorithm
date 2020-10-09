# 선택 정렬
# 최솟값을 찾고 추가하는 방식으로 작동.
# n, n-1 n-2... n-(n+1) 까지 찾아야 하므로 O(n^2)임. 좋은 정렬이 아님

input = [5, 10, 2, 7, 11, 30, 15]
result = []

while len(input) != 0:
  min_value = min(input)
  result.append(min_value)
  input.pop(input.index(min_value))

print(result)