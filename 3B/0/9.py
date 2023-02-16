# 9. Сумма в прямоугольнике

n, m, k = map(int, input().split())
matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
	line = list(map(int, input().split()))
	matrix[i][1:] = line

prefix = [[0] * (m + 1) for _ in range(n + 1)]
prefix[1][1] = matrix[1][1]
for i in range(2, m + 1):
	prefix[1][i] = prefix[1][i-1] + matrix[1][i]
for i in range(2, n + 1):
	prefix[i][1] = prefix[i-1][1] + matrix[i][1]
for x in range(2, n + 1):
	for y in range(2,m + 1):
		prefix[x][y] = prefix[x][y-1] + prefix[x-1][y] - prefix[x-1][y-1] + matrix[x][y]

for _ in range(k):
	x1, y1, x2, y2 = map(int, input().split())
	area = prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x1-1][y2] - prefix[x2][y1-1]
	print(area)
