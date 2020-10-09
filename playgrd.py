# 삽입 정렬
# 점차 범위를 넓혀가며 순회를 돌며 최소값을 찾아냄
# 따라서 1, 2, 3,... n-1 까지 다 돌면서 동시에 해당 배열의 길이만큼을 다시 돌아야 하므로
# 시간복잡도는 O(n^2)이다. 

input = [5, 10, 2, 7, 11, 30, 15]
result = []

# 선택한 값에 어떤 인덱스를 부여해야 할지 결정함
def findIndex(result, insertion_num):
  for i in range(len(result)):
    if insertion_num < result[i]:
      return i
  # 만약 선택한 값보다 작은 값이 배열에 없다면 마지막 인덱스 할당
  return len(result)

while len(input) != 0:
  insertion_num = input.pop(0)
  index = findIndex(result, insertion_num)
  result.insert(index, insertion_num)

print(result)

  
# def insertion_sort(input):
#     for end in range(1, len(input)):
#         for i in range(end, 0, -1):
#             if input[i - 1] > input[i]:
#                 input[i - 1], input[i] = input[i], input[i - 1]

# insertion_sort(input)
# print(input)