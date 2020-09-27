''' python tips '''

# list, dictionary, set, tuple 이용만 잘해도 먹고 들어감


'''
무한을 표기하기 위한 e표기
'''
INF = int(1e9)
print(INF)


'''
List Comprehension 활용
'''
arr = [i * i for i in range(10)]
print(arr)

# 조건문 달기
arr = [i for i in range(10) if i % 2 == 1]
print(arr)

# 4, 3 행렬을 생성하고 싶다.
n = 4
m = 3
arr = [[0] * m for _ in range(n)]
print(arr)


'''
List 관련 메서드와 시간복잡도
'''

# sort는 원본 변환/sorted는 sort한 값을 반환하므로 원본은 immutable
a = [4, 3, 9, 7]
a.sort()
print(a)

a = [4, 3, 9, 7]
sorted_a = sorted(a)
print(a)
print(sorted_a)

'''
list 내 특정 값의 원소 모두 제거
'''
# 일반 remove는 처음 발견되는 값만 지움
a = [5, 2, 4, 4, 5]
a.remove(5)

# 모두 지우기 위해서는 set을 이용
a = [5, 2, 4, 4, 5]
remove_set = {4, 5}
removed_a = [i for i in a if i not in remove_set]
print(removed_a)

'''
dictionary
'''

# 키, 값 뽑아내기
a = {"name": "darren", "job": "CTO"}
a["code"] = 123
print(list(a.keys()))
print(list(a.values()))


'''
Set (집합)
'''
# 리스트를 set으로 형변환 하면 중복 제거 됨. set은 애초에 중복과 순서를 따지지 않기 때문
data = set([1, 2, 2, 3, 3, 4])
print(data)

# {}로 감싸 set 초기화 가능
data = {1, 2, 4}
print(data)

# 합, 교, 차집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)

'''
자주 사용되는 표준 입력 input, map
'''

# 하나의 변수만 받을 때
a = int(input("숫자를 입력하세요 int 돌릴거라 ㅎ"))
print(a)

# input으로 받고 공백을 split으로 나눈후 int 함수 적용
# map이 받은 내용은 각 a, b, c로 들어감(unpack)
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트로 받고 싶다면
arr = list(map(int, input().split()))
print(arr)

'''
빠르게 입력을 받아야 할 때. sys.stdin.readline()
'''

# 최대한 빠르게 입력을 받아야 한다면 => 입력 결과가 1000만 개 이런 수준이면 map 돌려서 받으면 시간이 초과된다.
import sys

# enter가 줄 바꿈 기로로 입력되므로 rstrip으로 제거해주자
data = sys.stdin.readline().rstrip()

print(data)


'''
출력
'''
# end로 구분자 가능
print(8, end = "|")
print(10)

# 출력시 타입이 같아야
# print("정답은", 7) 타입이 달라 에러
print("정답은", str(7))

