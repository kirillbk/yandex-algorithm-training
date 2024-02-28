# D. Бусинки

from collections import defaultdict
from sys import setrecursionlimit


def dfs(v: int, graph: defaultdict[list[int]], sub_depth: list[int], visited: list[bool]) -> int:
    visited[v] = True
    best = 1
    max1 = max2 = -1

    for to in graph[v]:
        if visited[to]:
            continue
        best = max(best, dfs(to, graph, sub_depth, visited))
        if sub_depth[to] > max1:
            max2 = max1
            max1 = sub_depth[to]
        elif sub_depth[to] > max2:
            max2 = sub_depth[to]

    # максимальная глубина поддерева, которое начинается в этой вершине (1, если v - лист)
    sub_depth[v] = max(1, max1 + 1)

    # максимальное количество бусинок в цепочке, проходящей через вершину v
    best = max(best, max1 + 1)          # v - лист
    best = max(best, max1 + max2 + 1)   # v - не лист

    return best


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
sub_depth = [0] * (n + 1)
setrecursionlimit(10**6)
print(dfs(1, graph, sub_depth, visited))
