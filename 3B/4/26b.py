# 26. Самый дешевый путь

n, m = map(int, input().split())
table = list()
for _ in range(n):
	line = map(int, input().split())
	table.append(list(line))

for i in range(1, m):
	table[0][i] = table[0][i-1] + table[0][i]
for i in range(1, n):
	table[i][0] = table[i-1][0] + table[i][0]
for i in range(1, n):
	for j in range(1, m):
		table[i][j] = table[i][j] + min(table[i][j-1], table[i-1][j])
print(table[n-1][m-1])
