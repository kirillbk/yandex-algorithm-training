# 38. Игрушечный лабиринт

from collections import deque

def bfs(maze, n, m):
	dx = 0, 0, -1, 1
	dy = -1, 1, 0, 0
	q = deque()

	q.append((0, 0, 0))
	while q:
		x, y, distance = q.popleft()
		maze[y][x] = '1'

		for i in range(4):
			to_x = x + dx[i]
			to_y = y + dy[i]
			while 0 <= to_y < n and 0 <= to_x < m and maze[to_y][to_x] != '1':
				if maze[to_y][to_x] == '2':
					return distance + 1
				to_x += dx[i]
				to_y += dy[i]
			to_x -= dx[i]
			to_y -= dy[i]

			if 0 <= to_y < n and 0 <= to_x < m and (to_x != x or to_y != y):
				q.append((to_x, to_y, distance + 1))


n, m = map(int, input().split())
maze = [input().split() for _ in range(n)]

print(bfs(maze, n, m))

