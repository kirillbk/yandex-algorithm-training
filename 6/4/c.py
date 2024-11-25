# C. Родословная: LCA

from sys import stdin


n = int(input())
descendants = dict()
for _ in range(n - 1):
    child, parent = input().split()
    descendants[child] = parent
q = []
for line in stdin:
    name1, name2 = line.split()
    q.append((name1, name2))


# потомок: множество предков
parents = dict()
for name in descendants:
    ancestors = set()
    parent = name
    while parent:
        ancestors.add(parent)
        parent = descendants.get(parent)
    parents[name] = ancestors

for name1, name2 in q:
    ancestors = parents.get(name1, {name1})
    while name2 not in ancestors:
        name2 = descendants.get(name2, name2)
    print(name2)
