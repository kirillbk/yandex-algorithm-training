# 31. Поиск в глубину

from sys import setrecursionlimit


def dfs(graph: list[list[int]], visited: list[bool], v: int, log: list[int]):
	visited[v] = True
	log.append(v)
	for to in graph[v]:
		if not visited[to]:
			dfs(graph, visited, to, log)


n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]
for _ in range(m):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	if v1 != v2:
		graph[v2].append(v1)

visited = [False] * (n + 1)
log = list()
setrecursionlimit(1000000)
dfs(graph, visited, 1, log)
print(len(log))
print(*sorted(log))
