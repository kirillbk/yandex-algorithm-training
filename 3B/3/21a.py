# 21. Разложение в сумму кубов

n = int(input())

dp = [0] * (n + 1)
for i in range(1, n + 1):
	dp[i] = dp[i - 1] + 1
	j = 1
	while j ** 3 <= i:
		dp[i] = min(dp[i], dp[i - j ** 3] + 1)
		j += 1

print(dp[n])
