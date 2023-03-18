# 40. Метро

from collections import deque

def bfs(stations, lines, start, end):
	visited = [False] * len(lines)
	q = deque()

	for line in stations[start]:
		q.append((line, 0))
	while q:
		line, distance = q.popleft()
		visited[line] = True
		if end in lines[line]:
			return distance
		for station in lines[line]:
			for l in stations[station]:
				if not visited[l]:
					q.append((l, distance + 1))
	return -1


n = int(input())
m = int(input())
stations = [[] for _ in range(n + 1)]
lines = [[] for _ in range(m + 1)]
for l in range(1, m + 1):
	lines[l] = list(map(int, input().split()[1:]))
	for s in lines[l]:
		stations[s].append(l)
start, end = map(int, input().split())
print(bfs(stations, lines, start, end))
