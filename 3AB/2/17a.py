# 17. Гоблины и шаманы

from collections import deque

n = int(input())
first_half = deque()
second_half = deque()
for _ in range(n):
	q = input().split()
	if q[0] == '+':
		second_half.append(q[1])
	elif q[0] == '*':
		second_half.appendleft(int(q[1]))
	else:
		print(first_half.popleft())
	if len(first_half) < len(second_half):
		first_half.append(second_half.popleft())

