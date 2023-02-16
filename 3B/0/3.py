# 3. Коллекционер Диего

from bisect import bisect_left

def	lbs(a: list, x: int):
	l = -1
	r = len(a)
	while l + 1 < r:
		m = (l + r) // 2
		if a[m] < x:
			l = m
		else:
			r = m
	return r


n = int(input())
stickers = set(map(int, input().split()))
stickers = sorted(stickers)
k = int(input())
for collector in map(int, input().split()):
	print(lbs(stickers, collector))
	# print(bisect_left(stickers, collector))
