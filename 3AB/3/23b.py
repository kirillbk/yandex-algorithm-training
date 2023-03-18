# 23. Калькулятор

from collections import deque


n = int(input())

dp = [0] * (n + 1)
prev = [0] * (n + 1)

for i in range(2, n+1):
	parent = i - 1
	best = dp[parent]
	if i % 2 == 0 and dp[i//2] < best:
		parent = i // 2
		best = dp[i//2]
	if i % 3 == 0 and dp[i//3] < best:
		parent = i // 3
		best = dp[i//3]
	prev[i] = parent
	dp[i] = best + 1

print(dp[n])
path = deque()
path.append(n)
while path[0] != 1:
	path.appendleft(prev[path[0]])
print(*path)
