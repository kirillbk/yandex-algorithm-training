# 21. Три единицы подряд

n = int(input())

dp = [0] * n
base = (i for i in (2, 4, 7))
for i in range(min(3, n)):
	dp[i] = next(base)
for i in range(3, n):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(dp[-1])
