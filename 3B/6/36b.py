# 36. Длина кратчайшего пути

from collections import deque


def bfs(graph, start, end):
	visited = [False] * len(graph)
	d = deque()
	d.append((start, 0))
	while d:
		now, steps = d.popleft()
		visited[now] = True
		if now == end:
			return steps
		for i in range(1, len(graph)):
			if graph[now][i] == 1 and not visited[i]:
				d.append((i, steps + 1))
	return -1

n = int(input())
graph = [[0,] for _ in range(n + 1)]
for i in range(1, n + 1):
	graph[i].extend(map(int, input().split()))
start, end = map(int, input().split())

print(bfs(graph, start, end))
