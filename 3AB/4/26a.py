# 26. Ход конём - 2

def lazy_dp(dp, i, j, n, m):
	if i < 1 or i > n or j < 1 or j > m:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	dp[i][j] = lazy_dp(dp, i-2, j-1, n, m) + lazy_dp(dp, i-2, j+1, n, m) + lazy_dp(dp, i-1, j-2, n, m) + lazy_dp(dp, i+1, j-2, n, m)
	return dp[i][j]


n, m = map(int, input().split())

dp = [[-1] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1
print(lazy_dp(dp, n, m, n, m))
