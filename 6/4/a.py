# A. Родословная: подсчет уровней

from collections import defaultdict


def dfs(name: str, level: int, tree: dict[str, list[str]], ans: dict[str, int]):
    ans[name] = level
    for child in tree[name]:
        dfs(child, level + 1, tree, ans)


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
dfs(root, 0, tree, ans)

for name, level in sorted(ans.items()):
    print(name, level)
