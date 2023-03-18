# 25. Гвоздики

n = int(input())
nails = [0]
nails.extend(map(int, input().split()))

nails.sort()
dp = [0] * len(nails)
for i in range(2 , min(4,n+1)):
	dp[i] = nails[i] - nails[1]
for i in range(4, n+1):
	dp[i] = min(dp[i-1], dp[i-2]) + nails[i] - nails[i-1]

print(dp[n])
