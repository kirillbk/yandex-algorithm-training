# C. Максимальный разрез

def solution1(graph: list[list[int]], n: int) -> tuple[int, list[int]]:
    def solve(v: int, state: list[int], cut_weight: int):
        if v == n:
            nonlocal max_cut_weight, max_cut_weight
            if cut_weight > max_cut_weight:
                max_cut_weight = cut_weight
                max_cut_state[:] = state
            return

        solve(v + 1, state, cut_weight)
        for u in range(n):
            if state[u] == 1:
                cut_weight += graph[v][u]
            else:
                cut_weight -= graph[v][u]
        state[v] = 2
        solve(v + 1, state, cut_weight)
        state[v] = 1

    max_cut_weight = 0
    max_cut_state = [0] * n

    solve(0, [1] * n, 0)

    return max_cut_weight, max_cut_state


def solution2(graph: list[list[int]], n: int) -> tuple[int, list[int]]:
    max_cut_weight = 0
    max_cut_state = 0
    cut_weight = [0] * (2**n // 2 + 1)

    for state in range(1, 2**n // 2 + 1):
        v = 0
        while not (state & (1 << v)):
            v += 1

        cut_weight[state] = cut_weight[state & ~(1 << v)]
        for u in range(n):
            if state & (1 << u):
                cut_weight[state] -= graph[v][u]
            else:
                cut_weight[state] += graph[v][u]

        if cut_weight[state] > max_cut_weight:
            max_cut_weight = cut_weight[state]
            max_cut_state = state

    partitions = [1 if max_cut_state & (1 << v) else 2 for v in range(n)]
    return max_cut_weight, partitions


n = int(input())
graph = []
for _ in range(n):
    edges = map(int, input().split())
    edges = list(edges)
    graph.append(edges)

weight, partitions = solution2(graph, n)

print(weight)
print(*partitions)
