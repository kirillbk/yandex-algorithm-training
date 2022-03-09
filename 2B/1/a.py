def	result(r, i, c):
	if i == 0:
		return 3 if r != 0 else c
	elif i == 1:
		return c
	elif i == 4:
		return 3 if r != 0 else 4
	elif i == 6:
		return 0
	elif i == 7:
		return 1
	else:
		return i

r = int(input())
i = int(input())
c = int(input())
print(result(r, i, c))
