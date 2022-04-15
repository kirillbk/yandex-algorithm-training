n, m = map(int, input().split())
x = map(int, input().split())
y = map(int, input().split())

x = enumerate(x)
x = sorted(x, key=lambda x: x[1])
y = enumerate(y, start=1)
y = sorted(y, key=lambda x: x[1])
cntr = 0
answer = [0] * n
room = 0
for group, students in x:
	while room < m and y[room][1] < students + 1:
		room += 1
	if room == m:
		break
	cntr += 1
	answer[group] = y[room][0]
	room += 1
	
print(cntr)
print(*answer)
