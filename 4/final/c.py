# C. Переезд

from heapq import heappush, heappop


def check_cups(
        start: int,
        finish: int,
        graph: list[list[(int, int, int)]],
        total_weight: int
    ) -> bool:
    time = [float('inf')] * len(graph)
    heap = [(0, start)]

    time[start] = 0
    while heap:
        v_time, v = heappop(heap)
        if time[v] != v_time:
            continue
        if v == finish:
            break
        for to, t, w in graph[v]:
            new_time = v_time + t
            if new_time < time[to] and total_weight <= w:
                time[to] = new_time
                heappush(heap, (new_time, to))

    if time[finish] > 24 * 60:
        return False
    return True


n, m = map(int, input().split())
graph = [[] for _ in range((n + 1))]
for _ in range(m):
    a, b, t, w = map(int, input().split())
    graph[a].append((b, t, w))
    graph[b].append((a, t, w))

l = 0
r = 10**7 + 1
car_weight = 3000 * 1000
while r - l > 1:
    m = (l + r) // 2
    if check_cups(1, n, graph, car_weight + m * 100):
        l = m
    else:
        r = m

print(l)
