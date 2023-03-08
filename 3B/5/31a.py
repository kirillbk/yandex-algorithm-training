# 31. Площадь комнаты


dx = 0, 0, 1, -1
dy = 1, -1, 0, 0

def dfs_area(maze, x, y):
	if maze[x][y] == '*':
		return 0
	maze[x][y] = '*'
	area = 1
	for i in range(4):
		area += dfs_area(maze, x + dx[i], y + dy[i])

	return area

n = int(input())
maze = [['*'] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
	maze[i][1:] = list(input())
x, y = map(int, input().split())

print(dfs_area(maze, x, y))

