# 35. Поиск цикла

from sys import setrecursionlimit

setrecursionlimit(1000000)


WHITE = 0
GRAY = 1
BLACK = 2

'''
	Возвращает вершину начала первого встреченного цикла, если он есть, иначе 0
		graph - граф в виде матрицы
		visited - цвет для каждой вершины
		prev - предыдущая вершина для каждой вершины(из какой вершины попали в эту вершину)
		v - текущая вершина
'''
def dfs_get_cycle(
	graph: list[list[int]],
	visited: list[int],
	prev: list[int],
	v: int
) -> int:

	visited[v] = GRAY
	for to in range(1, n + 1):
		'''
			если есть ребро и оно не ведет в вершину из которой пришли,
			чтобы не возвращатся в вершину из которой пришли, т. к. граф неориентированный
		'''
		if graph[v][to] == 1 and to != prev[v]:
			# есть цикл с началом в вершине to
			if visited[to] == GRAY:
				prev[to] = v
				return to
			if visited[to] == WHITE:
				prev[to] = v
				cycle = dfs_get_cycle(graph, visited, prev, to)
				if cycle != 0:
					return cycle
	visited[v] = BLACK
	return 0


n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
	line = map(int, input().split())
	graph[i][1:] = line

visited = [WHITE] * (n + 1)
prev = [0] * (n + 1)
for v in range(1, len(graph)):
	if visited[v] == WHITE:
		cycle = dfs_get_cycle(graph, visited, prev, v)
		if cycle != 0:
			answer = list()
			next = prev[cycle]
			while next != cycle:
				answer.append(next)
				next = prev[next]
			answer.append(cycle)
			print('YES')
			print(len(answer))
			print(*answer)
			break
else:
	print('NO')
