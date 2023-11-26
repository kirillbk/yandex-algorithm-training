# E. На санях

from collections import deque
from math import isinf


def bfs(start: int, graph: list[list[(int, int)]]) -> list[int]:
    distance = [float('inf')] * len(graph)
    queue = deque()

    queue.append(start)
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for to, s in graph[v]:
            if isinf(distance[to]):
                distance[to] = distance[v] + s
                queue.append(to)

    return distance


def solution(start: int, graph: list[list[(int, int)]]) -> (list[float], list[int]):
    visited = [False] * len(graph)
    time = [float('inf')] * len(graph)
    prev = [0] * len(graph)

    time[start] = 0
    while True:
        v = 0
        for u in range(1, len(graph)):
            if not visited[u] and time[u] < time[v]:
                v = u
        if isinf(time[v]):
            break
        visited[v] = True
        for to in range(1, n + 1):
            new_time = time[v] + graph[v][to]
            if new_time < time[to]:
                time[to] = new_time
                prev[to] = v

    return time, prev


n = int(input())
sleighs = [None, ]
for _ in range(n):
    t, v = map(int, input().split())
    sleighs.append((t, v))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, s = map(int, input().split())
    graph[a].append((b, s))
    graph[b].append((a, s))

# матрица времени в пути от каждой деревни до каждой
time_graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for v in range(1, n + 1):
    distance  = bfs(v, graph)
    for to in range(1, n + 1):
        time_graph[v][to] = sleighs[v][0] + distance[to] / sleighs[v][1]
    time_graph[v][v] = 0
# время в пути от столицы до каждой деревни (транспонирование матрицы - переворачиваем граф)
time_graph = [[time_graph[j][i]  for j in range(n + 1)] for i in range(n + 1)]
# время до столицы для каждой деревни
time, prev = solution(1, time_graph)

max_time = 0
slowest = 1
for i in range(1, len(time)):
    if time[i] > time[slowest]:
        slowest = i
        max_time = time[i]
print(max_time)

path = []
while slowest != 0:
    path.append(slowest)
    slowest = prev[slowest]
print(*path)
