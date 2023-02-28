# 22. НВП с восстановлением ответа

from collections import deque


n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
prev = [-1] * n
for i in range(n):
	for j in range(i):
		if a[j] < a[i] and dp[j] > dp[i]:
			dp[i] = dp[j]
			prev[i] = j
	dp[i] += 1

i = dp.index(max(dp))
sequence = deque()
while i != -1:
	sequence.appendleft(a[i])
	i = prev[i]

print(*sequence)
