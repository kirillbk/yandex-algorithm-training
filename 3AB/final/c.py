# C. Доставка со склада

n = int(input())
orders = []
for _ in range(n):
    a, b = map(int, input().split())
    orders.append((a, b))

max_time = sum(a for a, _ in orders)
# dp[i][j] = минимальное суммарное время курьера B, если курьеры A и B разнесли все заказы
# i - количество заказов
# j - суммарное время курьера A
INF = 100 * 1000 + 1
dp = [[INF] * (max_time + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    a, b = orders[i - 1]
    for j in range(max_time + 1):
        # заказ выполнит курьер B
        dp[i][j] = dp[i - 1][j] + b
        if j >= a:
            # заказ выполнит курьер A
            dp[i][j] = min(dp[i][j], dp[i - 1][j - a])

# dp[n][j] - минимальное время, необходимое курьеру В
# j - время курьера А
min_time = float('inf')
for j in range(max_time + 1):
    # время, когда освободится последний курьер
    time = max(j, dp[n][j])
    if time < min_time:
        min_time = time
        idx = j

# восстановление ответа
first_time = idx
second_time = dp[n][idx]
answer = []
for i in range(n - 1, -1, -1):
    a, b = orders[i]
    if dp[i][first_time] + b == second_time:
        answer.append(2)
        second_time -= b
    else:
        answer.append(1)
        first_time -= a

answer.reverse()
print(*answer)
