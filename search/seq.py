# 순차 탐색 sequnetial search
# 어떤 수 x가 n개로 구성된 배열 S에 존재하는가?

def seqsearch(n, S, x):
  location = 1

  # 해당 로케이션이 n보다 작고, 해당 인덱스가 x가 아닐 경우
  while(location <= n and S[location] != x):
    
    location += 1

  # location이 n을 다 찾아봤는데도 없다면 해당 x가 없다는 의미이므로 0 반환
  if (location > n):
    location = 0

  # 찾았다면 해당 로케이션 반환  
  return location

# 테스트 1
test = seqsearch(3, [1, 2, 3], 3)
print(test)

# 테스트 2
arr = [2, 3, 5, 7, 9]
print(seqsearch(len(arr), arr, 7))
