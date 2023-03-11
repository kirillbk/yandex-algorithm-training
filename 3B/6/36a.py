# 36. Два коня

from collections import deque

def solution(x1, y1, x2, y2):
	desk = [[[-1] * 10 for _ in range(10)] for _ in range(2)]
	q = deque()
	step = (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)

	for i in range(2):
		for j in range(10):
			desk[i][8][j] = desk[i][9][j] = 0
			desk[i][j][8] = desk[i][j][9] = 0
	desk[0][y1][x1] = desk[1][y2][x2] = 0

	q.append((x1, y1, 0))
	q.append((x2, y2, 1))
	while q:
		x, y, n = q.popleft()
		if desk[0][y][x] == desk[1][y][x]:
			return desk[0][y][x]
		for dx, dy in step:
			to_x = x + dx
			to_y = y + dy
			if desk[n][to_y][to_x] == -1:
				desk[n][to_y][to_x] = desk[n][y][x] + 1
				q.append((to_x, to_y, n))

	return -1


red, green = input().split()
x1 = ord(red[0]) - ord('a')
y1 = int(red[1]) - 1
x2 = ord(green[0]) - ord('a')
y2 = int(green[1]) - 1

print(solution(x1, y1, x2, y2))
