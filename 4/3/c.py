# C. Быстрый алгоритм Дейкстры

from heapq import heappop, heappush
from math import isinf


def solution(start: int, finish: int, graph: list[(int, int)]) -> int:
    distance = [float("inf")] * len(graph)
    pqueue = []

    distance[start] = 0
    pqueue.append((0, start))
    while pqueue:
        # город с минимальным расстоянием от start
        dist, city = heappop(pqueue)
        if distance[city] != dist:
            continue
        if city == finish:
            break

        # рассмотрим все соседние города
        for to_city, l in graph[city]:
            new_distance = dist + l
            if new_distance < distance[to_city]:
                distance[to_city] = new_distance
                heappush(pqueue, (new_distance, to_city))

    if isinf(distance[finish]):
        return -1
    return distance[finish]


n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
a, b = map(int, input().split())

print(solution(a, b, graph))
