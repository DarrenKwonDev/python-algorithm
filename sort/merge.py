# 병합정렬
# 중앙값을 찾아 배열을 재귀적으로 계속 반으로 나눈 후 조각난 배열 별로 정렬 후 병합하는 정렬 알고리즘

arr = [5, 66, 88, 11, 2, 34, 7]

def merge_sort(arr):
  length = len(arr)
  result = []

  if length <= 1:
    return arr

  # 배열의 길이가 홀수인 경우를 대비해 몫만 가져옴
  median = length // 2

  # 잘라낸 배열을 재귀적으로 다시 잘라냄
  former = merge_sort(arr[:median])
  latter = merge_sort(arr[median:])
  # 연산 결과 (([5], ([66], [88])), (([11], [2]), ([34], [7]))) 꼴

  while former and latter:
    if (former[0] < latter[0]):
      result.append(former.pop(0))
    else:
      result.append(latter.pop(0))
  
  while former:
    result.append(former.pop(0))

  while latter:
    result.append(latter.pop(0))

  return result

print(merge_sort(arr))
