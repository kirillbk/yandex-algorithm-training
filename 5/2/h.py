# H. Наилучший запрет

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
    m3 = 0
    j3 = 0
    for i in range(n):
        if i == i1:
            continue
        for j in range(m):
            if a[i][j] > m3:
                m3 = a[i][j]
                j3 = j
    i, j = i1, j3
elif j1 == j2:
    m3 = 0
    i3 = 0
    for j in range(m):
        if j == j1:
            continue
        for i in range(n):
            if a[i][j] > m3:
                m3 = a[i][j]
                i3 = i
    i, j = i3, j1
else:
    m3 = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > m3 and i != i1 and j != j2:
                m3 = a[i][j]
                j3 = j

    m4 = 0
    for j in range(m):
        for i in range(n):
            if a[i][j] > m4 and i != i2 and j != j1:
                m4 = a[i][j]

    i, j = (i1, j2) if m3 < m4 else (i2, j1)

print(i + 1, j + 1)
