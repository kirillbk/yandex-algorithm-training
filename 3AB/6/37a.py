# 37. Числа

from collections import deque

def add(n):
	if n // 1000 != 9:
		return n + 1000
	return 0


def minus(n):
	if n % 10 != 1:
		return n - 1
	return 0


def l_shift(n):
	return n % 1000 * 10 + n // 1000


def r_shift(n):
	return n // 10 + n % 10 * 1000


def solution(n1, n2):
	prev = {n1: 0}
	q = deque()
	operations = add, minus, l_shift, r_shift

	q.append(n1)
	while q:
		now = q.popleft()
		if now == n2:
			answer = deque()
			while now != 0:
				answer.appendleft(now)
				now = prev[now]
			return(answer)
		for op in operations:
			to = op(now)
			if to != 0 and to not in prev:
				prev[to] = now
				q.append(to)

	return deque()


n1 = int(input())
n2 = int(input())

print(*solution(n1, n2), sep='\n')
