# D. Простая задача коммивояжера

from math import isinf


# перебор c отсечениями n!
def solution1(graph: list[list[int]], n: int) -> int:
    def tsp(i: int, v: int, path: int, used: list[bool], left_path_min):
        if i == n:
            path += graph[v][0]
            nonlocal answer
            if path < answer:
                answer = path
            return

        if path + left_path_min >= answer:
            return

        left_path_min -= min_edges[v]
        for u in range(1, n):
            if used[u]:
                continue
            if graph[v][u] == 0:
                continue
            used[u] = True
            tsp(i + 1, u, path + graph[v][u], used, left_path_min)
            used[u] = False

    min_edges = [float('inf')] * n
    for i in range(n):
        for edge in graph[i]:
            if edge != 0 and edge < min_edges[i]:
                min_edges[i] = edge
    answer = float('inf')
    tsp(1, 0, 0, [False] * n, sum(min_edges))

    if isinf(answer):
        return -1
    return answer


# ДП по подмножествам 2^n * n^2
def solution2(graph: list[list[int]], n: int) -> int:
    def rm(bit: int, s: int) -> int:
        return s & ~(1 << bit)

    def isin(bit: int, s: int) -> int:
        return s & (1 << bit)

    # минимальный путь из вершины 0 в вершину v, проходящий через вершины в множестве set
    # dp[set][v]
    dp = [[float('inf')] * n for _ in range(2**n)]
    # путь в нулевую вершину через set = 0...01
    dp[1][0] = 0

    # set от 0...011 до 1...111
    for set in range(2, 2**n):
        for v in range(n):
            # если вершина есть в текущем set, найдем минимальный путь в эту вершину через множество set
            if isin(v, set):
                prev_set = rm(v, set)
                for q in range(n):
                    if isin(q, set) and graph[q][v] != 0:
                        dp[set][v] = min(dp[set][v], dp[prev_set][q] + graph[q][v])

    answer = float('inf')
    full_set = (1 << n) - 1 # 1...111
    for v in range(n):
        answer = min(answer, dp[full_set][v] + graph[v][0])

    return -1 if isinf(answer) else answer


n = int(input())
graph = []
for _ in range(n):
    edges = map(int, input().split())
    edges = list(edges)
    graph.append(edges)

# print(solution1(graph, n))
print(solution2(graph, n))
