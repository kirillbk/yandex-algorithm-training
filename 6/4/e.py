# E. Размер поддеревьев

from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(v: int, tree: list[list[int]], visited: list[bool], ans: list[int]):
    visited[v] = True
    for u in tree[v]:
        if visited[u]:
            continue
        dfs(u, tree, visited, ans)
        ans[v] += ans[u]


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = [1] * (n + 1)
visited = [False] * (n + 1)
dfs(1, tree, visited, ans)

print(*ans[1:])
