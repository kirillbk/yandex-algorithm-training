def lbs(a, x):
	l = -1
	r = len(a)
	while l + 1 < r:
		m = (l + r) // 2
		if a[m] >= x:
			r = m
		else:
			l = m
	if r == len(a) or a[r] != x:
		return 0
	return r + 1

def rbs(a, x):
	l = -1
	r = len(a)
	while l + 1 < r:
		m = (l + r) // 2
		if a[m] > x:
			r = m
		else:
			l = m
	if l == -1 or a[l] != x:
		return 0
	return l + 1


n  = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
q = list(map(int, input().split()))
answer = list()
for x in q:
	answer.append(str(lbs(a, x)) + ' ' + str(rbs(a,x)))
         
print('\n'.join(answer))
