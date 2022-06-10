def covered(x, length):
	lines = 0
	line_end = x[0] - 1
	for point in x:
		if point > line_end:
			line_end = point + length
			lines += 1
	return lines


n, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
l = 0
r = x[-1] - x[0]
while l < r:
	length = (l + r) // 2
	if covered(x, length) <= k:
		r = length
	else:
		l = length + 1

print(l)
