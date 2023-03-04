# 32. Компоненты связности

from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfs(graph, visited, now, component):
	visited[now] = True
	component.append(now)
	for neighbour in graph[now]:
		if not visited[neighbour]:
			dfs(graph, visited, neighbour, component)


n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	graph[v2].append(v1)

visited = [False] * (n + 1)
answer = list()
for v in range(1, len(graph)):
	if not visited[v]:
		component = list()
		dfs(graph, visited, v, component)
		answer.append(component)

print(len(answer))
for component in answer:
	print(len(component))
	print(*component)
