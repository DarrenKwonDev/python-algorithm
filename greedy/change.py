'''
그리디 알고리즘?
현재 상황에서 지금 당장 가장 좋은 것을 고르는 방법.
따라서, 그리디 알고리즘으로 최적의 해를 얻는 다는 보장은 없습니다.
'''

# # 거스름돈 문제
# # N은 10의 배수여야 함
# N = int(input("거슬러줘야 할 돈 :\n"))
# a = N // 500
# after500 = N % 500

# b = after500 // 100
# after100 = after500 % 100

# c = after100 // 50
# after50 = after100 % 50

# d = after50 // 10
# after10 = after50 % 10

# if (after10 == 0):
#   print(a, b, c, d)
# else:
#   print('N should be a multiple by 10')


'''''''''''''''''''''''''''''''''''''''
리팩토링
'''''''''''''''''''''''''''''''''''''''
N = int(input("거슬러줘야 할 돈 : "))
count = 0;

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += N // coin
  N %= coin

print(f"{count}번 거슬러주는 것이 최소")