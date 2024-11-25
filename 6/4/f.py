# F. Бюрократия

from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfs(v, tree: list[list[int]], ans: list[int]) -> int:
    size = 1
    for u in tree[v]:
        size += dfs(u, tree, ans)
        ans[v] += ans[u]
    ans[v] += size

    return size


n = int(input())
a = list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
for i, a in enumerate(a, 2):
    tree[a].append(i)
ans = [0] * (n + 1)
dfs(1, tree, ans)

print(*ans[1:])
