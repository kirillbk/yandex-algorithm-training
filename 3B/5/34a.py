# 34. Десант

from sys import setrecursionlimit

setrecursionlimit(1000000)


steps = (0, -1), (0, 1), (-1, 0), (1, 0)

def dfs(field: list[list[int]], visited: list[int], x: int, y: int):
	visited[y][x] = True
	now_top = field[y][x]
	for dx, dy in steps:
		next_x = x + dx
		next_y = y + dy
		if not visited[next_y][next_x] and now_top <= field[next_y][next_x]:
			dfs(field, visited, next_x, next_y)


n, m = map(int, input().split())
field = [[10001] * (m + 2) for _ in range(n + 2)]
for y in range(1, n + 1):
	field[y][1:m+1] = map(int, input().split())

# найти возможные точки размещения ловушек
traps = list()
for y in range(1, n + 1):
	for x in range(1, m + 1):
		for dx, dy in steps:
			to_x = x + dx
			to_y = y + dy
			if field[y][x] > field[to_y][to_x]:
				break
		else:
			traps.append((field[y][x], x, y))
# отсортировать точки размещения ловушек по высоте
traps.sort()

visited = [[False] * (m + 2) for _ in range(n + 2)]
for i in range(n + 2):
	visited[i][0] = visited[i][m + 1] = True
for j in range(m + 2):
	visited[0][j] = visited[n + 1][j] = True

# дфс от каждой возможной точки размещения ловушки, если ранее она не была посещена
answer = 0
for _, x, y in traps:
	if not visited[y][x]:
		dfs(field, visited, x, y)
		answer += 1

print(answer)
