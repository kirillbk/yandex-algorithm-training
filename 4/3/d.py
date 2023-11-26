# D. Автобусы в Васюках

from heapq import heappop, heappush
from math import isinf


def solution(start: int, finish: int, graph: list[list[(int, int, int)]]) -> int:
    time = [float('inf')] * len(graph)
    heap = [(0, d)]
    time[start] = 0

    while heap:
        now_time, village = heappop(heap)
        if time[village] != now_time:
            continue
        if village == finish:
            break

        for to, dep_time, arr_time in graph[village]:
            if dep_time < now_time:
                continue
            if arr_time < time[to]:
                time[to] = arr_time
                heappush(heap, (arr_time, to))

    if isinf(time[finish]):
        return -1
    return time[finish]


n = int(input())
d, v = map(int, input().split())
r = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    from_, dep_time, to, arr_time = map(int, input().split())
    graph[from_].append((to, dep_time, arr_time))

print(solution(d, v, graph))
