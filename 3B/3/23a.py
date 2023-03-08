# 23. Количество треугольников

n = int(input())

dp = [0] * max(3, (n + 1))
dp[1] = 1
dp[2] = 5
for i in range(3, n+1):
	dp[i] = 3 * dp[i-1] - 3 * dp[i-2] + dp[i-3] + 1
	if i % 2 == 0:
		dp[i] += 1

print(dp[n])
