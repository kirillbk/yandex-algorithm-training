# 22. Кузнечик

n, k = map(int, input().split())

dp = [0] * n
dp[0] = 1
for i in range(1, min(k, n)):
	dp[i] = sum(dp[j] for j in range(i))
for i in range(k,n):
	dp[i] = sum(dp[j] for j in range(i - k, i))

print(dp[-1])
