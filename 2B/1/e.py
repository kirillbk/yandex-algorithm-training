d = int(input())
x, y = map(int, input().split())

(d, 0), (0, d)
if x >= 0 and y >= 0 and x + y <= d:
	print(0)
else:
	distance = ((abs(0 - x) + abs(0 - y), 1),
				(abs(d - x) + abs(0 - y), 2),
				(abs(0 - x) + abs(d - y), 3))
	print(min(distance)[1])
