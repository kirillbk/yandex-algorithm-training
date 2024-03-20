# H. Наилучший запрет

def matrix_max(
    a: list[list[int]],
    n: int,
    m: int,
    i_excluded: int,
    j_excluded: int
) -> tuple[int, int, int]:
    amax = -1
    i_max = j_max = -1
    for i in range(n):
        if i == i_excluded:
            continue
        for j in range(m):
            if j != j_excluded and a[i][j] > amax:
                amax = a[i][j]
                i_max = i
                j_max = j

    return amax, i_max, j_max


n, m = map(int, input().split())
a = []
for _ in range(n):
    line = map(int, input().split())
    a.append([*line])

m1 = m2 = 0
i1 = j1 = i2 = j2 = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > m1:
            m2 = m1
            i2, j2 = i1, j1
            m1 = a[i][j]
            i1, j1 = i, j
        elif a[i][j] > m2:
            m2 = a[i][j]
            i2, j2 = i, j

if i1 == i2:
    _, _, j3 = matrix_max(a, n, m, i1, -1)
    i, j = i1, j3
elif j1 == j2:
    _, i3, _ = matrix_max(a, n, m, -1, j1)
    i, j = i3, j1
else:
    m3, i3, j3 = matrix_max(a, n, m, i1, j2)
    m4, i4, j4 = matrix_max(a, n, m, i2, j1)
    i, j = (i1, j2) if m3 < m4 else (i2, j1)

print(i + 1, j + 1)
