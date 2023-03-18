# 34. Топологическая сортировка

from sys import setrecursionlimit

setrecursionlimit(1000000)


WHITE = 0
GRAY = 1
BLACK = 2

def dfs_has_cycle(graph: list[int], visited: list[bool], now: int, top_sorted: list[int]) -> bool:
	visited[now] = GRAY

	for neigbour in graph[now]:
		if visited[neigbour] == GRAY:
			return True
		elif visited[neigbour] == WHITE:
			if (dfs_has_cycle(graph, visited, neigbour, top_sorted)):
				return True

	visited[now] = BLACK
	top_sorted.append(now)
	return False


n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)

visited = [WHITE] * (n + 1)
top_sorted = list()
for v in range(1, len(graph)):
	if visited[v] == WHITE:
		if dfs_has_cycle(graph, visited, v, top_sorted):
			top_sorted = -1,
			break

print(*reversed(top_sorted))

