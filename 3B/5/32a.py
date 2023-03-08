# 32. Откуда достижима первая вершина

from sys import setrecursionlimit

def dfs(graph, visited, path, v):
	visited[v] = True
	path.append(v)
	for to in graph[v]:
		if not visited[to]:
			dfs(graph, visited, path, to)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	v1, v2 = map(int, input().split())
	graph[v2].append(v1)

visited = [False] * (n + 1)
path = []
dfs(graph, visited, path, 1)
print(*sorted(path))
