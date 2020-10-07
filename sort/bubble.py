# 교환 정렬이라고도 부름
# O(n²)

def bubble(S):
  n = len(S)
  for i in range(n -1):
    for j in range(i + 1, n):
      if (S[i] > S[j]):
        S[i], S[j] = S[j], S[i] #swap

# test
S = [1, 4, 2, 5]
bubble(S)
print(S)

'''
그런데 python에는 sort/sorted를 쓰죠...
bubble의 시간복잡도가 n^2인 반면
sort는 O(nLogn)입니다.
'''

arr= [3, 4, 1, 2]
# sorted 사용 (파이썬 내장 함수)
print(sorted(arr))

# sort 사용 (보다시피 리스트 객체의 메서드임 => 원본을 immutable하게 유지할 수가 없다!)
arr.sort()
print(arr)