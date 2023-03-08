# 37. Путь в графе

from collections import deque

def bfs(graph, start, end):
	prev = [0] * len(graph)
	prev[start] = 0
	q = deque()
	q.append(start)
	while q:
		now = q.popleft()
		if now == end:
			path = []
			while end != start:
				path.append(end)
				end = prev[end]
			path.append(start)
			path.reverse()
			return path
		for to in range(1, len(graph)):
			if graph[now][to] == 1 and prev[to] == 0:
				prev[to] = now
				q.append(to)
	return []


n = int(input())
graph = [[0,] for _ in range(n + 1)]
for i in range(1, n + 1):
	graph[i].extend(map(int, input().split()))
start, end = map(int, input().split())

path = bfs(graph, start, end)
if path:
	print(len(path) - 1)
	if len(path) > 1:
		print(*path)
else:
	print(-1)
