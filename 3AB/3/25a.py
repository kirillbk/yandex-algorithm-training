# 25. Увлекательная игра

n, a, b = map(int, input().split())

dp = [0] * (n + 1)
for i in range(2, n + 1):
	tmp = (max(dp[k] + a, dp[i - k] + b) for k in range(1, i))
	dp[i] = min(tmp)
print(dp[n])
