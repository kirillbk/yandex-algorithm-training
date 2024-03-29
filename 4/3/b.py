# B. Дейкстра с восстановлением пути

INF = 1_000_000

def solution(start: int, finish: int, graph: list[list[int]]) -> list[int] | None:
    visited = [False] * len(graph)
    distance = [INF] * len(graph)
    prev = [None] * len(graph)

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
            new_distance = distance[v] + m[v][to]
            if new_distance < distance[to]:
                distance[to] = new_distance
                prev[to] = v

    if distance[finish] == INF:
        return None
    # восстановление пути от start до finish
    path = []
    while finish:
        path.append(finish)
        finish = prev[finish]

    return path[::-1]


n, s, f = map(int, input().split())
m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    line = map(int, input().split())
    m[i][1:] = line

path = solution(s, f, m)
if path:
    print(*path)
else:
    print(-1)
