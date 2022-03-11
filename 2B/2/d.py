l, k = map(int, input().split())
legs = list(map(int, input().split()))

i = 0
while legs[i] < l // 2:
	i += 1
if l % 2 and legs[i] == l // 2:
	print(legs[i])
else:
	print(legs[i - 1], legs[i])
