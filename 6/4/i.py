# I. Пара путей

from sys import setrecursionlimit

setrecursionlimit(1000000)


def get_diameter(n: int, tree: list[list[int]]) -> list[int]:
    """
    возвращает список вершин диаметра дерева
    """

    def dfs(v: int, p: int, length: int):
        prev[v] = p
        nonlocal max_lenght, x
        if length > max_lenght:
            max_lenght = length
            x = v
        max_lenght = max(max_lenght, length)
        for u in tree[v]:
            if u != p:
                dfs(u, v, length + 1)

    prev = [0] * (n + 1)
    x = 0
    max_lenght = 0
    dfs(1, -1, 0)
    max_lenght = 0
    dfs(x, -1, 0)

    d = []
    while x != -1:
        d.append(x)
        x = prev[x]
    return d


def dfs_length(v: int, p: int, tree: list[list[int]]) -> tuple[int, int]:
    """
    возвращает длину двух самых длинных поддеревьев дерева
    """
    max_len1 = max_len2 = 0
    for u in tree[v]:
        if u == p:
            continue
        tmp = dfs_length(u, v, tree)[0] + 1
        if tmp >= max_len1:
            max_len2 = max_len1
            max_len1 = tmp
        elif tmp > max_len2:
            max_len2 = tmp

    return max_len1, max_len2


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

d = get_diameter(n, tree)
subtree_len = [0] * len(d)
ans = 0
for i in range(len(d)):
    for v in tree[d[i]]:
        # не рассматриваем рёбра, которые входят в диаметр
        if i > 0 and v == d[i - 1] or i + 1 < len(d) and v == d[i + 1]:
            continue
        l1, l2 = dfs_length(v, d[i], tree)
        # один путь - диаметр, другой - диаметр поддерева
        ans = max(ans, (l1 + l2) * (len(d) - 1))
        # размер максимального поддерева для вершины диаметра
        subtree_len[i] = max(subtree_len[i], l1 + 1)

pref_max = [0] * len(d)
pref_max[0] = subtree_len[0]
for i in range(1, len(d)):
    length = i + subtree_len[i]
    if length > pref_max[i - 1]:
        pref_max[i] = length
    else:
        pref_max[i] = pref_max[i - 1]

suff_max = [0] * len(d)
suff_max[-1] = subtree_len[-1]
for i in range(len(d) - 2, -1, -1):
    length = len(d) - (i + 1) + subtree_len[i]
    if length > suff_max[i + 1]:
        suff_max[i] = length
    else:
        suff_max[i] = suff_max[i + 1]

# рассмотрим вариант, когда часть одного из путей проходит по диаметру
for i in range(len(d) - 1):
    ans = max(ans, pref_max[i] * suff_max[i + 1])

print(ans)
