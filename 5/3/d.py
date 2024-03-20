# D. Повторяющееся число

last_pos = dict()

n, k = map(int, input().split())
a = [*map(int, input().split())]

for i in range(n):
    number = a[i]
    if number not in last_pos or i - last_pos[number] > k:
        last_pos[number] = i
    else:
        print('YES')
        break
else:
    print('NO')
