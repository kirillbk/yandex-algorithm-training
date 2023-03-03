n = int(input())
s1 = list(map(int, input().split()))
m = int(input())
s2 = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
	for j in range(1, m + 1):
		if s1[i-1] == s2[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = list()
i = n
j = m
while j > 0 and i > 0:
	if s1[i-1] == s2[j-1]:
		answer.append(s1[i-1])
		i -= 1
		j -= 1
	elif dp[i][j] == dp[i-1][j]:
		i -= 1
	else:
		j -= 1
print(*reversed(answer))
