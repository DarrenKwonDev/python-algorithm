# n*n 정방행렬 끼리의 곱셈
# numpy쓰면 참 좋은데 못 씁니다...

def matrixMult(A, B):
  n = len(A)

  # 우선 n*n 크기의 영행렬을 생성
  C = [[0] * n for _ in range(n)]

  # 곱셈 결과 행렬 C의 ij 원소는 A의 i행 * B의 j열 각 원소의 전체 곱
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]

  return C

# test
A = [[1, 2], [1, 2]]
B = [[1, 0], [0, 1]] # 단위 행렬

print(matrixMult(A, B))