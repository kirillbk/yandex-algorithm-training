# 39. Путь спелеолога

from collections import deque


def bfs(cave, start_z, start_y, start_x):
	dx = 0, 0, -1, 1, 0, 0
	dy = -1, 1, 0, 0, 0, 0
	dz = 0, 0, 0, 0, -1, 1
	q = deque()

	q.append((start_z, start_y, start_x))
	while q:
		z, y, x = q.popleft()
		if z == 1:
			return cave[z][y][x]
		for i in range(6):
			to_z = z + dz[i]
			to_y = y + dy[i]
			to_x = x + dx[i]
			if cave[to_z][to_y][to_x] == -1:
				cave[to_z][to_y][to_x] = cave[z][y][x] + 1
				q.append((to_z, to_y, to_x))
	return -1


n = int(input())
cave = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n+2)]
for z in range(1, n + 1):
	input()
	for y in range(1, n + 1):
		for x, cell in enumerate(list(input()), start=1):
			if cell == '#':
				cave[z][y][x] = 0
			elif cell == '.':
				cave[z][y][x] = -1
			else:
				start = z, y, x

print(bfs(cave, *start))
