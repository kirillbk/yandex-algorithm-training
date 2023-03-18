# 35. Кружки в Маховниках

from heapq import heappush, heappop

n = int(input())
in_degree = [0] * (n + 1)
graph = [list() for _ in range(n + 1)]
# обратный граф
for i in range (1, n + 1):
	for v in map(int, input().split()[1:]):
		graph[i].append(v)
		in_degree[v] += 1

max_heap = list()
for v in range(1, n + 1):
	if in_degree[v] == 0:
		heappush(max_heap, -v)
answer = list()
while max_heap:
	v = -heappop(max_heap)
	answer.append(v)
	for child in graph[v]:
		in_degree[child] -= 1
		if in_degree[child] == 0:
			heappush(max_heap, -child)

print(*reversed(answer))
