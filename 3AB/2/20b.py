# 20. Пирамидальная сортировка

from typing import List


def siftDown(a: List, i: int, n: int):
	while i * 2 + 1 < n:
		l = i * 2 + 1
		r = i * 2 + 2
		child = l
		if r < n and a[r] > a[l]:
			child = r
		if a[i] > a[child]:
			break
		a[i], a[child] = a[child], a[i]
		i = child



n = int(input())
a = list(map(int, input().split()))

for i in range(n // 2 - 1, -1, -1):
	siftDown(a, i, n)
for i in range(n - 1, 0, -1):
	a[0], a[i] = a[i], a[0]
	siftDown(a, 0, i)

print(*a)
