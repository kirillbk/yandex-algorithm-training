# 33. Списывание

from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfs_bipartite(graph, colors, v, c):
	colors[v] = c
	for to in graph[v]:
		if colors[to] != 0 and colors[to] != 3 - c:
			return False
		elif colors[to] == 0:
			if not dfs_bipartite(graph, colors, to, 3 - c):
				return False
	return True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	s1, s2 = map(int, input().split())
	graph[s1].append(s2)
	graph[s2].append(s1)

colors = [0] * (n + 1)
for v in range(1, len(graph)):
	if colors[v] == 0:
		if not dfs_bipartite(graph, colors, v, 1):
			print('NO')
			break
else:
	print('YES')
