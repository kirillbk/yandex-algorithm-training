# 27. Вывести маршрут максимальной стоимости

from collections import deque


n, m = map(int, input().split())
table = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
	table[i][1:] = map(int, input().split())

answer = deque()
for i in range(1, n+1):
	for j in range(1, m+1):
		table[i][j] = table[i][j] + max(table[i][j-1], table[i-1][j])

print(table[n][m])
i, j = n, m
while i != 1 or j != 1:
	if j - 1 == 0 or table[i-1][j] > table[i][j-1]:
		i -= 1
		answer.appendleft('D')
	else:
		j -= 1
		answer.appendleft('R')
print(' '.join(answer))
