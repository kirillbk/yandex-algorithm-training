# G. Кролик учит геометрию


n, m = map(int, input().split())
field = list()
for _ in range(n):
    line = list(map(int, input().split()))
    field.append(line)

dp = [[0 for _ in range(m)] for _ in range(n)]
for j in range(m):
    dp[0][j] = field[0][j]
for i in range(n):
    dp[i][0] = field[i][0]

answer = 0
for i in range(1, n):
    for j in range(1, m):
        if field[i][j] == 0:
            continue
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer)
