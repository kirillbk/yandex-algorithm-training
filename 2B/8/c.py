# C. Родословная: LCA

from sys import stdin


n = int(input())
ansectors = dict()
for _ in range(n - 1):
    desc, ans = input().split()
    ansectors[desc] = ans

for line in stdin:
    p1, p2 = line.split()

    p1_ansectors = {p1}
    while p1 in ansectors:
        p1 = ansectors[p1]
        p1_ansectors.add(p1)

    while p2 not in p1_ansectors:
        p2 = ansectors[p2]

    print(p2)
