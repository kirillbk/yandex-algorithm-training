def lbs(a, x):
	l = -1
	r = len(a)
	while l + 1 < r:
		m = (l + r) // 2
		if a[m] >= x:
			r = m
		else:
			l = m
	return r

def rbs(a, x):
	l = -1
	r = len(a)
	while l + 1 < r:
		m = (l + r) // 2
		if a[m] > x:
			r = m
		else:
			l = m
	return l


n = int(input())
array = list(map(int, input().split()))
k = int(input())
array.sort()
answer = list()
for i in range(k):
	l, r = map(int, input().split())
	ge = lbs(array, l)
	le = rbs(array, r)
	if le < ge:
		answer.append(0)
	else: 
		answer.append(le - ge + 1)

print(*answer)
