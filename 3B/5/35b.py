# 35. Поиск цикла

from sys import setrecursionlimit

setrecursionlimit(1000000)


WHITE = 0
GRAY = 1
BLACK = 2

'''
	Возвращает вершины начала и конца первого встреченного цикла, если он есть
		graph - граф в виде матрицы
		prev - предыдущая вершина для каждой вершины(из какой вершины попали в эту вершину)
		visited - цвет для каждой вершины
		v - текущая вершина
'''
def dfs_get_cycle(
	graph: list[list[int]],
	prev: list[int],
	visited: list[int],
	v: int
) -> tuple[int, int] | None:

	visited[v] = GRAY
	for to in range(1, n + 1):
		'''
			если есть ребро и оно не ведет в вершину из которой пришли,
			чтобы не возвращатся в вершину из которой пришли, т. к. граф неориентированный
		'''
		if graph[v][to] == 1 and to != prev[v]:
			# есть цикл с началом в вершине to и концом в v
			if visited[to] == GRAY:
				prev[to] = v
				return to, v
			if visited[to] == WHITE:
				prev[to] = v
				cycle = dfs_get_cycle(graph, prev, visited, to)
				if cycle:
					return cycle

	return None


n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
	line = map(int, input().split())
	graph[i][1:] = line

visited = [WHITE] * (n + 1)
prev = [0] * (n + 1)
for v in range(1, len(graph)):
	if visited[v] == WHITE:
		cycle = dfs_get_cycle(graph, prev, visited, v)
		if cycle:
			break

if cycle:
	first, last = cycle
	answer = list()
	while first != last:
		answer.append(last)
		last = prev[last]
	answer.append(first)

	print('YES')
	print(len(answer))
	print(*answer)
else:
	print('NO')
