# A. Дейкстра

INF = 1_000_000

def solution(start: int, finish: int, graph: list[list[int]]) -> int:
    visited = [False] * len(graph)
    distance = [INF] * len(graph)

    distance[start] = 0
    for _ in range(1, len(graph)):
        # найдем непосещенную вершину с минимальным расстоянием
        v = 0
        for u in range(1, len(graph)):
            if not visited[u] and distance[u] < distance[v]:
                v = u
        if v == 0 or v == finish:
            break
        # рассмотрим все исходящие рёбра
        visited[v] = True
        for to in range(1, len(graph)):
            if m[v][to] <= 0:
                continue
            distance[to] = min(distance[to], distance[v] + m[v][to])

    return distance[finish]


n, s, f = map(int, input().split())
m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    line = map(int, input().split())
    m[i][1:] = line

answer = solution(s, f, m)
if answer != INF:
    print(answer)
else:
    print(-1)
