# B. Родословная: число потомков

from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(name: str, tree: dict[str, list[str]], ans: dict[str, int]):
    ans[name] = len(tree[name])
    for child in tree[name]:
        dfs(child, tree, ans)
        ans[name] += ans[child]


n = int(input())
descendants = dict()
for _ in range(n - 1):
    child, parent = input().split()
    descendants[child] = parent

tree = defaultdict(list)
for child, parent in descendants.items():
    tree[parent].append(child)

root = tree.keys() - descendants.keys()
root = root.pop()
ans = dict()
dfs(root, tree, ans)

for name, num in sorted(ans.items()):
    print(name, num)
