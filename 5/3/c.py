# C. Удаление чисел

from collections import Counter


n = int(input())
a = [*map(int, input().split())]

cntr = Counter(a)

answer = float('inf')
for number in cntr:
    answer = min(answer, n - cntr[number] - cntr[number + 1])
    answer = min(answer, n - cntr[number] - cntr[number - 1])

print(answer)
