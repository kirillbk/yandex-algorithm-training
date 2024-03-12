# E. Прибыльный стартап

n, k, d = map(int, input().split())

answer = '-1'
n *= 10
for i in range(0, 10):
    if (n + i) % k == 0:
        answer = str(n + i) + '0' * (d - 1)
        break

print(answer)

