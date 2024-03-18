# B. Продавец рыбы

n, k = map(int, input().split())
fish = list(map(int, input().split()))

profit = 0
for i in range(0, n):
    for j in range(i + 1, min(i + k + 1, n)):
        profit = max(profit, fish[j] - fish[i])

print(profit)
