# A. Не минимум на отрезке

n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    minimum = min(a[l:r+1])
    for i in range(l, r + 1):
        if a[i] != minimum:
            print(a[i])
            break
    else:
        print("NOT FOUND")
