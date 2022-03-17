s = set()
for n in input().split():
	if n in s:
		print("YES")
	else:
		print("NO")
		s.add(n)
