# 퀵 정렬
arr = [3, 5, 7, 9, 2, 4]

def quick_sort(arr):
  length = len(arr)

  if length <= 1:
    return arr
  
  pivot = arr.pop(0)
  former = []
  latter = []

  for i in range(length-1):
    if arr[i] < pivot:
      former.append(arr[i])
    else:
      latter.append(arr[i])

  return quick_sort(former) + [pivot] + quick_sort(latter)

print(quick_sort(arr))