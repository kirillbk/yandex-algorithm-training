# G. Новый офис плюса

def make_prefix(area: list[str], n: int, m: int) -> list[list[int]]:
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    prefix[1][1] = 1 if area[0][0] == '#' else 0

    for i in range(1, m + 1):
        prefix[1][i] = prefix[1][i - 1]
        if area[0][i - 1] == '#':
            prefix[1][i] += 1
    for i in range(1, n + 1):
        prefix[i][1] = prefix[i - 1][1]
        if area[i - 1][0] == '#':
            prefix[i][1] += 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1]
            if area[i - 1][j - 1] == '#':
                prefix[i][j] += 1

    return prefix


def place_office(prefix: list[int], n: int, m: int, k: int) -> bool:
    for i in range(k + 1, (n + 1) - 2 * k + 1):
        ay1 = i
        ay2 = ay1 + k - 1
        by1 = ay1 - k
        by2 = by1 + 3 * k - 1

        if prefix[ay2][m] + prefix[ay1 - 1][0] - prefix[ay2][0] - prefix[ay1 - 1][m] < 3 * k * k:
            continue

        for j in range(k + 1, (m + 1) - 2 * k + 1):
            ax1 = j - k
            ax2 = ax1 + 3 * k - 1
            a = prefix[ay2][ax2] + prefix[ay1 - 1][ax1 - 1] - prefix[ay2][ax1 - 1] - prefix[ay1 - 1][ax2]
            if a != 3 * k * k:
                continue

            bx1 = j
            bx2 = bx1 + k - 1
            b = prefix[by2][bx2] + prefix[by1 - 1][bx1 - 1] - prefix[by2][bx1 - 1] - prefix[by1 - 1][bx2]
            if b != 3 * k * k:
                continue

            return True

    return False


n, m = map(int, input().split())
area = []
for _ in range(n):
    area.append(input())

prefix = make_prefix(area, n, m)
l = 1
r = n
while r - l > 1:
    middle = (r + l) // 2
    if place_office(prefix, n, m, middle):
        l = middle
    else:
        r = middle

print(l)
