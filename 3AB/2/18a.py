# 18. Тупики

from heapq import heappop, heappush


k, n = map(int, input().split())
available = list(range(1, k + 1))
used = list()
answer = [0] * n
for i in range(n):
	arrival, departure = map(int, input().split())
	while used and used[0][0] < arrival:
		_, deadend = heappop(used)
		heappush(available, deadend)
	if available:
		deadend = heappop(available)
		heappush(used, (departure, deadend))
		answer[i] = deadend
	else:
		answer = 0, i + 1
		break

print(*answer)
