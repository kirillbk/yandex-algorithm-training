# H. Вершинно-реберное покрытие дерева

from collections.abc import Iterable
from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfs(v: int, p: int, tree: list[list[int]], dp_excl: list[int], dp_incl: list[int]):
    incl = excl = 0
    for u in tree[v]:
        if u != p:
            dfs(u, v, tree, dp_excl, dp_incl)
            incl += dp_incl[u]
            excl += min(dp_excl[u], dp_incl[u])
    dp_excl[v] = incl
    dp_incl[v] += excl


def ans_dfs(
    v: int,
    p: int,
    tree: list[list[int]],
    dp_excl: list[int],
    dp_incl: list[int],
    ans: set[int],
):
    for u in tree[v]:
        if u != p:
            if v not in ans or dp_incl[u] < dp_excl[u]:
                ans.add(u)
            ans_dfs(u, v, tree, dp_excl, dp_incl, ans)


def solution(n: int, tree: list[list[int]], a: Iterable[int]):
    if n == 1:
        print(*a, 1)
        print(1)
        return

    dp_include = [0, *a]
    dp_exclude = [0] * (n + 1)
    dfs(1, -1, tree, dp_exclude, dp_include)

    ans = set()
    if dp_include[1] < dp_exclude[1]:
        ans.add(1)
    ans_dfs(1, -1, tree, dp_exclude, dp_include, ans)

    print(min(dp_include[1], dp_exclude[1]), len(ans))
    print(*ans)


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
a = map(int, input().split())

solution(n, tree, a)
