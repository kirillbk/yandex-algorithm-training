# B. Родословная: предки и потомки

from sys import stdin


def is_ansector(ans: str, desc: str, ansectors: dict[str, str]) -> bool:
    while desc in ansectors:
        desc = ansectors[desc]
        if desc == ans:
            return True

    return False


n = int(input())
ansectors = dict()
for _ in range(n - 1):
    desc, ans = input().split()
    ansectors[desc] = ans

answer = []
for line in stdin:
    p1, p2 = line.split()

    a = 0
    if is_ansector(p1, p2, ansectors):
        a = 1
    elif is_ansector(p2, p1, ansectors):
        a = 2
    answer.append(a)

print(*answer)
